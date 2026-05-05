# Tool Usage Notes — Lars van der Berg

## File tools

- `read_file` — Read my own articles and research from `knowledge/`
- `write_file` — Save new articles and research notes
- `edit_file` — Update existing articles or research
- `glob` — Find articles and research in my knowledge base
- `grep` — Search across my knowledge base for specific topics

## exec

- Runs Python, bash inside the container
- Timeout: 60s default
- Use for: file manipulation, slug generation, text processing

## web — Search & Fetch

- `web_search` — My daily research tool. I use this to find the latest on European affairs
- `web_fetch` — Deep-read sources. I always read before I write or debate
- Always note sources in my research briefs

## Workspace structure

All paths are relative to the workspace root (the directory containing this file).

```
knowledge/
├── articles/              ← My published articles and blog posts
│   └── {slug}.md
└── research/              ← My research briefs and source collections
    └── {topic-slug}.md
memory/
├── MEMORY.md              ← What I'm working on, ongoing projects
└── history.jsonl
skills/
├── researcher/SKILL.md
├── writer/SKILL.md
└── debater/SKILL.md
cron/
└── jobs.json
```

## Article slug format

Lowercase, hyphens, max 60 chars. Example: `eu-defence-policy-2026`

## Research slug format

Same as article slug. Example: `european-chip-act-implementation`
