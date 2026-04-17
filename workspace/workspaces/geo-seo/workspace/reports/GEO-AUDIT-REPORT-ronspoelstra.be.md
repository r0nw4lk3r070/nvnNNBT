# GEO Audit Report: Ron Spoelstra — ronspoelstra.be

**Audit Date:** 15 April 2026  
**URL:** https://ronspoelstra.be  
**Business Type:** Publisher / Independent Advisory (content-heavy, EU AI legislation focus)  
**Pages Analyzed:** 18  
**Auditor:** GEO Audit System

---

## Executive Summary

**Overall GEO Score: 33/100 (Critical)**

ronspoelstra.be has exceptional content quality and strong E-E-A-T signals — the writing is authoritative, bilingual, and contains original research. But the site is nearly invisible to AI systems because it lacks every piece of technical infrastructure that makes content discoverable, parseable, and citable by AI crawlers. No robots.txt, no sitemap, no llms.txt, no schema markup, no brand presence on AI-training platforms. The content deserves to be cited. The architecture prevents it.

### Score Breakdown

| Category | Score | Weight | Weighted Score |
|---|---|---|---|
| AI Citability & Visibility | 52/100 | 25% | 13.0 |
| Brand Authority Signals | 12/100 | 20% | 2.4 |
| Content Quality & E-E-A-T | 68/100 | 20% | 13.6 |
| Technical GEO Foundations | 18/100 | 15% | 2.7 |
| Schema & Structured Data | 5/100 | 10% | 0.5 |
| Platform Optimization | 10/100 | 10% | 1.0 |
| **Overall GEO Score** | | | **33/100** |

---

## Critical Issues (Fix Immediately)

1. **No robots.txt** — 404 on `/robots.txt`. All AI crawlers have zero guidance. They may crawl freely but receive no directives about what to prioritize, what sitemap to use, or crawl rate limits. This is the most basic GEO infrastructure file and it's missing entirely.
   - **Fix:** Create `/robots.txt` with explicit allow directives for GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Bytespider, and Applebot-Extended. Include sitemap reference.

2. **No sitemap.xml** — 404 on `/sitemap.xml`. No crawl map exists for any bot. With 18+ pages of high-quality content, a sitemap is essential for discovery.
   - **Fix:** Generate and deploy `/sitemap.xml` listing all pages with lastmod dates and priority weights.

3. **No llms.txt** — 404 on `/llms.txt`. This is the file specifically designed for LLM-based crawlers to understand your site's purpose, structure, and key content. Without it, AI systems have no curated entry point.
   - **Fix:** Create `/llms.txt` with site description, content categories, and key page references.

4. **Zero structured data / schema.org markup** — No JSON-LD, Microdata, or RDFa detected on any page. No Organization, Person, Article, FAQPage, or any other schema type. This is a complete absence — not a partial gap.
   - **Fix:** Add Organization schema to all pages (site-wide), Person schema to About page and article bylines, Article schema to all content pages, FAQPage schema where applicable.

5. **No Open Graph or Twitter Card meta tags** — Pages have title tags and meta descriptions but lack OG title/description/image and Twitter Card markup. This reduces visibility when links are shared on any platform.
   - **Fix:** Add OG and Twitter Card meta tags to all pages with appropriate titles, descriptions, and images.

## High Priority Issues

1. **No brand mentions on AI-training platforms** — Zero presence on Reddit, Wikipedia, YouTube, LinkedIn (for this venture). The only external profiles found are an empty Pinterest account and an old Twitter/X account (@RonaldSpoelstra) unrelated to this site's topic. AI models train on platform data; without mentions, there's no entity recognition.

2. **No author schema or entity markup** — The About page (over-mij.html) has strong personal narrative and credentials but no Person schema. AI systems cannot programmatically identify "Ron Spoelstra" as the author entity.

3. **"The Great Return" research paper has zero external citations** — The 12,000-word paper on Zenodo (doi:10.5281/zenodo.18511984) has no external mentions found in web search. This is a missed authority signal.

4. **No LinkedIn company/professional page for this venture** — The only LinkedIn result is an unrelated Ron Spoelstra (sailing/yachting, Netherlands). No professional presence exists for the EU AI legislation advisory work.

