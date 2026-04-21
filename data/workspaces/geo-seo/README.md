# GEO-SEO Agent

Generative Engine Optimization specialist for AI-powered search visibility.

## What this agent does

Audits websites for visibility in AI search engines (ChatGPT, Perplexity, Claude, Gemini, Google AI Overviews). Produces composite GEO Scores (0-100), actionable reports, and client-ready PDF deliverables.

## Quick start

1. Load in the Lab: http://localhost:6161/lab
2. Start with: `/geo audit https://example.com`
3. Get a PDF: `/geo report-pdf https://example.com`

## Commands

| Command | What it does |
|---------|-------------|
| `/geo audit <url>` | Full GEO + SEO audit |
| `/geo quick <url>` | 60-second snapshot |
| `/geo citability <url>` | AI citation readiness score |
| `/geo crawlers <url>` | AI crawler access check |
| `/geo llmstxt <url>` | Analyze or generate llms.txt |
| `/geo brands <url>` | Brand mention scan |
| `/geo platforms <url>` | Platform-specific optimization |
| `/geo schema <url>` | Structured data analysis |
| `/geo technical <url>` | Technical SEO audit |
| `/geo content <url>` | Content E-E-A-T assessment |
| `/geo report <url>` | Markdown report |
| `/geo report-pdf <url>` | Professional PDF report |
| `/geo prospect <cmd>` | Prospect pipeline management |
| `/geo proposal <domain>` | Client proposal generator |
| `/geo compare <domain>` | Monthly delta report |

## Scoring

| Category | Weight |
|----------|--------|
| AI Citability & Visibility | 25% |
| Brand Authority Signals | 20% |
| Content Quality & E-E-A-T | 20% |
| Technical Foundations | 15% |
| Structured Data | 10% |
| Platform Optimization | 10% |

## Dependencies

```bash
pip install -r workspace/scripts/requirements.txt
```

Required: requests, beautifulsoup4, lxml, reportlab

## File structure

```
geo-seo/
├── SOUL.md              # Agent identity
├── AGENTS.md            # Instructions & workflow
├── USER.md              # User profile (Ron)
├── TOOLS.md             # Tool usage patterns
├── HEARTBEAT.md         # Heartbeat (disabled)
├── README.md            # This file
├── cron/jobs.json       # Cron jobs (empty)
├── memory/
│   ├── MEMORY.md        # Persistent context
│   └── HISTORY.md       # Event log
├── skills/              # 13 sub-skills
│   ├── geo-audit/SKILL.md
│   ├── geo-citability/SKILL.md
│   ├── geo-crawlers/SKILL.md
│   ├── geo-llmstxt/SKILL.md
│   ├── geo-brand-mentions/SKILL.md
│   ├── geo-platform-optimizer/SKILL.md
│   ├── geo-schema/SKILL.md
│   ├── geo-technical/SKILL.md
│   ├── geo-content/SKILL.md
│   ├── geo-report/SKILL.md
│   ├── geo-report-pdf/SKILL.md
│   ├── geo-prospect/SKILL.md
│   ├── geo-proposal/SKILL.md
│   └── geo-compare/SKILL.md
├── agents/              # 5 parallel agent definitions
│   ├── geo-ai-visibility.md
│   ├── geo-platform-analysis.md
│   ├── geo-technical.md
│   ├── geo-content.md
│   └── geo-schema.md
└── workspace/           # Runtime workspace (mirror + data)
    ├── SOUL.md, AGENTS.md, USER.md, TOOLS.md, HEARTBEAT.md
    ├── cron/jobs.json
    ├── memory/
    ├── scripts/          # Python audit scripts
    ├── schema/           # JSON-LD templates
    ├── reports/          # Generated audit reports
    ├── generated/        # Generated files (llms.txt, schema)
    ├── prospects/        # Prospect pipeline data
    └── examples/         # Sample reports & proposals
```

## Source

Adapted from [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) (MIT license).
Modified for nanobot architecture: Claude Code tool references replaced with nanobot equivalents.