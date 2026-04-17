"""state.py — Shared mutable globals and config helpers for nvnNNBT agent."""
from __future__ import annotations

import json
import os
from pathlib import Path

# ── Paths — all resolved from environment variables ─────────────────────────
# In Docker: env vars are set in docker-compose.yml / .env
# Locally:   set WORKSPACE_PATH, SKILLSETS_PATH etc. before running

WORKSPACE_PATH = Path(os.environ.get("WORKSPACE_PATH", "/workspace"))
SKILLSETS_PATH = Path(os.environ.get("SKILLSETS_PATH", "/skill-sets"))

CONFIG_PATH    = WORKSPACE_PATH / "config.json"
HTTP_PORT      = int(os.environ.get("AGENT_PORT", "6161"))
AGENT_MODE     = os.environ.get("AGENT_MODE", "art")   # "art" | "production"
OLLAMA_BASE    = os.environ.get("OLLAMA_BASE_URL", "http://ollama:11434")
GROK_API_KEY   = os.environ.get("GROK_API_KEY", "")
GROK_API_BASE  = "https://api.x.ai/v1"

SKILLSETS_DIR  = SKILLSETS_PATH
CHATS_DIR      = WORKSPACE_PATH / "memory" / "chats"
UPLOADS_DIR    = WORKSPACE_PATH / "memory" / "uploads"
LAB_STATE_FILE = WORKSPACE_PATH / "memory" / "lab_state.json"

SESSION_KEY   = "web:nanobot"
CHANNEL       = "web"
CHAT_ID       = "nanobot"

_agent       = None
_cron        = None
_bus         = None
_base_config = None
_chat_task   = None
_discord_channel = None
_channel_manager = None

# ── Lab (skill-set) state ─────────────────────────────────────────────────
_lab_agent = None
_lab_cron  = None
_lab_name  = None
_lab_model = None
_lab_task  = None


# ── Config helpers ────────────────────────────────────────────────────────

def _read_config_raw() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def _write_config_raw(data: dict) -> None:
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def _current_model() -> str:
    return _read_config_raw()["agents"]["defaults"]["model"]


def _save_lab_state(name: str | None, model: str | None) -> None:
    LAB_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LAB_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump({"name": name, "model": model}, f)


def _load_lab_state() -> tuple[str | None, str | None]:
    if not LAB_STATE_FILE.exists():
        return None, None
    try:
        with open(LAB_STATE_FILE, encoding="utf-8") as f:
            d = json.load(f)
        return d.get("name") or None, d.get("model") or None
    except Exception:
        return None, None
