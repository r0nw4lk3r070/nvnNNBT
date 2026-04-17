# GEO Client Report Generator

## Purpose

This skill aggregates GEO audit data into a professional client report. The report is written for **business owners and marketing leaders** — technical findings are translated into business impact and clear action items.

## Critical: Write in Stages

**Do NOT attempt to write the entire report in a single write_file call.** The report is too large for one output. Instead, write it in 4 separate writes, appending each part:

1. **Part 1**: Header + Executive Summary + Score Breakdown + AI Visibility Dashboard
2. **Part 2**: Crawler Access + Brand Authority + Citability Analysis
3. **Part 3**: Technical Health + Schema + llms.txt + Action Plan
4. **Part 4**: Estimated Impact + Appendix

Use `write_file` for Part 1, then `edit_file` to append Parts 2-4 by replacing the last line. Or write each part to a temp file and combine at the end.

**The file path is always**: `workspace/reports/GEO-CLIENT-REPORT-[domain].md`

---

## How to Use This Skill

1. Run audits first (or use existing data from a completed geo-audit)
2. Collect all scores and findings
3. Calculate the composite GEO Readiness Score
4. Write the report in 4 stages (see below)
5. After all 4 parts are written, confirm the report is complete

---

## GEO Readiness Score Calculation

### Component Weights

| Component | Weight | Source Skill |
|---|---|---|
| AI Platform Readiness | 25% | geo-platform-optimizer |
| Content Quality & E-E-A-T | 25% | geo-content |
| Technical Foundation | 20% | geo-technical |
| Schema & Structured Data | 15% | geo-schema |
| Brand Authority & Entity Presence | 15% | geo-platform-optimizer (entity signals) |

### Score Formula
```
GEO Score = (Platform Score * 0.25) + (Content Score * 0.25) + (Technical Score * 0.20) + (Schema Score * 0.15) + (Brand Score * 0.15)
```
Round to nearest integer. Cap at 100.

### Score Interpretation

| Score Range | Label | Client-Facing Description |
|---|---|---|
| 85-100 | Excellent | Well-positioned for AI search. Maintain and expand. |
| 70-84 | Good | Solid foundation, clear opportunities. Targeted optimizations yield significant results. |
| 55-69 | Moderate | Gaps competitors may exploit. Structured plan will close them. |
| 40-54 | Below Average | Significant barriers. Risk of invisibility in AI answers. |
| 0-39 | Needs Attention | Critical issues. Immediate action required. |

---

## Stage 1: Header + Executive Summary + Scores

Write to: `workspace/reports/GEO-CLIENT-REPORT-[domain].md`

```markdown
# GEO Audit Report: [Brand Name]

**Audit Date:** [Date]
**URL:** [URL]
**Business Type:** [Detected Type]
**Pages Analyzed:** [Count]

---

## Executive Summary

[ONE paragraph, 4-6 sentences: what was analyzed, overall GEO score with label, most impactful finding, top 3 recommendations, business impact estimate]

---

## GEO Readiness Score: [XX]/100 — [Label]

| Component | Score | Weight | Weighted Score |
|---|---|---|---|
| AI Platform Readiness | XX/100 | 25% | XX |
| Content Quality & E-E-A-T | XX/100 | 25% | XX |
| Technical Foundation | XX/100 | 20% | XX |
| Schema & Structured Data | XX/100 | 15% | XX |
| Brand Authority | XX/100 | 15% | XX |
| **Overall** | | | **XX/100** |

---

## AI Visibility Dashboard

| AI Platform | Readiness Score | Key Gap | Priority Action |
|---|---|---|---|
| Google AI Overviews | XX/100 | [gap] | [action] |
| ChatGPT Web Search | XX/100 | [gap] | [action] |
| Perplexity AI | XX/100 | [gap] | [action] |
| Google Gemini | XX/100 | [gap] | [action] |
| Bing Copilot | XX/100 | [gap] | [action] |

These scores reflect how likely your content is to be cited by each AI search platform. A score below 50 indicates significant barriers to citation.

---
```

**After writing Stage 1, immediately proceed to Stage 2. Do not wait for user confirmation.**

---

## Stage 2: Crawler Access + Brand Authority + Citability

Append to the same file. Add:

```markdown

## AI Crawler Access

| AI Crawler | Platform | Status | Impact | Recommendation |
|---|---|---|---|---|
| Googlebot | Google Search + AIO | Allowed/Blocked | Critical | [Action] |
| GPTBot | ChatGPT / OpenAI | Allowed/Blocked | High | [Action] |
| Bingbot | Bing + Copilot + ChatGPT | Allowed/Blocked | High | [Action] |
| PerplexityBot | Perplexity AI | Allowed/Blocked | Medium | [Action] |
| Google-Extended | Gemini Training | Allowed/Blocked | Medium | [Action] |
| ClaudeBot | Anthropic Claude | Allowed/Blocked | Medium | [Action] |
| Applebot-Extended | Apple Intelligence | Allowed/Blocked | Medium | [Action] |

Blocking AI crawlers is like closing your store during business hours. We recommend allowing all major AI crawlers unless you have a specific data licensing concern.

---

## Brand Authority

| Platform | Presence | Status | Impact on AI Visibility |
|---|---|---|---|
| Wikipedia | Yes/No | [Detail] | Very High |
| Wikidata | Yes/No | [Detail] | High |
| LinkedIn | Yes/No | [Detail] | High |
| YouTube | Yes/No | [Detail] | High |
| Reddit | Yes/No | [Detail] | Very High |
| Google Knowledge Panel | Yes/No | [Detail] | High |
| Crunchbase | Yes/No | [Detail] | Medium |
| GitHub | Yes/No | [Detail] | Medium |

AI platforms build trust by cross-referencing your brand across authoritative sources. Each accurate, consistent presence increases citation likelihood.

---

## Citability Analysis

### Top 5 Most Citable Pages
For each: URL, why citable, one improvement

### Top 5 Least Citable Pages
For each: URL, why not citable, specific rewrite recommendation

Improving the 5 least citable pages represents the highest-ROI content investment for AI visibility.

---
```

