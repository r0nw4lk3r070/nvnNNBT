# Editorial — The Daily Stack

## Status
Active — workspace built, pipeline designed, voice profile extracted, site scaffold ready

## Architecture
- Single agent (Editor-in-Chief) with 9 skills as pipeline phases
- File-based state: each article gets `/articles/{slug}/` with phase outputs
- Voice profiles per publisher in `/library/voice-profiles/`

## Voice profiles
- `ronspoelstra-great-return.md` — derived from Kill Switch, Local by Necessity, Person Is the Perimeter

## Site
- Static HTML served by `server.py` (Python http.server) on port 8900
- Dark theme, serif typography, matches ronspoelstra.be aesthetic
- Coder skill converts approved drafts to HTML using `article-template.html`
- Docker: server.py runs inside the container; port 8900 needs exposing on the host

## Test case
- Source: https://ronspoelstra.be/articles/ (The Great Return series)
- Voice: ronspoelstra-great-return.md
- Goal: run full pipeline Scout→Referee on a Great Return topic, publish to local site

## Open
- [ ] Port 8900 exposure in docker-compose for the spawned agent
- [ ] Voice agent skill (TTS / audio version) — not yet built
- [ ] First pipeline test run