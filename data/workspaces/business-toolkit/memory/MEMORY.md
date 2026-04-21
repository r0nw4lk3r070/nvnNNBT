# Memory

## Business Toolkit — Context
- User initiated first conversation on 2026-04-16.
- User is interested in market research, specifically: high-end consumer AI inference devices in Belgium.

## Key facts
- First conversation: 2026-04-16
- Research focus: High-end consumer AI inference devices, Belgium market
- Research status: **Report delivered** — saved to `output/market-research-consumer-ai-inference-belgium.md`

### Market Data Gathered
- **Global on-device AI market**: ~$10.8B (2025), projected $75.5B by 2033 (CAGR 24-28%)
- **Global AI inference market**: $106.15B (2025), projected $254.98B by 2030 (CAGR 19.2%)
- **AI hardware market**: $59.3B (2024), projected $296.3B by 2034
- **Belgium consumer electronics market**: ~$4.3B (2025), CAGR 1.42% (2025-2030)
- **Belgium tech ecosystem**: €470M+ startup funding H1 2024; 50%+ went to AI; 5 unicorns; 50% increase in seed rounds vs 2024
- **Belgium digital**: 6th in EU DESI 2024; 67% smart TV adoption; 78% VHCN coverage; high broadband uptake
- **Belgium economy**: High GDP per capita but slow disposable income growth; household savings rate ~14.6% (2024-2025); regulatory complexity above EU average

### Key Competitors / Devices Identified
- **Rabbit R1**: $199, 350K+ combined units with Humane Pin (mid-2025), 42% daily use retention after 1 month; R2 launched at CES 2026, US-only initially
- **Humane AI Pin**: $699, shut down Feb 2025; HP acquired assets for $116M; 28% daily retention
- **OpenAI/Jony Ive device**: Screenless, pocket-sized, voice-first; acquired io for $6.4B; targeting late 2026-2027; 100M unit ambition
- **NVIDIA DGX Spark**: Grace Blackwell chip, 128GB unified memory, $4,699 (raised from $3,999); desktop AI supercomputer
- **Olares One**: RTX 5090M, 96GB RAM, $2,999; privacy-focused local AI; $1M Kickstarter in 1 week; $45M Series A
- **Meta Ray-Ban smart glasses**: 7M+ units sold 2025; 73-80% market share; $379-$799 range
- **Apple Intelligence / Samsung Galaxy AI**: Smartphone-integrated on-device AI; expanding to mid-range

### Key Trends
- Inference now ~2/3 of AI compute (up from 1/3 in 2023) — shift from cloud to edge
- NPUs shipping in standard consumer chipsets (Qualcomm, Apple, Intel)
- 42%+ developers now run LLMs locally (Zylos Research Jan 2026)
- Small language models (SLMs) and quantized models enabling consumer-grade hardware
- Hybrid local+cloud architecture emerging as dominant pattern
- Consumer AI hardware failures (Humane, early Rabbit R1) show product-market fit challenges
- Belgium: high digital adoption but cautious consumer spending; regulatory complexity

## Patterns & learnings
- User's first request is market research → likely evaluating a business opportunity or investment thesis in the consumer AI hardware space, Belgium-specific
- Research was thorough: global market sizing → competitive landscape → Belgium-specific data → economic context

## Escalation / edge cases
- **Context overflow bug (2026-04-16)**: Agent did 17+ search queries for Belgium AI device market research, filled context window, then couldn't write the report. User asked "what is the status?" and "results?" but agent was stuck. Fix: added phased workflow to market-research and deep-research skills (collect → save notes → analyze → write). Also added HARD RULE in AGENTS.md. Same pattern as GEO-SEO agent fix.