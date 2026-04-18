"""main.py — Agent Factory API service.

Phase 1: health endpoint + SQLite init + events + workspaces + system stats.
Subsequent phases add routers for agents, teams, arena, benchmark.
"""
from __future__ import annotations

import asyncio
import os
from contextlib import asynccontextmanager
from pathlib import Path

import httpx
from fastapi import FastAPI, Header, HTTPException

from database import DB_PATH, init_db
from routers import events as events_router
from routers import workspaces as workspaces_router
from routers import system as system_router
from routers import sandbox as sandbox_router
from routers import agents as agents_router
from routers import teams as teams_router
from routers import benchmark as benchmark_router

# ── Config ────────────────────────────────────────────────────────────────────
AGENT_URL     = os.environ.get("AGENT_URL",       "http://agent:6161")
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
app.include_router(sandbox_router.router)
app.include_router(agents_router.router)
app.include_router(teams_router.router)
app.include_router(benchmark_router.router)


# ── Health ────────────────────────────────────────────────────────────────────
@app.get("/health")
async def health() -> dict:
    """
    Returns factory status and probes all configured providers dynamically.
    Response shape:
      { "status": "ok", "services": { "agent": "ok|warn|err", "<provider>": "ok|warn|err", ... } }
    """
    services: dict[str, str] = {}

    async with httpx.AsyncClient(timeout=3.0) as client:
        # Agent
        try:
            r = await client.get(f"{AGENT_URL}/health")
            services["agent"] = "ok" if r.status_code == 200 else "warn"
        except Exception:
            services["agent"] = "err"

        # Dynamically probe all configured providers
        if services["agent"] != "err":
            try:
                r = await client.get(f"{AGENT_URL}/api/providers")
                if r.status_code == 200:
                    providers = r.json().get("providers", [])

                    async def _probe(p: dict) -> tuple[str, str]:
                        base = (p.get("apiBase") or "").rstrip("/")
                        name = p.get("name", "unknown")
                        if not base:
                            return name, "warn"
                        try:
                            resp = await client.get(f"{base}/models", timeout=3.0)
                            # <500 covers 200 (ok) and 401/403/405 (reachable, auth wall)
                            return name, "ok" if resp.status_code < 500 else "warn"
                        except Exception:
                            return name, "err"

                    results = await asyncio.gather(*[_probe(p) for p in providers])
                    for name, status in results:
                        services[name] = status
            except Exception:
                pass  # agent unreachable — already recorded above

    return {"status": "ok", "services": services}
