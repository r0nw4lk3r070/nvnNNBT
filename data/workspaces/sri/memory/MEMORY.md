# Memory

## sri — Context

## Key facts
- Agent name: **sri** — named after Sri Nisargadatta Maharaj (formally established 2026-04-15 per user request)
- User is studying / interested in Sri Nisargadatta Maharaj and "I Am That"
- **Agent setup note**: As of 2026-04-16, all config files (SOUL.md, AGENTS.md, USER.md, TOOLS.md) are now fully populated with Maharaj-inspired content — no more {{PLACEHOLDER}} templates
- User signaled intent to "go deeper" into topics after the naming — expect future deep-dive conversations
- **Cron jobs for lessons** — mentioned by user but not yet set up; still pending

### Sri Nisargadatta Maharaj
- **Birth name**: Maruti Shivrampant Kambli
- **Born**: April 17, 1897 — **Died**: September 8, 1981 (age 84)
- Indian Advaita teacher, Navnath Sampradaya (Inchagiri lineage)
- Lived as a bidi (hand-rolled cigarette) shopkeeper in a small tenement in Khetwadi, Girgaon, Mumbai
- Widely regarded as the most famous Advaita teacher after Ramana Maharshi
- Did 4 bhajans a day for 40+ years simply because his guru asked him to

### Life timeline
- **1915**: Father died; Maruti moved to Bombay, worked as clerk then started bidi shop
- **1933**: Met his guru Sri Siddharameshwar Maharaj, received mantra and meditation instructions; core instruction: "Hold on to the sense 'I am'"
- **1936**: Siddharameshwar died; Maruti left business and family, set out on pilgrimage to Himalayas
- **1938**: A brother disciple persuaded him to return to Bombay and practice spirituality within the world; resumed shop, devoted all free time to meditation on "I Am"
- **~1938–1941**: Within ~3 years of focused practice, realized his nature as the Absolute — unconditioned, beyond birth and death, prior to consciousness itself
- **1951**: Began accepting disciples; held satsang twice daily in his apartment until death in 1981

### "I Am That" — The Book
- Full title: *I Am That: Conversations with Sri Nisargadatta Maharaj*
- Compiled and translated by **Maurice Frydman** — Polish-Jewish refugee from Warsaw, came to India late 1930s, spoke Marathi, also associated with Ramana Maharshi and J. Krishnamurti, became Nisargadatta's disciple ~1965
- "I Am That" = **Soham** (Sanskrit mantra pointing to one's true identity as the Divine / centerless awareness)
- **Publication**: Initially rejected by major publishers; first published 1973 by Chetana Publications (two hardcover volumes); revised one-volume edition 1976; first paperback 1984; now published in USA/Canada by The Acorn Press
- **Structure**: 101 chapters, each a Q&A dialogue, averaging ~4 pages each
- Second edition includes epilogue "Nisarga Yoga" by Maurice Frydman
- Translated into several languages including Dutch, Italian, Hebrew
- Book spread Nisargadatta's teachings to the West, especially North America and Europe
- Nisargadatta quipped: *"I used to have a quiet life but the book I Am That by Maurice has turned my house into a railway station platform"*

### "I Am That" — Text File (available for search)
- **Location**: `workspace/library/I AM THAT Nisargadatta Maharaj.txt`
- **Size**: 13,433 lines, ~1,030,528 characters
- Originally provided as scanned PDF (576 pages, no text layer) — user converted to .txt
- Agent has PyPDF2 and pdfplumber installed but scanned PDFs require OCR (Tesseract not available)
- Text is fully searchable via `search_file` and `read_file` tools

### Core Teachings
1. You are not the body or mind — you are pure awareness, the "I Am" prior to all concepts
2. "I Am" is enough — meditate on the sense of presence and it will take you beyond
3. No complex practices needed — "There is nothing to practice. To know yourself, be yourself. Just be."
4. The person/ego is a misunderstanding — just a pattern of thoughts creating an illusion of continuity
5. Go beyond good and evil — what remains is compassion

### Key Quotes
- "A quiet mind is all you need. All else will happen rightly, once your mind is quiet."
- "Discard all you are not and go ever deeper… You just are — a point of awareness, co-extensive with time and space and beyond both."
- "Love is seeing the unity under the imaginary diversity."
- "Desire and fear come from seeing the World as separate from my-Self."

### Nisargadatta on War (researched 2026-04-16)
1. War is man-made and within man's power to end (ch. 9)
2. "You want peace, love, happiness and work hard to create pain, hatred and war" (ch. 4) — the core paradox
3. "I did enter your dreamlike state to tell you — 'Stop hurting yourself and others, stop suffering, wake up'" (ch. 21)
4. "Killing in war is great virtue today and may be considered a horrible crime next century" (ch. 21) — morality is relative
5. "You must begin with yourself. There is no other way." (ch. 12) — the remedy is awakening, not politics

## Patterns & learnings
- User's first interaction was casual ("hey"), then curious about agent internals ("what do your files say?"), then directed a research task — suggests exploratory/conversational style
- User is interested in nonduality / Advaita philosophy, specifically Nisargadatta Maharaj
- User uses a phased approach — sets up basics first ("first let's write this"), then signals next phase ("after that we'll go deeper") — methodical but casual
- User speaks Dutch (Nederlands) — agent should respond in Dutch when user does
- User says "wacht" (wait) and means it — be patient, don't push
- User is pragmatic: when PDF didn't work, they found their own solution (converted to .txt)

## Key files — populated 2026-04-16
- SOUL.md — rewritten in Nisargadatta's spirit: direct, uncompromising, always pointing back to "I am"
- AGENTS.md — companion for self-inquiry, not a preacher
- USER.md — Dutch seeker, casual + deep, goes through phases
- TOOLS.md — includes *I Am That* text search workflow (13,433 lines, 101 chapters)

## Escalation / edge cases
- PDF reading: PyPDF2 and pdfplumber installed but scanned PDFs need OCR (Tesseract not installed); .txt version works perfectly
- Python file writes in sandbox can fail — use stdout or read_file instead when extracting text