"""sandbox.py — Lab sandbox: proxy workspace test sessions through the agent service."""
from __future__ import annotations

import os
from pathlib import Path

import httpx
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from routers.events import log_event

AGENT_URL       = os.environ.get("AGENT_URL", "http://agent:6161")
WORKSPACES_ROOT = Path(os.environ.get("WORKSPACES_ROOT", "/app/data/workspaces"))

router = APIRouter(prefix="/sandbox", tags=["sandbox"])


# ── Load workspace into lab ───────────────────────────────────────────────────

class LoadBody(BaseModel):
    slug: str
    model: str = ""
    provider: str = ""


@router.post("/load")
async def sandbox_load(body: LoadBody) -> dict:
    ws = WORKSPACES_ROOT / body.slug
    if not ws.exists():
        raise HTTPException(status_code=404, detail=f"Workspace '{body.slug}' not found")

    # The agent service expects a path relative to its /skill-sets mount.
    # WORKSPACES_ROOT inside factory = /app/data/workspaces
    # Agent container mounts: ./data/workspaces → /skill-sets
    # So the slug is the skill-set name from the agent's perspective.
    payload: dict = {"name": body.slug}
    if body.model:
        payload["model"] = body.model
    if body.provider:
        payload["provider"] = body.provider

    async with httpx.AsyncClient(base_url=AGENT_URL, timeout=30) as client:
        r = await client.post("/api/lab/load", json=payload)
        if r.status_code != 200:
            raise HTTPException(status_code=r.status_code, detail=r.text)

    log_event("lab_session_open", target_type="workspace", target_slug=body.slug,
              detail=f"Lab session opened for '{body.slug}'")
    return r.json()


# ── Sandbox status ────────────────────────────────────────────────────────────

@router.get("/status")
async def sandbox_status() -> dict:
    async with httpx.AsyncClient(base_url=AGENT_URL, timeout=10) as client:
        r = await client.get("/api/lab/status")
        if r.status_code != 200:
            return {"loaded": False}
    return r.json()


# ── Sandbox chat (SSE proxy) ──────────────────────────────────────────────────

class ChatBody(BaseModel):
    messages: list[dict]


@router.post("/chat")
async def sandbox_chat(body: ChatBody) -> StreamingResponse:
    async def _stream():
        async with httpx.AsyncClient(base_url=AGENT_URL, timeout=None) as client:
            async with client.stream(
                "POST", "/lab/chat",
                json={"messages": body.messages},
                headers={"Content-Type": "application/json"},
            ) as r:
                async for chunk in r.aiter_bytes():
                    yield chunk

    return StreamingResponse(
        _stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection":    "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


# ── Stop sandbox ──────────────────────────────────────────────────────────────

@router.post("/stop")
async def sandbox_stop() -> dict:
    async with httpx.AsyncClient(base_url=AGENT_URL, timeout=10) as client:
        r = await client.post("/api/lab/stop")
        if r.status_code != 200:
            raise HTTPException(status_code=r.status_code, detail=r.text)

    log_event("lab_session_close", detail="Lab session closed")
    return {"ok": True}


# ── Unload workspace ──────────────────────────────────────────────────────────

@router.post("/unload")
async def sandbox_unload() -> dict:
    async with httpx.AsyncClient(base_url=AGENT_URL, timeout=10) as client:
        r = await client.post("/api/lab/unload")
        if r.status_code != 200:
            raise HTTPException(status_code=r.status_code, detail=r.text)

    log_event("lab_session_close", detail="Lab session unloaded")
    return {"ok": True}
