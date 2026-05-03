# nvnNNBT — Agent Factory

**Version:** 0.4.0 · Phase 3 complete · Phase 4 next  
Build, test, and deploy AI agents and agent teams. One application, Docker-first.

---

## Services

| Service | Port | What |
|---|---|---|
| `ui` | 3000 | nginx — SPA entry point, proxies to factory + agent |
| `factory` | 4000 | FastAPI — workspace CRUD, sandbox, spawn, teams, benchmark, events |
| `agent` | 6161 | nanobot-ai — Art (persistent top-level agent) |
| `chrome` | 9222 | Headless Chromium — CDP endpoint for browser harness |

Spawned solo agents use ports **4330–4399** (chat). Team members use **4400–4499**, team managers **4500–4549**.

---

## Quick start

### Prerequisites

- Docker Desktop
- Ollama running on the host (`localhost:11434`) — or see [Bundled Ollama](#bundled-ollama)
- Optional: cloud API keys (xAI Grok, OpenAI, etc.)

### Configure

```bash
cp .env.example .env
# Required for agent/team spawning:
HOST_PROJECT_PATH=E:/nvnNNBT   # absolute path to this folder on the host
# Optional provider keys:
GROK_API_KEY=...
```

### Start

```bash
docker compose up --build
```

### Open

http://localhost:3000

---

## What's inside

The factory UI is a VS Code–style single-page app with sections in the activity bar:

| Section | What |
|---|---|
| **Room** | P2P room chat — real-time messaging via SSE, @mention agent invocation, optional peer federation across machines |
| **Art Office** | Top-level agent — persistent chat, streaming, tool use, right-panel settings |
| **Lab** | Workspace editor — write SOUL, AGENTS, TOOLS, HEARTBEAT, USER, skills. Open any workspace in the sandbox to chat with the scoped agent and iterate. Version tagging, restore, and promote to production. |
| **Agents** | Solo agent spawn — slug, display name, model → own Docker container, own workspace, own chat UI |
| **Teams** | Multi-agent teams — create with skillset + model picker per member and manager, shared knowledge base (`shared.db`), spawn/stop/delete |
| **Arena** | Test teams before going live — spawn in test mode, interact with the manager, observe delegation |
| **Benchmark** | Tag workspace versions, define task sets, run LLM-as-judge evals, compare across versions and models |
| **DevOps / Settings** | Provider onboarding wizard — add/remove LLM providers, test connection, discover models, set API keys |

---

## LLM providers

Providers are configured in the **Settings** section of the UI and stored in `workspace/config.json`. Any OpenAI-compatible endpoint works. Defaults:

| Profile | Endpoint | Key |
|---|---|---|
| `local` | `http://host.docker.internal:11434/v1` | — |
| `xai` | `https://api.x.ai/v1` | `GROK_API_KEY` |

Add more (OpenAI, Anthropic via proxy, LM Studio, etc.) directly in the UI. Model switching is available in every section — Art panel, sandbox tab, team create form, and benchmark runs.

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
| `HOST_PROJECT_PATH` | *(must set)* | Absolute host path to this folder — required for agent/team spawning |
| `OLLAMA_BASE_URL` | `http://host.docker.internal:11434` | Ollama endpoint |
| `GROK_API_KEY` | *(empty)* | xAI key — leave empty if not using Grok |
| `FACTORY_TOKEN` | *(empty)* | Optional bearer token for factory API auth |
| `HOST_RAM_MB` | `0` | Physical host RAM in MB — set for accurate dashboard memory display |
| `USER_NAME` | `user` | Display name shown in room chat |
| `PEER_URL` | *(empty)* | URL of a peer instance for P2P room federation (e.g. a Tailscale address) |
| `UI_PORT` | `3000` | Host port for the UI |
| `FACTORY_PORT` | `4000` | Host port for the factory API |
| `AGENT_PORT` | `6161` | Host port for the Art agent |
| `CHROME_PORT` | `9222` | Host port for headless Chromium CDP |

---

## Project structure

```
nvnNNBT/
├── docker-compose.yml
├── .env
├── services/
│   ├── agent/              # nanobot-ai — Art agent (Python 3.12, aiohttp)
│   ├── factory/            # Agent Factory backend (Python 3.12, FastAPI)
│   │   ├── main.py
│   │   ├── database.py
│   │   └── routers/
│   │       ├── agents.py       # solo agent spawn/stop/delete
│   │       ├── teams.py        # team create/spawn/stop/delete
│   │       ├── workspaces.py   # skill-set CRUD, file editor, git versioning
│   │       ├── sandbox.py      # ephemeral sandbox sessions
│   │       ├── benchmark.py    # task sets, LLM-as-judge runs
│   │       ├── room.py         # P2P room chat — SSE fan-out, peer federation, @mention agent
│   │       ├── system.py       # health, CPU/RAM, provider probes
│   │       └── events.py       # activity log
│   └── ui/                 # SPA + nginx reverse proxy
├── workspace/              # Art's workspace — mounted as /workspace in agent
│   ├── config.json         # Model, provider, and agent config
│   ├── SOUL.md / AGENTS.md / TOOLS.md / HEARTBEAT.md / USER.md
│   ├── memory/
│   └── workspaces/         # Skill-sets managed via Lab
│       ├── _template/
│       └── ...
├── data/
│   ├── factory.db          # SQLite — agent registry, teams, benchmark runs
│   └── workspaces/         # Workspaces for spawned agents and teams
│       └── teams/          # Team roots — manager + members/ + knowledge/
└── skill-sets/             # Bundled skill-set templates
    └── _template/
```

---

## Roadmap

- **Phase 1** — Art + Lab in Docker, factory service, SPA shell ✅
- **Phase 2** — Solo agent spawn, standalone agent UI, Lab editor + sandbox, workspace CRUD ✅
- **Phase 3** — Teams, Arena, shared knowledge base, delegation log, session replay, member override ✅
- **Phase 4** — Provider onboarding wizard, P2P room chat, Lab version restore/promote, cross-platform setup scripts ✅
- **Phase 5** — Export (portable agent bundles)

See [docs/factory.md](docs/factory.md) for the full architecture document.

---

## Maintenance

- [docs/nanobot-upgrade.md](docs/nanobot-upgrade.md) — How to upgrade `nanobot-ai` (compatibility checklist, build steps, rollback, propagation to downstream stacks)
