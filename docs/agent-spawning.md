# Agent Spawning

nvnNNBT can spawn additional nanobot agents on demand — each running in its own Docker container, with its own identity, workspace, and model. The API orchestrates this through the Docker socket without Docker-in-Docker.

---

## How it works

The `api` service mounts the host Docker socket (`/var/run/docker.sock`). When a spawn request comes in, the API calls the Docker daemon directly — creating a sibling container (not a child), attaching it to the same internal network, and binding a workspace folder from the host. The agent is then reachable from the API by its container name.

```
┌─────────────┐        POST /agents        ┌─────────────┐
│  api        │ ──────────────────────────▶ │  Docker     │
│  :4000      │                             │  daemon     │
│             │ ◀── container created ───── │  (socket)   │
└──────┬──────┘                             └─────────────┘
       │  proxy /agents/:slug/chat
       ▼
┌─────────────────────┐
│  nvnnnbt-agent-slug │  spawned sibling container
│  :6161              │  on nvnnnbt-net
└─────────────────────┘
```

All spawned containers share the same `nvnnnbt-agent:latest` image built by Compose. They are isolated from each other by workspace and container name.

---

## Prerequisites

Before spawning, two things must be true:

1. **`HOST_PROJECT_PATH` is set** in `.env` — the absolute path to the nvnNNBT folder on the host machine. The API container needs this because Docker bind-mounts require host-absolute paths.

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

The API keeps a SQLite database at `/app/data/nanobot.db` (persisted to `./data/nanobot.db` on the host via bind mount). This acts as the agent registry.

| Column | Type | Description |
|---|---|---|
| `slug` | TEXT (PK) | URL-safe identifier. Lowercase, alphanumeric + hyphens, max 31 chars |
| `display_name` | TEXT | Human-readable name |
| `model` | TEXT | Model identifier passed to the agent container |
| `port` | INTEGER | Host port assigned (range 6200–6299) |
| `container` | TEXT | Docker container name (`nvnnnbt-agent-{slug}`) |
| `status` | TEXT | Last known status: `running`, `stopped`, `removed`, etc. |
| `created_at` | TEXT | ISO datetime (UTC) |
| `started_at` | TEXT | ISO datetime of last start (UTC) |

Status is synced live from the Docker daemon on `GET /agents` and `GET /agents/:slug/status`.

---

## API reference

All routes are under `/agents`. If `API_KEY` is set in `.env`, include it as `x-api-key` header or `?key=` query param.

### List agents

```
GET /agents
```

Returns all agents from the registry with live status.

```json
{
  "agents": [
    {
      "slug": "demo",
      "display_name": "Demo Agent",
      "model": "gemma4:2b",
      "port": 6200,
      "container": "nvnnnbt-agent-demo",
      "status": "running",
      "created_at": "2026-04-16T10:00:00",
      "started_at": "2026-04-16T10:00:05"
    }
  ]
}
```

### Spawn an agent

```
POST /agents
Content-Type: application/json

{
  "slug": "demo",
  "display_name": "Demo Agent",
  "model": "gemma4:2b"
}
```

- `slug` — required. Unique, lowercase, alphanumeric + hyphens, max 31 chars.
- `display_name` — required.
- `model` — optional, defaults to `gemma4:2b`. Any model available in the connected LLM backend.

Returns `201` with the created agent record. Returns `400` for validation errors, `409` if slug already exists, `500` if `HOST_PROJECT_PATH` is not set or Docker fails.

### Get status

```
GET /agents/:slug/status
```

Inspects the container live. Returns `running`, `stopped`, `exited`, or `removed` (if the container was deleted outside of the API).

### Start / stop

```
POST /agents/:slug/start
POST /agents/:slug/stop
```

### Delete

```
DELETE /agents/:slug
```

Force-removes the container and deletes the agent from the registry. **Does not delete** the workspace folder at `data/workspaces/{slug}/` — that is intentional. Data is kept; the agent entry is removed.

### Chat with a spawned agent

```
POST /agents/:slug/chat
```

SSE-streaming proxy to the agent container. Same request/response format as the primary agent's `/chat` endpoint. The spawned agent must be in `running` status.

```bash
curl -N -X POST http://localhost:4000/agents/demo/chat \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hello"}]}'
```

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
├── config.json     # (optional) override model, Ollama URL, etc.
├── cron/
│   └── jobs.json   # Scheduled tasks (empty array = no cron)
└── memory/
    └── MEMORY.md   # Persistent context the agent reads on load
```

Copy `data/workspaces/demo/` as a starting point or copy `skill-sets/_template/` and adapt it.

---

## Port allocation

Spawned agents are assigned host ports in the range **6200–6299** (100 concurrent agents). Port assignment is sequential from the lowest free port in that range, tracked in the SQLite registry.

Spawned agents are **not** accessible through the UI nginx proxy — only through the API (`/agents/:slug/chat`). They run directly on `nvnnnbt-net` and the API reaches them by container name.

---

## Cleanup

When you delete an agent (`DELETE /agents/:slug`), the container is force-removed. The workspace data in `data/workspaces/{slug}/` is left intact.

To fully clean spawned containers when the stack is brought down:

```bash
docker compose down
docker ps -a --filter "name=nvnnnbt-agent-" --format "{{.Names}}" | ForEach-Object { docker rm -f $_ }
```

On Linux:

```bash
docker ps -a --filter "name=nvnnnbt-agent-" --format "{{.Names}}" | xargs -r docker rm -f
```
