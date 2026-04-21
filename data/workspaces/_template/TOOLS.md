# Tool Usage Notes

Tool signatures are provided automatically via function calling.
This file documents non-obvious constraints and {{AGENT_NAME}}-specific patterns.

## File tools

- `edit_file` / `write_file` — create or update files in the workspace
- `read_file` — read files in the workspace

## exec — Safety Limits

- Commands have a configurable timeout (default 60s)
- Dangerous commands are blocked (rm -rf, format, dd, shutdown, etc.)
- Output is truncated at 10,000 characters
- `restrictToWorkspace` config can limit file access to the workspace

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
4. {{WORKFLOW_STEP_4}}

## Skills

Skills are in `skills/` — each skill is a folder with a `SKILL.md`.
Load a skill's SKILL.md when the task matches its domain.