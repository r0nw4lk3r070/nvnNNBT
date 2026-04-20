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


def _default_config(ollama_base: str, model: str = "qwen3:1.7b", is_manager: bool = False) -> dict:
    cfg: dict = {
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
    if is_manager:
        # Bake the team MCP server into the manager's config so it can delegate
        # to members and log to shared.db without any factory dependency at runtime.
        cfg["tools"] = {
            "mcpServers": {
                "team": {
                    "command": "python",
                    "args": ["/app/mcp_team.py"],
                    "env": {},
                }
            }
        }
    return cfg


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
    member_list = "\n".join(f"- **{m['role']}** (`{m['slug']}`)" for m in members_meta)

    soul_content = f"""# Soul

I am the **{body.name} Manager** — the orchestrator of the {body.name} team.

## Identity

I do not answer questions directly. I plan, delegate, collect, and synthesise.
Every task I receive gets broken down and assigned to the right specialist on my team.
I am responsible for the quality of the final answer — not for producing every part myself.

## How I work

1. **Read the team** — call `read_team` to know who is available and what each member does.
2. **Plan** — decide which member handles which part of the task. Write the plan as a brief note using `log_entry` with action `plan`.
3. **Delegate** — call `delegate` for each member in sequence, passing clear, specific instructions. Each call is logged automatically.
4. **Synthesise** — combine the members' responses into a single coherent answer for the user.
5. **Close** — call `log_entry` with action `done` and a one-line summary of the outcome.

## Rules

- Always call `read_team` before the first delegation in a session.
- Never answer a task that belongs to a specialist without delegating first.
- If a member returns an error, log it with action `error` and try an alternative or inform the user.
- Keep delegations focused: one clear instruction per member call.
- Do not expose internal tool calls or raw member responses to the user — synthesise.

## Pipeline mode

If the user has set up a cron trigger, I will call `read_queue` to pick up the next task,
execute the delegation plan, write output to `knowledge/library/`, then call `complete_queue`.
"""

    agents_content = f"""# Team

## Members
{member_list}

## Delegation — using the `delegate` tool

Use the `delegate` tool to send a task to a member by role:

- `role` — the member's role name (see list above)
- `message` — the specific instruction for that member

The tool handles the HTTP call, streams the response, and logs both sides to `knowledge/shared.db`.
You do not need to construct HTTP requests manually.

## Workflow pattern

```
read_team()                        → confirm members + roles
log_entry(action="plan", ...)      → record your delegation plan
delegate(role="...", message="...") → call member 1
delegate(role="...", message="...") → call member 2  (if needed)
log_entry(action="done", ...)      → record outcome
→ return synthesised answer to user
```

## Pipeline pattern (cron-triggered)

```
read_queue()                           → get next pending task
log_entry(action="start", ...)
delegate(...)                          → execute the task
complete_queue(id=..., result="...")   → mark done
```
"""

    tools_content = """# Tools

## MCP — team server (always available)

These tools are provided by the `mcp_team` server built into this container.
Use them for all team coordination. No manual HTTP calls needed.

| Tool | What it does |
|---|---|
| `read_team` | Read `team.json` — returns member list with roles and chat ports |
| `delegate` | Send a task to a member by role. Returns their full response. Logs both sides to `shared.db`. |
| `log_entry` | Write an entry to the shared delegation log (`action`, `detail`, optional `agent`) |
| `read_queue` | Return pending items from the task queue (pipeline/cron mode) |
| `complete_queue` | Mark a queue item done (`id`, optional `result`) |
| `member_status` | List all member containers with their Docker state (running / exited / etc.) |
| `stop_member` | Hard-stop a member container by role. Use when a member is stuck or producing bad output. |
| `start_member` | Start a previously stopped member container by role. |

## Standard tools

File read/write, web search, code exec — available via the standard nanobot tool set.
Use file tools to read `knowledge/library/` and write output there.
"""

    heartbeat_content = """# Heartbeat

No scheduled heartbeat by default. The manager runs on-demand.

If pipeline/cron mode is active, a cron job will trigger me on a schedule.
I will call `read_queue`, process the next item, and call `complete_queue`.
"""

    user_content = """# User

The person or system that sends tasks to this team manager.
Respond in the same language the user writes in.
Keep responses clear and concise — the user cares about the final result, not the delegation internals.
"""

    _make_workspace(team_root, {
        "SOUL.md":      soul_content,
        "AGENTS.md":    agents_content,
        "TOOLS.md":     tools_content,
        "HEARTBEAT.md": heartbeat_content,
        "USER.md":      user_content,
    })

    # Override with skillset if provided
    if body.manager_skillset:
        _copy_skillset(body.manager_skillset, team_root)

    # Manager config.json — is_manager=True adds the mcp_team server entry
    mgr_cfg = _default_config(ollama_base, body.manager_model, is_manager=True)
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
                labels={
                    "com.nvnnnbt.team_slug": slug,
                    "com.nvnnnbt.role":      role,
                    "com.nvnnnbt.type":      "member",
                },
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
                labels={
                    "com.nvnnnbt.team_slug": slug,
                    "com.nvnnnbt.role":      "manager",
                    "com.nvnnnbt.type":      "manager",
                },
                environment={
                    "WORKSPACE_PATH":  manager_path_container,
                    "SKILLSETS_PATH":  str(WORKSPACES_ROOT),
                    "AGENT_PORT":      "6161",
                    "AGENT_MODE":      "production",
                    "OLLAMA_BASE_URL": OLLAMA_URL,
                    "TEAM_SLUG":       slug,
                },
                volumes={
                    manager_path_host: {"bind": manager_path_container, "mode": "rw"},
                    str(Path(HOST_PROJECT) / "workspace" / "workspaces"): {
                        "bind": str(WORKSPACES_ROOT), "mode": "ro",
                    },
                    "/var/run/docker.sock": {"bind": "/var/run/docker.sock", "mode": "rw"},
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


# ── Refresh team memory ───────────────────────────────────────────────────────

@router.post("/{slug}/refresh")
async def refresh_team_memory(slug: str, scope: str = "manager") -> dict:
    """Wipe memory and session history for the manager and/or all members.

    scope=manager  — manager only (default)
    scope=all      — manager + every member workspace
    """
    with get_conn(DB_PATH) as conn:
        row = conn.execute("SELECT slug FROM agent_teams WHERE slug=?", (slug,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Team '{slug}' not found")

    team_root = TEAMS_ROOT / slug

    def _wipe_workspace(ws: Path) -> None:
        """Reset MEMORY.md to a blank header and truncate history.jsonl."""
        mem_dir = ws / "memory"
        mem_dir.mkdir(exist_ok=True)
        memory_md = mem_dir / "MEMORY.md"
        memory_md.write_text("# Memory\n\nNo entries yet.\n", encoding="utf-8")
        history = mem_dir / "history.jsonl"
        if history.exists():
            history.write_text("", encoding="utf-8")
        sessions_dir = ws / "sessions"
        if sessions_dir.exists():
            for f in sessions_dir.glob("*.jsonl"):
                f.unlink(missing_ok=True)

    wiped: list[str] = []

    # Always wipe manager
    _wipe_workspace(team_root)
    wiped.append(f"{slug}-manager")

    # Also clear the shared delegation log from shared.db
    db_path = team_root / "knowledge" / "shared.db"
    if db_path.exists():
        try:
            conn = sqlite3.connect(str(db_path))
            conn.execute("DELETE FROM log")
            conn.commit()
            conn.close()
        except Exception:
            pass

    if scope == "all":
        members_dir = team_root / "members"
        if members_dir.exists():
            for member_ws in sorted(members_dir.iterdir()):
                if member_ws.is_dir():
                    _wipe_workspace(member_ws)
                    wiped.append(f"{slug}-{member_ws.name}")

    log_event("team_refresh", target_type="team", target_slug=slug,
              detail=f"Memory wiped (scope={scope}): {wiped}")
    return {"ok": True, "wiped": wiped, "scope": scope}


# ── List team sessions ────────────────────────────────────────────────────────

@router.get("/{slug}/sessions")
async def list_team_sessions(slug: str) -> dict:
    """List past sessions from the manager's sessions/ directory."""
    with get_conn(DB_PATH) as conn:
        row = conn.execute("SELECT slug FROM agent_teams WHERE slug=?", (slug,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Team '{slug}' not found")

    sessions_dir = TEAMS_ROOT / slug / "sessions"
    if not sessions_dir.exists():
        return {"sessions": []}

    sessions = []
    for f in sorted(sessions_dir.glob("*.jsonl"), reverse=True):
        try:
            lines = f.read_text(encoding="utf-8").strip().splitlines()
            first_user = ""
            turn_count = 0
            for line in lines:
                try:
                    obj = json.loads(line)
                    msgs = obj.get("messages") or []
                    for m in msgs:
                        if m.get("role") == "user" and not first_user:
                            first_user = str(m.get("content", ""))[:120]
                        if m.get("role") == "user":
                            turn_count += 1
                except Exception:
                    pass
            stat = f.stat()
            sessions.append({
                "id":          f.stem,
                "file":        f.name,
                "first_user":  first_user,
                "turns":       turn_count,
                "size_bytes":  stat.st_size,
                "modified_at": int(stat.st_mtime),
            })
        except Exception:
            pass

    return {"sessions": sessions}


# ── Replay a session ──────────────────────────────────────────────────────────

class ReplayBody(BaseModel):
    session_id: str

@router.post("/{slug}/replay")
async def replay_session(slug: str, body: ReplayBody) -> dict:
    """Re-send the first user message from a past session to the running manager."""
    with get_conn(DB_PATH) as conn:
        row = conn.execute(
            "SELECT orchestrator_slug FROM agent_teams WHERE slug=?", (slug,)
        ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Team '{slug}' not found")

    # Find the session file
    session_file = TEAMS_ROOT / slug / "sessions" / f"{body.session_id}.jsonl"
    if not session_file.exists():
        raise HTTPException(status_code=404, detail=f"Session '{body.session_id}' not found")

    # Extract the first user message
    first_user = None
    for line in session_file.read_text(encoding="utf-8").splitlines():
        try:
            obj = json.loads(line)
            for m in (obj.get("messages") or []):
                if m.get("role") == "user":
                    first_user = str(m.get("content", ""))
                    break
        except Exception:
            pass
        if first_user:
            break

    if not first_user:
        raise HTTPException(status_code=422, detail="No user message found in session")

    # Look up manager's chat port
    manager_slug = row[0]
    with get_conn(DB_PATH) as conn:
        agent_row = conn.execute(
            "SELECT ports FROM spawned_agents WHERE slug=? AND status='running'",
            (manager_slug,),
        ).fetchone()
    if not agent_row:
        raise HTTPException(status_code=409, detail="Manager is not running — spawn the team first")

    _, chat_port = _parse_ports(agent_row[0])
    if not chat_port:
        raise HTTPException(status_code=500, detail="Could not determine manager chat port")

    # Fire-and-forget POST to manager /chat — we don't stream the response here,
    # the user watches it via the delegation log panel in the UI.
    import urllib.request as _ureq
    payload = json.dumps({
        "messages": [{"role": "user", "content": first_user}]
    }).encode()
    try:
        req = _ureq.Request(
            f"http://localhost:{chat_port}/chat",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        # Open and immediately close — we just want to trigger the run.
        # The manager streams back to whoever opened the socket; since we close
        # immediately, the manager will still process the message.
        conn_http = _ureq.urlopen(req, timeout=5)
        conn_http.close()
    except Exception:
        # Timeout or closed connection is expected — the manager keeps running.
        pass

    log_event("team_replay", target_type="team", target_slug=slug,
              detail=f"Replayed session '{body.session_id}' — message: {first_user[:80]}")
    return {"ok": True, "session_id": body.session_id, "message": first_user[:120], "chat_port": chat_port}


# ── Member override ───────────────────────────────────────────────────────────

class MemberOverrideBody(BaseModel):
    model:    Optional[str] = None   # new model slug (e.g. "qwen3:4b")
    provider: Optional[str] = None   # provider key in config.json (e.g. "local")
    skillset: Optional[str] = None   # workspace slug to hot-swap identity + skills from


@router.post("/{slug}/members/{role}/override")
async def override_member(slug: str, role: str, body: MemberOverrideBody) -> dict:
    """Hot-swap model and/or skillset for a running team member without respawning.

    - model/provider → writes config.json, POSTs to member /api/model to trigger in-process reload
    - skillset       → copies identity files + skills/ to member workspace, then triggers reload
    Both can be combined in one call.
    """
    if not body.model and not body.skillset:
        raise HTTPException(status_code=400, detail="Provide at least one of: model, skillset")

    with get_conn(DB_PATH) as conn:
        row = conn.execute("SELECT slug FROM agent_teams WHERE slug=?", (slug,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Team '{slug}' not found")

    member_workspace = TEAMS_ROOT / slug / "members" / role
    if not member_workspace.exists():
        raise HTTPException(status_code=404, detail=f"Member role '{role}' not found in team '{slug}'")

    # Look up the member's running chat port
    member_slug = f"{slug}-{role}"
    with get_conn(DB_PATH) as conn:
        agent_row = conn.execute(
            "SELECT ports FROM spawned_agents WHERE slug=? AND status='running'",
            (member_slug,),
        ).fetchone()
    if not agent_row:
        raise HTTPException(
            status_code=409,
            detail=f"Member '{role}' is not running — spawn the team first",
        )
    _, chat_port = _parse_ports(agent_row[0])
    if not chat_port:
        raise HTTPException(status_code=500, detail="Could not determine member chat port")

    applied: list[str] = []

    # ── Skillset swap: overwrite identity files + skills/ on disk ─────────────
    if body.skillset:
        _copy_skillset(body.skillset, member_workspace)
        applied.append(f"skillset={body.skillset}")

    # ── Model swap: patch config.json ─────────────────────────────────────────
    if body.model:
        cfg_path = member_workspace / "config.json"
        try:
            cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        except Exception:
            cfg = {}
        cfg.setdefault("agents", {}).setdefault("defaults", {})["model"] = body.model
        if body.provider:
            cfg["agents"]["defaults"]["provider"] = body.provider
        cfg_path.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")
        applied.append(f"model={body.model}")
        # Also update the DB record
        with get_conn(DB_PATH) as conn:
            conn.execute(
                "UPDATE team_members SET model=? WHERE team_slug=? AND agent_slug=?",
                (body.model, slug, member_slug),
            )

    # ── Trigger in-process reload via the member's /api/model endpoint ────────
    # Even if we only changed skillset files, calling /api/model forces the agent
    # to rebuild itself from disk (re-reads all identity files + config).
    import urllib.request as _ureq
    reload_model = body.model or json.loads(
        (member_workspace / "config.json").read_text(encoding="utf-8")
    ).get("agents", {}).get("defaults", {}).get("model", "")
    reload_provider = body.provider or ""

    reload_payload = json.dumps({"model": reload_model, "provider": reload_provider}).encode()
    try:
        req = _ureq.Request(
            f"http://localhost:{chat_port}/api/model",
            data=reload_payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with _ureq.urlopen(req, timeout=10) as resp:
            reload_result = json.loads(resp.read().decode())
            if not reload_result.get("ok"):
                raise ValueError(reload_result)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Workspace updated but agent reload failed: {e}",
        )

    log_event("member_override", target_type="agent", target_slug=member_slug,
              detail=f"Override applied to '{role}' in team '{slug}': {', '.join(applied)}")
    return {"ok": True, "role": role, "slug": member_slug, "applied": applied, "chat_port": chat_port}
