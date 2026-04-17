# Weather Skill for EUAI (Ticket 003)

**Name**: weather  
**Description**: Get current weather, 5-day forecast and interpretation for Sint-Joris-Weert (Leuven area) using the free Open-Meteo API. No key required.  
**Priority**: High (unblocks Portal weather widget and EUAI regulatory context for smart-home/IoT sector).

## Capabilities

- Current conditions (temperature, feels-like, humidity, wind, weather code + emoji)
- 5-day daily forecast (min/max temp, precipitation probability)
- Simple interpretation (e.g. "good conditions for outdoor solar installation" or "high wind risk for rooftop equipment")
- Caching (5-10 minutes)
- Graceful fallback when offline

## Usage in EUAI

- Ask "wat is het weer vandaag?" or "how is the weather for the next days?"
- Use in sector guides (T03 Smart Home, solar, EV charging, outdoor sensors)
- Feed into compliance checklists (e.g. weather resilience under NIS2/CRA)

## Implementation

The skill is implemented as a Python module that can be called from the agent or the research site.

Location: `skills/weather/`

Run `python -m skills.weather` to test.

**Status**: Ready for integration into the research site and Portal (Ticket 003 complete when both are wired up).

**Next**: Add the skill to the main EUAI agent and expose a clean `/api/weather` endpoint on port 6163.
