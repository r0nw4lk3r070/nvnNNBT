# Tool Usage Notes

Tool signatures are provided automatically via function calling.
This file documents non-obvious constraints and Business Toolkit-specific patterns.

## File tools

- `edit_file` / `write_file` — create or update files in the workspace
- `read_file` — read files in the workspace

## exec — Safety Limits

- Commands have a configurable timeout (default 60s)
- Dangerous commands are blocked (rm -rf, format, dd, shutdown, etc.)
- Output is truncated at 10,000 characters
- `restrictToWorkspace` config can limit file access to the workspace

## web — Search & Fetch

Use web search for:
- Market sizing data and industry reports
- Competitor information and pricing
- Investor thesis and portfolio data
- Technology trends and benchmarks
- SEO-related research (keyword volumes, competitor pages)

Use web_fetch for:
- Reading full content from research sources
- Fetching competitor landing pages for analysis
- Pulling structured data from web pages

## Memory tools

- `memory/MEMORY.md` — persistent facts and context
- `memory/HISTORY.md` — interaction log

Load MEMORY.md at conversation start. Write to it when something is worth keeping.

## Business Toolkit workflow

1. Identify which skill(s) the task requires
2. Load the relevant SKILL.md from `skills/`
3. Follow the skill's workflow and quality gate
4. Cross-reference with other active deliverables for consistency
5. Save reusable artifacts (voice profiles, instincts, research) to memory

## Skills

Skills are in `skills/` — each skill is a folder with a `SKILL.md`.
Load a skill's SKILL.md when the task matches its domain.

Available skills:
- `market-research` — market sizing, competitive analysis, investor due diligence
- `deep-research` — multi-source cited research reports
- `investor-materials` — pitch decks, memos, financial models
- `investor-outreach` — cold emails, warm intros, follow-ups
- `brand-voice` — source-derived voice profiles
- `content-engine` — platform-native content creation
- `seo` — technical SEO, on-page optimization, structured data
- `security-review` — code security checklists and audits
- `continuous-learning` — instinct-based learning from sessions