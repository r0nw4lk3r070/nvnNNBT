# Tool Usage Notes

## File tools

- `edit_file` / `write_file` — create or update files in the workspace
- `read_file` — read files in the workspace

## web — Search

Use web search for: {{WEB_SEARCH_USE_CASES}}

## Memory tools

- `memory/MEMORY.md` — persistent facts and context
- `memory/HISTORY.md` — interaction log

Load MEMORY.md at conversation start. Write to it when something is worth keeping.

## {{AGENT_NAME}} workflow

1. {{WORKFLOW_STEP_1}}
2. {{WORKFLOW_STEP_2}}
3. {{WORKFLOW_STEP_3}}

## Skills

Skills are in `skills/` — each skill is a folder with a `SKILL.md`.
Load a skill's SKILL.md when the task matches its domain.