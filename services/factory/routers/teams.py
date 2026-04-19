"""teams.py — Team CRUD, spawn, stop, delete."""
from __future__ import annotations

import json
import os
import shutil
import sqlite3
import time
from pathlib import Path
from typing import Optional

import docker
import docker.errors
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database import DB_PATH, get_conn
from routers.events import log_event

router = APIRouter(prefix="/teams", tags=["teams"])

# ── Config ────────────────────────────────────────────────────────────────────
AGENT_IMAGE     = os.environ.get("AGENT_IMAGE",      "nvnnnbt-agent:latest")
COMPOSE_NETWORK = os.environ.get("COMPOSE_NETWORK",  "nvnnnbt-net")
OLLAMA_URL      = os.environ.get("OLLAMA_BASE_URL",  "http://host.docker.internal:11434")
HOST_PROJECT    = os.environ.get("HOST_PROJECT_PATH", "")

WORKSPACES_ROOT = Path(os.environ.get("WORKSPACES_ROOT", "/app/data/workspaces"))
TEAMS_ROOT      = WORKSPACES_ROOT / "teams"

# Port bands for teams
_TEAM_MEMBER_BAND  = range(4400, 4500)   # member agents
_TEAM_MANAGER_BAND = range(4500, 4550)   # manager agents

# ── Helpers ───────────────────────────────────────────────────────────────────

def _docker_client():
    try:
        return docker.from_env()
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Docker unavailable: {e}")


def _used_ports() -> set[int]:
    """All ports currently claimed in spawned_agents (running)."""
    with get_conn(DB_PATH) as conn:
        rows = conn.execute("SELECT ports FROM spawned_agents WHERE status='running'").fetchall()
    ports: set[int] = set()
    for row in rows:
        if row[0]:
            for v in row[0].split(","):
                v = v.strip()
                if v.isdigit():
                    ports.add(int(v))
    return ports


def _claim_port(band: range, used: set[int]) -> int:
    for p in band:
        if p not in used:
            return p
    raise HTTPException(status_code=507, detail=f"No free ports in band {band.start}–{band.stop}")


def _default_config(ollama_base: str, model: str = "qwen3:1.7b") -> dict:
    return {
        "agents": {
            "defaults": {
                "workspace": "/workspace",
                "model": model,
                "provider": "local",
                "maxTokens": 4096,
                "contextWindowTokens": 16384,
                "temperature": 0.7,
                "maxToolIterations": 10,
                "timezone": "Europe/Brussels",
            }
        },
        "channels": {"sendProgress": False, "sendToolHints": False, "sendMaxRetries": 3},
        "providers": {
            "local": {"label": "Local", "apiKey": "", "apiBase": f"{ollama_base}/v1"},
        },
        "gateway": {"host": "0.0.0.0", "port": 6161},
    }


