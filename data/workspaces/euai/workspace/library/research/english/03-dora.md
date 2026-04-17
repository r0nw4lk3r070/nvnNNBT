# 03 — DORA
### LocAI Library · Deep Dive
_Regulation (EU) 2022/2554 · In force 17 January 2025_
_Version 0.1 · March 2026_

---

## What this document is

DORA stands for Digital Operational Resilience Act. It is a regulation — directly binding in all member states, no national implementation required. Specifically aimed at the financial sector. This document follows the same structure: literal text, translation, implication for local AI versus cloud AI.

---

## The core in one sentence

DORA obliges financial institutions to take their digital resilience seriously — including the resilience of all ICT services they procure from third parties.

---

## Part 1 — Why DORA exists

The financial sector has become entirely dependent on digital systems and external ICT suppliers. Banks run on cloud infrastructure from Amazon, Microsoft and Google. Payment systems are intertwined with dozens of third parties. A disruption at one major supplier can affect the entire financial system.

The European supervisory authorities — ECB, EBA, ESMA, EIOPA — watched this risk grow and concluded that existing regulation was insufficient. DORA is the answer.

What is new compared to what already existed: the focus on operational resilience as a whole, including the full chain of ICT suppliers. Not just "is your own system secure" but "can you withstand the failure of systems you depend on."

---

## Part 2 — Who does DORA apply to?

### The literal text (Art. 2)

DORA applies to:

> "a) credit institutions; b) payment institutions; c) electronic money institutions; d) investment firms; e) crypto-asset service providers; f) central securities depositories; g) central counterparties; h) trading venues; i) trade repositories; j) managers of alternative investment funds; k) management companies; l) data reporting service providers; m) insurance and reinsurance undertakings; n) insurance intermediaries, reinsurance intermediaries and ancillary insurance intermediaries; o) institutions for occupational retirement provision; p) credit rating agencies; q) administrators of critical benchmarks; r) crowdfunding service providers; s) securitisation repositories; t) ICT third-party service providers."

### The translation

In plain language: everything related to financial services.

The most relevant categories for our target audience:

**Credit institutions:** banks, savings banks, credit cooperatives.

**Payment institutions:** companies that process payment transactions.

**Investment firms:** asset managers, stockbrokers.

**Insurance undertakings:** all forms of insurance.

**Insurance intermediaries:** brokers, agents — including the small independent insurance broker.

**ICT third-party service providers:** this is the category that changes everything. A cloud provider delivering services to a bank itself also falls under DORA. A software-as-a-service company providing HR software to an insurance company: also under DORA.

**The thresholds:**
Simplified obligations apply to small financial institutions. But "simplified" does not mean "no obligations."

### What this means for our target audience

An accountancy firm doing the bookkeeping for an insurance broker: the broker falls under DORA. That broker must assess the ICT suppliers of its accountant if those ICT services affect the financial service delivery.

A software company providing invoicing software to a bank: directly under DORA as an ICT third-party service provider.

The boundary is not always sharp — but the direction is clear: DORA flows through the entire chain.

---

## Part 3 — The five pillars of DORA

DORA is built around five core areas. Together they form a framework for digital operational resilience.

### Pillar 1 — ICT risk management (Art. 5-16)

### The literal text (Art. 5(1))

> "Financial entities shall have in place a sound, comprehensive and well-documented ICT risk management framework as part of their overall risk management system, enabling them to address ICT risk quickly, efficiently and comprehensively and to ensure a high level of digital operational resilience."

### The translation

You must have a framework for managing ICT risks. Not a document sitting in a drawer — a working system that you can demonstrate to a regulator.

What that framework must include at minimum:
- Identification of all ICT assets (hardware, software, data, networks)
- Protection of those assets
- Detection of anomalies and incidents
- Response to incidents
- Recovery after incidents
- Learning from incidents

### The implication for local AI versus cloud AI

A cloud AI service is an ICT asset. It goes in your register. You must assess its risk. You must have an exit strategy.

With local AI: the AI component is on your own hardware. It is an internal ICT asset you fully manage. No external dependency to register and monitor.

---

### Pillar 2 — Management of ICT-related incidents (Art. 17-23)

### The literal text (Art. 17(1))

> "Financial entities shall define, establish, and implement an ICT-related incident management process to detect, manage and notify ICT-related incidents."

With notification timeframes (Art. 19):

> "Financial entities shall report major ICT-related incidents [...] to the competent authority [...]:
> a) an initial notification, without undue delay and no later than four hours after the classification of the incident as major;
> b) an intermediate report [...] no later than 72 hours after the initial notification;
> c) a final report [...] no later than one month after the submission of the intermediate report."

