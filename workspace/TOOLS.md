# Tool Usage Notes

## File tools

- `edit_file` / `write_file` — create or update files in `/workspace`
- `read_file` — read files in `/workspace`
- `restrictToWorkspace` is enabled — cannot access files outside `/workspace`

## exec

- Runs Python, bash, PowerShell inside the container
- Timeout: 60s default
- Dangerous commands are blocked
- Output truncated at 10,000 characters

## web — Search

Use DuckDuckGo search for: current events, documentation lookups, research tasks.

## Memory tools

- `memory/MEMORY.md` — persistent facts and context
- `memory/HISTORY.md` — interaction log

Load MEMORY.md at conversation start. Write to it when something is worth keeping.

## Skills

Skills are in `skills/` — each skill is a folder with a `SKILL.md`.
Load a skill's SKILL.md when the task matches its domain.
