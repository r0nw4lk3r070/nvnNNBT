#!/usr/bin/env python3
"""mcp_team.py — MCP stdio server for team manager agents.

Provides tools for:
  - read_team()                      → parse /workspace/team.json
  - delegate(role, message)          → POST to member /chat, stream + log to shared.db
  - log_entry(action, detail, agent) → write to knowledge/shared.db log table
  - read_queue()                     → pending items from queue table
  - complete_queue(id, result)       → mark queue item done
  - member_status()                  → list member containers + running state
  - stop_member(role)                → docker stop on a specific member container
  - start_member(role)               → docker start on a specific member container

Docker tools use the Unix socket at /var/run/docker.sock (mounted into the manager
container at spawn time). Operations are scoped to this team's containers only via
the com.nvnnnbt.team_slug label.

This script runs as a subprocess of the nanobot agent runtime (stdio/MCP transport).
No factory dependency at runtime — all state is local to the workspace or Docker socket.
"""
from __future__ import annotations

import http.client
import json
import os
import socket
import sqlite3
import sys
import urllib.parse
from pathlib import Path

# ── Paths + identity ──────────────────────────────────────────────────────────
WORKSPACE_PATH = Path(os.environ.get("WORKSPACE_PATH", "/workspace"))
TEAM_JSON      = WORKSPACE_PATH / "team.json"
KNOWLEDGE_DB   = WORKSPACE_PATH / "knowledge" / "shared.db"
TEAM_SLUG      = os.environ.get("TEAM_SLUG", "")        # set by factory at spawn
DOCKER_SOCKET  = "/var/run/docker.sock"


# ── Helpers ───────────────────────────────────────────────────────────────────

def _read_team() -> dict:
    if not TEAM_JSON.exists():
        return {}
    with open(TEAM_JSON, encoding="utf-8") as f:
        return json.load(f)


def _db_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(str(KNOWLEDGE_DB))
    conn.row_factory = sqlite3.Row
    return conn


def _log(agent: str, action: str, detail: str) -> None:
    if not KNOWLEDGE_DB.exists():
        return
    try:
        conn = _db_conn()
        conn.execute(
            "INSERT INTO log (agent, action, detail) VALUES (?, ?, ?)",
            (agent, action, detail),
        )
        conn.commit()
        conn.close()
    except Exception:
        pass  # log failures are non-fatal


# ── Tool implementations ──────────────────────────────────────────────────────

def tool_read_team(_args: dict) -> dict:
    """Return team.json as JSON text."""
    team = _read_team()
    if not team:
        return _text("team.json not found or empty")
    return _text(json.dumps(team, indent=2))


def tool_delegate(args: dict) -> dict:
    """POST to a member's /chat endpoint and return their full response."""
    import urllib.request

    role    = (args.get("role") or "").strip()
    message = (args.get("message") or "").strip()

    if not role or not message:
        return _text("ERROR: role and message are required")

    team = _read_team()
    if not team:
        return _text("ERROR: team.json not found — cannot delegate")

    members = {m["role"]: m for m in team.get("members", [])}
    if role not in members:
        return _text(f"ERROR: unknown role '{role}'. Available: {list(members.keys())}")

    member = members[role]
    port   = member.get("chat_port")
    slug   = member.get("slug", role)

    if not port:
        return _text(f"ERROR: member '{role}' has no chat_port in team.json")

    _log("manager", "delegate", f"→ {role} ({slug}): {message[:200]}")

    url     = f"http://localhost:{port}/chat"
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
                data = line[5:].strip()
                if data == "[DONE]":
                    break
                try:
                    chunk = json.loads(data)
                    delta = (
                        chunk.get("choices", [{}])[0]
                        .get("delta", {})
                        .get("content", "")
                    )
                    full_text += delta
                except Exception:
                    pass

        _log(slug, "response", full_text[:500])
        return _text(full_text)

    except Exception as e:
        _log("manager", "error", f"delegate to {role} failed: {e}")
        return _text(f"ERROR calling {role} ({slug} on port {port}): {e}")


def tool_log_entry(args: dict) -> dict:
    """Write a log entry to the team's shared.db."""
    agent  = (args.get("agent") or "manager").strip()
    action = (args.get("action") or "").strip()
    detail = (args.get("detail") or "").strip()
    if not action:
        return _text("ERROR: action is required")
    _log(agent, action, detail)
    return _text("logged")


def tool_read_queue(_args: dict) -> dict:
    """Return pending items from the task queue."""
    if not KNOWLEDGE_DB.exists():
        return _text("[]")
    try:
        conn = _db_conn()
        rows = conn.execute(
            "SELECT id, task, status, assigned FROM queue WHERE status='pending' ORDER BY id LIMIT 10"
        ).fetchall()
        conn.close()
        return _text(json.dumps([dict(r) for r in rows], indent=2))
    except Exception as e:
        return _text(f"ERROR reading queue: {e}")


