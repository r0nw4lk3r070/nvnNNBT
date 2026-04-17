# Business Toolkit

Market research, investor materials, content creation, SEO, security review, and continuous learning skills for business-focused agents.

## Skills

| Skill | Description |
|-------|-------------|
| `market-research` | Market sizing, competitive analysis, investor due diligence, technology scans |
| `deep-research` | Multi-source cited research reports with source attribution |
| `investor-materials` | Pitch decks, one-pagers, memos, financial models, accelerator applications |
| `investor-outreach` | Cold emails, warm intro requests, follow-ups, investor communications |
| `brand-voice` | Source-derived voice profiles for consistent writing across channels |
| `content-engine` | Platform-native content creation and repurposing systems |
| `seo` | Technical SEO audits, on-page optimization, structured data, keyword mapping |
| `security-review` | Code security checklists, vulnerability identification, pre-deployment audits |
| `continuous-learning` | Instinct-based learning from sessions, evolving patterns into reusable knowledge |

## Serves

- **MKT** (marketing) agents from the ticket system
- **SALES** agents from the ticket system
- Any agent needing business-focused capabilities

## Skill Dependencies

- `brand-voice` is the canonical voice layer — used by `content-engine` and `investor-outreach`
- `market-research` feeds into `investor-materials` and `investor-outreach`
- `deep-research` is the general-purpose research engine
- `security-review` is independent but complements development workflows

## Quick Start

1. Copy this skill-set to your agent's workspace
2. Load the relevant `skills/*/SKILL.md` when the task matches
3. Run quality gates before delivering output
4. Save reusable artifacts (voice profiles, instincts, research) to `memory/MEMORY.md`

## File structure

```
business-toolkit/
├── SOUL.md              # Identity, personality, voice, hard rules
├── AGENTS.md            # Instructions, responsibilities, workflow
├── USER.md              # Who the agent serves
├── TOOLS.md             # Tool usage patterns
├── HEARTBEAT.md         # Periodic tasks (disabled by default)
├── README.md            # This file
├── cron/
│   └── jobs.json        # Cron job definitions
├── memory/
│   ├── MEMORY.md        # Persistent context (starts empty)
│   └── HISTORY.md       # Interaction log (starts empty)
├── skills/
│   ├── market-research/SKILL.md
│   ├── deep-research/SKILL.md
│   ├── investor-materials/SKILL.md
│   ├── investor-outreach/SKILL.md
│   ├── brand-voice/SKILL.md
│   ├── content-engine/SKILL.md
│   ├── seo/SKILL.md
│   ├── security-review/SKILL.md
│   └── continuous-learning/SKILL.md
└── workspace/           # Agent workspace copy (mirrors above)
    ├── SOUL.md
    ├── AGENTS.md
    ├── USER.md
    ├── TOOLS.md
    ├── HEARTBEAT.md
    ├── cron/jobs.json
    ├── memory/
    │   ├── MEMORY.md
    │   └── HISTORY.md
    └── skills/
        ├── market-research/SKILL.md
        ├── deep-research/SKILL.md
        ├── investor-materials/SKILL.md
        ├── investor-outreach/SKILL.md
        ├── brand-voice/SKILL.md
        ├── content-engine/SKILL.md
        ├── seo/SKILL.md
        ├── security-review/SKILL.md
        └── continuous-learning/SKILL.md
```