def _init_shared_db(knowledge_dir: Path) -> None:
    """Create shared SQLite knowledge base for team."""
    knowledge_dir.mkdir(parents=True, exist_ok=True)
    db_path = knowledge_dir / "shared.db"
    conn = sqlite3.connect(str(db_path))
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS facts (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            key        TEXT NOT NULL,
            value      TEXT DEFAULT '',
            source     TEXT DEFAULT '',
            created_at TEXT DEFAULT (datetime('now'))
        );
        CREATE TABLE IF NOT EXISTS articles (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            title      TEXT NOT NULL,
            body       TEXT DEFAULT '',
            status     TEXT DEFAULT 'draft',
            author     TEXT DEFAULT '',
            created_at TEXT DEFAULT (datetime('now')),
            updated_at TEXT DEFAULT (datetime('now'))
        );
        CREATE TABLE IF NOT EXISTS queue (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            task       TEXT NOT NULL,
            status     TEXT DEFAULT 'pending',
            assigned   TEXT DEFAULT '',
            result     TEXT DEFAULT '',
            created_at TEXT DEFAULT (datetime('now')),
            updated_at TEXT DEFAULT (datetime('now'))
        );
        CREATE TABLE IF NOT EXISTS log (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            agent      TEXT NOT NULL,
            action     TEXT DEFAULT '',
            detail     TEXT DEFAULT '',
            created_at TEXT DEFAULT (datetime('now'))
        );
    """)
    conn.commit()
    conn.close()


def _make_workspace(path: Path, identity_files: dict[str, str]) -> None:
    """Create workspace directory structure."""
    path.mkdir(parents=True, exist_ok=True)
    for subdir in ("memory", "sessions", "skills", "cron"):
        (path / subdir).mkdir(parents=True, exist_ok=True)
    (path / "memory" / "MEMORY.md").touch(exist_ok=True)
    (path / "cron" / "jobs.json").write_text('{"version": 1, "jobs": []}', encoding="utf-8")
    for fname, content in identity_files.items():
        p = path / fname
        if not p.exists():
            p.write_text(content, encoding="utf-8")


def _copy_skillset(src_slug: str, dst: Path) -> None:
    """Copy identity files and skills/ from an existing workspace into dst.
    Skips config.json — model is set separately per member."""
    _IDENTITY = ["SOUL.md", "AGENTS.md", "TOOLS.md", "HEARTBEAT.md", "USER.md"]
    src = WORKSPACES_ROOT / src_slug
    if not src.exists():
        raise HTTPException(status_code=404, detail=f"Skillset workspace '{src_slug}' not found")
    for fname in _IDENTITY:
        fp = src / fname
        if fp.exists():
            (dst / fname).write_text(fp.read_text(encoding="utf-8"), encoding="utf-8")
    src_skills = src / "skills"
    if src_skills.exists():
        dst_skills = dst / "skills"
        if dst_skills.exists():
            shutil.rmtree(dst_skills)
        shutil.copytree(src_skills, dst_skills)


# ── List teams ────────────────────────────────────────────────────────────────

@router.get("")
async def list_teams() -> dict:
    with get_conn(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT slug, name, orchestrator_slug, created_at, mode FROM agent_teams ORDER BY created_at DESC"
        ).fetchall()

    teams = []
    for r in rows:
        slug = r[0]
        # Load member status
        with get_conn(DB_PATH) as conn:
            members = conn.execute(
                "SELECT sa.slug, sa.status, sa.ports, sa.model "
                "FROM team_members tm "
                "JOIN spawned_agents sa ON sa.slug = tm.agent_slug "
                "WHERE tm.team_slug = ?",
                (slug,),
            ).fetchall()

        member_list = []
        for m in members:
            _, chat_port = _parse_ports(m[2])
            member_list.append({
                "slug":      m[0],
                "status":    m[1],
                "chat_port": chat_port,
                "model":     m[3],
            })

        # Manager status
        manager_slug = r[2]
        manager_status = "unknown"
        manager_chat_port = None
        if manager_slug:
            with get_conn(DB_PATH) as conn:
                mgr = conn.execute(
                    "SELECT status, ports FROM spawned_agents WHERE slug=?",
                    (manager_slug,),
                ).fetchone()
            if mgr:
                manager_status = mgr[0]
                _, manager_chat_port = _parse_ports(mgr[1])

        teams.append({
            "slug":              slug,
            "name":              r[1],
            "manager_slug":      manager_slug,
            "manager_status":    manager_status,
            "manager_chat_port": manager_chat_port,
            "members":           member_list,
            "member_count":      len(member_list),
            "created_at":        r[3],
            "mode":              r[4] if r[4] else "production",
        })

    return {"teams": teams}


# ── Get single team ───────────────────────────────────────────────────────────

@router.get("/{slug}")
async def get_team(slug: str) -> dict:
    with get_conn(DB_PATH) as conn:
        row = conn.execute(
            "SELECT slug, name, orchestrator_slug, created_at FROM agent_teams WHERE slug=?",
            (slug,),
        ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Team '{slug}' not found")

    team_json_path = TEAMS_ROOT / slug / "team.json"
    team_json = {}
    if team_json_path.exists():
        try:
            team_json = json.loads(team_json_path.read_text())
        except Exception:
            pass

    return {
        "slug":            row[0],
        "name":            row[1],
        "manager_slug":    row[2],
        "created_at":      row[3],
        "team_json":       team_json,
    }


# ── Create team workspace ─────────────────────────────────────────────────────

class MemberSpec(BaseModel):
    role:     str
    skillset: Optional[str] = None   # workspace slug to copy identity files from
    model:    Optional[str] = None   # per-member model override


class CreateTeamBody(BaseModel):
    slug:             str
    name:             str
    members:          list[MemberSpec]
    manager_model:    str = "qwen3:1.7b"
    manager_skillset: Optional[str] = None   # workspace slug for manager identity
    member_model:     str = "qwen3:1.7b"     # default model when member.model is None


class SpawnTeamBody(BaseModel):
    mode: str = "production"     # "test" or "production"


class SetModeBody(BaseModel):
    mode: str                    # "test" or "production"


@router.post("")
async def create_team(body: CreateTeamBody) -> dict:
    import re
    if not re.match(r"^[a-z0-9][a-z0-9_-]{0,63}$", body.slug):
        raise HTTPException(status_code=400, detail="Invalid slug")
    if not body.members:
        raise HTTPException(status_code=400, detail="At least one member required")

    team_root = TEAMS_ROOT / body.slug
    if team_root.exists():
        raise HTTPException(status_code=409, detail=f"Team '{body.slug}' already exists")

    ollama_base = os.environ.get("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
    manager_slug = f"{body.slug}-manager"

    members_meta = [{"slug": f"{body.slug}-{m.role}", "role": m.role} for m in body.members]

    # ── Manager workspace ─────────────────────────────────────────────────────
    # Build default identity content (used when no skillset is selected)
    soul_content = f"""# Soul

