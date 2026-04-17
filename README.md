# nvnNNBT — Agent Factory

**Version:** 0.2.0 · Phase 1 complete → Phase 2 next  
Build, test, and deploy AI agents and agent teams. One application, Docker-first.

---

## Services

| Service | Port | What |
|---|---|---|
| `ui` | 3000 | nginx — SPA entry point, proxies to factory + agent |
| `factory` | 4000 | FastAPI — workspace CRUD, sandbox, spawn, events |
| `agent` | 6161 | nanobot-ai — Art (persistent top-level agent) |

---

## Quick start

### Prerequisites

- Docker Desktop
- Ollama running on the host (`localhost:11434`) — or see [Bundled Ollama](#bundled-ollama)
- Optional: xAI API key for Grok models

### Configure

```bash
cp .env.example .env
# Add GROK_API_KEY if using xAI models (optional)
```

### Start

```bash
docker compose up --build
```

### Open

http://localhost:3000

---

## What's inside

**Art** — top-level agent. Always accessible via the right panel. Ask anything, get help building skill-sets, research, delegate. Supports Ollama local/cloud models and xAI Grok.

**Lab** — workspace editor and sandbox. Create or edit a skill-set (SOUL, AGENTS, TOOLS, HEARTBEAT, USER, skills). Load it into the sandbox, pick a model in the tab, chat with the scoped agent, iterate.

**Overview** — system health (factory, agent, Ollama), CPU/RAM, recent activity feed.

---

## LLM providers

Configured in `workspace/config.json`. Three provider profiles ship by default:

| Profile | Endpoint | Key |
|---|---|---|
| `local` | `http://host.docker.internal:11434/v1` | no |
| `ollamaCloud` | `http://host.docker.internal:11434/v1` | no |
| `xai` | `https://api.x.ai/v1` | `GROK_API_KEY` env var |

All model switching happens in the UI — Art panel header or the sandbox tab's model picker. Changes persist to `workspace/config.json`.

---

## Bundled Ollama

By default the stack expects Ollama on the host. To run it in Docker instead:

```bash
docker compose --profile bundled-ollama up --build
```

Then set in `.env`:

```env
OLLAMA_BASE_URL=http://ollama:11434
```

---

## Environment variables

| Variable | Default | Description |
|---|---|---|
| `OLLAMA_BASE_URL` | `http://host.docker.internal:11434` | Ollama endpoint for the agent |
| `GROK_API_KEY` | *(empty)* | xAI key — leave empty if not using Grok |
| `HOST_PROJECT_PATH` | `e:/nvnNNBT` | Host path for volume mounts |

---

## Project structure

```
nvnNNBT/
├── docker-compose.yml
├── .env
├── services/
│   ├── agent/          # nanobot-ai — Art agent (Python 3.12, aiohttp)
│   ├── factory/        # Agent Factory backend (Python 3.11, FastAPI)
│   └── ui/             # SPA + nginx reverse proxy
├── workspace/          # Art's workspace — mounted as /workspace in agent
│   ├── config.json     # Model, provider, and agent config
│   ├── SOUL.md
│   ├── AGENTS.md
│   ├── USER.md
│   ├── TOOLS.md
│   ├── HEARTBEAT.md
│   └── memory/
└── data/
    └── workspaces/     # Skill-sets — mounted into factory + agent
        ├── _template/
        ├── call-centre/
        ├── business-toolkit/
        └── ...
```

---

## Roadmap

- **Phase 1** — Art + Lab in Docker, factory service, SPA shell ✅
- **Phase 2** — Workspace spawn (solo agents as containers), Lab identity editor, Agents section
- **Phase 3** — Teams + Arena (multi-agent sessions)
- **Phase 4** — Version control + Benchmark (git tags, LLM-as-judge evals)
- **Phase 5** — Export (portable agent bundles)

See [docs/factory.md](docs/factory.md) for the full design document.
