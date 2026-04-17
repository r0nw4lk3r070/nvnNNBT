# Tool Usage Notes

Tool signatures are provided automatically via function calling.
This file documents non-obvious constraints and EUAI-specific patterns.

## File tools — workspace scope

- `edit_file` / `write_file` — create or update files in the nvnJRST workspace
- `read_file` — read files in the nvnJRST workspace
- The workspace contains the legislation library (`library/`) — use it as primary reference before web search
- **Library structure**:
  - `library/eu-laws/EN/` — full text of EU regulations in English (PDF + .txt)
  - `library/eu-laws/NL/` — full text of EU regulations in Dutch (PDF + .txt)
  - `library/research/english/` — deep-dive analysis per regulation + sector guides (English)
  - `library/research/nederlands/` — deep-dive analysis per regulation + sector guides (Dutch)
  - Key regulations in library: GDPR (32016R0679), DORA (32022L2555), Data Act (32022R2554), NIS2 (32023R2854), Cyber Resilience Act (32024R1183), AI Act (32024R1689), Data Governance Act (32024R2847)

## exec — Safety Limits

- Commands have a configurable timeout (default 60s)
- Dangerous commands are blocked
- Output is truncated at 10,000 characters
- Use for: git operations, file management, running scripts

## web — Research

Use web search extensively for EUAI's core work:
- **EUR-Lex** (eur-lex.europa.eu) — official EU legal texts
- **EP Legislative Observatory** (oeil.secure.europarl.europa.eu) — track legislative procedures
- **European Commission — Digital Strategy** — proposals, press releases, impact assessments
- **ENISA** (enisa.europa.eu) — cybersecurity guidance and frameworks
- **EDPB / EDPS** — data protection guidance and opinions
- **National transposition trackers** — member state implementation status
- **Academic and think-tank analysis** — for context on contested provisions

Tip: always verify the latest status on EUR-Lex. Proposals evolve through trilogues.

## Memory tools

- `memory/MEMORY.md` — key regulations tracked, active dossiers, important deadlines
- `memory/HISTORY.md` — research log, analyses completed, developments noted

Load MEMORY.md at conversation start. Write to it when something is worth keeping.

## EUAI workflow

1. Check workspace library (`library/`) for existing analysis on the topic
2. If not covered (or outdated), search the web for current status
3. Cross-reference EUR-Lex for official text and status
4. Structure the answer: status → substance → obligations → deadlines
5. Save significant new analysis to the workspace library (`library/research/`)

## Skills

Skills are in `skills/` — each skill is a folder with a `SKILL.md`.
Load a skill's SKILL.md when the task matches its domain.