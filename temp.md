#### spawning agents. 

Spawning a production agent is the complete workspace and its key files. 
This must also include a backend server and a ui to continue tweaking and managing the production spawned bot. This also gives room for the agent to maintain a "website" with a dedicated chat to the agent and visual status and health of the bot. 

Once a bot or agent is spawned it leaves the factory. The process from workspace to spawning gets documented and archived. Development stays active from within the bot's spawned environment. 

Docker. Nothing of the spawned bot can be tied to the host machine. Pull it from github and it works everywhere right? All you need to do is give it its place, connect it to whichever intelligence provider you are using and it runs. 

---

I think it would also be wise to take into account spawning teams while building the solo stream. So we implement this right and ready for teams also. 

---

## Planning notes & Q&A

_This section is our shared scratchpad. Questions marked `Q:` need an answer before we build. Decisions marked `DECIDED:` are locked._

---

### The workflow (CORRECTED)

```
[Lab — load a skill-set, edit identity files]
    ↓  test personality in sandbox chat (already works)
[Satisfied? Go to Agents section]
    ↓  pick workspace, pick model, hit Spawn
[Agents section — factory registry]
    ↓  shows status, lets you start/stop/delete the container
    ↓  no chat here — the factory is done
[Spawned agent — independent container]
    ↓  has its own web UI on a second port (its own HTML server)
    ↓  chat + status + provider wizard all live there
    ↓  factory has no further connection to it
```

**Key principle:** the factory is the manufacturing step. Once a car leaves the factory, the factory has no connection to it. ART is the only agent that permanently lives inside the factory. Spawned agents are the product. They stand on their own.

---

### What already exists (don't rebuild)

- `factory/routers/agents.py` — spawn, stop, delete, list with live Docker status sync. Backend is ~80% done.
- `factory/routers/workspaces.py` — list, get, create, file editor, git versioning. Fully built.
- `factory/database.py` — full schema: `spawned_agents`, `workspaces`, `providers`, `team_members`, `agent_teams`. All there.
- `ui/index.html` — Agents section stub: workspace picker, spawn form, agent list with status dot + stop/delete. JS is there.

What's still missing from the backend agents.py:
- `POST /agents/{slug}/start` — start a stopped container (stop exists, start doesn't).
- `workspace_slug` not saved on spawn (body.slug is used as both, need to store it explicitly).

What was removed from scope (no longer needed):
- ~~`POST /agents/{slug}/chat` — chat proxy from factory to spawned agent.~~ Factory has no connection to spawned agents after spawn. Chat lives in the agent's own web UI.

---

### Q&A block

---

**Q1: Workspace slug = Agent slug?**

Currently `agents.py` uses `body.slug` as the workspace folder name AND the agent identifier. This means one workspace can only ever have one running agent. 

Options:
- A) Keep it: workspace slug = agent slug. Simple. One production agent per workspace. (Current approach.)
- B) Decouple: spawn form takes a workspace slug + a separate agent name. You can spawn "my-agent-v2" from workspace "my-agent". Supports multiple agents from one template.

> DECIDED: Option A — workspace slug = agent slug, 1:1. Lab works on skill-set templates. Load one in, test it. Unload, load another. That's all the Lab does.

**Elaboration on Q1:**

The choice has a deeper consequence than just naming — it determines what actually gets mounted into the container and where the agent writes its memory.

**Option A — coupled (1:1)**

```
data/workspaces/demo/   ←→   container nvnnnbt-agent-demo
                              reads and writes to the same folder
```

- The workspace IS the agent. Lab editor edits it. Sandbox tests it. Spawn runs it. One object.
- Memory, sessions, and history all write back to `data/workspaces/demo/memory/`. You can `git diff` the workspace to see what the agent has learned.
- Delete the agent → container removed, workspace stays. Respawn → picks up where it left off.
- **Limitation:** you can never run two copies of "demo" at the same time. One workspace = one live agent.
- **For teams:** each team member would need its own workspace folder. That's fine — the Lab already supports creating workspaces. You'd create `data/workspaces/support-a/`, `data/workspaces/support-b/` etc., each with their own identity. Team just links multiple agent slugs.

**Option B — decoupled (template → named copy)**

```
data/workspaces/demo/   ←   template (read-only)
data/workspaces/demo-v2/ ← copy made at spawn time, mounted rw into nvnnnbt-agent-demo-v2
```

