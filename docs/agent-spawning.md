# Agent Spawning

nvnNNBT can spawn additional nanobot agents on demand — each running in its own Docker container, with its own identity, workspace, model, and web UI. The factory orchestrates this through the Docker socket without Docker-in-Docker.

---

## How it works

The `factory` service (FastAPI :4000) mounts the host Docker socket (`/var/run/docker.sock`). When a spawn request comes in, the factory calls the Docker daemon directly — creating a sibling container (not a child), attaching it to the same internal network, and binding the workspace folder from the host. The spawned agent serves its own web UI and chat API on its own port.

```
┌────────────────┐    POST /api/factory/agents    ┌─────────────────────────────┐
│  ui / caller   │ ──────────────────────────────▶ │  factory :4000              │
│                │ ◀── { chat_port: 4330 } ──────── │                             │
│                │                                  └────────────┬────────────────┘
│                │                                               │  docker run nvnnnbt-agent:latest
│                │                                               ▼
│                │                                  ┌─────────────────────────────┐
│                │                                  │  nvnnnbt-agent-demo         │
│  GET /api/factory/agents/demo/proxy/*             │  AGENT_MODE=production      │
│ ─────────────────────────────────────────────────▶  host: 0.0.0.0:4330         │
│                │  ◀─── proxied response ─────────  Serves own web UI + /chat   │
└────────────────┘                                  └─────────────────────────────┘
```

Spawned agents are **proxied through the factory** at `/api/factory/agents/{slug}/proxy/{path}`. This means the standalone chat is accessible from any machine without knowing the agent's raw host port. Direct access at `http://host:{chat_port}/` also works. Each one runs `nvnnnbt-agent:latest` with `AGENT_MODE=production`, which switches the agent to its standalone teal dark UI (`html_agent.py`) instead of the ART interface.

```
---

## Prerequisites

Before spawning, two things must be true:

1. **`HOST_PROJECT_PATH` is set** in `.env` — the absolute path to the nvnNNBT folder on the host machine. The factory needs this because Docker bind-mounts require host-absolute paths.

   ```env
   # Windows
   HOST_PROJECT_PATH=e:/nvnNNBT

   # Linux / macOS
   HOST_PROJECT_PATH=/home/user/nvnNNBT
   ```

2. **A workspace folder exists** at `data/workspaces/{slug}/` containing at minimum a `SOUL.md`. Without identity files, the agent will start but produce generic responses.

A working example is included at `data/workspaces/demo/`.

---

## Agent registry

The factory keeps a SQLite database at `/app/data/nanobot.db` (persisted to `./data/nanobot.db` on the host via bind mount). This acts as the agent registry.

Table: `spawned_agents`

| Column | Type | Description |
|---|---|---|
| `slug` | TEXT (PK) | URL-safe identifier, doubles as workspace slug |
| `container` | TEXT | Docker container name (`nvnnnbt-agent-{slug}`) |
| `ports` | TEXT | `"gateway,chat"` — e.g. `"4230,4330"` |
| `model` | TEXT | Model identifier (from workspace config.json) |
| `status` | TEXT | Last known status: `running`, `stopped`, `missing`, etc. |
| `session_type` | TEXT | Always `production` for spawned agents |
| `workspace_slug` | TEXT | Workspace backing this agent (same as slug for solo spawn) |
| `created_at` | INTEGER | Unix timestamp |

Status is synced live from the Docker daemon on `GET /agents`.

---

## Port allocation

Each spawned agent is assigned two ports from reserved bands. The bands are configurable via `.env` so multiple instances of the factory can run on the same host without collision.

| Band | Default range | Env var | Purpose |
|---|---|---|---|
| Gateway | 4230–4299 | `AGENT_GATEWAY_PORT_BASE=4230` | Reserved for future agent gateway (MCP, etc.) |
| Chat | 4330–4399 | `AGENT_CHAT_PORT_BASE=4330` | Agent web UI + chat API |

Port assignment picks the lowest free port in each band. The **chat port** is exposed on the host bound to `0.0.0.0:{chat_port}:6161/tcp` so the factory proxy can reach it via `host.docker.internal`. The gateway port is allocated and stored for future use.

With these bands, up to **70 simultaneous spawned agents** are supported per instance.

> **Running two factory instances on one machine?** Offset the bases in each `.env` to avoid collision — see [Running multiple instances](#running-multiple-instances) below.

---

## Factory API

All spawn routes live on the factory at `/agents`. Via nginx at port 3000 they are at `/api/factory/agents`.

If `API_KEY` is set in `.env`, include it as `x-api-key` header or `?key=` query param.

### List agents

```
GET /api/factory/agents
```

Returns all agents from the registry with live status synced from Docker.

```json
{
  "agents": [
    {
      "slug": "demo",
      "container": "nvnnnbt-agent-demo",
      "ports": "4230,4330",
      "gateway_port": 4230,
      "chat_port": 4330,
      "model": "gemma4:2b",
      "status": "running",
      "session_type": "production",
      "workspace_slug": "demo",
      "created_at": 1744900000
    }
  ]
}
```

### Spawn an agent

```
POST /api/factory/agents
Content-Type: application/json

