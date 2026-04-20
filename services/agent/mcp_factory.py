#!/usr/bin/env python3
"""mcp_factory.py — MCP stdio server that gives any agent access to the factory API.

Tools:
  - list_agents()                    → list all solo spawned agents
  - list_teams()                     → list all teams + manager/member status
  - spawn_team(slug, mode?)          → spawn a team (mode: test|prod, default test)
  - stop_team(slug)                  → stop all containers for a team
  - talk_to_agent(slug, message)     → send a message to any running agent's /chat
                                       and stream back the full response
  - get_delegation_log(slug, limit?) → tail the team's shared.db log table

All factory calls go through FACTORY_BASE_URL (default http://host.docker.internal:4000).
talk_to_agent connects to http://localhost:{chat_port}/chat — chat ports are host-mapped
ports, reachable from inside a container via host.docker.internal.

This server runs as a subprocess of the nanobot agent runtime (stdio/MCP transport).
Configure in config.json:
  {
    "tools": {
      "mcpServers": {
        "factory": {
          "command": "python",
          "args": ["/app/mcp_factory.py"],
          "env": {}
        }
      }
    }
  }
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
import urllib.parse
import urllib.request
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────
FACTORY_BASE = os.environ.get("FACTORY_BASE_URL", "http://host.docker.internal:4000")
# Strip trailing slash
FACTORY_BASE = FACTORY_BASE.rstrip("/")


# ── HTTP helpers ──────────────────────────────────────────────────────────────

def _factory_get(path: str) -> tuple[int, dict | list | None]:
    """GET from the factory REST API. Returns (status, parsed_json)."""
    try:
        req = urllib.request.Request(
            f"{FACTORY_BASE}{path}",
            headers={"Accept": "application/json"},
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status, json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        try:
            body = json.loads(e.read().decode())
        except Exception:
            body = {"detail": str(e)}
        return e.code, body
    except Exception as e:
        return 503, {"detail": str(e)}


def _factory_post(path: str, payload: dict | None = None) -> tuple[int, dict | list | None]:
    """POST to the factory REST API. Returns (status, parsed_json)."""
    data = json.dumps(payload or {}).encode()
    try:
        req = urllib.request.Request(
            f"{FACTORY_BASE}{path}",
            data=data,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status, json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        try:
            body = json.loads(e.read().decode())
        except Exception:
            body = {"detail": str(e)}
        return e.code, body
    except Exception as e:
        return 503, {"detail": str(e)}


# ── Tool implementations ──────────────────────────────────────────────────────

def tool_list_agents(_args: dict) -> dict:
    """List all solo spawned agents on the factory."""
    status, data = _factory_get("/api/factory/agents")
    if status != 200 or data is None:
        detail = data.get("detail", "unknown error") if isinstance(data, dict) else str(data)
        return _text(f"ERROR {status}: {detail}")
    agents = data.get("agents", [])
    if not agents:
        return _text("No agents spawned.")
    lines = ["Spawned agents:"]
    for a in agents:
        lines.append(
            f"  {a.get('slug','?')} — {a.get('model','?')} — {a.get('status','?')} "
            f"(chat port: {a.get('chat_port') or 'n/a'})"
        )
    return _text("\n".join(lines))


def tool_list_teams(_args: dict) -> dict:
    """List all teams with their manager status and member list."""
    status, data = _factory_get("/api/factory/teams")
    if status != 200 or data is None:
        detail = data.get("detail", "unknown error") if isinstance(data, dict) else str(data)
        return _text(f"ERROR {status}: {detail}")
    teams = data.get("teams", [])
    if not teams:
        return _text("No teams created yet.")
    lines = ["Teams:"]
    for t in teams:
        lines.append(
            f"  [{t.get('slug','?')}] {t.get('name','?')} — manager: {t.get('manager_status','?')}"
        )
        for m in t.get("members", []):
            lines.append(
                f"    • {m.get('role','?')} ({m.get('slug','?')}) — {m.get('status','?')}"
            )
    return _text("\n".join(lines))


def tool_spawn_team(args: dict) -> dict:
    """Spawn all containers for a team."""
    slug = (args.get("slug") or "").strip()
    mode = (args.get("mode") or "test").strip()
    if not slug:
        return _text("ERROR: slug is required")
    if mode not in ("test", "prod"):
        return _text("ERROR: mode must be 'test' or 'prod'")
    status, data = _factory_post(f"/api/factory/teams/{slug}/spawn", {"mode": mode})
    if status != 200 or data is None:
        detail = data.get("detail", "unknown error") if isinstance(data, dict) else str(data)
        return _text(f"ERROR {status}: {detail}")
    return _text(f"Team '{slug}' spawned in {mode} mode.")


def tool_stop_team(args: dict) -> dict:
    """Stop all running containers for a team."""
    slug = (args.get("slug") or "").strip()
    if not slug:
        return _text("ERROR: slug is required")
    status, data = _factory_post(f"/api/factory/teams/{slug}/stop")
    if status != 200 or data is None:
        detail = data.get("detail", "unknown error") if isinstance(data, dict) else str(data)
        return _text(f"ERROR {status}: {detail}")
    return _text(f"Team '{slug}' stopped.")


def tool_talk_to_agent(args: dict) -> dict:
    """Send a message to any running agent (manager, member, or solo) and return the response.

    The agent is identified by its slug. The factory is queried for the chat port.
    Works for: team managers, team members, solo agents — any spawned agent.
    """
    slug    = (args.get("slug") or "").strip()
    message = (args.get("message") or "").strip()
    if not slug or not message:
        return _text("ERROR: slug and message are required")

    # Resolve chat port via factory
    status, data = _factory_get(f"/api/factory/agents/{slug}/port")
    chat_port = None
    if status == 200 and isinstance(data, dict):
        chat_port = data.get("chat_port")
    if not chat_port:
        # Fallback: search in agents list
        _, agents_data = _factory_get("/api/factory/agents")
        if isinstance(agents_data, dict):
            for a in agents_data.get("agents", []):
                if a.get("slug") == slug:
                    chat_port = a.get("chat_port")
                    break
    if not chat_port:
        # Also check team members
        _, teams_data = _factory_get("/api/factory/teams")
        if isinstance(teams_data, dict):
            for t in teams_data.get("teams", []):
                if t.get("manager_slug") == slug:
                    chat_port = t.get("manager_chat_port")
                    break
                for m in t.get("members", []):
                    if m.get("slug") == slug:
                        chat_port = m.get("chat_port")
                        break
    if not chat_port:
        return _text(
            f"ERROR: could not find a running agent with slug '{slug}'. "
            f"Check list_agents() or list_teams() to see available slugs."
        )

    url     = f"http://host.docker.internal:{chat_port}/chat"
    payload = json.dumps({"messages": [{"role": "user", "content": message}]}).encode()

    try:
        req = urllib.request.Request(
            url, data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        full_text = ""
        with urllib.request.urlopen(req, timeout=120) as resp:
            for raw_line in resp:
                line = raw_line.decode("utf-8", errors="replace").strip()
                if not line.startswith("data:"):
                    continue
                data_str = line[5:].strip()
                if data_str == "[DONE]":
                    break
                try:
                    chunk = json.loads(data_str)
                    delta = (
                        chunk.get("choices", [{}])[0]
                        .get("delta", {})
                        .get("content", "")
                    )
                    full_text += delta
                except Exception:
                    pass
        return _text(full_text or "(no response)")
    except Exception as e:
        return _text(f"ERROR talking to agent '{slug}' on port {chat_port}: {e}")


def tool_get_delegation_log(args: dict) -> dict:
    """Tail the delegation log from a team's shared.db.

    Useful to understand what a team has been doing, review outcomes, or
    diagnose issues without spinning up a full session.
    """
    slug  = (args.get("slug") or "").strip()
    limit = int(args.get("limit") or 20)
    if not slug:
        return _text("ERROR: slug is required")

    # Teams root is mounted at /teams inside factory, but from Art's perspective
    # we fetch via the factory REST API
    status, data = _factory_get(f"/api/factory/teams/{slug}/log?limit={limit}")
    if status != 200 or data is None:
        detail = data.get("detail", "unknown error") if isinstance(data, dict) else str(data)
        return _text(f"ERROR {status}: {detail}")

    entries = data.get("entries", [])
    if not entries:
        return _text(f"No log entries for team '{slug}' yet.")

    lines = [f"Delegation log for '{slug}' (last {len(entries)} entries):"]
    for e in entries:
        ts    = e.get("created_at", "")
        agent = e.get("agent", "?")
        act   = e.get("action", "?")
        det   = (e.get("detail") or "")[:200]
        lines.append(f"  [{ts}] {agent} / {act}: {det}")
    return _text("\n".join(lines))


# ── MCP response helpers ──────────────────────────────────────────────────────

def _text(content: str) -> dict:
    return {"content": [{"type": "text", "text": content}]}


# ── Tool registry ─────────────────────────────────────────────────────────────

TOOLS: dict[str, dict] = {
    "list_agents": {
        "fn": tool_list_agents,
        "schema": {
            "name": "list_agents",
            "description": "List all solo agents currently spawned on the factory with their status and chat ports.",
            "inputSchema": {"type": "object", "properties": {}, "required": []},
        },
    },
    "list_teams": {
        "fn": tool_list_teams,
        "schema": {
            "name": "list_teams",
            "description": "List all teams with their manager status and member list. Use this to discover team slugs and member slugs before calling talk_to_agent.",
            "inputSchema": {"type": "object", "properties": {}, "required": []},
        },
    },
    "spawn_team": {
        "fn": tool_spawn_team,
        "schema": {
            "name": "spawn_team",
            "description": "Spawn all containers for a team. The team must already exist (created in the factory UI or API).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "slug": {"type": "string", "description": "Team slug (e.g. 'research-team')."},
                    "mode": {"type": "string", "description": "Spawn mode: 'test' or 'prod'. Defaults to 'test'."},
                },
                "required": ["slug"],
            },
        },
    },
    "stop_team": {
        "fn": tool_stop_team,
        "schema": {
            "name": "stop_team",
            "description": "Stop all running containers for a team without deleting the workspace.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "slug": {"type": "string", "description": "Team slug to stop."},
                },
                "required": ["slug"],
            },
        },
    },
    "talk_to_agent": {
        "fn": tool_talk_to_agent,
        "schema": {
            "name": "talk_to_agent",
            "description": (
                "Send a message to any running agent by slug and return their full response. "
                "Works for team managers (steer the whole team), team members (direct bypass), "
                "or solo agents. Use list_teams() or list_agents() first to discover available slugs."
            ),
            "inputSchema": {
                "type": "object",
                "properties": {
                    "slug": {
                        "type": "string",
                        "description": "Agent slug to talk to (e.g. 'my-team-manager', 'my-team-writer', 'solo-researcher').",
                    },
                    "message": {
                        "type": "string",
                        "description": "The message or task to send to the agent.",
                    },
                },
                "required": ["slug", "message"],
            },
        },
    },
    "get_delegation_log": {
        "fn": tool_get_delegation_log,
        "schema": {
            "name": "get_delegation_log",
            "description": "Read the recent delegation log from a team's shared database. Shows what the manager and members have been doing.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "slug": {"type": "string", "description": "Team slug."},
                    "limit": {"type": "integer", "description": "Number of recent entries to return. Defaults to 20."},
                },
                "required": ["slug"],
            },
        },
    },
}


# ── MCP stdio loop ────────────────────────────────────────────────────────────

def _send(obj: dict) -> None:
    sys.stdout.write(json.dumps(obj) + "\n")
    sys.stdout.flush()


def _handle(request: dict) -> dict | None:
    method = request.get("method", "")
    req_id = request.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0", "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "mcp_factory", "version": "1.0.0"},
            },
        }

    if method == "notifications/initialized":
        return None

    if method == "tools/list":
        return {
            "jsonrpc": "2.0", "id": req_id,
            "result": {"tools": [t["schema"] for t in TOOLS.values()]},
        }

    if method == "tools/call":
        params    = request.get("params", {})
        tool_name = params.get("name", "")
        tool_args = params.get("arguments", {})
        entry     = TOOLS.get(tool_name)
        if not entry:
            return {
                "jsonrpc": "2.0", "id": req_id,
                "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"},
            }
        try:
            result = entry["fn"](tool_args)
        except Exception as exc:
            result = _text(f"ERROR (internal): {exc}")
        return {"jsonrpc": "2.0", "id": req_id, "result": result}

    # Unknown method — return error only for requests (have id), not notifications
    if req_id is not None:
        return {
            "jsonrpc": "2.0", "id": req_id,
            "error": {"code": -32601, "message": f"Method not found: {method}"},
        }
    return None


def main() -> None:
    for raw_line in sys.stdin:
        raw_line = raw_line.strip()
        if not raw_line:
            continue
        try:
            request = json.loads(raw_line)
        except json.JSONDecodeError:
            _send({"jsonrpc": "2.0", "id": None,
                   "error": {"code": -32700, "message": "Parse error"}})
            continue
        response = _handle(request)
        if response is not None:
            _send(response)


if __name__ == "__main__":
    main()