- Spawn = "copy this workspace folder to a new slug, then run it." The original is the template.
- Lets you spin up `demo-alice` and `demo-bob` from the same personality template, each with their own memory.
- More powerful for teams (one template, many instances), but adds complexity: the factory has to manage which folders are templates vs. live agents.
- **Problem:** two agents sharing a mounted folder (rw) would corrupt each other's memory. So if you decouple, you MUST copy on spawn, not share the folder. This means workspace storage grows with every spawn.
- **Lab editor question:** when you open the Lab, are you editing the template or the live agent's workspace? Need a clear answer. ---- working on templates. skill-sets. load one in and it becomes this one. unload and reload with another and it becomes that one. ----

**My read:**

For Phase 2 (solo spawn), Option A is the right call. It's clean, the mental model is simple, and the constraint (one running agent per workspace) is not a real limitation for a solo agent factory — you just create a new workspace in the Lab if you want a second agent with the same personality. Option B becomes relevant when teams want to stamp out N copies of the same role, which is a Phase 3 problem.

The one thing we should add regardless: if you try to spawn a workspace that already has a running container, the UI shows a clear message — "this workspace has a running agent" — rather than silently failing with a 409.

> DECIDED: Option A for Phase 2 — workspace slug = agent slug, 1:1. Revisit for teams.

---

**Q2: Docker volumes vs bind-mount — the portability question**

Your note says "nothing of the spawned bot tied to the host machine." 

The current code does a **bind-mount** from `HOST_PROJECT_PATH/data/workspaces/{slug}` into the container. This works great locally and IS portable in the sense that any machine can clone the repo and run it — the workspace data lives in the repo (we committed it in Phase 1). `HOST_PROJECT_PATH` is just the path where you cloned it.

So the question is really: when the spawned agent writes to its `memory/` or `sessions/`, does that data:
- A) Write back to `data/workspaces/{slug}/memory/` on the host (current bind-mount behaviour). The workspace on disk is the live state.
- B) Write into a Docker named volume (isolated from the host folder). Host folder = template only; volume = live state.

Option A is simpler and means you can `git status` the workspace to see what the agent has been doing. Option B is cleaner isolation but adds volume management complexity.

> DECIDED: Option A — bind-mount. Pull from git, files come with it, mount wherever you cloned it. `HOST_PROJECT_PATH` is just the path on the current machine. Simple and git-trackable.

---

**Q3: The agent's "website" — what does it look like?**

You mentioned each spawned agent should have a "dedicated chat to the agent and visual status and health." 

The current `nvnnnbt-agent` image only serves a JSON API (port 6161). It has no web UI of its own.

Options:
- A) The factory acts as the web UI for all spawned agents. Chat with agent via the Agents section in the factory, using the `/agents/{slug}/chat` proxy. No per-agent website. Simple.
- B) Each spawned agent gets a minimal standalone web page (served from the agent container itself on a second port). Pull it up in a browser by port number. This requires adding a static HTML server to the agent image.
- C) The factory generates a per-agent URL that proxies through nginx (e.g. `/agents/demo/ui`). Requires dynamic nginx config or a reverse-proxy approach.

This decision affects the agent image and whether we add a web-band port (4430–4499 is already in the docs but not implemented).

> DECIDED: Option B — each spawned agent runs its own static HTML server on a second port. Web-band (4430–4499) gets used. Pull it up by port number directly. Factory is not involved.

---

**Q4: "Development stays active from within the bot's spawned environment"**

I want to make sure I understand this correctly. Does it mean:
- A) The factory UI can still open the spawned agent's workspace in the Lab editor and edit its identity files while it's running. The agent hot-reloads (or reloads on next conversation). Manage everything through the factory.
- B) The spawned agent has its own separate management interface (different URL, different port), independent from the factory.
- C) Something else — e.g. the agent's workspace becomes its own git repo that you can push changes to independently?

> DECIDED: The agent's own static HTML server serves both the management interface AND the direct chat. Factory is completely out of the picture after spawn. Independent product.

---

**Q5: Model picker in the spawn form**

The current Agents UI spawn form only has a workspace dropdown — no model picker. `SpawnBody` in agents.py already has a `model` field (defaults to `qwen3:1.7b`).