def tool_complete_queue(args: dict) -> dict:
    """Mark a queue item as done."""
    item_id = args.get("id")
    result  = (args.get("result") or "").strip()
    if item_id is None:
        return _text("ERROR: id is required")
    try:
        conn = _db_conn()
        conn.execute(
            "UPDATE queue SET status='done', result=?, updated_at=datetime('now') WHERE id=?",
            (result, item_id),
        )
        conn.commit()
        conn.close()
        return _text(f"Queue item {item_id} marked done")
    except Exception as e:
        return _text(f"ERROR: {e}")


# ── Docker Unix socket client ─────────────────────────────────────────────────

class _UnixHTTPConnection(http.client.HTTPConnection):
    """HTTPConnection that talks over a Unix domain socket."""
    def __init__(self, socket_path: str) -> None:
        super().__init__("localhost")
        self._socket_path = socket_path

    def connect(self) -> None:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect(self._socket_path)
        self.sock = s


def _docker_get(path: str) -> dict | list | None:
    """GET from Docker socket, return parsed JSON or None on error."""
    if not os.path.exists(DOCKER_SOCKET):
        return None
    try:
        conn = _UnixHTTPConnection(DOCKER_SOCKET)
        conn.request("GET", path, headers={"Host": "localhost"})
        resp = conn.getresponse()
        body = resp.read().decode("utf-8", errors="replace")
        conn.close()
        return json.loads(body)
    except Exception:
        return None


def _docker_post(path: str) -> tuple[int, str]:
    """POST to Docker socket (no body). Return (status_code, body_text)."""
    if not os.path.exists(DOCKER_SOCKET):
        return 503, "Docker socket not available"
    try:
        conn = _UnixHTTPConnection(DOCKER_SOCKET)
        conn.request("POST", path, headers={"Host": "localhost", "Content-Length": "0"})
        resp = conn.getresponse()
        body = resp.read().decode("utf-8", errors="replace")
        conn.close()
        return resp.status, body
    except Exception as e:
        return 500, str(e)


def _container_name(role: str) -> str:
    """Construct the expected container name for a team member."""
    # Factory naming convention: nvnnnbt-team-{team_slug}-{role}
    return f"nvnnnbt-team-{TEAM_SLUG}-{role}"


# ── Docker tools ──────────────────────────────────────────────────────────────

def tool_member_status(_args: dict) -> dict:
    """List all member containers for this team with their running state."""
    if not TEAM_SLUG:
        return _text("ERROR: TEAM_SLUG env var not set — cannot scope Docker query")
    if not os.path.exists(DOCKER_SOCKET):
        return _text("ERROR: Docker socket not available at /var/run/docker.sock")

    label_filter = urllib.parse.quote(
        json.dumps({"label": [f"com.nvnnnbt.team_slug={TEAM_SLUG}"]})
    )
    data = _docker_get(f"/containers/json?all=1&filters={label_filter}")
    if data is None:
        return _text("ERROR: failed to query Docker")

    results = []
    for c in data:
        names  = [n.lstrip("/") for n in c.get("Names", [])]
        state  = c.get("State", "unknown")
        status = c.get("Status", "")
        labels = c.get("Labels", {})
        role   = labels.get("com.nvnnnbt.role", "?")
        results.append({"role": role, "name": names[0] if names else "?", "state": state, "status": status})

    return _text(json.dumps(results, indent=2))


def tool_stop_member(args: dict) -> dict:
    """Stop a team member's container."""
    role = (args.get("role") or "").strip()
    if not role:
        return _text("ERROR: role is required")
    if not TEAM_SLUG:
        return _text("ERROR: TEAM_SLUG env var not set")

    name = _container_name(role)
    # t=10 gives the container 10 seconds to shut down gracefully before SIGKILL
    status, body = _docker_post(f"/containers/{name}/stop?t=10")
    if status in (204, 304):
        _log("manager", "stop_member", f"Stopped container '{name}' (role: {role})")
        return _text(f"Container '{name}' stopped")
    elif status == 404:
        return _text(f"ERROR: container '{name}' not found — is the role name correct?")
    else:
        return _text(f"ERROR: Docker returned {status}: {body.strip()}")


def tool_start_member(args: dict) -> dict:
    """Start a team member's container."""
    role = (args.get("role") or "").strip()
    if not role:
        return _text("ERROR: role is required")
    if not TEAM_SLUG:
        return _text("ERROR: TEAM_SLUG env var not set")

    name = _container_name(role)
    status, body = _docker_post(f"/containers/{name}/start")
    if status in (204, 304):
        _log("manager", "start_member", f"Started container '{name}' (role: {role})")
        return _text(f"Container '{name}' started")
    elif status == 404:
        return _text(f"ERROR: container '{name}' not found — has the team been spawned?")
    else:
        return _text(f"ERROR: Docker returned {status}: {body.strip()}")


# ── Tool registry ─────────────────────────────────────────────────────────────

