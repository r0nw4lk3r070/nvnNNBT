# nanobot-ai Upgrade Procedure

**Last updated:** April 2026  
**Applies to:** nvnNNBT and any downstream project that uses the same `services/agent/` pattern (spawned bots, cloned stacks).

---

## Overview

The agent service (`services/agent/`) runs on top of the `nanobot-ai` PyPI package. We pin the version explicitly in `requirements.txt` so upgrades are deliberate and reproducible.

```
services/agent/requirements.txt
  nanobot-ai==<version>     ← pinned here
  aiohttp
  loguru
```

---

## How to check for updates

```powershell
# Latest on PyPI
Invoke-RestMethod "https://pypi.org/pypi/nanobot-ai/json" | Select-Object -ExpandProperty info | Select-Object version, summary

# What is currently pinned
Get-Content services/agent/requirements.txt | Select-String nanobot
```

Or check the upstream GitHub releases:  
https://github.com/HKUDS/nanobot/releases

---

## Before upgrading — compatibility checklist

Before bumping the version, review the release notes for changes in these areas:

| Area | Why it matters | Our touch points |
|---|---|---|
| `OpenAICompatProvider.__init__` | We instantiate it directly in `agent.py` | `_make_provider()`, `_build_skillset_agent()` |
| `AgentLoop.__init__` kwargs | We pass ~12 named params | `_build_agent()`, `_build_skillset_agent()` |
| `SessionManager` / `CronService` | Constructor and start() API | `_build_agent()` |
| `MessageBus` | We hold a reference in `state._bus` | `server.py`, `handlers.py` |
| `ChannelManager` | Used for Discord channel | `server.py` |

**Rule:** if a release note mentions a refactor of any of the above, read the diff before upgrading.

**Safe to ignore for us:** Telegram, Feishu, WeChat, QQ, DingTalk, Slack, Discord channel improvements, CLI changes, WebUI, bwrap sandbox (Linux-only).

---

## Upgrade steps

### 1. Pin the version

```
# services/agent/requirements.txt
nanobot-ai==<new-version>
```

### 2. Build the agent image

```powershell
cd e:\nvnNNBT
docker compose build agent
```

Watch for errors during the pip install step. A clean build ends with:
```
 => exporting to image
 => => writing image sha256:...
```

### 3. Restart the agent container

```powershell
docker compose up -d agent
```

### 4. Verify

```powershell
# Health check
Invoke-RestMethod http://localhost:6161/health

# Installed version inside the container
docker exec nvnnnbt-agent-1 pip show nanobot-ai | Select-String Version
```

Expected: `Version: <new-version>`

### 5. Smoke test

- Open http://localhost:3000 → Art Office
- Send a message, confirm streaming reply
- Open Lab → load a skill-set workspace, send a message
- Check `/api/status` returns valid JSON with `ready: true`

### 6. Commit

```bash
git add services/agent/requirements.txt
git commit -m "chore(agent): bump nanobot-ai to <new-version>"
```

---

## Version history

| Date | From | To | Notes |
|---|---|---|---|
| 2026-04-23 | `0.1.4.post6` | `0.1.5.post2` | Dream memory, auto-compact, multi-MCP, mid-turn injection, cron hardening. No breaking changes in our touch points. |

---

## Applying to other bots / stacks

Every spawned agent and downstream stack (e.g. nvnTLS) that uses the same `services/agent/` base should follow this same procedure. The version is locked per-project — stacks do not auto-follow nvnNNBT.

**Pattern for downstream stacks:**

1. Copy `services/agent/requirements.txt` from nvnNNBT after a successful upgrade here
2. Run `docker compose build agent` in the downstream stack
3. Restart and smoke-test using the same checklist above

This project (nvnNNBT) acts as the **integration test bed** — upgrade here first, then propagate to production stacks only after smoke tests pass.

---

## Rollback

If something breaks after an upgrade:

```powershell
# Revert requirements.txt to the previous version
# services/agent/requirements.txt:
#   nanobot-ai==<previous-version>

docker compose build agent
docker compose up -d agent
```

The previous image layer is cached by Docker as long as you haven't pruned. A rollback build is fast (seconds, not minutes).
