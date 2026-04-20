# Workspace Lifecycle — from Lab to Deployment

**Last updated:** April 2026  
**Covers:** The complete path from building a workspace in nvnNNBT Lab → promoting to production → version-controlling via GitHub → deploying as a standalone container in another stack (e.g. nvnTLS).

---

## Overview

```
Lab (sandbox)          Production            GitHub             Remote stack
──────────────         ──────────────        ──────────         ────────────────
workspace/             data/                 nvnDTRL            nvnTLS/
  workspaces/    ──▶     workspaces/   ──▶   (main)      ──▶    workspaces/
    {slug}/               {slug}/                                  {slug}/
                                                                docker restart
```

---

## Part 1 — Build in the Lab

The sandbox lives at `workspace/workspaces/{slug}/` on the host (inside the container: `/app/sandbox/workspaces/{slug}/`). This is where you iterate freely — edits here do **not** affect a running spawned agent.

Minimum required files:

| File | Purpose |
|---|---|
| `SOUL.md` | Identity and personality (system prompt backbone) |
| `AGENTS.md` | Self-knowledge reference |
| `TOOLS.md` | Tool usage notes |
| `HEARTBEAT.md` | Periodic task schedule |
| `USER.md` | Who this agent serves |

Skills go in `skills/{name}/SKILL.md`. Each skill is a separate subdirectory.

The Lab UI loads workspaces from `workspace/workspaces/` — **not** from `data/workspaces/`. Keep this separation clear: sandbox is for building, production is for running.

---

## Part 2 — Promote to Production

When the workspace is ready, promote it:

```
POST http://localhost:4000/workspaces/{slug}/promote
```

Or via PowerShell:

```powershell
Invoke-RestMethod -Uri "http://localhost:4000/workspaces/{slug}/promote" -Method POST | ConvertTo-Json
```

**What promote does:**

- Copies `workspace/workspaces/{slug}/` → `data/workspaces/{slug}/`
- Skips: `sessions/`, `memory/`, `.git` (never overwrites runtime state or history)
- If a spawned container for this slug is running, restarts it automatically

**Response:**

```json
{ "ok": true, "slug": "editorial", "container_restarted": false }
```

`container_restarted: false` means no spawned container was running — which is expected if you only run this workspace in nvnTLS, not as a spawned agent in nvnNNBT.

---

## Part 3 — Version Control

The production workspace at `data/workspaces/{slug}/` is a standalone git repo (separate from the nvnNNBT repo). It is tracked on GitHub under a dedicated repository (e.g. `nvnDTRL` for the editorial workspace).

### First-time setup

```powershell
cd e:\nvnNNBT\data\workspaces\{slug}
git init
git remote add origin https://github.com/r0nw4lk3r070/{repo}.git
git branch -M main
```

### Committing

The workspace uses a whitelist `.gitignore` (`/*` + explicit exceptions). This means **new files are ignored by default** and must be force-added:

```powershell
# Skills must be force-added
git add -f skills/{name}/SKILL.md

# Identity files are already tracked after first add
git add SOUL.md AGENTS.md TOOLS.md HEARTBEAT.md USER.md

git commit -m "feat: describe the change"
git push origin main
```

### Tagging versions

```powershell
git tag v1.1 -m "add deploy skill"
git push origin --tags
```

### What is NOT committed

- `sessions/` — conversation logs (runtime state)
- `memory/history.jsonl` — message history (runtime state)  
- `cron/jobs.json` — managed by CronService at runtime (auto-reload)
- `config.json` — environment-specific (different per stack)

---

## Part 4 — Deploy to Remote Stack (nvnTLS)

### Prerequisites

1. The remote stack has the workspace cloned (first time):
   ```powershell
   cd e:\nvnTLS\workspaces
   git clone https://github.com/r0nw4lk3r070/{repo}.git {slug}
   ```

2. A `config.json` exists at `e:\nvnTLS\workspaces\{slug}\config.json` (not tracked in git — environment-specific). See config format below.

3. The service is defined in `e:\nvnTLS\docker-compose.yml`. See service definition below.

### Update flow (after every promote + push)

```powershell
cd e:\nvnTLS\workspaces\{slug}
git pull origin main
docker restart {slug}-nanobot
```

That's all. The workspace directory is bind-mounted into the container — no rebuild needed.

### Full pipeline (from sandbox to live)

```powershell
# 1. Promote sandbox → production
Invoke-RestMethod -Uri "http://localhost:4000/workspaces/{slug}/promote" -Method POST

# 2. Commit and push
cd e:\nvnNNBT\data\workspaces\{slug}
git add -A
git add -f skills/new-skill/SKILL.md    # if any new skill files
git commit -m "feat: describe change"
git push origin main

# 3. Pull and restart in nvnTLS
cd e:\nvnTLS\workspaces\{slug}
git pull origin main
docker restart {slug}-nanobot
```

---

## Part 5 — config.json per stack

Each stack needs its own `config.json` because port and provider differ. This file is **not** committed to git.

### nvnNNBT (spawned agent format)