TOOLS: dict[str, dict] = {
    "read_team": {
        "fn": tool_read_team,
        "schema": {
            "name": "read_team",
            "description": (
                "Read team.json to discover team members, their roles, and their "
                "chat ports. Call this first when you receive a task so you know who "
                "is available."
            ),
            "inputSchema": {"type": "object", "properties": {}, "required": []},
        },
    },
    "delegate": {
        "fn": tool_delegate,
        "schema": {
            "name": "delegate",
            "description": (
                "Send a task to a team member by role and return their full response. "
                "Automatically logs the delegation and response to the team's shared.db. "
                "The member must be running (spawned) for this to succeed."
            ),
            "inputSchema": {
                "type": "object",
                "properties": {
                    "role": {
                        "type": "string",
                        "description": "The member role to delegate to (e.g. 'writer', 'researcher').",
                    },
                    "message": {
                        "type": "string",
                        "description": "The instruction or task to send to the member.",
                    },
                },
                "required": ["role", "message"],
            },
        },
    },
    "log_entry": {
        "fn": tool_log_entry,
        "schema": {
            "name": "log_entry",
            "description": "Write an entry to the team's shared delegation log in shared.db.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "agent": {
                        "type": "string",
                        "description": "The agent writing the entry. Defaults to 'manager'.",
                    },
                    "action": {
                        "type": "string",
                        "description": "Short label for the action (e.g. 'plan', 'delegate', 'synthesise', 'done').",
                    },
                    "detail": {
                        "type": "string",
                        "description": "Detail text for this log entry.",
                    },
                },
                "required": ["action", "detail"],
            },
        },
    },
    "read_queue": {
        "fn": tool_read_queue,
        "schema": {
            "name": "read_queue",
            "description": (
                "Read pending items from the team's task queue in shared.db. "
                "Use this in pipeline/cron mode to pick up the next task to process."
            ),
            "inputSchema": {"type": "object", "properties": {}, "required": []},
        },
    },
    "complete_queue": {
        "fn": tool_complete_queue,
        "schema": {
            "name": "complete_queue",
            "description": "Mark a queue item as done and record the result.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "The queue item id returned by read_queue.",
                    },
                    "result": {
                        "type": "string",
                        "description": "The result or summary to store.",
                    },
                },
                "required": ["id"],
            },
        },
    },
    "member_status": {
        "fn": tool_member_status,
        "schema": {
            "name": "member_status",
            "description": (
                "List all member containers for this team with their current Docker state "
                "(running, exited, etc.). Use this to check whether members are up before delegating, "
                "or to diagnose why a delegation failed."
            ),
            "inputSchema": {"type": "object", "properties": {}, "required": []},
        },
    },
    "stop_member": {
        "fn": tool_stop_member,
        "schema": {
            "name": "stop_member",
            "description": (
                "Stop a team member's Docker container by role. "
                "Use this as a hard stop when a member is stuck, producing bad output, "
                "or consuming resources it shouldn't. The container can be restarted with start_member."
            ),
            "inputSchema": {
                "type": "object",
                "properties": {
                    "role": {
                        "type": "string",
                        "description": "The member role to stop (e.g. 'writer', 'researcher').",
                    },
                },
                "required": ["role"],
            },
        },
    },
    "start_member": {
        "fn": tool_start_member,
        "schema": {
            "name": "start_member",
            "description": (
                "Start a previously stopped team member container by role. "
                "Use this to restart a member after stopping it, or to bring up a member "
                "that was stopped to save resources."
            ),
            "inputSchema": {
                "type": "object",
                "properties": {
                    "role": {
                        "type": "string",
                        "description": "The member role to start (e.g. 'writer', 'researcher').",
                    },
                },
                "required": ["role"],
            },
        },
    },
}


# ── MCP stdio transport (JSON-RPC 2.0) ────────────────────────────────────────

def _text(text: str) -> dict:
    return {"content": [{"type": "text", "text": text}]}


def _send(msg: dict) -> None:
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()


def _handle(msg: dict) -> None:
    method = msg.get("method", "")
    msg_id = msg.get("id")

    if method == "initialize":
        _send({
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "team-manager", "version": "1.0.0"},
            },
        })

    elif method == "notifications/initialized":
        pass  # notification — no response

    elif method == "tools/list":
        _send({
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {"tools": [t["schema"] for t in TOOLS.values()]},
        })

    elif method == "tools/call":
        params    = msg.get("params", {})
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})
        if tool_name in TOOLS:
            try:
                result = TOOLS[tool_name]["fn"](arguments)
                _send({"jsonrpc": "2.0", "id": msg_id, "result": result})
            except Exception as e:
                _send({
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "error": {"code": -32603, "message": str(e)},
                })
        else:
            _send({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"},
            })

    elif msg_id is not None:
        # Unknown method with an id — respond with error
        _send({
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32601, "message": f"Method not found: {method}"},
        })


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        _handle(msg)


if __name__ == "__main__":
    main()
