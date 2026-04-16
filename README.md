# nvnNNBT — Neven Nanobot Blueprint

**Version:** 0.1.0 · Phase 1  
A portable, Docker-first nanobot platform. `docker compose up` and go.

---

## Services

| Service | Port | What |
|---|---|---|
| `ui` | 3000 | nginx — entry point, proxies to agent |
| `api` | 4000 | Express/TS — agent registry, spawn API |
| `agent` | 6161 | nanobot-ai — chat, lab, skill-sets |
| `ollama` | — | Bundled Ollama (optional, profiled out by default — see below) |

---

## Quick start

### 1. Prerequisites

- Docker Desktop (or Docker Engine on Linux)
- 4 GB RAM minimum (8+ recommended for larger models)

### 2. Configure

```bash
cp .env.example .env
# Edit .env if needed (defaults work out of the box)
```

### 3. Start

```bash
docker compose up --build
```

This assumes Ollama is already running on your host (the default). If you don't have Ollama, see [Bundled Ollama](#bundled-ollama) below.

### 4. Open

| URL | What |
|---|---|
| http://localhost:3000 | Chat with the nanobot |
| http://localhost:3000/lab | Lab — load and test skill-sets |
| http://localhost:6161 | Agent direct (no nginx) |
| http://localhost:4000/health | API health check |

---

## Using the Lab

The Lab lets you load a skill-set and chat with a scoped nanobot agent. Skill-sets live in `./skill-sets/`. A `_template` is included to get started.

**To create a new skill-set:**

1. Copy `skill-sets/_template/` → `skill-sets/my-agent/`
2. Fill in `SOUL.md`, `AGENTS.md`, `USER.md` (replace `{{PLACEHOLDERS}}`)
3. Open http://localhost:3000/lab
4. Select your skill-set from the sidebar, choose a model, click Load

---

## Bundled Ollama

By default the stack uses Ollama running on your host. If you don't have a host Ollama, you can start the bundled one:

```bash
docker compose --profile bundled-ollama up --build
```

Then set `.env`:

```env
OLLAMA_BASE_URL=http://ollama:11434
```

Pull a model into it:

```bash
docker exec nvnnnbt-ollama ollama pull qwen3:1.7b
```

---

## Environment variables

See [.env.example](.env.example) for the full list with descriptions.

| Variable | Default | Description |
|---|---|---|
| `UI_PORT` | 3000 | Host port for the UI |
| `API_PORT` | 4000 | Host port for the API |
| `AGENT_PORT` | 6161 | Host port for the agent (direct) |
| `OLLAMA_PORT` | 11434 | Host port for Ollama |
| `OLLAMA_BASE_URL` | http://host.docker.internal:11434 | URL agent uses to reach Ollama |
| `API_KEY` | *(empty)* | Auth key for the API. Empty = no auth |
| `GROK_API_KEY` | *(empty)* | xAI Grok key (optional cloud models) |

---

## Project structure

```
nvnNNBT/
├── docker-compose.yml
├── .env.example
├── services/
│   ├── agent/          # nanobot-ai server (Python 3.12)
│   ├── api/            # Express/TS proxy (Node 20)
│   └── ui/             # nginx reverse proxy
├── workspace/          # Mounted as /workspace in agent container
│   ├── config.json     # Agent config (model, Ollama URL, etc.)
│   ├── SOUL.md         # Agent identity
│   ├── AGENTS.md       # Agent instructions
│   ├── USER.md         # User profile
│   ├── TOOLS.md        # Tool usage notes
│   ├── HEARTBEAT.md    # Periodic tasks
│   ├── cron/jobs.json
│   └── memory/
└── skill-sets/         # Mounted as /skill-sets in agent container
    └── _template/      # Starter template for new skill-sets
```

---

## Changing the default model

Edit `workspace/config.json`:

```json
{
  "agents": {
    "defaults": {
      "model": "gemma4:12b"
    }
  }
}
```

Or use the Model selector in the chat UI header (persists to config.json).

---

## Roadmap

- **Phase 1** — Chat + Lab in Docker ✅
- **Phase 2** — Agent spawning via REST API (`POST /agents`) ✅
- **Phase 3** — Agent spawning UI, team pipelines
- **Phase 4** — Discord bot service, MCP server integrations

---

## Docs

- [LLM providers — Ollama, vLLM, external APIs](docs/llm-providers.md)
- [Agent spawning — spawn and manage multiple agents](docs/agent-spawning.md)
- [BLUEPRINT.md](BLUEPRINT.md) — full design document
