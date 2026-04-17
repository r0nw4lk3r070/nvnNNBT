# Phase 3 — Team Agents

**Status:** Spec · April 2026  
**Prerequisite:** Phase 2 solo spawn complete and stable.

This document is the authoritative spec for team agent support in nvnNNBT.  
All architecture decisions recorded here are locked unless explicitly reopened.

---

## Core principle

A team is a set of solo agents that know about each other. Each member is a full nanobot — own container, own workspace, own chat endpoint, solo-reachable by a user. The team structure adds one thing on top: a **manager agent** that orchestrates them, and a **shared layer** they all read from.

The factory manufactures the team and then steps away. After spawn the team is self-contained — no factory dependency at runtime.

---

## Architecture decisions (locked)

| # | Question | Decision |
|---|---|---|
| 1 | Inter-agent communication | HTTP — manager POSTs to each member's `/chat` endpoint directly |
| 2 | Manager agent type | Regular nanobot with a SOUL/AGENTS.md that knows the team. No special factory access at runtime. |
| 3 | Arena for teams | Not a simulation. Spawn the team in a test configuration, interact with the manager, observe. Same containers, not shipped yet. |
| 4 | Shared knowledge format | SQLite DB in the team root (`knowledge/shared.db`). Members also have access to shared markdown in `knowledge/` |
| 5 | Team workspace structure | One parent folder per team. Manager lives at the root. Members each have their own sub-folder. |
| 6 | Port discovery at runtime | `team.json` written by the factory at spawn time. Manager reads it directly — no factory call at runtime. |

---

## Disk structure

```
data/workspaces/teams/editorial/        ← team root
  SOUL.md                               ← manager identity
  AGENTS.md                             ← manager instructions (knows team)
  TOOLS.md
  HEARTBEAT.md
  USER.md
  config.json                           ← manager model + provider
  team.json                             ← written by factory at spawn time
  knowledge/
    shared.db                           ← shared SQLite knowledge base
    inbox/                              ← drop zone for raw input
    library/                            ← curated output / reference docs
  memory/
    MEMORY.md                           ← manager's own memory
    history.jsonl
  sessions/
  skills/
  members/
    fetcher/                            ← member workspace (full nanobot)
      SOUL.md
      AGENTS.md
      config.json
      memory/
      sessions/
      skills/
    judge/
    writer/
```

### team.json (written by factory at spawn, read by manager at runtime)

```json
{
  "name": "editorial",
  "manager": "editorial",
  "members": [
    { "slug": "editorial-fetcher", "role": "fetcher", "chat_port": 4331 },
    { "slug": "editorial-judge",   "role": "judge",   "chat_port": 4332 },
    { "slug": "editorial-writer",  "role": "writer",  "chat_port": 4333 }
  ]
}
```

The factory allocates ports at spawn time and writes this file before starting any containers.  
The manager's AGENTS.md instructs it to load `team.json` and use those ports for delegation.

---

## Manager agent behaviour

The manager is the only agent the user talks to directly. It:

1. Reads `team.json` on startup — knows who the team members are and where they run
2. Writes a plan when given a task
3. Calls each member's `/chat` endpoint in sequence, passing input + previous output
4. Collects the final result and returns it to the user
5. Updates `memory/MEMORY.md` with decisions and outcomes

Members are called with a structured prompt — their role, the current task, and any context from previous steps. They respond as they normally would in chat. No special protocol needed.

Members can also be called directly by a user if needed — they're solo agents. But in team mode, the manager orchestrates.

---

## Shared knowledge layer

The shared SQLite DB (`knowledge/shared.db`) holds:

| Table | Purpose |
|---|---|
| `facts` | Key-value knowledge entries with source + timestamp |
| `articles` | Longer text pieces (title, body, status, author slug) |
| `queue` | Task pipeline queue (for pipeline/cron mode) |
| `log` | Cross-agent activity log |

Members access it via a tool registered in their `TOOLS.md`. The factory creates and migrates the schema at team spawn time.

The `knowledge/inbox/` and `knowledge/library/` directories provide raw file access for agents that process documents.

---

## Execution modes

### On-demand (manager-driven)

User sends a task to the manager. Manager writes a plan, calls members in sequence, returns result. No cron involved. Good for: article drafts, research tasks, one-off jobs.

### Pipeline (cron-driven)

