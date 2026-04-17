# Agent Creation Template

Use this template to spin up a new nanobot agent in minutes.

## Quick start

1. **Copy the template**
   ```
   cp -r skill-sets/_template skill-sets/your-agent-name
   ```

2. **Rename skill folders** (optional)
   ```
   mv skill-sets/your-agent-name/skills/skill-1 skill-sets/your-agent-name/skills/your-skill-name
   ```
   Do the same for `skill-2`, `skill-3` and in `workspace/skills/`.

3. **Fill in the placeholders**

   Every file uses `{{PLACEHOLDER}}` syntax. Search for `{{` and replace each one with your agent's specifics.

   **Must-fill files** (do these first):
   - `SOUL.md` — agent identity, personality, voice, hard rules
   - `AGENTS.md` — responsibilities, workflow, communication style
   - `USER.md` — who the agent talks to, common needs, handling tips
   - `TOOLS.md` — tool usage patterns specific to your agent

   **Skills** (customise per domain):
   - `skills/skill-1/SKILL.md` — rename folder, fill in skill details
   - `skills/skill-2/SKILL.md` — same
   - `skills/skill-3/SKILL.md` — same
   - Remove skill folders you don't need. Add more if needed.

   **Workspace mirror** — repeat the same fills in `workspace/`:
   - `workspace/SOUL.md`
   - `workspace/AGENTS.md`
   - `workspace/USER.md`
   - `workspace/TOOLS.md`
   - `workspace/skills/*/SKILL.md`

   **Memory** — leave empty, agents fill these during use:
   - `memory/MEMORY.md`
   - `memory/HISTORY.md`
   - `workspace/memory/MEMORY.md`
   - `workspace/memory/HISTORY.md`

4. **Test it**

   Load the agent in the Lab (http://localhost:6161/lab) and start a conversation. Verify:
   - Identity is correct
   - Voice/personality matches
   - Skills load when relevant
   - Memory writes work

5. **Clean up**

   - Delete any unused skill folders
   - Remove placeholders you didn't fill (or replace with "N/A")
   - Make sure `cron/jobs.json` is valid empty JSON: `{}`

## Placeholder reference

| Placeholder | Description | Example |
|---|---|---|
| `{{AGENT_NAME}}` | Agent's name | "bol.com Call Centre Agent" |
| `{{ORG_NAME}}` | Organisation | "bol.com" |
| `{{ROLE_DESCRIPTION}}` | One-line role | "a professional customer service agent" |
| `{{ONE_LINE_IDENTITY}}` | Core identity statement | "I handle customer calls with care and efficiency." |
| `{{CORE_PURPOSE}}` | What the agent does | "resolve customer issues" |
| `{{KEY_BEHAVIOUR}}` | Signature behaviour | "stay calm when customers are upset" |
| `{{LANGUAGE}}` | Language(s) | "English" / "Dutch + English" |
| `{{TONE}}` | Communication tone | "professional" / "casual" / "direct" |
| `{{USER_GROUP}}` | Who the agent serves | "Customer" / "Student" / "Developer" |
| `{{HARD_RULE_*}}` | Non-negotiable rules | "Never share customer data" |
| `{{SKILL_NAME}}` | Skill name | "Customer Resolution" / "De-escalation" |

## File structure

```
_template/
├── SOUL.md              # Identity, personality, voice, hard rules
├── AGENTS.md            # Instructions, responsibilities, workflow
├── USER.md              # Who the agent talks to
├── TOOLS.md             # Tool usage patterns
├── HEARTBEAT.md         # Periodic tasks (disabled by default)
├── cron/
│   └── jobs.json        # Cron job definitions
├── memory/
│   ├── MEMORY.md        # Persistent context (starts empty)
│   └── HISTORY.md       # Interaction log (starts empty)
├── sessions/            # Session storage (auto-created)
├── skills/
│   ├── skill-1/SKILL.md
│   ├── skill-2/SKILL.md
│   └── skill-3/SKILL.md
└── workspace/           # Mirror of above (agent workspace copy)
    ├── SOUL.md
    ├── AGENTS.md
    ├── USER.md
    ├── TOOLS.md
    ├── HEARTBEAT.md
    ├── cron/jobs.json
    ├── memory/
    │   ├── MEMORY.md
    │   └── HISTORY.md
    ├── sessions/
    └── skills/
        ├── skill-1/SKILL.md
        ├── skill-2/SKILL.md
        └── skill-3/SKILL.md
```

## Tips

- Start with the call-centre agent (`skill-sets/call-centre/`) as a reference — it was the first agent built from scratch.
- The `workspace/` mirror is what the agent sees at runtime. Both root and workspace must be filled in.
- Skills are domain-specific. Rename them to match what the agent actually does. 1–3 is usually enough.
- Keep `HEARTBEAT.md` empty unless you want periodic tasks.
- Don't overthink placeholders — fill what's obvious, leave the rest for iteration.