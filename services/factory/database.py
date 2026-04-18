"""database.py — SQLite schema init for Agent Factory."""
from __future__ import annotations

import sqlite3
from pathlib import Path

DB_PATH = Path("/app/data/factory.db")

_SCHEMA = """
CREATE TABLE IF NOT EXISTS providers (
    id          TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    base_url    TEXT NOT NULL,
    api_key     TEXT DEFAULT '',
    capabilities TEXT DEFAULT '[]',
    is_default  INTEGER DEFAULT 0,
    created_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS workspaces (
    slug              TEXT PRIMARY KEY,
    name              TEXT NOT NULL,
    path              TEXT NOT NULL,
    provider_id       TEXT DEFAULT '',
    image_provider_id TEXT DEFAULT '',
    embed_provider_id TEXT DEFAULT '',
    model             TEXT DEFAULT '',
    mcp_servers       TEXT DEFAULT '[]',
    created_at        TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS spawned_agents (
    slug          TEXT PRIMARY KEY,
    container     TEXT DEFAULT '',
    ports         TEXT DEFAULT '{}',
    provider_id   TEXT DEFAULT '',
    model         TEXT DEFAULT '',
    team_slug     TEXT DEFAULT '',
    session_type  TEXT DEFAULT 'production',
    status        TEXT DEFAULT 'stopped',
    workspace_slug TEXT DEFAULT '',
    created_at    TEXT DEFAULT (datetime('now')),
    updated_at    TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS agent_teams (
    slug                    TEXT PRIMARY KEY,
    name                    TEXT NOT NULL,
    knowledge_dir           TEXT DEFAULT '',
    orchestrator_slug       TEXT DEFAULT '',
    orchestrator_provider_id TEXT DEFAULT '',
    created_at              TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS team_members (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    team_slug   TEXT NOT NULL,
    agent_slug  TEXT NOT NULL,
    provider_id TEXT DEFAULT '',
    model       TEXT DEFAULT ''
);

CREATE TABLE IF NOT EXISTS arena_sessions (
    id         TEXT PRIMARY KEY,
    mode       TEXT NOT NULL,
    agents     TEXT DEFAULT '[]',
    goal       TEXT DEFAULT '',
    turn_log   TEXT DEFAULT '[]',
    status     TEXT DEFAULT 'pending',
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS benchmark_runs (
    id                   TEXT PRIMARY KEY,
    workspace_slug       TEXT DEFAULT '',
    workspace_version_tag TEXT DEFAULT '',
    task_set_name        TEXT DEFAULT '',
    provider_id          TEXT DEFAULT '',
    model                TEXT DEFAULT '',
    judge_provider_id    TEXT DEFAULT '',
    judge_model          TEXT DEFAULT '',
    score                REAL DEFAULT 0,
    created_at           TEXT DEFAULT (datetime('now')),
    completed_at         TEXT DEFAULT ''
);

CREATE TABLE IF NOT EXISTS benchmark_results (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id       TEXT NOT NULL,
    task_id      TEXT DEFAULT '',
    input        TEXT DEFAULT '',
    response     TEXT DEFAULT '',
    score        REAL DEFAULT 0,
    judge_reason TEXT DEFAULT ''
);

CREATE TABLE IF NOT EXISTS token_usage (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    provider_id       TEXT NOT NULL,
    prompt_tokens     INTEGER DEFAULT 0,
    completion_tokens INTEGER DEFAULT 0,
    estimated_cost    REAL DEFAULT 0,
    session_date      TEXT DEFAULT (date('now'))
);

CREATE TABLE IF NOT EXISTS workspace_versions (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    workspace_slug TEXT NOT NULL,
    tag            TEXT NOT NULL,
    commit_hash    TEXT DEFAULT '',
    notes          TEXT DEFAULT '',
    created_at     TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS events (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    type        TEXT NOT NULL,
    actor       TEXT DEFAULT 'factory',
    target_type TEXT DEFAULT '',
    target_slug TEXT DEFAULT '',
    detail      TEXT DEFAULT '',
    level       TEXT DEFAULT 'info',
    created_at  TEXT DEFAULT (datetime('now'))
);
"""


# Migrations — applied after schema init (idempotent: errors ignored)
_MIGRATIONS = [
    "ALTER TABLE agent_teams ADD COLUMN mode TEXT DEFAULT 'production'",
]


def init_db(path: Path = DB_PATH) -> None:
    """Create all tables if they don't exist yet."""
    path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.executescript(_SCHEMA)
    for migration in _MIGRATIONS:
        try:
            con.execute(migration)
        except sqlite3.OperationalError:
            pass  # column already exists
    con.commit()
    con.close()


def get_conn(path: Path = DB_PATH) -> sqlite3.Connection:
    """Return a sqlite3 connection with row_factory set."""
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    return con