A cron job triggers the manager on a schedule. Manager picks the next item from `knowledge/queue`, executes the plan, writes output to `knowledge/library/`. Good for: continuous content production, monitoring, batch processing.

Both modes use the same underlying delegation mechanism (HTTP to member `/chat`). Cron is just the trigger.

---

## Deployment sizes

Teams are not all the same size. The factory should warn at spawn time if the team is large.

| Team size | Deployment model |
|---|---|
| 2–4 members | Can share host resources comfortably. One compose stack. |
| 5–8 members | One container per agent recommended. Monitor RAM. |
| 9+ members | Dedicated host or split across machines. Out of factory scope. |

Each member gets the same port bands as solo agents. The factory allocates sequentially within the band.

---

## Port bands (extended for teams)

Existing bands from Phase 2:
- Chat band: 4330–4399 (solo agents)

New bands for teams:
- Team chat band: 4400–4499 (team members)
- Team manager band: 4500–4549 (manager agents)

If bands fill up, the factory returns an error and the user must stop old containers.

---

## Factory changes required (Phase 3 build list)

### Backend (`factory/routers/`)

1. **`teams.py`** — new router
   - `GET  /teams` — list team workspaces from `data/workspaces/teams/`
   - `GET  /teams/{slug}` — read team.json + member status
   - `POST /teams` — create team workspace skeleton on disk + DB row
   - `POST /teams/{slug}/spawn` — allocate ports for all members, write `team.json`, start all containers
   - `POST /teams/{slug}/stop` — stop all member containers + manager
   - `DELETE /teams/{slug}` — stop + remove all containers (workspace stays)

2. **`agents.py`** — small additions
   - Store `team_slug` in DB on spawn (already in schema, not wired)
   - `GET /agents` — include `team_slug` in response

### Database (`factory/database.py`)

- `agent_teams` and `team_members` tables already in schema — wire them up
- Add `team_slug` index on `spawned_agents`

### Shared knowledge init

- At team spawn: create `knowledge/` dirs, initialise `shared.db` with schema above

---

## UI changes required

### Factory UI (`services/ui/index.html`)

1. **Teams section** (currently Phase 3 placeholder card)
   - Team list — name, member count, status (all running / partial / stopped)
   - Create team form — name, initial member list
   - Team detail — member list with individual status dots + ports
   - Spawn / Stop / Delete team actions
   - Link to manager agent's chat UI (by port)

2. **Lab** — no changes needed for Phase 3. Lab still works on individual workspaces/skill-sets. Team members are individual workspaces, tested individually in Lab before being added to a team.

---

## Arena (Phase 3 scope — test teams before shipping)

The Arena is not a simulation. It is a real spawned team in a "test" state:

1. User creates a team workspace in the Lab (members individually tested)
2. User spawns the team from the Teams section with `mode: test` flag
3. Arena section shows the running team — user interacts with the manager
4. Session logs show the full delegation chain (manager → member → result)
5. When satisfied: flip to `mode: production`, team is considered shipped

The `test` flag is just metadata in the DB. Containers are identical. The distinction tells the factory which teams are still being validated vs. live.

**Arena UI additions:**
- Delegation trace panel — shows each HTTP call the manager made, to which member, with what input/output
- Replay — rerun a previous session's plan against the current team state
- Member override — temporarily swap one member's model without respawning

---

## What Phase 3 does NOT include

- Multi-host / distributed teams (out of scope)
- Agent-to-agent communication outside the manager (members only talk to the manager, not each other directly)
- Real-time streaming from member to manager (request/response only — no event streams between agents)
- Vector DB or embedding-based knowledge retrieval (SQLite facts table is sufficient for Phase 3)
- Automatic team scaling

---

## Open questions (not blocking Phase 3 start)

- **Export format for teams** — how does a team get packaged for handoff? Separate compose file per team? Single multi-service compose? (Phase 4 / export spec)
- **Versioning** — should `team.json` be git-tracked automatically at spawn? Probably yes.

---

## Build order

1. DB wiring — `team_slug` in agents, `agent_teams` + `team_members` tables active
2. `teams.py` router — CRUD + spawn
3. `knowledge/shared.db` init at spawn
4. Teams UI section — list, create, spawn, stop, delete
5. Manager agent template (`skill-sets/_team-manager/`) — SOUL + AGENTS with team.json tooling
6. Arena UI additions — delegation trace, replay
7. `mode: test` flag + Arena section wiring
