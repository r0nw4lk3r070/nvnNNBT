"""main.py — Agent Factory API service.

Phase 1: health endpoint + SQLite init + events + workspaces + system stats.
Subsequent phases add routers for agents, teams, arena, benchmark.
"""
from __future__ import annotations

import os
from contextlib import asynccontextmanager
from pathlib import Path

import httpx
from fastapi import FastAPI, Header, HTTPException

from database import DB_PATH, init_db
from routers import events as events_router
from routers import workspaces as workspaces_router
from routers import system as system_router

# ── Config ────────────────────────────────────────────────────────────────────
AGENT_URL     = os.environ.get("AGENT_URL",       "http://agent:6161")
OLLAMA_URL    = os.environ.get("OLLAMA_BASE_URL",  "http://ollama:11434")
_DB_PATH      = Path(os.environ.get("DB_PATH",    str(DB_PATH)))
FACTORY_TOKEN = os.environ.get("FACTORY_TOKEN",   "")          # empty = no auth

# ── Auth dependency (optional) ────────────────────────────────────────────────
def _check_token(x_factory_token: str = Header(default="")) -> None:
    if FACTORY_TOKEN and x_factory_token != FACTORY_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

# ── Startup ───────────────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db(_DB_PATH)
    events_router.log_event("factory_started", detail="Factory service started")
    yield


app = FastAPI(title="Agent Factory", version="0.1.0", lifespan=lifespan)

app.include_router(events_router.router)
app.include_router(workspaces_router.router)
app.include_router(system_router.router)


# ── Health ────────────────────────────────────────────────────────────────────
@app.get("/health")
async def health() -> dict:
    """
    Returns factory status and probes downstream services.
    Response shape:
      { "status": "ok", "services": { "agent": "ok|warn|err", "ollama": "ok|warn|err" } }
    """
    services: dict[str, str] = {}

    async with httpx.AsyncClient(timeout=3.0) as client:
        # Agent
        try:
            r = await client.get(f"{AGENT_URL}/health")
            services["agent"] = "ok" if r.status_code == 200 else "warn"
        except Exception:
            services["agent"] = "err"

        # Ollama
        try:
            r = await client.get(f"{OLLAMA_URL}/api/tags")
            services["ollama"] = "ok" if r.status_code == 200 else "warn"
        except Exception:
            services["ollama"] = "err"

    return {"status": "ok", "services": services}