I am {body.name} Manager, the orchestrator of the {body.name} team.

## Who I am

I coordinate a team of specialised agents to complete complex tasks.
I read `team.json` to know my team, delegate work via their chat endpoints,
and synthesise results for the user.

## What I do

- Receive a task from the user
- Break it into sub-tasks for each team member
- Call each member's `/chat` endpoint with their specific instructions
- Collect and synthesise the results
- Return the final answer to the user

## My team

See `team.json` for current member ports and roles.

## Behaviour

- Always make a plan before delegating
- Be explicit about which member handles which part
- Summarise what each member returned before giving the final answer
"""

    agents_content = f"""# Team members

Load `team.json` from your workspace root to discover team members and their ports.

## How to delegate

POST to `http://localhost:<chat_port>/chat` with:
```json
{{"messages": [{{"role": "user", "content": "<your instruction>"}}]}}
```

## Members
{chr(10).join(f"- **{m['role']}** ({m['slug']})" for m in members_meta)}
"""

    _make_workspace(team_root, {
        "SOUL.md":      soul_content,
        "AGENTS.md":    agents_content,
        "TOOLS.md":     "# Tools\n\nStandard tool set. Use file tools to read team.json.\n",
        "HEARTBEAT.md": "# Heartbeat\n\nCoordinate. Delegate. Synthesise.\n",
        "USER.md":      "# User\n\nThe user who spawned this team.\n",
    })

    # Override with skillset if provided
    if body.manager_skillset:
        _copy_skillset(body.manager_skillset, team_root)

    # Manager config.json
    mgr_cfg = _default_config(ollama_base, body.manager_model)
    (team_root / "config.json").write_text(json.dumps(mgr_cfg, indent=2) + "\n", encoding="utf-8")

    # knowledge/ dirs + shared.db
    _init_shared_db(team_root / "knowledge")
    (team_root / "knowledge" / "inbox").mkdir(exist_ok=True)
    (team_root / "knowledge" / "library").mkdir(exist_ok=True)

    # ── Member workspaces ─────────────────────────────────────────────────────
    members_dir = team_root / "members"
    for spec, m in zip(body.members, members_meta):
        member_path = members_dir / spec.role
        _make_workspace(member_path, {
            "SOUL.md":      f"# Soul\n\nI am {spec.role} in the {body.name} team.\n",
            "AGENTS.md":    f"# Role\n\nI am the **{spec.role}**. I receive tasks from the manager and complete them.\n",
            "TOOLS.md":     "# Tools\n\nStandard tool set.\n",
            "HEARTBEAT.md": f"# Heartbeat\n\nFocus. Execute. Report back.\n",
            "USER.md":      "# User\n\nThe team manager.\n",
        })
        # Override with skillset if provided
        if spec.skillset:
            _copy_skillset(spec.skillset, member_path)

        member_model = spec.model or body.member_model
        member_cfg = _default_config(ollama_base, member_model)
        (member_path / "config.json").write_text(
            json.dumps(member_cfg, indent=2) + "\n", encoding="utf-8"
        )

    # ── Register in DB ────────────────────────────────────────────────────────
    with get_conn(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO agent_teams (slug, name, knowledge_dir, orchestrator_slug, created_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (body.slug, body.name, str(team_root / "knowledge"), manager_slug, int(time.time())),
        )
        for spec, m in zip(body.members, members_meta):
            conn.execute(
                "INSERT INTO team_members (team_slug, agent_slug, model) VALUES (?, ?, ?)",
                (body.slug, m["slug"], spec.model or body.member_model),
            )

    log_event("team_create", target_type="team", target_slug=body.slug,
              detail=f"Team '{body.slug}' created with members: {[m['slug'] for m in members_meta]}")

    return {
        "ok":      True,
        "slug":    body.slug,
        "manager": manager_slug,
        "members": members_meta,
    }


# ── Spawn team ────────────────────────────────────────────────────────────────

def _parse_ports(ports_str: str) -> tuple[int | None, int | None]:
    if not ports_str:
        return None, None
    parts = [p.strip() for p in ports_str.split(",") if p.strip().isdigit()]
    gateway = int(parts[0]) if len(parts) > 0 else None
    chat    = int(parts[1]) if len(parts) > 1 else None
    return gateway, chat


@router.get("/{slug}/log")
async def get_team_log(slug: str, limit: int = 100) -> dict:
    """Read delegation log from team's shared.db."""
    db_path = TEAMS_ROOT / slug / "knowledge" / "shared.db"
    if not db_path.exists():
        return {"entries": []}
    try:
        conn = sqlite3.connect(str(db_path))
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT id, agent, action, detail, created_at FROM log ORDER BY id DESC LIMIT ?",
            (limit,)
        ).fetchall()
        conn.close()
        return {"entries": [dict(r) for r in reversed(rows)]}
    except Exception:
        return {"entries": []}