Should the spawn form also show the model picker (same provider tabs + model list as the sandbox), or is it fine to just type a model name? The workspace's `config.json` already sets a default model — should spawn just inherit that and let you override?

> DECIDED: Model picker lives in the spawned agent's own web UI, not the factory spawn form. Agent reads whatever LLM providers are available where it's running. If nothing configured, a first-run wizard guides setup. Factory spawn form just needs a minimal model field (inherit from workspace config.json, optional text override).

---

**Q6: Teams — what to stub in now?**

The DB already has `team_members` and `agent_teams` tables. The `spawned_agents` table has a `team_slug` column.

For Phase 2 solo spawn, I propose we:
- Pass `team_slug` as an optional field in `SpawnBody` (can be empty string).
- Store it in the DB on spawn.
- Don't build any team management UI yet — just make sure the data model is correct for later.

The Teams section in the UI is already a Phase 3 placeholder card. We leave it as-is.

> DECIDED: Yes — `team_slug` stays as optional field in `SpawnBody`, stored in DB. Teams UI stays as Phase 3 placeholder. No team management built in Phase 2.

---

**Q7: Spawn form — what fields exactly?**

Based on what we have and what makes sense:

```
Workspace:  [dropdown of data/workspaces/]
Model:      [inherited from workspace config.json, overridable]
            (or full model picker — see Q5)
[Spawn button]
```

That's the minimal. Anything else needed at spawn time? E.g. display name separate from slug?

> DECIDED: Workspace (slug dropdown) + model (text input, inherit from workspace config.json). No separate display name — slug is the name for now.

---

### Phase 2 scope (REVISED — all Q&A resolved)

Two separate streams. The factory and spawned agents are different products.

**Stream 1 — Factory spawn loop (Agents section end-to-end)**
1. Backend: `POST /agents/{slug}/start` — start a stopped container
2. Backend: fix `spawn_agent()` — save `workspace_slug` in DB, wire model from request
3. UI: add model text field to spawn form (pre-filled from workspace config.json via API)
4. UI: add Start button in agent list (for stopped agents, next to existing Stop/Delete)
5. UI: show `workspace_slug`, `model`, and `web_port` in each agent card
6. UI: show clear "already running" state if workspace already has a live container (no silent 409)

**Stream 2 — Spawned agent web UI (built into the agent image)**
7. Add static HTML server to agent image (aiohttp serves one HTML file on web-band port)
8. Agent web UI: chat interface (talks directly to port 6161 on the same container)
9. Agent web UI: status/health panel (model, uptime, memory size)
10. Agent web UI: provider wizard — if no LLM provider configured, prompt to set Ollama URL or API key
11. Web port (4430–4499) exposed and stored in DB alongside chat port

**Not in Phase 2:**
- ~~Chat proxy from factory to spawned agent~~ — factory loses connection at spawn
- ~~Lab promote button~~ — Lab is skill-set testing only; spawning is a separate step in Agents
- Teams, Arena, Benchmarks — Phase 3+

**Total: 11 items across 2 streams.**

---

### Status check (April 17, 2026)

| Area | State |
|---|---|
| Lab sandbox (chat + model picker) | ✅ Done |
| Lab skill-set loading | ✅ Done |
| Factory backend: spawn / stop / delete / list | ✅ Done (~80%) |
| Factory backend: start stopped container | ❌ Missing |
| Factory backend: workspace_slug saved on spawn | ❌ Missing |
| Factory UI: Agents section stub | ✅ Stub wired, untested end-to-end |
| Factory UI: model field in spawn form | ❌ Missing |
| Factory UI: Start button + web_port display | ❌ Missing |
| Agent image: own web UI server | ❌ Not started |
| Agent web UI: chat + status + provider wizard | ❌ Not started |

Stream 1 is 2 small backend fixes + 3 UI tweaks — fast.
Stream 2 (agent's own web UI) is the bigger build and where the product becomes truly portable.

Ready to start building when you are.

---

**Q8: One port or two for spawned agent web UI?**

> DECIDED: Option A — `GET /` served from the existing aiohttp server on port 6161. Web UI and chat API on the same port. No web-band ports needed for now. Adding a second port is a post-spawn choice if it ever comes up.

---

**Q9: Visual style of the agent web UI?**

> DECIDED: Same dark mode foundation as the factory, but different accent/element colors. Same family, clearly different product. Signals "you're now in the agent's own space."