### The translation

If there is a major ICT incident, you have:

- 4 hours for an initial notification to the regulator
- 72 hours for an intermediate report
- 1 month for a final report

That is faster than NIS2 (24-hour initial notification) and GDPR (72 hours). The financial sector is held to a higher standard.

"Major" incident means: significant number of customers affected, prolonged outage, data integrity compromised, reputational damage, or financial impact above a certain threshold.

### The implication for local AI versus cloud AI

If a cloud AI service goes down or is hacked and that has an impact on your financial service delivery, the 4-hour clock starts running the moment you become aware.

But if the cloud AI provider only communicates about the incident after 6 hours, you already have a problem with your notification obligation.

With local AI: the incident is in your own environment. You detect it yourself. You control the communication strategy. No dependence on the communication speed of an external provider.

---

### Pillar 3 — Digital operational resilience testing (Art. 24-27)

### The literal text (Art. 24(1))

> "Financial entities shall establish, maintain and review a sound and comprehensive digital operational resilience testing programme as an integral part of the ICT risk management framework referred to in Article 6."

### The translation

You cannot simply say your systems are secure — you must test it. And document it.

Basic level: annual tests of all ICT systems and applications.

Advanced level (mandatory for large financial institutions): Threat-Led Penetration Testing (TLPT) — simulated attacks on production systems by certified external testers, at least every three years.

### The implication for local AI versus cloud AI

Testing a cloud AI service for resilience is complex: you have limited access to the infrastructure, and the provider largely determines what you are allowed to test.

Local AI systems are fully accessible for penetration tests. You can test the full stack — hardware, software, network, access control — without permission from an external party.

---

### Pillar 4 — Management of ICT third-party risk (Art. 28-44)

This is the pillar with the most impact on daily practice.

### The literal text (Art. 28(1))

> "Financial entities shall manage ICT third-party risk as an integral component of ICT risk within their ICT risk management framework and in accordance with the following principles:
> a) financial entities that have contractual arrangements for the use of ICT services shall act with due diligence [...];
> b) financial entities shall only enter into contractual arrangements with ICT third-party service providers that comply with appropriate information security standards."

And (Art. 28(2)):

> "Financial entities shall maintain a register of information in relation to all contractual arrangements on the use of ICT services provided by ICT third-party service providers."

### The literal text (Art. 30 — mandatory contract content)

Contracts with ICT suppliers must contain at minimum:

> "a) a clear and comprehensive description of all functions and ICT services to be provided;
> b) the locations where the contractual functions and ICT services are to be provided [...];
> c) provisions on availability, authenticity, integrity and confidentiality [...];
> d) provisions on access, recovery and return of data [...];
> e) full service level descriptions [...];
> f) the relevant provisions on exit strategies."

### The translation

Every cloud provider, every SaaS supplier, every external ICT service must:

1. Be in a register
2. Have a contract meeting DORA requirements
3. Be assessed on their cybersecurity practices
4. Have an exit strategy

**The register:** you must be able to demonstrate which ICT services you procure, from whom, for what purpose, and how critical they are to your service delivery.

**The exit strategy:** if a supplier disappears, goes bankrupt, or terminates your contract — what do you do? You must have a plan. And that plan must work.

**The location:** you must know where your data is. "In the cloud" is not an answer. Which data centre, in which country, under which jurisdiction?

### The implication for local AI versus cloud AI

This is the article that makes cloud AI expensive for financial institutions — not financially, but administratively.

A cloud AI service requires:
- An entry in the DORA register
- A contract complying with Art. 30 (including data location, exit strategy, SLA)
- An assessment of the provider's security practices
- Periodic review of that assessment
- A documented exit strategy

With local AI: no external ICT third-party provider for the AI component. No register entry, no DORA-compliant contract needed, no exit strategy required. The AI functionality is in the organisation's own infrastructure.

The exit strategy for local AI is straightforward: the hardware is at your premises. The models are open-source. If the hardware maintenance supplier disappears, you buy a new supplier. Your data stays with you.

---

### Pillar 5 — Information sharing (Art. 45)

### The literal text

> "Financial entities may exchange amongst themselves cyber threat information and intelligence, including indicators of compromise, tactics, techniques and procedures, cybersecurity alerts and configuration tools."

### The translation

DORA encourages financial institutions to share threat intelligence. This is optional, not mandatory. But it creates an ecosystem of shared intelligence on cyber threats.

---

## Part 4 — DORA and cloud AI: the practical consequence

Let us make it concrete for a typical client.

**Scenario: an insurance broker with 12 employees**

He falls under DORA as an insurance intermediary (Art. 2(n)). He uses ChatGPT Team to draft policy advice and summarise insurance terms.

