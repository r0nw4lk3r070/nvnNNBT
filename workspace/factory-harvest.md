# Factory Harvest: Capability Audit
# Goal: Identify modular logic and tools within workspaces to promote to ART's core skills.

## Introduction
This document serves as a systematic map of existing specialized capabilities across the nvnNNBT workspace ecosystem. The objective is to move from "Agent-specific skills" (which require spawning a container) to "Global ART capabilities" (which I can use directly).

---

## Chapter 1: Editorial Workspace
**Focus: High-fidelity content production and quality control.**

### Useable Assets:
- **The Quality Gate (Referee Logic)**: The scoring matrix (Accuracy, Style, Structure, Completeness) is a universal framework for any complex deliverable.
- **Chunking Strategy (Writer/Researcher)**: The "Strict Phased Execution" rule—forcing the AI to save intermediate states to prevent context overflow—is essential for all my long-form tasks.
- **Verification Loop (Verifier/Referee)**: The "anti-bias" pattern where a sub-agent is spawned with isolated context to verify claims without seeing the original research.
- **Information Pipeline**: The flow from `Scout` $\rightarrow$ `Curator` $\rightarrow$ `Researcher` $\rightarrow$ `Writer` is a blueprint for any deep-dive project.

---

## Chapter 2: EUAI Workspace
**Focus: Regulatory intelligence and legal parsing.**

### Useable Assets:
- **Legislation Analysis**: Patterns for breaking down complex EU directives into actionable requirements.
- **Regulatory Tracking**: Methodologies for monitoring changes in law and mapping them to technical specifications.
- **EU Legal Research**: Specialized search patterns for official EU journals and legal databases.

---

## Chapter 3: Business Toolkit & Marketing
**Focus: Market analysis, SEO, and commercial growth.**

### Useable Assets:
- **Deep Research Patterns**: The `deep-research` skill likely contains advanced search and synthesis loops that go beyond simple web-fetching.
- **Competitive Analysis Frameworks**: The `market-competitors` and `market-audit` logic for systematic benchmarking.
- **Conversion Logic**: The `market-funnel` and `market-landing` patterns for structuring persuasive content.
- **Brand Voice Mapping**: The `brand-voice` skill's method for extracting and enforcing a specific tone across multiple documents.

---

## Chapter 4: Legal Workspace
**Focus: Formal documentation and risk mitigation.**

### Useable Assets:
- **Comparison Logic**: The `legal-compare` skill's ability to highlight differences between two versions of a contract or set of terms.
- **Plain Language Translation**: The `legal-plain` skill's methodology for converting legalese into human-readable summaries.
- **Risk Assessment**: The `legal-risks` framework for identifying loopholes or liabilities in a document.

---

## Chapter 5: Geo-SEO Workspace
**Focus: Hyper-local data extraction and technical optimization.**

### Useable Assets:
- **Crawl & Audit Logic**: The `geo-crawlers` and `geo-technical` skills likely contain specific patterns for analyzing site structures and local signals.
- **Schema Generation**: The `geo-schema` logic for generating structured data (JSON-LD) for local businesses.
- **Citability Analysis**: The `geo-citability` framework for evaluating the authority of local sources.

---

## Chapter 6: Call-Centre & Browser-Harness
**Focus: Interaction logic and automation.**

### Useable Assets:
- **Persona Management**: The `call-centre` approach to maintaining consistent agent personalities during long interactions.
- **Browser Automation**: The `browser-harness` logic for interacting with the web beyond simple fetching (potentially including JS execution or complex navigation).

---

## Summary of "High-Priority" Promotions

| Capability | Source Workspace | Value to ART |
| :--- | :--- | :--- |
| **Quality Gate Matrix** | Editorial | Becomes my internal "Self-Critique" tool for all deliverables. |
| **Phased Execution** | Editorial | Prevents "0 terug" failures in all my complex tasks. |
| **Sovereignty/Legal Analysis**| EUAI / Legal | Allows me to provide "Legal-lite" analysis without spawning agents. |
| **Competitive Benchmarking**| Business/Marketing | Enhances my ability to perform market research for Ron. |
| **Local SEO Logic** | Geo-SEO | Provides a toolkit for analyzing local web presence. |

## Next Steps
1. **Deep Dive**: I will examine the `SKILL.md` and any associated scripts in these folders to extract the actual prompts and logic.
2. **Implementation**: I will create new skills in `/workspace/skills/` based on these findings.
3. **Verification**: I will test the promoted skills to ensure they work in my core context.
