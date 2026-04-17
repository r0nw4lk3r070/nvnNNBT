# Tool Usage Notes

## File tools

- `edit_file` / `write_file` — create or update files in the workspace
- `read_file` — read files in the workspace

## web — Search

Use web search for: product information, bol.com policies, current info that helps resolve customer issues.

## Memory tools

- `memory/MEMORY.md` — persistent facts and context
- `memory/HISTORY.md` — interaction log

Load MEMORY.md at conversation start. Write to it when something is worth keeping.

## Customer service workflow

1. Listen to the customer's issue
2. Search knowledge base / web if needed
3. Offer resolution or escalate
4. Log the interaction in HISTORY.md if notable

## Skills

Skills are in `skills/` — each skill is a folder with a `SKILL.md`.
Load a skill's SKILL.md when the task matches its domain.