5. **No hreflang or language alternate tags** — Despite having full Dutch + English content pairs (e.g., `/ondernemers/de-ai-act.html` ↔ `/for-business/the-ai-act.html`), no hreflang tags connect them. AI systems and search engines cannot identify the language/region relationship.

## Medium Priority Issues

1. **Listing pages have thin heading hierarchy** — `/ondernemers/` and `/ondernemers/sectoren/` use H1 + H2 only, with no H3 substructure. Category filter labels (Zorg & welzijn, Financieel & juridisch, etc.) are plain text, not headings.
2. **No breadcrumbs markup** — Deep content pages (e.g., `/ondernemers/therapeuten.html`) have breadcrumb-style navigation ("← Voor ondernemers") but no BreadcrumbList schema.
3. **Contact page is minimal** — `/contact.html` has a basic form and email address. No Organization schema, no address, no structured contact information.
4. **No RSS or Atom feed** — Publishers benefit from feeds for content syndication. None detected.
5. **News section has only one article** — `/nieuws/` contains only the March 26 omnibus vote article. Thin section with limited citability surface.
6. **Share buttons link to "#"** — LinkedIn and X share buttons on articles link to `#` (non-functional). They don't actually share content.
7. **No canonical URL tags detected** — Pages lack `<link rel="canonical">` directives. Risk of duplicate content interpretation.

## Low Priority Issues

1. **Some images may lack descriptive alt text** — Hero images have generic alt text patterns (verification limited by Jina extraction).
2. **No favicon or app-touch-icon** — Minor but affects platform appearance.
3. **Privacy and cookies pages lack structured legal schema** — Opportunity for Service/Terms schema.
4. **No email newsletter or subscription mechanism** — Limits audience building and return traffic.
5. **Footer legal disclaimer is consistent** — Good practice, but could benefit from structured markup.

---

## Category Deep Dives

### AI Citability & Visibility (52/100)

**What's working:**
- Content uses answer-first patterns: articles open with a direct statement, then build context. AI systems prefer extractable opening passages.
- Key articles contain definition patterns ("De AI Act is de eerste bindende AI-wet ter wereld"), specific statistics ("boetes tot vijfendertig miljoen euro of zeven procent van uw omzet"), and EU article references (Art. 10, Art. 13, Art. 458 Strafwetboek). These are highly citable.
- Bilingual content doubles the citation surface — Dutch articles for NL queries, English for global.
- Content is well-structured with clear H2/H3 headings that map to natural questions ("Wat valt er onder hoog risico?", "What falls under high risk?").

**What's broken:**
- No robots.txt means AI crawlers receive no guidance on what to crawl or how often. They may crawl freely but inefficiently — or may deprioritize the site due to lack of crawl directives.
- No llms.txt means no curated entry point for LLM-based systems. When ChatGPT, Perplexity, or Claude look for a site summary, they find nothing.
- No sitemap means crawlers must discover pages through link-following only — slower, less complete.
- No schema markup means AI systems cannot programmatically understand what each page is about (article? FAQ? person? organization?).
- Share buttons are broken (link to `#`), eliminating a potential distribution channel.

**Citable content examples found:**

| Page | Citable Passage | Citability |
|---|---|---|
| /ondernemers/de-ai-act.html | "De AI Act is de eerste bindende AI-wet ter wereld. Ze is van toepassing op iedereen die AI gebruikt, verkoopt of in de EU exploiteert" | High |
| /ondernemers/wat-europa-van-u-verwacht.html | "Drie Amerikaanse bedrijven controleren samen ongeveer twee derde van de wereldwijde cloudmarkt" | High |
| /thuis/de-smart-home.html | "Uw televisie maakt elke halve seconde een screenshot van wat er op het scherm staat" | High |
| /articles/the-great-return.html | "New generations of chips from AMD (55 TOPS), Qualcomm (80–85 TOPS), and Intel (48 TOPS) now include dedicated NPUs" | High |
| /ondernemers/therapeuten.html | "Artikel 458 van het Belgische Strafwetboek stelt schelling van het beroepsgeheim strafbaar" | High |
| /nieuws/ai-act-omnibus-mars-2026.html | "569 stemmen voor, 45 tegen, 23 onthoudingen" | High |

### Brand Authority Signals (12/100)

