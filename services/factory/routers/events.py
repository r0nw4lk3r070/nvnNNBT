"""events.py — Factory event log: write, read, and SSE stream."""
from __future__ import annotations

import asyncio
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import AsyncGenerator

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

DB_PATH = Path(os.environ.get("DB_PATH", "/app/data/factory.db"))

router = APIRouter(prefix="/events", tags=["events"])

# ── In-memory fan-out to SSE subscribers ─────────────────────────────────────
_subscribers: set[asyncio.Queue] = set()


# ── Internal write helper (called from other routers and main) ────────────────

def log_event(
    type: str,
    target_type: str = "",
    target_slug: str = "",
    detail: str = "",
    level: str = "info",
    actor: str = "factory",
) -> None:
    """Write one event row, enforce 1 000-row rolling retention, notify subscribers."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    con = sqlite3.connect(DB_PATH)
    con.execute(
        """
        INSERT INTO events (type, actor, target_type, target_slug, detail, level, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (type, actor, target_type, target_slug, detail, level, ts),
    )
    con.execute(
        "DELETE FROM events WHERE id NOT IN (SELECT id FROM events ORDER BY id DESC LIMIT 1000)"
    )
    con.commit()
    row = con.execute(
        "SELECT id, type, actor, target_type, target_slug, detail, level, created_at "
        "FROM events ORDER BY id DESC LIMIT 1"
    ).fetchone()
    con.close()

    if row:
        payload = {
            "id": row[0], "type": row[1], "actor": row[2],
            "target_type": row[3], "target_slug": row[4],
            "detail": row[5], "level": row[6], "created_at": row[7],
        }
        for q in list(_subscribers):
            try:
                q.put_nowait(payload)
            except asyncio.QueueFull:
                pass


# ── REST — recent events ──────────────────────────────────────────────────────

@router.get("")
async def get_events(limit: int = 20) -> dict:
    """
    Return the last N events (default 20, max 200).
    Excludes arena_turn — those are only visible in the Arena session detail view.
    """
    limit = min(max(1, limit), 200)
    con = sqlite3.connect(DB_PATH)
    rows = con.execute(
        """
        SELECT id, type, actor, target_type, target_slug, detail, level, created_at
        FROM events
        WHERE type != 'arena_turn'
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,),
    ).fetchall()
    con.close()
    return {
        "events": [
            {
                "id": r[0], "type": r[1], "actor": r[2],
                "target_type": r[3], "target_slug": r[4],
                "detail": r[5], "level": r[6], "created_at": r[7],
            }
            for r in rows
        ]
    }


# ── SSE — live stream ─────────────────────────────────────────────────────────

async def _stream(queue: asyncio.Queue) -> AsyncGenerator[str, None]:
    try:
        while True:
            try:
                event = await asyncio.wait_for(queue.get(), timeout=25.0)
                yield f"data: {json.dumps(event)}\n\n"
            except asyncio.TimeoutError:
                yield ": keepalive\n\n"
    finally:
        _subscribers.discard(queue)


@router.get("/stream")
async def events_stream() -> StreamingResponse:
    """SSE stream — emits a JSON event object whenever log_event() is called."""
    q: asyncio.Queue = asyncio.Queue(maxsize=50)
    _subscribers.add(q)
    return StreamingResponse(
        _stream(q),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
