# Brand Voice

Build a durable voice profile from real source material, then use that profile everywhere instead of re-deriving style from scratch or defaulting to generic AI copy.

## Tools

- `read_file` — read existing voice profiles, source material files, and prior content
- `write_file` — save voice profiles and content drafts
- `edit_file` — revise existing voice profiles
- `web_search` — find public writing samples, posts, and articles by the author
- `web_fetch` — read full content from author's published pages and posts

## When to Activate

- the user wants content or outreach in a specific voice
- writing for X, LinkedIn, email, launch posts, threads, or product updates
- adapting a known author's tone across channels
- the existing content lane needs a reusable style system instead of one-off mimicry

## Source Priority

Use the strongest real source set available, in this order:

1. recent original social posts and threads
2. articles, essays, memos, launch notes, or newsletters
3. real outbound emails or DMs that worked
4. product docs, changelogs, README framing, and site copy

Do not use generic platform exemplars as source material.

## Collection Workflow

1. Gather 5 to 20 representative samples when available.
2. Prefer recent material over old material unless the user says the older writing is more canonical.
3. Separate "public launch voice" from "private working voice" if the source set clearly splits.
4. If live social access is available, use web_search and web_fetch to pull recent original posts before drafting.
5. If site copy matters, include the current landing page and documentation framing.

## What to Extract

- rhythm and sentence length
- compression vs explanation
- capitalization norms
- parenthetical use
- question frequency and purpose
- how sharply claims are made
- how often numbers, mechanisms, or receipts show up
- how transitions work
- what the author never does

## Output Contract

Produce a reusable `VOICE PROFILE` block that downstream skills can consume directly. Use this schema:

```text
VOICE PROFILE
=============
Author:
Goal:
Confidence:

Source Set
- source 1
- source 2
- source 3

Rhythm
- short note on sentence length, pacing, and fragmentation

Compression
- how dense or explanatory the writing is

Capitalization
- conventional, mixed, or situational

Parentheticals
- how they are used and how they are not used

Question Use
- rare, frequent, rhetorical, direct, or mostly absent

Claim Style
- how claims are framed, supported, and sharpened

Preferred Moves
- concrete moves the author does use

Banned Moves
- specific patterns the author does not use

CTA Rules
- how, when, or whether to close with asks

Channel Notes
- X:
- LinkedIn:
- Email:
```

Keep the profile structured and short enough to reuse in session context. The point is not literary criticism. The point is operational reuse.

## Hard Bans

Delete and rewrite any of these:

- fake curiosity hooks
- "not X, just Y"
- "no fluff"
- forced lowercase
- LinkedIn thought-leader cadence
- bait questions
- "Excited to share"
- generic founder-journey filler
- corny parentheticals

## Persistence Rules

- Reuse the latest confirmed `VOICE PROFILE` across related tasks in the same session.
- If the user asks for a durable artifact, save the profile to `memory/MEMORY.md` or the requested workspace location.
- Do not create tracked files that store personal voice fingerprints unless the user explicitly asks for that.

## Downstream Use

Use this skill before or inside:

- `content-engine`
- `investor-outreach`
- article or launch writing
- cold or warm outbound across social and email

If another skill already has a partial voice capture section, this skill is the canonical source of truth.