**Current state:**
- **Reddit:** Zero mentions of ronspoelstra.be or "Ron Spoelstra" in AI legislation context on Reddit.
- **Wikipedia/Wikidata:** No entity page. "Ron Spoelstra" does not appear as a recognized entity.
- **YouTube:** No channel. No video content found.
- **LinkedIn:** Only result is an unrelated Ron Spoelstra (sailing/yachting, Netherlands, Rossinante). No professional page for EU AI advisory work.
- **Twitter/X:** Old account @RonaldSpoelstra exists but unrelated to current work. @ronniespoelstra also found but inactive.
- **Pinterest:** Empty profile (ronspoelstra, 0 pins).
- **Facebook:** Personal profile exists (ron.spoelstra.33) but not a professional/business page.
- **Zenodo:** "The Great Return" paper published (doi:10.5281/zenodo.18511984) but zero external citations or mentions found via web search.

**Why this matters:**
Brand mentions on AI-training platforms (Reddit, YouTube, Wikipedia, LinkedIn) correlate 3x more with AI visibility than traditional backlinks. AI models learn entity recognition from these sources. Without any presence, "Ron Spoelstra" is not recognized as an entity in the EU AI legislation domain — even though the content quality suggests it should be.

**Opportunity:**
The niche is wide open. EU AI legislation explained in plain language for small businesses is underserved on all major platforms. First-mover advantage is significant.

### Content Quality & E-E-A-T (68/100)

**Experience:**
- Ron's background in youth care (jeugdzorg) provides authentic perspective on data privacy stakes — not theoretical, lived.
- AETHER platform is self-built and running for 3+ months. Not hypothetical — operational.
- Content references specific real-world incidents (Odido/Lifemote data breach, Samsung ACR, Meta Ray-Ban privacy issues) with verifiable details.

**Expertise:**
- Articles demonstrate deep understanding of EU regulatory framework: AI Act, NIS2, DORA, Data Act, GDPR — and how they interconnect.
- "The Great Return" research paper (12,000 words) on Zenodo with DOI — formal academic publishing.
- Sector-specific articles show domain knowledge across healthcare, legal, financial, hospitality, and other sectors.
- Content references specific EU regulation articles (Art. 10, Art. 13, Art. 458 Strafwetboek, Art. 7 lid 4 GDPR, Art. 9 GDPR).

**Authoritativeness:**
- Original research publication (Zenodo DOI) — rare for independent advisors.
- Bilingual content (Dutch + English) demonstrates authority in both markets.
- Content is timely: March 26, 2026 omnibus vote covered same-day.
- **Gap:** No external validation. Zero citations of "The Great Return." No guest articles. No conference presentations. No media mentions.

**Trustworthiness:**
- Consistent legal disclaimer on every page: "Deze website is uitsluitend informatief van aard. Er worden geen diensten aangeboden of verkocht. De inhoud vormt geen juridisch advies."
- Contact information (email) prominently displayed.
- Privacy and cookie pages present.
- No affiliate links, no ads, no sponsored content detected.
- **Gap:** No author schema or Person entity markup to programmatically convey trust signals to AI systems.

**Content depth metrics (sampled pages):**

| Page | Approx. Words | Headings | Specific Stats | EU Article Refs |
|---|---|---|---|---|
| /ondernemers/wat-europa-van-u-verwacht.html | ~1,400 | H1+4xH2 | 5+ | 5 |
| /ondernemers/de-ai-act.html | ~1,800 | H1+6xH2 | 4+ | 8+ |
| /articles/the-great-return.html | ~2,200 | H1+6xH2 | 6+ | 4 |
| /thuis/de-smart-home.html | ~2,000 | H1+5xH2 | 7+ | 3 |
| /ondernemers/therapeuten.html | ~1,500 | H1+4xH2 | 3+ | 5 |
| /nieuws/ai-act-omnibus-mars-2026.html | ~1,200 | H1+5xH2 | 3+ | 6+ |

### Technical GEO Foundations (18/100)

**Infrastructure checklist:**