```json
{
  "agents": {
    "defaults": {
      "model": "glm-5.1:cloud",
      "provider": "ollamaCloud"
    }
  },
  "providers": {
    "ollamaCloud": {
      "base_url": "http://host.docker.internal:11434/v1",
      "api_key": "ollama"
    }
  },
  "gateway": {
    "port": 6161
  }
}
```

### nvnTLS (standalone nanobot container format)

```json
{
  "agents": {
    "defaults": {
      "model": "glm-5.1:cloud",
      "provider": "ollama"
    }
  },
  "providers": {
    "ollama": {
      "base_url": "http://host.docker.internal:11434/v1",
      "api_key": "ollama"
    }
  },
  "gateway": {
    "port": 18800
  }
}
```

**Important:** nvnTLS uses the standard `nanobot-ai` package which does not know `ollamaCloud` — use `ollama` as the provider name. The port in `gateway.port` must match the port in `docker-compose.yml`.

---

## Part 6 — nvnTLS service definition

Template for adding a nanobot workspace as a container in nvnTLS:

```yaml
{slug}-nanobot:
  image: tls-nanobot:latest
  container_name: {slug}-nanobot
  ports:
    - "{host_port}:{host_port}"
  volumes:
    - ./workspaces/{slug}:/workspace
    - ./workspaces/{slug}/config.json:/root/.nanobot/config.json:ro
  environment:
    - OLLAMA_HOST=${OLLAMA_HOST:-http://host.docker.internal:11434}
    - GITHUB_TOKEN=${GITHUB_TOKEN:-}      # only if workspace uses deploy skill
  networks:
    - nvntls-internal
  restart: unless-stopped
```

The `tls-nanobot:latest` image is built from `Dockerfile.nanobot` in the nvnTLS root. It includes `git` (required for deploy skills).

---

## Part 7 — Spawn flow in nvnNNBT

For reference: spawning a workspace as a live agent inside nvnNNBT (separate from nvnTLS deployment).

```
POST http://localhost:4000/agents
{ "slug": "editorial", "model": "qwen3:1.7b" }
```

**What happens:**

1. Factory validates `HOST_PROJECT_PATH` is set (absolute host path, forward slashes: `e:/nvnNNBT`)
2. Workspace `data/workspaces/{slug}/` must exist
3. Factory claims two ports from reserved bands:
   - Gateway: 4230–4299 (allocated for future use, not currently exposed)
   - Chat: 4330–4399 (exposed as `127.0.0.1:{chat_port}:6161/tcp`)
4. Runs `nvnnnbt-agent:latest` as a sibling container on `nvnnnbt-net`
5. Bind-mounts the workspace from the host
6. Stores the agent in `data/nanobot.db`

**Access:** `http://localhost:{chat_port}/`  
**Stop:** `POST /agents/{slug}/stop`  
**Delete:** `DELETE /agents/{slug}` (removes container + registry entry, preserves workspace)

**API response includes:**

```json
{ "ok": true, "slug": "editorial", "container": "nvnnnbt-agent-editorial",
  "chat_port": 4330, "port": 4330 }
```

`port` and `chat_port` are the same value — `port` is an alias used by the factory UI to open the agent link.

---

## Environment variables

### nvnNNBT `.env`

| Variable | Required | Notes |
|---|---|---|
| `HOST_PROJECT_PATH` | **Yes** | Absolute host path to nvnNNBT folder. Use forward slashes. e.g. `e:/nvnNNBT` |
| `AGENT_IMAGE` | No | Defaults to `nvnnnbt-agent:latest` |
| `COMPOSE_NETWORK` | No | Defaults to `nvnnnbt-net` |
| `SANDBOX_ROOT` | No | Set via docker-compose.yml env block — `/app/sandbox/workspaces` |

### nvnTLS `.env`

| Variable | Required | Notes |
|---|---|---|
| `OLLAMA_HOST` | No | Defaults to `http://host.docker.internal:11434` |
| `GITHUB_TOKEN` | For deploy skill | Classic PAT with `public_repo` scope, or fine-grained PAT with `Contents: Read+Write` on the target repo |

---

## Known issues and lessons learned

| Issue | Root cause | Fix |
|---|---|---|
| Spawn fails with "workspace not found" | `HOST_PROJECT_PATH` not set or wrong path | Set in `.env` as absolute path with forward slashes |
| Container starts but agent uses wrong workspace | Volume path built from `workspace/workspaces/` instead of `data/workspaces/` | Fixed in `agents.py` — always use `HOST_PROJECT / "data" / "workspaces"` |
| `docker compose restart` doesn't pick up new volumes | `restart` reuses existing container config | Use `docker compose up -d --force-recreate {service}` for volume changes |
| Config validation error on startup | `config.json` was flat format instead of nested | Nanobot requires nested: `agents.defaults`, `providers`, `gateway` |
| `ollamaCloud` provider unknown in nvnTLS | nvnTLS uses standard `nanobot-ai`, not the custom build | Use `ollama` as provider name in nvnTLS config |
| `git` not found in container (deploy skill fails) | Base image didn't include git | Added `apt-get install git` to `Dockerfile.nanobot` — rebuild required |
| UI shows `http://localhost:undefined` for agent link | API returned `chat_port` but UI expected `port` | Added `"port": chat_port` alias to both `list_agents()` and `spawn_agent()` |