@router.post("/{slug}/mode")
async def set_team_mode(slug: str, body: SetModeBody) -> dict:
    """Flip a team between test and production mode."""
    if body.mode not in ("test", "production"):
        raise HTTPException(status_code=400, detail="mode must be 'test' or 'production'")
    with get_conn(DB_PATH) as conn:
        row = conn.execute("SELECT slug FROM agent_teams WHERE slug=?", (slug,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Team '{slug}' not found")
    with get_conn(DB_PATH) as conn:
        conn.execute("UPDATE agent_teams SET mode=? WHERE slug=?", (body.mode, slug))
    log_event("team_mode", target_type="team", target_slug=slug,
              detail=f"Team '{slug}' mode set to '{body.mode}'")
    return {"ok": True, "slug": slug, "mode": body.mode}


@router.post("/{slug}/spawn")
async def spawn_team(slug: str, body: SpawnTeamBody = None) -> dict:
    if body is None:
        body = SpawnTeamBody()
    if not HOST_PROJECT:
        raise HTTPException(status_code=503, detail="HOST_PROJECT_PATH env var not set")

    with get_conn(DB_PATH) as conn:
        team = conn.execute(
            "SELECT slug, name, orchestrator_slug FROM agent_teams WHERE slug=?", (slug,)
        ).fetchone()
    if not team:
        raise HTTPException(status_code=404, detail=f"Team '{slug}' not found")

    team_root = TEAMS_ROOT / slug
    if not team_root.exists():
        raise HTTPException(status_code=404, detail=f"Team workspace '{slug}' missing on disk")

    with get_conn(DB_PATH) as conn:
        member_rows = conn.execute(
            "SELECT agent_slug, model FROM team_members WHERE team_slug=?", (slug,)
        ).fetchall()

    if not member_rows:
        raise HTTPException(status_code=400, detail="Team has no members")

    dc = _docker_client()
    used = _used_ports()
    manager_slug = team[2]
    spawned = []
    team_json_members = []

    try:
        # Spawn each member
        for agent_slug, model in member_rows:
            role = agent_slug.replace(f"{slug}-", "", 1)
            member_path_container = str(TEAMS_ROOT / slug / "members" / role)
            member_path_host = str(
                Path(HOST_PROJECT) / "workspace" / "workspaces" / "teams" / slug / "members" / role
            )

            # Skip if already running
            with get_conn(DB_PATH) as conn:
                existing = conn.execute(
                    "SELECT container FROM spawned_agents WHERE slug=? AND status='running'",
                    (agent_slug,),
                ).fetchone()
            if existing:
                _, chat_port = _parse_ports("")
                # Get existing port
                with get_conn(DB_PATH) as conn:
                    pr = conn.execute("SELECT ports FROM spawned_agents WHERE slug=?", (agent_slug,)).fetchone()
                _, chat_port = _parse_ports(pr[0] if pr else "")
                team_json_members.append({"slug": agent_slug, "role": role, "chat_port": chat_port})
                continue

            chat_port = _claim_port(_TEAM_MEMBER_BAND, used)
            used.add(chat_port)

            container_name = f"nvnnnbt-team-{agent_slug}"
            container = dc.containers.run(
                AGENT_IMAGE,
                name=container_name,
                detach=True,
                network=COMPOSE_NETWORK,
                ports={"6161/tcp": ("127.0.0.1", chat_port)},
                environment={
                    "WORKSPACE_PATH":  member_path_container,
                    "SKILLSETS_PATH":  str(WORKSPACES_ROOT),
                    "AGENT_PORT":      "6161",
                    "AGENT_MODE":      "production",
                    "OLLAMA_BASE_URL": OLLAMA_URL,
                },
                volumes={
                    member_path_host: {"bind": member_path_container, "mode": "rw"},
                    str(Path(HOST_PROJECT) / "workspace" / "workspaces"): {
                        "bind": str(WORKSPACES_ROOT), "mode": "ro",
                    },
                },
                restart_policy={"Name": "unless-stopped"},
            )

            with get_conn(DB_PATH) as conn:
                conn.execute(
                    "INSERT OR REPLACE INTO spawned_agents "
                    "(slug, container, ports, model, status, session_type, workspace_slug, team_slug, created_at) "
                    "VALUES (?, ?, ?, ?, 'running', 'production', ?, ?, ?)",
                    (agent_slug, container_name, f"0,{chat_port}", model,
                     agent_slug, slug, int(time.time())),
                )

            spawned.append(agent_slug)
            team_json_members.append({"slug": agent_slug, "role": role, "chat_port": chat_port})

        # Write team.json before starting manager
        team_json = {
            "name":    slug,
            "manager": manager_slug,
            "members": team_json_members,
        }
        (team_root / "team.json").write_text(json.dumps(team_json, indent=2) + "\n", encoding="utf-8")

        # Spawn manager
        manager_path_container = str(team_root)
        manager_path_host = str(
            Path(HOST_PROJECT) / "workspace" / "workspaces" / "teams" / slug
        )

        with get_conn(DB_PATH) as conn:
            existing_mgr = conn.execute(
                "SELECT container FROM spawned_agents WHERE slug=? AND status='running'",
                (manager_slug,),
            ).fetchone()

        if not existing_mgr:
            mgr_port = _claim_port(_TEAM_MANAGER_BAND, used)
            used.add(mgr_port)
            container_name = f"nvnnnbt-team-{manager_slug}"

            dc.containers.run(
                AGENT_IMAGE,
                name=container_name,
                detach=True,
                network=COMPOSE_NETWORK,
                ports={"6161/tcp": ("127.0.0.1", mgr_port)},
                environment={
                    "WORKSPACE_PATH":  manager_path_container,
                    "SKILLSETS_PATH":  str(WORKSPACES_ROOT),
                    "AGENT_PORT":      "6161",
                    "AGENT_MODE":      "production",
                    "OLLAMA_BASE_URL": OLLAMA_URL,
                },
                volumes={
                    manager_path_host: {"bind": manager_path_container, "mode": "rw"},
                    str(Path(HOST_PROJECT) / "workspace" / "workspaces"): {
                        "bind": str(WORKSPACES_ROOT), "mode": "ro",
                    },
                },
                restart_policy={"Name": "unless-stopped"},
            )

            with get_conn(DB_PATH) as conn:
                conn.execute(
                    "INSERT OR REPLACE INTO spawned_agents "
                    "(slug, container, ports, model, status, session_type, workspace_slug, team_slug, created_at) "
                    "VALUES (?, ?, ?, ?, 'running', 'production', ?, ?, ?)",
                    (manager_slug, container_name, f"0,{mgr_port}", "qwen3:1.7b",
                     manager_slug, slug, int(time.time())),
                )
            spawned.append(manager_slug)

        # Update team with manager slug + mode
        with get_conn(DB_PATH) as conn:
            conn.execute(
                "UPDATE agent_teams SET orchestrator_slug=?, mode=? WHERE slug=?",
                (manager_slug, body.mode, slug),
            )

    except (docker.errors.ImageNotFound, docker.errors.APIError) as e:
        raise HTTPException(status_code=500, detail=str(e))

    log_event("team_spawn", target_type="team", target_slug=slug,
              detail=f"Team '{slug}' spawned: {spawned}")
    return {"ok": True, "slug": slug, "spawned": spawned, "team_json": team_json}


# ── Stop team ─────────────────────────────────────────────────────────────────

@router.post("/{slug}/stop")
async def stop_team(slug: str) -> dict:
    with get_conn(DB_PATH) as conn:
        row = conn.execute("SELECT slug FROM agent_teams WHERE slug=?", (slug,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Team '{slug}' not found")

    # All agents for this team
    with get_conn(DB_PATH) as conn:
        agents = conn.execute(
            "SELECT slug, container FROM spawned_agents WHERE team_slug=? AND status='running'",
            (slug,),
        ).fetchall()

    dc = _docker_client()
    stopped = []
    for agent_slug, container in agents:
        try:
            c = dc.containers.get(container)
            c.stop(timeout=10)
        except docker.errors.NotFound:
            pass
        with get_conn(DB_PATH) as conn:
            conn.execute("UPDATE spawned_agents SET status='stopped' WHERE slug=?", (agent_slug,))
        stopped.append(agent_slug)

    log_event("team_stop", target_type="team", target_slug=slug,
              detail=f"Team '{slug}' stopped: {stopped}")
    return {"ok": True, "stopped": stopped}


# ── Delete team ───────────────────────────────────────────────────────────────

@router.delete("/{slug}")
async def delete_team(slug: str) -> dict:
    with get_conn(DB_PATH) as conn:
        row = conn.execute("SELECT slug FROM agent_teams WHERE slug=?", (slug,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Team '{slug}' not found")

    # Stop and remove all containers
    with get_conn(DB_PATH) as conn:
        agents = conn.execute(
            "SELECT slug, container FROM spawned_agents WHERE team_slug=?", (slug,)
        ).fetchall()

    dc = _docker_client()
    for agent_slug, container in agents:
        try:
            c = dc.containers.get(container)
            c.stop(timeout=5)
            c.remove(force=True)
        except docker.errors.NotFound:
            pass
        with get_conn(DB_PATH) as conn:
            conn.execute("DELETE FROM spawned_agents WHERE slug=?", (agent_slug,))

    # Remove DB rows
    with get_conn(DB_PATH) as conn:
        conn.execute("DELETE FROM team_members WHERE team_slug=?", (slug,))
        conn.execute("DELETE FROM agent_teams WHERE slug=?", (slug,))

    log_event("team_delete", target_type="team", target_slug=slug,
              detail=f"Team '{slug}' deleted (workspace kept)")
    return {"ok": True}