| Component | Status | Impact |
|---|---|---|
| robots.txt | X 404 | Critical — no crawler guidance |
| sitemap.xml | X 404 | Critical — no crawl map |
| llms.txt | X 404 | Critical — no AI entry point |
| HTTPS | OK Active | Good |
| Server-side rendering | OK Static HTML | Good — fully crawlable |
| Canonical URLs | X Missing | Medium — duplicate content risk |
| Open Graph tags | X Missing | High — reduces shareability |
| Twitter Card tags | X Missing | High — reduces shareability |
| Hreflang tags | X Missing | High — bilingual content not linked |
| Meta descriptions | OK Present | Good |
| Title tags | OK Present | Good |
| Heading structure | ~Partial | Medium — listing pages thin |
| Security headers | Not verified | — |
| Mobile responsive | OK Likely (static site) | — |
| Core Web Vitals | Not measured (static site, likely fast) | — |

**Positive signals:**
- Site serves static HTML — fast, crawlable, no JavaScript dependency.
- HTTPS is active and working.
- Page titles and meta descriptions are present and descriptive.
- Clean URL structure with semantic paths (`/ondernemers/therapeuten.html`, `/for-business/the-ai-act.html`).

**Critical gaps:**
- The complete absence of robots.txt, sitemap.xml, and llms.txt means the site provides zero guidance to any crawler — AI or traditional. This is the single biggest technical GEO deficit.
- Missing hreflang tags between Dutch/English page pairs means AI systems cannot identify the language relationship between equivalent content.

### Schema & Structured Data (5/100)

**Detection results:** Zero schema.org markup found on any page. No JSON-LD, no Microdata, no RDFa.

**Missing schema opportunities by page type:**

| Page Type | Recommended Schema | Priority |
|---|---|---|
| All pages | Organization (site-wide) | Critical |
| About page | Person (Ron Spoelstra entity) | Critical |
| All articles | Article + Author | Critical |
| Sector pages | Article + Service | High |
| News article | NewsArticle | High |
| The Great Return | ScholarlyArticle + Citation | High |
| FAQ sections | FAQPage | Medium |
| Listing pages | ItemList | Medium |
| Breadcrumbs | BreadcrumbList | Medium |
| Contact | Organization + ContactPoint | Low |

**Impact of zero schema:**
Without Article schema, AI systems cannot programmatically identify page type, author, publication date, or content structure. Without Organization schema, there's no entity definition for "Ron Spoelstra" as an advisory organization. Without Person schema, the About page's strong credentials are invisible to AI parsing.

This is the lowest-scoring category because the absence is complete — not a gap, but a void.

### Platform Optimization (10/100)

**Platform presence assessment:**

| Platform | Presence | AI Training Impact |
|---|---|---|
| Reddit | X None | High — Reddit is a primary training source for ChatGPT/Claude |
| YouTube | X None | High — YouTube transcripts train LLMs |
| Wikipedia | X None | Critical — Wikipedia is the #1 entity source for AI |
| LinkedIn | X None (for this venture) | High — LinkedIn content trains professional AI tools |
| Twitter/X | ~Old account, unrelated | Low — inactive, wrong topic |
| Pinterest | ~Empty profile | None |
| Facebook | ~Personal only | Low |
| Medium/Substack | X None | Medium — good for AI citation |
| GitHub | X None | Low — not relevant for this niche |
| Podcasts | X None | Medium — transcripts train LLMs |

**Competitive landscape:**
The EU AI legislation space is growing but still underserved for plain-language, SMB-focused content. Major competitors (law firms, consultancies) publish in legal jargon. Ron's "in gewone taal" approach is a genuine differentiator — but it's invisible to AI systems without platform presence.

**Zero-platform risk:**
When someone asks ChatGPT "What does the AI Act mean for my therapy practice?" or "EU AI legislation for small businesses explained", the AI has no training data from ronspoelstra.be to draw from. The content exists, but it's not in the training corpus — and without platform presence, it won't get there.

---

## Quick Wins (Implement This Week)

1. **Create `/robots.txt`** — Allow all AI crawlers, reference sitemap. 10-minute task. Impact: Critical — enables guided crawling.
   ```
   User-agent: *
   Allow: /
   
   User-agent: GPTBot
   Allow: /
   
   User-agent: ClaudeBot
   Allow: /
   
   User-agent: PerplexityBot
   Allow: /
   
   User-agent: Google-Extended
   Allow: /
   
   User-agent: Bytespider
   Allow: /
   
   User-agent: Applebot-Extended
   Allow: /
   
   Sitemap: https://ronspoelstra.be/sitemap.xml
   ```

