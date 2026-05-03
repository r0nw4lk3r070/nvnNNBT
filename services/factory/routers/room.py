"""room.py — P2P room chat: local SSE fan-out + peer federation.

Routes (all under /room, proxied from /api/factory/room/ by nginx):
  GET  /room/identity         — returns caller's display name
  GET  /room/sync?since=<ts>  — message history (up to 200, or since timestamp)
  GET  /room/stream           — SSE stream: messages + peer_status + agent tokens
  POST /room/send             — post a message (local author)
  POST /room/receive          — called by peer to deliver their messages here
"""
from __future__ import annotations

import asyncio
import json
import os
import re
import sqlite3
from datetime import datetime, timezone
from typing import AsyncGenerator

import httpx
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

DB_PATH_STR = os.environ.get("DB_PATH", "/app/data/factory.db")
PEER_URL    = (os.environ.get("PEER_URL", "") or "").rstrip("/")
USER_NAME   = os.environ.get("USER_NAME", "user")
AGENT_URL   = os.environ.get("AGENT_URL", "http://agent:6161")

router = APIRouter(prefix="/room", tags=["room"])

# ── In-memory SSE fan-out ─────────────────────────────────────────────────────
_subscribers: set[asyncio.Queue] = set()


def _db() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH_STR)


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def _broadcast(payload: dict) -> None:
    data = json.dumps(payload)
    for q in list(_subscribers):
        try:
            q.put_nowait(data)
        except asyncio.QueueFull:
            pass


def _peer_label() -> str:
    if not PEER_URL:
        return ""
    try:
        from urllib.parse import urlparse
        return urlparse(PEER_URL).hostname or "peer"
    except Exception:
        return "peer"


# ── Identity ──────────────────────────────────────────────────────────────────

@router.get("/identity")
async def get_identity() -> dict:
    return {"name": USER_NAME}


# ── History / sync ────────────────────────────────────────────────────────────

@router.get("/sync")
async def sync(since: str = "") -> dict:
    con = _db()
    if since:
        rows = con.execute(
            "SELECT id, user, text, origin, created_at FROM room_messages "
            "WHERE created_at > ? ORDER BY id ASC",
            (since,),
        ).fetchall()
    else:
        rows = con.execute(
            "SELECT id, user, text, origin, created_at FROM room_messages "
            "ORDER BY id ASC LIMIT 200"
        ).fetchall()
    con.close()
    return {
        "messages": [
            {"id": r[0], "user": r[1], "text": r[2], "origin": r[3], "created_at": r[4]}
            for r in rows
        ]
    }


# ── SSE stream ────────────────────────────────────────────────────────────────

@router.get("/stream")
async def stream() -> StreamingResponse:
    async def _generate() -> AsyncGenerator[str, None]:
        q: asyncio.Queue = asyncio.Queue(maxsize=100)
        _subscribers.add(q)
        try:
            # Announce peer status on connect
            yield (
                f"data: {json.dumps({'type': 'peer_status', 'online': bool(PEER_URL), 'name': _peer_label()})}\n\n"
            )
            while True:
                try:
                    data = await asyncio.wait_for(q.get(), timeout=20)
                    yield f"data: {data}\n\n"
                except asyncio.TimeoutError:
                    yield ": keepalive\n\n"
        except asyncio.CancelledError:
            pass
        finally:
            _subscribers.discard(q)

    return StreamingResponse(
        _generate(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


# ── Send / receive ────────────────────────────────────────────────────────────

class MessageBody(BaseModel):
    text: str
    user: str = ""        # populated when forwarded=True; otherwise USER_NAME is used
    forwarded: bool = False


async def _store_and_broadcast(user: str, text: str, origin: str) -> dict:
    ts = _now()
    con = _db()
    cur = con.execute(
        "INSERT INTO room_messages (user, text, origin, created_at) VALUES (?, ?, ?, ?)",
        (user, text, origin, ts),
    )
    msg_id = cur.lastrowid
    con.commit()
    con.close()
    msg = {"id": msg_id, "user": user, "text": text, "origin": origin, "created_at": ts}
    _broadcast(msg)
    return msg


@router.post("/send")
async def send(body: MessageBody) -> dict:
    text = body.text.strip()
    if not text:
        return {"ok": False, "error": "empty"}

    user   = (body.user.strip() if body.forwarded and body.user else "") or USER_NAME
    origin = "peer" if body.forwarded else "local"
    msg    = await _store_and_broadcast(user, text, origin)

    # Forward to peer for locally-authored messages only
    if not body.forwarded and PEER_URL:
        asyncio.create_task(_forward_to_peer(text, user))

    # @mention triggers agent
    if re.search(r"@\w", text):
        asyncio.create_task(_invoke_agent(text))

    return {"ok": True, "id": msg["id"]}


@router.post("/receive")
async def receive(body: MessageBody) -> dict:
    """Called by the peer to deliver their messages into our room."""
    body.forwarded = True
    return await send(body)


# ── Federation helpers ────────────────────────────────────────────────────────

async def _forward_to_peer(text: str, user: str) -> None:
    """POST our message to the peer's /receive endpoint. Silently drops if offline."""
    if not PEER_URL:
        return
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            await client.post(
                f"{PEER_URL}/api/factory/room/receive",
                json={"text": text, "user": user, "forwarded": True},
            )
    except Exception:
        pass  # peer offline — they can sync via GET /room/sync?since=<ts> on reconnect


async def _invoke_agent(text: str) -> None:
    """Stream agent response tokens into the room, then persist the full reply."""
    mention = re.search(r"@(\w[\w-]*)", text)
    agent_name = mention.group(1) if mention else "art"

    _broadcast({"type": "agent_token", "agent": agent_name, "token": ""})
    full = ""
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            async with client.stream(
                "POST",
                f"{AGENT_URL}/chat",
                json={"messages": [{"role": "user", "content": text}]},
            ) as r:
                async for line in r.aiter_lines():
                    if not line.startswith("data: "):
                        continue
                    raw = line[6:].strip()
                    if raw == "[DONE]":
                        break
                    try:
                        d = json.loads(raw)
                        token = (
                            d.get("choices", [{}])[0].get("delta", {}).get("content")
                            or d.get("text")
                            or ""
                        )
                        if token:
                            full += token
                            _broadcast({"type": "agent_token", "agent": agent_name, "token": token})
                    except Exception:
                        pass
    except Exception:
        pass

    _broadcast({"type": "agent_done", "agent": agent_name})

    if full:
        msg = await _store_and_broadcast(agent_name, full, "agent")
        # Forward agent reply to peer too
        if PEER_URL:
            asyncio.create_task(_forward_to_peer(full, agent_name))
