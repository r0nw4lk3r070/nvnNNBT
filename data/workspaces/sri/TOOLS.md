# Tool Usage Notes

Tool signatures are provided automatically via function calling.
This file documents non-obvious constraints and sri-specific patterns.

## File tools

- `edit_file` / `write_file` — create or update files in the workspace
- `read_file` — read files in the workspace

## exec — Safety Limits

- Commands have a configurable timeout (default 60s)
- Dangerous commands are blocked (rm -rf, format, dd, shutdown, etc.)
- Output is truncated at 10,000 characters
- `restrictToWorkspace` config can limit file access to the workspace

## web — Search

Use web search for:
- Biographical details about Nisargadatta Maharaj
- Cross-references with other Advaita teachers (Ramana Maharshi, Siddharameshwar)
- Clarifying Sanskrit terms or historical context
- Finding supplementary resources when the *I Am That* text doesn't cover a question

## I Am That — Text Search

The full text of *I Am That* is at: `workspace/library/I AM THAT Nisargadatta Maharaj.txt`
- 13,433 lines, 101 chapters
- Search with Python: `lines[i]` for line-level queries
- Always cite chapter number and context when quoting

## Memory tools

- `memory/MEMORY.md` — persistent facts and context
- `memory/HISTORY.md` — interaction log

Load MEMORY.md at conversation start. Write to it when something is worth keeping.

## sri workflow

1. Hear the question — what is the seeker really asking?
2. Search the *I Am That* text for relevant passages
3. Present what Maharaj said — clearly, directly, without decoration
4. Point back to the user's own experience — "Is this something you can verify?"
5. If no passage fits, use web search or speak from the spirit of the teaching — but say so

## Skills

Skills are in `skills/` — each skill is a folder with a `SKILL.md`.
Load a skill's SKILL.md when the task matches its domain.