2. **Create `/sitemap.xml`** — List all 18+ pages with lastmod dates. 30-minute task. Impact: Critical — provides crawl map for all bots.

3. **Create `/llms.txt`** — Site summary, content categories, key page links. 20-minute task. Impact: Critical — AI-specific entry point.
   ```
   # ronspoelstra.be
   
   > EU AI legislation in plain language for businesses and citizens.
   > Independent advisory by Ron Spoelstra, Leuven, Belgium.
   
   ## Dutch (/ondernemers/)
   - /ondernemers/wat-europa-van-u-verwacht.html — Overview of all EU AI laws
   - /ondernemers/de-ai-act.html — AI Act explained for businesses
   - /ondernemers/de-data-act.html — Data Act: right to leave the cloud
   - /ondernemers/nis2.html — NIS2: personal liability for cybersecurity
   - /ondernemers/dora.html — DORA: digital resilience for finance
   - /ondernemers/therapeuten.html — AI for therapists
   - /ondernemers/artsen.html — AI for doctors
   - /ondernemers/accountants.html — AI for accountants
   - /ondernemers/juristen.html — AI for lawyers
   - /ondernemers/sectoren/ — All sector pages
   
   ## English (/for-business/)
   - /for-business/what-europe-expects.html — Overview of all EU AI laws
   - /for-business/the-ai-act.html — AI Act explained for businesses
   - /for-business/the-data-act.html — Data Act: right to leave the cloud
   - /for-business/nis2.html — NIS2: personal liability
   - /for-business/dora.html — DORA: digital resilience for finance
   - /for-business/therapists.html — AI for therapists
   - /for-business/doctors.html — AI for doctors
   - /for-business/accountants.html — AI for accountants
   
   ## Research
   - /articles/the-great-return.html — Why AI is coming home (12,000-word research)
   - https://doi.org/10.5281/zenodo.18511984 — Zenodo publication
   
   ## Home & Smart Living (/thuis/)
   - /thuis/de-smart-home.html — Smart home privacy analysis
   
   ## News
   - /nieuws/ai-act-omnibus-mars-2026.html — AI Act omnibus vote March 2026
   
   ## About
   - /over-mij.html — About Ron Spoelstra
   - /contact.html — Contact
   ```

4. **Add Organization schema to all pages** — JSON-LD snippet in `<head>`. 30-minute task. Impact: Critical — defines entity for AI systems.

5. **Add hreflang tags to bilingual page pairs** — Link Dutch and English equivalents. 1-hour task. Impact: High — connects language variants for AI and search engines.

## 30-Day Action Plan

### Week 1: Technical Infrastructure (GEO Score impact: +15-20 points)

- [ ] Deploy `/robots.txt` with AI crawler directives
- [ ] Deploy `/sitemap.xml` with all pages
- [ ] Deploy `/llms.txt` with site structure
- [ ] Add Organization JSON-LD schema to all page templates
- [ ] Add Person JSON-LD schema to About page
- [ ] Add Article JSON-LD schema to all content pages
- [ ] Add hreflang alternate links between Dutch/English page pairs
- [ ] Add canonical URL tags to all pages
- [ ] Fix share buttons (currently link to `#`, non-functional)

### Week 2: Content Optimization (GEO Score impact: +5-10 points)

- [ ] Add FAQ sections to top 5 articles (AI Act, NIS2, DORA, Data Act, GDPR overview)
- [ ] Add FAQPage schema to all pages with FAQ content
- [ ] Add BreadcrumbList schema to all sub-pages
- [ ] Add Open Graph + Twitter Card meta tags to all pages
- [ ] Enhance heading hierarchy on listing pages (/ondernemers/, /ondernemers/sectoren/)
- [ ] Add NewsArticle schema to nieuws/ articles
- [ ] Add ScholarlyArticle schema to The Great Return page with Zenodo DOI citation
- [ ] Expand news section with 2-3 additional timely articles

### Week 3: Platform Presence (GEO Score impact: +5-10 points)

- [ ] Create LinkedIn professional page for EU AI advisory work
- [ ] Publish first LinkedIn article (adapt existing content, e.g., "What the AI Act means for your business")
- [ ] Create Reddit account and participate in r/eu, r/artificial, r/privacy subreddits with genuine answers
- [ ] Cross-post "The Great Return" summary to Medium/Substack
- [ ] Create YouTube channel — record 3-5 short explainers (5 min each) on key topics
- [ ] Publish "The Great Return" on SSRN or another academic preprint server in addition to Zenodo