What he must now do under DORA:

1. Add ChatGPT/OpenAI to his ICT register as a third-party service provider
2. Assess his contract with OpenAI for DORA compliance (data location, exit strategy, SLA — these are not standard in the ChatGPT Team terms)
3. Document an assessment of OpenAI's cybersecurity practices
4. Document an exit strategy: what does he do if OpenAI stops its service, multiplies its price tenfold, or has a data breach?
5. Review this periodically

That is considerable work for an office of 12 people.

**With local AI:**

The AI runs on a mini-PC in the office. OpenAI is not in the register. No DORA-compliant contract is needed for the AI component. The exit strategy is simple: the hardware is there, the models are open-source.

Compliance burden: significantly lower.

---

## Part 5 — DORA, NIS2 and GDPR together

The three laws overlap for financial institutions.

| | GDPR | NIS2 | DORA |
|---|---|---|---|
| **Primary focus** | Personal data | Cybersecurity systems | Operational resilience — finance |
| **Notification obligation** | 72h for data breach | 24h warning, 72h notification | 4h initial notification, 72h intermediate |
| **Supply chain** | Via data processing agreement | Art. 21d | Art. 28-44 (extensive) |
| **Director liability** | Implicit | Explicit Art. 20 | Implicit via accountability obligation |
| **Testing mandatory** | No | Implicit | Explicit Art. 24-27 |
| **Register mandatory** | Processing register | Not specific | ICT third-party providers register |

For a bank or insurer all three apply simultaneously. That is a complex compliance environment where every external ICT service — including cloud AI — triggers multiple legal obligations.

---

## Part 6 — DORA and the small financial institution

DORA recognises that not all financial institutions are equally large. Art. 16 provides for "simplified ICT risk management arrangements" for small and non-interconnected institutions.

But "simplified" does not mean "exempt." The basic obligations remain:
- Document ICT risk management
- Register and report incidents
- Assess contracts with ICT suppliers
- Exit strategy for critical services

For a small insurance broker or small investment adviser: the simplified rules apply, but the core logic of DORA — know who you depend on and ensure you can survive if that dependency disappears — remains fully applicable.

---

## Glossary

**Financial entity** — any company providing financial services and falling within the scope of DORA (banks, insurers, investment firms, payment institutions, etc.).

**ICT third-party service provider** — an external party delivering ICT services to a financial entity. Cloud providers, software suppliers, data centres, but also AI services.

**Critical ICT third-party provider** — an ICT supplier so important to the financial sector that it falls directly under the supervision of European supervisory authorities (ESAs). Amazon AWS, Microsoft Azure and Google Cloud have been designated as critical suppliers.

**Digital operational resilience** — the ability of a financial entity to build, assure and review its ICT-related capabilities to ensure the integrity and reliability of its service delivery, including during ICT-related disruptions or incidents.

**ICT risk** — any reasonably identifiable risk relating to the use of network and information systems, including hardware or software failures, cyberattacks and data loss.

**TLPT (Threat-Led Penetration Testing)** — an advanced form of penetration test in which real attack tactics are simulated against production systems. Mandatory for large financial institutions at least every three years.

**ESAs (European Supervisory Authorities)** — the three European financial supervisory authorities: EBA (banks), ESMA (securities markets), EIOPA (insurance and pensions). They supervise the critical ICT third-party providers.

**EBA** — European Banking Authority. Supervision of banks and payment institutions.

**ESMA** — European Securities and Markets Authority. Supervision of investment firms and securities markets.

**EIOPA** — European Insurance and Occupational Pensions Authority. Supervision of insurers and pension funds.

**Exit strategy** — a documented plan for ending dependence on an ICT supplier without significant disruption to service delivery.

**Operational continuity** — the ability to continue critical business functions during and after a disruption.

---

## Checklist for a client conversation (financial sector)

- [ ] Does your organisation fall under DORA? (type of financial institution)
- [ ] Do you have a register of all ICT third-party service providers?
- [ ] Are your cloud suppliers — including AI services — in that register?
- [ ] Do your contracts with ICT suppliers meet the DORA requirements? (data location, SLA, exit strategy)
- [ ] Do you have a documented exit strategy for critical ICT services?
- [ ] Do you have an ICT risk management framework documented?
- [ ] Do you have an incident response plan with the correct notification timeframes? (4h, 72h, 1 month)
- [ ] Do you test your digital resilience regularly?
- [ ] Do you know where your data is — in which data centre, in which country?
- [ ] Have you as a director formally approved the ICT risk measures?

---

_Previous document: 02-nis2.md_
_Next document: 04-data-act.md_
_Last updated: March 2026_