{
  "slug": "demo"
}
```

- `slug` — required. Must match an existing workspace at `data/workspaces/{slug}/`.
- `model` — optional override, defaults to `"qwen3:1.7b"`. In practice the workspace's `config.json` controls the model the agent uses at runtime.

Returns `200` with `{ ok, slug, container, chat_port }`. Returns `404` if workspace not found, `409` if the agent is already running, `503` if Docker is unavailable or `HOST_PROJECT_PATH` is not set.

### Stop an agent

```
POST /api/factory/agents/{slug}/stop
```

Stops the container (does not remove it or its registry entry).

### Delete an agent

```
DELETE /api/factory/agents/{slug}
```

Force-removes the container **and** removes it from the registry. **Does not delete** the workspace folder at `data/workspaces/{slug}/` — data is always preserved.

---

## The standalone agent web UI

When a spawned agent is running its interface is reachable two ways:

| Access path | When to use |
|---|---|
| `/api/factory/agents/{slug}/proxy/` | Recommended — works from any machine, through the main UI's nginx |
| `http://{host}:{chat_port}/` | Direct access — useful for debugging or when factory is unreachable |

The **Agents** section of the UI links directly to the proxy path. Opening it shows the standalone agent interface:

- **Dark teal theme** — distinct from the ART assistant to make it clear this is a separate agent.
- **Agent name** — loaded from the first `#` heading in the workspace's `SOUL.md` on page load.
- **Streaming chat** — SSE via `POST /chat`, same protocol as ART.
- **Settings panel** — shows/edits the agent's `config.json` (model, API base URL, etc.) via `GET/PUT /api/settings`.
- **Status indicator** — a green dot when the agent is ready.

The interface is entirely self-contained — it runs from within the spawned container and requires no factory or UI service to function.

---

## config.json

Each workspace can carry a `config.json` that controls the agent's model and provider at runtime:

```json
{
  "agents": {
    "defaults": {
      "model": "gemma4:2b",
      "provider": "local",
      "apiBase": "http://host.docker.internal:11434/v1",
      "apiKey": ""
    }
  }
}
```

If `config.json` is absent, the factory creates a default one on workspace creation. The settings panel in the agent UI can edit these values live.

---

## Creating a workspace

Each spawnable agent needs a workspace directory at `data/workspaces/{slug}/`. The minimum viable workspace is a `SOUL.md`. The full scaffold:

```
data/workspaces/my-agent/
├── SOUL.md         # Who this agent is, personality, hard rules
├── AGENTS.md       # Task instructions and memory strategy
├── USER.md         # (optional) who the agent is talking to
├── TOOLS.md        # (optional) tool usage notes
├── HEARTBEAT.md    # (optional) periodic/proactive tasks
├── config.json     # model, provider, API base URL
├── cron/
│   └── jobs.json   # Scheduled tasks (empty array = no cron)
└── memory/
    └── MEMORY.md   # Persistent context the agent reads on load
```

Copy `data/workspaces/demo/` as a starting point, or copy `skill-sets/_template/` and adapt it.

---

## Environment variables (agent container)

The factory injects these into every spawned agent container:

| Variable | Value | Purpose |
|---|---|---|
| `AGENT_MODE` | `production` | Switches the agent to the standalone teal UI |
| `WORKSPACE_PATH` | `/app/data/workspaces/{slug}` | Primary workspace (read-write) |
| `SKILLSETS_PATH` | `/app/data/workspaces` | All workspaces root (read-only) |
| `AGENT_PORT` | `6161` | Internal HTTP port |
| `OLLAMA_BASE_URL` | from `.env` | LLM backend for this agent |
| `GROK_API_KEY` | from `.env` or empty | Optional xAI key |

---

## Cleanup

When you delete an agent from the UI (or `DELETE /api/factory/agents/{slug}`), the container is force-removed. The workspace at `data/workspaces/{slug}/` is left intact.

To clean up all spawned agent containers:

**Windows (PowerShell):**
```powershell
docker ps -a --filter "name=nvnnnbt-agent-" --format "{{.Names}}" | ForEach-Object { docker rm -f $_ }
```

**Linux / macOS:**
```bash
docker ps -a --filter "name=nvnnnbt-agent-" --format "{{.Names}}" | xargs -r docker rm -f
```

---

## Running multiple instances

Two (or more) instances of nvnNNBT can run on the same host — useful for a dev instance and a live instance side by side. Each instance needs:

**1. Its own directory** (separate clone or copy):
```
e:/nvnNNBT/          ← yellow / dev instance
e:/NEVEN/nvnnnbt/    ← NEVEN / live instance
```

**2. Its own `.env`** with offset ports and a unique project name:

```env
# .env for yellow (dev)
UI_PORT=3000
FACTORY_PORT=4000
AGENT_PORT=6161
CHROME_PORT=9222
AGENT_CHAT_PORT_BASE=4330
AGENT_GATEWAY_PORT_BASE=4230
COMPOSE_PROJECT_NAME=nvnnnbt

# .env for NEVEN (live)
UI_PORT=7446
FACTORY_PORT=4001
AGENT_PORT=6162
CHROME_PORT=9223
AGENT_CHAT_PORT_BASE=4430
AGENT_GATEWAY_PORT_BASE=4330
COMPOSE_PROJECT_NAME=nvn-neven
```

**3. Its own `docker-compose.yml`** with unique container and image names (so Docker doesn't confuse the two). The simplest way is to rename the `container_name:` and `image:` fields — or let `COMPOSE_PROJECT_NAME` handle auto-generated names (chrome, volumes, networks) while keeping explicit names unique manually.

With these settings, spawned agents from each instance pull from their own port band and their containers are named distinctly.
```