### Week 4: Authority Building (GEO Score impact: +3-5 points)

- [ ] Contact 5-10 EU AI legislation bloggers/podcasters for guest appearances
- [ ] Submit "The Great Return" to 3-5 relevant academic citation indexes
- [ ] Create a Wikipedia draft for "EU AI Act implementation" or "Local AI in Europe" (cite own research alongside others)
- [ ] Publish sector-specific content snippets on LinkedIn weekly
- [ ] Set up Google Alerts for brand name monitoring
- [ ] Create a simple email newsletter signup for the site
- [ ] Add RSS/Atom feed for content syndication

---

## Projected Score Improvement

| Category | Current | After Quick Wins | After 30 Days | After 90 Days |
|---|---|---|---|---|
| AI Citability | 52 | 62 | 70 | 78 |
| Brand Authority | 12 | 12 | 25 | 45 |
| Content E-E-A-T | 68 | 72 | 78 | 82 |
| Technical GEO | 18 | 45 | 60 | 70 |
| Schema & Structured Data | 5 | 35 | 55 | 65 |
| Platform Optimization | 10 | 10 | 30 | 50 |
| **Overall GEO Score** | **33** | **42** | **55** | **67** |

The biggest single leap comes from Week 1 technical infrastructure: deploying robots.txt, sitemap, llms.txt, and schema markup. This alone could push the score from 33 to ~42. Brand authority is the slowest category to build — it requires consistent platform presence over months.

---

## Appendix: Pages Analyzed

| URL | Title | Issues |
|---|---|---|
| / | Ron Spoelstra — AI-wetgeving in gewone taal | No schema, no OG tags, no canonical |
| /ondernemers/ | Voor ondernemers | No schema, thin heading hierarchy |
| /ondernemers/wat-europa-van-u-verwacht.html | Wat Europa van u verwacht — en waarom dat nu speelt | No Article schema, no hreflang, broken share buttons |
| /ondernemers/de-ai-act.html | De AI Act: wat u moet weten voor december 2027 | No Article schema, no hreflang, broken share buttons |
| /ondernemers/de-data-act.html | De Data Act: uw recht om de cloud te verlaten | No Article schema |
| /ondernemers/nis2.html | NIS2: persoonlijke aansprakelijkheid voor cyberbeveiliging | No Article schema |
| /ondernemers/dora.html | DORA: digitale weerbaarheid voor de financiële sector | No Article schema |
| /ondernemers/therapeuten.html | AI voor therapeuten: sessienotities die in de praktijk blijven | No Article schema, no hreflang, broken share buttons |
| /ondernemers/artsen.html | AI in uw praktijk: patiëntdata die het kabinet niet verlaat | No Article schema |
| /ondernemers/accountants.html | Als accountant AI gebruiken zonder uw beroepsgeheim te schenden | No Article schema |
| /ondernemers/juristen.html | Advocaten en AI: uw beroepsgeheim in het digitale tijdperk | No Article schema |
| /ondernemers/sectoren/ | Sectoren | No schema, thin heading hierarchy |
| /for-business/ | For Business | No schema, thin heading hierarchy |
| /for-business/what-europe-expects.html | What Europe Expects From You — and Why It Matters Now | No Article schema, no hreflang, broken share buttons |
| /for-business/the-ai-act.html | The AI Act: What You Need to Know Before December 2027 | No Article schema, no hreflang, broken share buttons |
| /articles/the-great-return.html | The Great Return | No ScholarlyArticle schema, no citation markup |
| /thuis/de-smart-home.html | De smart home: uw huis werkt. Maar voor wie? | No Article schema |
| /nieuws/ | Nieuws | No schema, thin section (1 article) |
| /nieuws/ai-act-omnibus-mars-2026.html | AI Act vereenvoudigd: wat het Europees Parlement vandaag besliste | No NewsArticle schema |
| /over-mij.html | Over mij — Ron Spoelstra | No Person schema |
| /contact.html | Contact — Ron Spoelstra | No Organization schema |

**Failed fetches:** None — all pages returned 200 OK.

**Infrastructure files (404):** /robots.txt, /sitemap.xml, /llms.txt