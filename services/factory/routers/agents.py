"""agents.py — Spawned agent registry: list, spawn, stop, delete."""
from __future__ import annotations

import os
import time
from pathlib import Path

import docker
import docker.errors
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database import DB_PATH, get_conn
from routers.events import log_event

router = APIRouter(prefix="/agents", tags=["agents"])

# ── Config ────────────────────────────────────────────────────────────────────
AGENT_IMAGE      = os.environ.get("AGENT_IMAGE",      "nvnnnbt-agent:latest")
COMPOSE_NETWORK  = os.environ.get("COMPOSE_NETWORK",  "nvnnnbt-net")
OLLAMA_URL       = os.environ.get("OLLAMA_BASE_URL",   "http://ollama:11434")
HOST_PROJECT     = os.environ.get("HOST_PROJECT_PATH", "")   # absolute path on HOST machine

# Port bands (from factory.md)
_GATEWAY_BAND = range(4230, 4300)
_CHAT_BAND    = range(4330, 4400)

# ── Helpers ───────────────────────────────────────────────────────────────────

def _docker_client():
    try:
        return docker.from_env()
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Docker unavailable: {e}")


def _claim_port(band: range, used: set[int]) -> int:
    for p in band:
        if p not in used:
            return p
    raise HTTPException(status_code=507, detail="No free ports in band")


def _used_ports() -> set[int]:
    with get_conn(DB_PATH) as conn:
        rows = conn.execute("SELECT ports FROM spawned_agents WHERE status = 'running'").fetchall()
    ports: set[int] = set()
    for row in rows:
        if row[0]:
            for v in row[0].split(","):
                v = v.strip()
                if v.isdigit():
                    ports.add(int(v))
    return ports


# ── List agents ───────────────────────────────────────────────────────────────

@router.get("")
async def list_agents() -> dict:
    with get_conn(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT slug, container, ports, model, status, session_type, created_at "
            "FROM spawned_agents ORDER BY created_at DESC"
        ).fetchall()
    agents = [
        {
            "slug":         r[0],
            "container":    r[1],
            "ports":        r[2],
            "model":        r[3],
            "status":       r[4],
            "session_type": r[5],
            "created_at":   r[6],
        }
        for r in rows
    ]
    # Sync live container status
    try:
        dc = _docker_client()
        for a in agents:
            if a["container"]:
                try:
                    c = dc.containers.get(a["container"])
                    live = c.status   # "running", "exited", etc.
                    if live != a["status"]:
                        a["status"] = live
                        with get_conn(DB_PATH) as conn:
                            conn.execute(
                                "UPDATE spawned_agents SET status=? WHERE container=?",
                                (live, a["container"]),
                            )
                except docker.errors.NotFound:
                    a["status"] = "missing"
    except HTTPException:
        pass
    return {"agents": agents}


# ── Spawn agent ───────────────────────────────────────────────────────────────

class SpawnBody(BaseModel):
    slug: str
    model: str = "qwen3:1.7b"
    grok_api_key: str = ""


@router.post("")
async def spawn_agent(body: SpawnBody) -> dict:
    if not HOST_PROJECT:
        raise HTTPException(
            status_code=503,
            detail="HOST_PROJECT_PATH env var not set — required for bind-mounting workspace",
        )

    # Validate workspace exists
    ws_path_container = f"/app/data/workspaces/{body.slug}"
    ws_path_host = Path(HOST_PROJECT) / "data" / "workspaces" / body.slug
    if not ws_path_host.exists():
        raise HTTPException(status_code=404, detail=f"Workspace '{body.slug}' not found")

    # Check not already running
    with get_conn(DB_PATH) as conn:
        existing = conn.execute(
            "SELECT container FROM spawned_agents WHERE slug=? AND status='running'",
            (body.slug,),
        ).fetchone()
    if existing:
        raise HTTPException(status_code=409, detail=f"Agent '{body.slug}' is already running")

    used = _used_ports()
    gateway_port = _claim_port(_GATEWAY_BAND, used)
    chat_port    = _claim_port(_CHAT_BAND, used | {gateway_port})

    container_name = f"nvnnnbt-agent-{body.slug}"
    dc = _docker_client()

    try:
        container = dc.containers.run(
            AGENT_IMAGE,
            name=container_name,
            detach=True,
            network=COMPOSE_NETWORK,
            ports={
                "6161/tcp": ("127.0.0.1", chat_port),
            },
            environment={
                "WORKSPACE_PATH": ws_path_container,
                "SKILLSETS_PATH": "/app/data/workspaces",
                "AGENT_PORT":     "6161",
                "OLLAMA_BASE_URL": OLLAMA_URL,
                "GROK_API_KEY":   body.grok_api_key,
            },
            volumes={
                str(ws_path_host): {"bind": ws_path_container, "mode": "rw"},
                str(Path(HOST_PROJECT) / "data" / "workspaces"): {
                    "bind": "/app/data/workspaces", "mode": "ro",
                },
            },
            restart_policy={"Name": "unless-stopped"},
        )
    except docker.errors.ImageNotFound:
        raise HTTPException(status_code=503, detail=f"Image '{AGENT_IMAGE}' not found")
    except docker.errors.APIError as e:
        raise HTTPException(status_code=500, detail=str(e))

    ports_str = f"{gateway_port},{chat_port}"
    with get_conn(DB_PATH) as conn:
        conn.execute(
            "INSERT OR REPLACE INTO spawned_agents "
            "(slug, container, ports, model, status, session_type, created_at) "
            "VALUES (?, ?, ?, ?, 'running', 'production', ?)",
            (body.slug, container_name, ports_str, body.model, int(time.time())),
        )

    log_event("agent_spawn", target_type="agent", target_slug=body.slug,
              detail=f"Spawned '{body.slug}' on chat_port={chat_port}")
    return {"ok": True, "slug": body.slug, "container": container_name,
            "chat_port": chat_port}


# ── Stop agent ────────────────────────────────────────────────────────────────

@router.post("/{slug}/stop")
async def stop_agent(slug: str) -> dict:
    with get_conn(DB_PATH) as conn:
        row = conn.execute(
            "SELECT container FROM spawned_agents WHERE slug=? AND status='running'",
            (slug,),
        ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"No running agent '{slug}'")

    dc = _docker_client()
    try:
        c = dc.containers.get(row[0])
        c.stop(timeout=10)
    except docker.errors.NotFound:
        pass

    with get_conn(DB_PATH) as conn:
        conn.execute("UPDATE spawned_agents SET status='stopped' WHERE slug=?", (slug,))

    log_event("agent_stop", target_type="agent", target_slug=slug,
              detail=f"Agent '{slug}' stopped")
    return {"ok": True}


# ── Delete agent ──────────────────────────────────────────────────────────────

@router.delete("/{slug}")
async def delete_agent(slug: str) -> dict:
    with get_conn(DB_PATH) as conn:
        row = conn.execute(
            "SELECT container FROM spawned_agents WHERE slug=?", (slug,)
        ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"No agent record for '{slug}'")

    dc = _docker_client()
    try:
        c = dc.containers.get(row[0])
        c.stop(timeout=5)
        c.remove(force=True)
    except docker.errors.NotFound:
        pass

    with get_conn(DB_PATH) as conn:
        conn.execute("DELETE FROM spawned_agents WHERE slug=?", (slug,))

    log_event("agent_stop", target_type="agent", target_slug=slug,
              detail=f"Agent '{slug}' deleted")
    return {"ok": True}
