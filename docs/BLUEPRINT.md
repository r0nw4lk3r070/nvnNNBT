# nvnNNBT — Neven Nanobot Blueprint

**Version:** 0.1.0  
**Status:** Planning  
**Workfolder:** `e:\nvnNNBT`  
**Source material:** `e:\art`, `e:\ron`

---

## What this is

nvnNNBT is a Neven blueprint: a self-contained, Docker-first nanobot platform that anyone (Derek, a client, a future team member) can run with a single `docker compose up`. No machine-specific paths. No manual startup scripts. Front to back.

It merges two working systems that currently live in Ron's personal lab:

- **e:\art** — the nanobot agent server with a proven chat UI and lab workspace
- **e:\ron** — the agent/team orchestration platform with Docker spawning and a React dashboard

The result is the first Neven-owned, portable, production-adjacent nanobot product.

---

## Source inventory

### From e:\art

| Component | What it does | Condition |
|---|---|---|
| `server.py` (aiohttp, :6161) | Core nanobot agent loop, chat API, skill-set lab | Working. Hardcoded to `E:\Art` paths |
| `html_art.py` | Chat UI — Alpine.js SPA, SSE streaming, model switching, cron, MCP panel | Working. Embedded in Python file |
| `html_lab.py` | Lab UI — sidebar skill-set list, load/unload, scoped agent per skill-set | Working. Embedded in Python file |
| `portal/main.py` (FastAPI, :6162) | Dashboard — kanban tickets, weather, memory viewer, agent status | Working. Hardcoded paths |
| `discord_bot.py` | Discord integration (ART#0086) | Working. Token in `.env` |
| `skill-sets/` | Specialist agents (geo-seo, nvnJRST, call-centre, _template) | Working. Folder-based, portable |
| `skills/` | Coding, planning, writing skill definitions | Working |
| `cron/` | CronService, jobs.json | Working |

**Known issues in e:\art:**
- All paths hardcoded to `E:\Art\` — must be replaced with env vars / container paths
- Nanobot safety guard blocks localhost HTTP calls between services (workaround: direct Python imports)
- Port bind conflicts on restart — old processes hold ports
- `docs/to-check-out/` content missing (possible deleted/moved files)
- `discord_bot.py` not included in `start_all.ps1` — must be started manually

---

### From e:\ron

| Component | What it does | Condition |
|---|---|---|
| `services/api/` (Express/TS, :4110) | REST API, SQLite DB, Docker spawning via Dockerode | Working. Has agent/team/notes/events/todos routes |
| `services/ui/` (React/Vite, :4300) | Dashboard — 9 pages, agent chat, monitor, logs, settings | Working. Proxies to API |
| `services/nanobot/` | Mary (default agent container) with `chat_api.py` (SSE) | Working |
| `data/workspaces/` | Agent identity files (SOUL.md, AGENTS.md, etc.) per agent | Working. Portable |
| `data/teams/` | Team knowledge centers (inbox/queue/drafts/published pipeline) | Spec done, partially built |
| Agent spawn system | `POST /agents/spawn` → Dockerode creates container, assigns ports | API done. UI page not yet built |
| Team pipeline | inbox → queue → drafts → published, cron-driven | Spec done. Not fully wired |

**Known issues in e:\ron:**
- Agents page (spawn/manage) not yet in React dashboard — spec complete, code not started
- Teams page not yet in React dashboard
- Agent spawning tested locally but not inside a compose network (spawns assume host Docker socket)
- SQLite file path hardcoded in some places

---

## Target architecture

```
┌──────────────────────────────────────────────────────────────┐
│  nvnNNBT  —  docker compose up                               │
│                                                              │
│  ┌──────────────────────────────┐                           │
│  │  ui  (React/Vite)  :3000     │  Dashboard + Chat         │
│  │  - Chats with loaded agent   │  + Lab                    │
│  │  - Lab: browse/load skill-sets│  + Agent/team mgmt       │
│  │  - Agents: spawn/stop/monitor│                           │
│  │  - Teams: pipeline overview  │                           │
│  └──────────────┬───────────────┘                           │
│                 │ REST + SSE proxy                           │
│  ┌──────────────▼───────────────┐                           │
│  │  api  (Express/TS)  :4000    │  Single entry point       │
│  │  - Agent management (SQLite) │  Auth, routing,           │
│  │  - Team management           │  Docker orchestration     │
│  │  - Chat proxy → agent        │                           │
│  │  - Docker socket (spawn)     │                           │
│  └──────┬──────────┬────────────┘                           │
│         │          │                                         │
│  ┌──────▼──┐  ┌────▼───────────────────────────────────┐   │
│  │  agent  │  │  skill-sets volume (shared)             │   │
│  │ (nanobot│  │  /skill-sets/geo-seo/                   │   │
│  │  :6161) │  │  /skill-sets/nvnJRST/                   │   │
│  │  Art    │  │  /skill-sets/_template/                  │   │
│  │  server │  └────────────────────────────────────────┘   │
│  └────┬────┘                                                │
│       │                                                      │
│  ┌────▼────────────────────────┐                           │
│  │  Ollama  :11434              │  Local LLM only           │
│  │  (or host-networked Ollama) │  No cloud                  │
│  └─────────────────────────────┘                           │
└──────────────────────────────────────────────────────────────┘
```

**Services:**

| Service | Image | Port | Description |
|---|---|---|---|
| `ui` | `nvnnnbt-ui` | 3000 | React dashboard (ported from ron/ui + art lab panels) |
| `api` | `nvnnnbt-api` | 4000 | Express/TS API (ported from ron/api, paths cleaned) |
| `agent` | `nvnnnbt-agent` | 6161 | Nanobot server (ported from art/server.py, paths → env vars) |
| `ollama` | `ollama/ollama` | 11434 | Local LLM. Can be host-networked if Ollama runs on host |

Optional (Phase 2):
| `discord` | `nvnnnbt-discord` | — | Discord bot (ported from art/discord_bot.py) |

---

## What needs to be built

### Phase 1 — Core pipeline (chat + lab, Docker-clean)

**Goal:** Derek can `docker compose up`, open `:3000`, chat with a nanobot, and load a skill-set in the lab.

#### 1.1 Agent service (port from e:\art)
- [ ] Replace all `E:\Art\` paths with env vars (`WORKSPACE_PATH`, `SKILL_SETS_PATH`, etc.)
- [ ] Move HTML templates out of Python files → separate `templates/` folder
- [ ] Create `Dockerfile` for agent service
- [ ] Config via environment variables (model, Ollama URL, port)
- [ ] `SOUL.md`, `AGENTS.md`, `USER.md`, `TOOLS.md` → mounted from volume
- [ ] Skill-sets dir → mounted shared volume

#### 1.2 UI (merge art lab into ron dashboard)
- [ ] Port ron/ui React dashboard as base
- [ ] Add **Lab** page: skill-set browser sidebar + scoped chat (from html_lab.py logic)
- [ ] Add **Chat** page: full chat with main agent (from html_art.py logic)
- [ ] Wire model selector to API
- [ ] Wire skill-set load/unload to agent API

#### 1.3 API (port from e:\ron/api, clean paths)
- [ ] Remove Windows-specific path assumptions
- [ ] `/agents/spawn` — keep for Phase 2 (stub out for now)
- [ ] `/chat` proxy → agent :6161
- [ ] `/lab/load`, `/lab/unload`, `/lab/chat` proxy → agent
- [ ] `/models` proxy → Ollama
- [ ] SQLite path → `/data/ron.db` inside container

#### 1.4 Docker Compose
- [ ] `docker-compose.yml` with all services
- [ ] `.env.example` — all required vars documented
- [ ] Named volumes: `skill-sets`, `agent-workspace`, `db-data`
- [ ] Health checks on all services
- [ ] Ollama: external (host network) OR bundled — configurable via env

---

### Phase 2 — Agent & team management

**Goal:** UI to spawn solo agents and assemble teams. Each agent runs in its own container.

#### 2.1 Agent spawning (from e:\ron)
- [ ] Agents page in dashboard (list, status, ports)
- [ ] Spawn modal: pick workspace template, name, model
- [ ] API: `POST /agents/spawn` → Dockerode creates container
- [ ] Port registry (4230–4299 gateway, 4330–4399 chat)
- [ ] Mount workspace from `data/workspaces/{slug}/`

#### 2.2 Team pipelines (from e:\ron/data/teams)
- [ ] Teams page: list teams, create team
- [ ] Team detail: members, pipeline stages (inbox/queue/drafts/published)
- [ ] Cron jobs per team (`cron/jobs.json`)
- [ ] Activity log viewer

---

## Bugs to address on the route

| # | Source | Issue | Fix |
|---|---|---|---|
| 1 | art/server.py | Hardcoded `E:\Art\` paths everywhere | Replace with `os.environ.get('WORKSPACE_PATH', '/workspace')` |
| 2 | art/html_art.py | HTML embedded in Python (unmaintainable) | Extract to `templates/art.html` |
| 3 | art/html_lab.py | HTML embedded in Python | Extract to `templates/lab.html` |
| 4 | art/server.py | Nanobot safety guard blocks localhost calls | Route inter-service calls via Docker service names, not localhost |
| 5 | ron/api | SQLite path may be hardcoded | Move to env var `DB_PATH=/data/ron.db` |
| 6 | ron/api | Docker socket spawning assumes host Docker | Map `/var/run/docker.sock` in compose; test in Linux container |
| 7 | ron/ui | Agents/Teams pages not yet built | Build in Phase 2 |
| 8 | art/start_all.ps1 | Discord bot not auto-started | Discord becomes its own compose service |
| 9 | art/portal | Port conflicts on restart | Docker handles this — no manual kill needed |
| 10 | both | No health checks | Add `/health` endpoints + compose `healthcheck` blocks |

---

## Skill-set structure (reference)

A skill-set is a folder. It is self-contained and portable. The agent mounts it as a scoped workspace.

```
skill-sets/
└── my-skill-set/
    ├── SOUL.md          # Who this agent is (identity, voice, hard rules)
    ├── AGENTS.md        # What it does, how it works
    ├── USER.md          # Who uses it
    ├── TOOLS.md         # Tool usage patterns
    ├── HEARTBEAT.md     # Periodic tasks (cron-driven)
    ├── README.md        # Setup notes
    ├── cron/
    │   └── jobs.json    # {} or job definitions
    ├── memory/
    │   ├── MEMORY.md    # Persistent context
    │   └── HISTORY.md   # Interaction log
    ├── sessions/        # Auto-created by nanobot
    └── skills/
        ├── skill-one/
        │   └── SKILL.md
        └── skill-two/
            └── SKILL.md
```

The `workspace/` mirror (present in art) is a nanobot-specific artifact — in Docker, the volume mount replaces this pattern.

---

## What nvnNNBT is NOT

- Not a cloud product — all inference is local (Ollama)
- Not a replacement for e:\art or e:\ron — they stay as Ron's personal lab
- Not feature-complete in Phase 1 — the goal is a working, runnable skeleton
- Not tied to Sporen VZW — this is the general nanobot infrastructure blueprint

---

## Next steps

1. Set up `nvnNNBT` folder structure (services/, data/, skill-sets/, docs/)
2. Port `agent` service from e:\art — clean paths, write Dockerfile
3. Scaffold `api` service from e:\ron/api — clean, minimal routes for Phase 1
4. Build `ui` service — React base from ron/ui, add Lab page from art lab logic
5. Write `docker-compose.yml`
6. Smoke test: `docker compose up`, open :3000, chat, load skill-set
7. Fix bugs as encountered (see bug table above)
8. Tag `v0.1.0` when smoke test passes