**After writing Stage 2, immediately proceed to Stage 3.**

---

## Stage 3: Technical + Schema + llms.txt + Action Plan

Append to the same file. Add:

```markdown

## Technical Health

| Area | Status | Business Impact |
|---|---|---|
| Core Web Vitals | Good/Needs Work/Poor | [Impact] |
| Server-Side Rendering | Yes/Partial/No | [Impact on AI crawler visibility] |
| Mobile Optimization | Good/Needs Work/Poor | [Impact] |
| Security (HTTPS + Headers) | Good/Needs Work/Poor | [Impact] |
| Page Speed | Fast/Average/Slow | [Impact] |
| IndexNow Protocol | Implemented/Not | [Impact on Bing/ChatGPT indexing] |

[If SSR is missing: "Your site uses client-side rendering — AI crawlers see an empty page. This is the single most impactful technical issue for AI search visibility."]

---

## Schema & Structured Data

| Schema Type | Present | Status | AI Impact |
|---|---|---|---|
| Organization | Yes/No | Valid/Issues | Critical — entity recognition |
| Article + Author | Yes/No | Valid/Issues | High — E-E-A-T signal |
| sameAs (entity links) | Yes/No | [Count] links | Critical — entity graph |
| [Business-specific] | Yes/No | Valid/Issues | [Impact] |
| WebSite + SearchAction | Yes/No | Valid/Issues | Medium — sitelinks |
| BreadcrumbList | Yes/No | Valid/Issues | Low-Medium — navigation |

---

## llms.txt — AI Content Guide

| File | Status | Recommendation |
|---|---|---|
| /llms.txt | Present/Missing | [Action] |
| /llms-full.txt | Present/Missing | [Action] |

llms.txt is an emerging standard that tells AI systems what your site is about. Implementing it positions your brand ahead of competitors.

---

## Prioritized Action Plan

### Quick Wins (This Week)

| # | Action | Impact | Effort | Platforms Affected |
|---|---|---|---|---|
| 1 | [action] | High/Med | [hours] | [platforms] |
| 2 | [action] | High/Med | [hours] | [platforms] |

### Medium-Term Improvements (This Month)

| # | Action | Impact | Effort | Platforms Affected |
|---|---|---|---|---|
| 1 | [action] | High/Med | [days] | [platforms] |

### Strategic Initiatives (This Quarter)

| # | Action | Impact | Effort | Platforms Affected |
|---|---|---|---|---|
| 1 | [action] | High/Med | [weeks] | [platforms] |

---
```

**After writing Stage 3, immediately proceed to Stage 4.**

---

## Stage 4: Impact Estimate + Appendix

Append to the same file. Add:

```markdown

## Estimated Impact

Based on industry benchmarks and the specific gaps identified:
- **Quick Wins alone** could improve your GEO score by approximately [X-Y] points
- **Full implementation** could improve your GEO score to approximately [XX]/100
- Improved AI visibility represents an estimated **€X,XXX - €XX,XXX per month** in additional organic value

*Estimates are conservative. Based on: AI search projected to drive 25-40% of organic discovery by end 2026; a 10-point GEO score improvement typically correlates with 15-25% increase in AI citation frequency.*

---

## Appendix

### Methodology
- **Pages analyzed**: [URLs]
- **Platforms assessed**: Google AI Overviews, ChatGPT, Perplexity AI, Google Gemini, Bing Copilot
- **Technical checks**: HTTP headers, robots.txt, HTML source analysis, structured data validation
- **Content assessment**: E-E-A-T framework per Google's December 2025 Quality Rater Guidelines
- **Date of analysis**: [Date]

### Data Sources
- Google Search Quality Rater Guidelines (December 2025)
- Schema.org type hierarchy
- Industry citation studies (Zyppy, Authoritas, Semrush, 2025-2026)
- Core Web Vitals thresholds (web.dev, 2026)
- AI crawler user-agent documentation (per-platform)

### Glossary

| Term | Definition |
|---|---|
| GEO | Generative Engine Optimization — optimizing for AI citation |
| AIO | AI Overviews — Google's AI answer boxes |
| E-E-A-T | Experience, Expertise, Authoritativeness, Trustworthiness |
| SSR | Server-Side Rendering — HTML generated on server for crawlers |
| CWV | Core Web Vitals — LCP, INP, CLS |
| JSON-LD | JSON for Linked Data — preferred structured data format |
| sameAs | Schema.org property linking entity to other profiles |
| IndexNow | Protocol for instant search engine content notifications |
| llms.txt | Proposed standard for guiding AI systems about site content |
| YMYL | Your Money or Your Life — topics requiring highest E-E-A-T |
| Topical Authority | Depth/breadth of site's coverage of its core topic |
```

**After Stage 4, the report is complete. Confirm to the user with the file path.**

---

## Formatting and Tone

- Clean markdown: tables, H2/H3, bullets, bold for emphasis
- Professional but accessible — written for business owners
- Confident and direct — state findings as conclusions
- Action-oriented — every finding connects to a specific action
- Business-impact focused — translate technical issues into outcomes
- Conservative estimates with stated assumptions
- Use € for European clients, $ otherwise