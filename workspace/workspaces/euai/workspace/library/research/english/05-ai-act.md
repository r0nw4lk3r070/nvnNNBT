# 05 — EU AI Act
### LocAI Library · Deep Dive
_Regulation (EU) 2024/1689 · Expected deadline for high-risk systems: 2 December 2027_
_Version 0.2 · March 2026 — updated after EP committee vote of 18 March 2026_

---

## What this document is

The AI Act is the first binding AI law in the world. It is complex, extensive, and directly relevant to every organisation deploying AI. This document follows the same structure as the previous documents: literal text, translation, implication for local AI versus cloud AI.

But the AI Act also deserves extra attention for its terminology — because the law introduces an entirely new vocabulary you need to know to have a meaningful conversation about it.

---

## The core in one sentence

The AI Act classifies AI systems by risk level, imposes heavy obligations on organisations developing or deploying high-risk AI, and makes local deployment the architecturally simplest path to compliance.

---

## Part 1 — Why the AI Act exists

### The literal text (Recital 1)

> "Artificial intelligence is a fast evolving family of technologies that can contribute to a wide array of economic and societal benefits across the entire spectrum of industries and social activities. [...] At the same time, depending on the circumstances regarding its specific application and use, artificial intelligence may generate risks and cause harm to public interests and rights that are protected by Union law."

### The translation

AI is powerful and useful. But it can also cause harm — to people, to democratic processes, to fundamental rights. Europe chooses to regulate those risks before they become reality, rather than reacting after the fact.

This is the European model: proactive regulation based on risks. The same principle is embedded in GDPR, NIS2 and DORA — but now applied to intelligent systems themselves.

### The historical context

The AI Act builds directly on everything that preceded it:
- GDPR regulates the data on which AI trains and operates
- NIS2 regulates the security of the systems on which AI runs
- DORA regulates the resilience of financial AI systems
- The Data Act regulates the data that AI systems generate

The AI Act closes the circle: it regulates the intelligence itself.

---

## Part 2 — The vocabulary of the AI Act

Before we get into the articles, the key concepts must be clear. The AI Act has its own language that you need to know.

### AI system

### The literal text (Art. 3(1))

> "'AI system' means a machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments."

### The translation

An AI system is any system that:
- Runs on a machine
- Operates with a degree of autonomy
- Processes input to generate output (predictions, content, recommendations, decisions)

ChatGPT is an AI system. A spam filter is an AI system. A credit scoring algorithm is an AI system. A route planner that uses AI is an AI system.

What is NOT an AI system: ordinary software that operates purely on rules without learning or inference. A calculator is not an AI system. An Excel formula is not an AI system.

---

### Provider

### The literal text (Art. 3(3))

> "'provider' means a natural or legal person, public authority, agency or other body that develops an AI system or a general-purpose AI model or that has an AI system or a general-purpose AI model developed and places it on the market or puts the AI system into service under its own name or trademark, whether for payment or free of charge."

### The translation

The provider is the one who builds the AI system and brings it to market. OpenAI is the provider of ChatGPT. Google is the provider of Gemini. Meta is the provider of Llama.

If you build an AI system for internal use and do not bring it to market, you are also a provider — but of an internal system, with corresponding obligations.

---

### Deployer

### The literal text (Art. 3(4))

> "'deployer' means a natural or legal person, public authority, agency or other body that uses an AI system under its own authority, except where the AI system is used in the course of a personal non-professional activity."

### The translation

The deployer is the one who uses the AI system for professional purposes. An accountant using ChatGPT for work is a deployer. A hospital deploying an AI diagnostic system is a deployer.

Important: the deployer also has obligations under the AI Act — not just the provider. If you deploy a high-risk AI system, you are responsible for correct use, human oversight, and transparency towards affected persons.

---

### GPAI model (General Purpose AI Model)

### The literal text (Art. 3(63))

> "'general-purpose AI model' means an AI model, including where such an AI model is trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks."

### The translation

A GPAI model is a large language model that can be deployed for a wide variety of purposes. GPT-4, Gemini, Llama, Claude, Mistral — all GPAI models.

GPAI models have their own obligations in the AI Act, separate from the risk classification of the system in which they are used.

---

### High-risk system

The core of the AI Act. Covered extensively in Part 4.

---

### Conformity assessment

### The literal text (Art. 3(20))

> "'conformity assessment' means the process of verifying whether the requirements set out in Chapter III, Section 2 of this Regulation relating to a high-risk AI system have been fulfilled."

### The translation

Before a high-risk AI system is put into service, it must be demonstrated that it meets all requirements of the AI Act. This is the conformity assessment. Think of the CE marking for products, but for AI.

---

## Part 3 — The timeline

### The literal text (Art. 113)

| Date | Event |
|---|---|
| 1 August 2024 | AI Act entered into force |
| 2 February 2025 | Prohibited practices (Art. 5) + AI literacy (Art. 4) applicable |
| 2 August 2025 | GPAI model obligations + fines framework active |
| ~~2 August 2026~~ | ~~All obligations for high-risk AI systems~~ _(original deadline — see update)_ |
| **2 December 2027** | **Expected new deadline for high-risk systems (Annex III)** |
| **2 August 2028** | **High-risk AI as safety component in products under sectoral legislation** |

> **Update March 2026:** The European Parliament (IMCO + LIBE committees) voted on 18 March 2026, with 101 votes in favour and 9 against, for a postponement of the high-risk deadline. The plenary vote is scheduled for 26 March, after which trilogue negotiations with the Council will follow. Until the law is officially amended, August 2026 remains legally in force as the operational deadline — but the direction is clear.

### The translation

We are currently in March 2026. This means:

- Prohibited practices already apply — since February 2025
- GPAI obligations already apply — since August 2025
- The high-risk deadline is expected to shift to 2 December 2027

The postponement removes the immediate time pressure — but not the obligation. Organisations waiting until 2027 are losing eighteen months of preparation.

---

## Part 4 — The risk classification

This is the architecture of the entire law. Everything depends on which risk category an AI system falls into.

### Level 1 — Unacceptable risk (Art. 5) — PROHIBITED

### The literal text (Art. 5(1), selection)

> "The following AI practices shall be prohibited:
> (a) the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person's consciousness [...] with the objective of or the effect of materially distorting the behaviour of a person;
> (b) the placing on the market, the putting into service or the use of an AI system that exploits any of the vulnerabilities of a specific group of persons [...];
> (c) the placing on the market, the putting into service or the use of AI systems for the evaluation or classification of natural persons [...] based on their social behaviour or known, inferred or predicted personal or personality characteristics ('social scoring');
> (d) the placing on the market, the putting into service or the use of AI systems for risk assessments of natural persons in order to assess the risk of a natural person committing a criminal offence;
> (e) the [...] creation of facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage;
> (f) the [...] inference of emotions of a natural person in the areas of workplace and education [...];
> (g) biometric categorisation systems that categorise individually natural persons [...] in order to deduce or infer their [...] sensitive or protected attributes;
> (h) the use of 'real-time' remote biometric identification systems in publicly accessible spaces for the purpose of law enforcement."

### The translation

Eight categories that are simply prohibited. No exceptions for good intentions, no transitional period.

In plain language:
- **No social scoring:** you may not rank people based on their behaviour or personality
- **No manipulation:** you may not use AI to unconsciously influence people
- **No emotion recognition at work or in class:** you may not measure how employees or students feel
- **No biometric mass identification in public spaces:** facial recognition for surveillance is prohibited (with very limited exceptions for law enforcement)
- **No predictive policing:** AI may not predict whether someone will commit a crime

---

### Level 2 — High risk (Art. 6 + Annex III) — HEAVY OBLIGATIONS

This is the core of the law. High-risk AI systems are permitted, but only if you meet all requirements.

### The literal text (Annex III — selection)

> "High-risk AI systems referred to in Article 6(2):
> 1. Biometrics [...]
> 2. Critical infrastructure [...]
> 3. Education and vocational training:
>    (a) AI systems intended to be used for the purpose of determining access or assigning natural persons to educational and vocational training institutions at all levels or to evaluate learning outcomes of persons in educational and vocational training institutions;
>    (b) AI systems intended to be used to assess and evaluate students [...]
> 4. Employment, workers management and access to self-employment:
>    (a) AI systems intended to be used for recruitment or selection of natural persons, notably for advertising vacancies, screening or filtering applications, evaluating candidates;
>    (b) AI systems intended to be used for making decisions affecting terms of work-related relationships, [...] including task allocation [...]
> 5. Access to and enjoyment of essential private services and essential public services and benefits:
>    (a) AI systems intended to be used by public authorities [...] to evaluate the eligibility of natural persons for essential public assistance benefits and services;
>    (b) AI systems intended to be used to evaluate the creditworthiness of natural persons [...]
>    (c) AI systems intended to be used for risk assessment and pricing in relation to natural persons in the case of life and health insurance;
> 6. Law enforcement [...]
> 7. Migration, asylum and border control management [...]
> 8. Administration of justice and democratic processes [...]"

### The translation

High-risk AI systems are systems used in contexts where errors can have serious consequences for people.

The sectors most relevant to our target audience:

**Education:** an AI that determines whether a student is admitted, or that assesses learning outcomes. A school using AI for pupil guidance must treat this as high-risk.

**HR and recruitment:** an AI that screens CVs, ranks candidates, or determines work conditions. A company using AI in its recruitment process has a high-risk system.

**Credit and insurance:** an AI that assesses creditworthiness or determines insurance premiums. Banks and insurers using AI for these decisions are firmly in the high-risk category.

**Essential public services:** an AI that determines whether someone is entitled to a benefit or a service.

---

### Level 3 — Limited risk — TRANSPARENCY OBLIGATION

Chatbots and systems generating text that people can read must make clear that it is AI. Deepfakes must be labelled.

A customer service bot that does not identify itself as AI — that is a violation.

---

### Level 4 — Minimal risk — NO OBLIGATIONS

Spam filters, streaming recommendation systems, AI in video games. The vast majority of AI applications fall here.

---

## Part 5 — Obligations for high-risk AI (Art. 8-15)

These are the articles most directly relevant to organisations deploying high-risk AI.

### Art. 9 — Risk management system

### The literal text

> "A risk management system shall be established, implemented, documented and maintained in relation to high-risk AI systems."

> "The risk management system shall be understood as a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system."

### The translation

You must know what risks your AI system entails. And document it. And maintain it. Not once — continuously, throughout the entire lifespan of the system.

### The implication for local AI versus cloud AI

With a cloud AI system, the risks are partly dependent on how the provider manages the system. You have limited visibility into model updates, training data changes, or changes in the inference infrastructure.

With local AI: you manage the system completely. You know which model version is running, when it was updated, and what changed. The risk management system is entirely in your own hands.

---

### Art. 10 — Data and data governance

### The literal text

> "High-risk AI systems which make use of techniques involving the training of AI models with data shall be developed on the basis of training, validation and testing data sets that meet the quality criteria referred to in paragraphs 2 to 5."

> "Training, validation and testing data sets shall be relevant, sufficiently representative, and to the best extent possible, free of errors and complete with regard to the intended purpose."

And crucially:

> "The data sets shall be subject to appropriate data governance and management practices, in particular as regards the choice of relevant training data [...], possible biases [...], and the identification of any possible deficiencies or shortcomings in the data."

### The translation

If you use a high-risk AI system, you must be able to demonstrate that the data it was trained on is of good quality, representative, and as free as possible from bias.

### The implication for local AI versus cloud AI

This is the article that makes cloud AI fundamentally problematic for high-risk applications.

If you use ChatGPT for a high-risk application — say, screening job applications — you must be able to demonstrate that the training data of GPT-4 is representative and free from bias. You cannot. OpenAI does not publish that information to the extent Art. 10 requires.

With a local open-weight model that you fine-tune on your own data: you know the training data. You can conduct the bias analysis. You can fulfil Art. 10.

---

### Art. 11 — Technical documentation

### The literal text

> "Before a high-risk AI system is placed on the market or put into service, the provider of that AI system shall draw up technical documentation in accordance with Article 11 and Annex IV."

Annex IV specifies among other things:
- General description of the system
- Description of the components and the development process
- Detailed information about the training data
- Description of the monitoring procedures
- Description of the validation and testing procedures

### The translation

There must be a comprehensive technical file fully documenting the AI system. This file must be available to regulators.

### The implication for local AI versus cloud AI

With cloud AI: you depend on the documentation the provider supplies. If that is incomplete or does not meet Annex IV, you have a compliance problem — even though it is not your fault.

With local AI: you create the documentation. You have full access to all components. You can fulfil Annex IV based on your own knowledge of the system.

---

### Art. 12 — Logging and traceability

### The literal text

> "High-risk AI systems shall technically allow for the automatic recording of events ('logs') over the lifetime of the system."

> "The logging capabilities shall ensure a level of traceability of the AI system's functioning throughout its lifecycle that is appropriate to the intended purpose of the system."

### The translation

A high-risk AI system must keep a record of what it does. Every decision, every output, every interaction — logged, time-stamped, traceable.

If there is a later question about why the system made a particular decision, you must be able to reconstruct it.

### The implication for local AI versus cloud AI

With cloud AI: the logs are at the provider. You can request them, but the provider determines what is logged, how long it is retained, and in what format you receive it.

With local AI: the logs are with you. You manage the log format, the retention period, and the access. You can trace every output to the exact model version, the exact input, and the exact time.

---

### Art. 13 — Transparency and information provision

### The literal text

> "High-risk AI systems shall be designed and developed in such a way that their operation is sufficiently transparent to enable deployers to interpret the system's output and use it appropriately."

### The translation

The deployer must be able to understand and explain the output of the AI system. A black box making decisions nobody can explain — that does not comply.

### The implication for local AI versus cloud AI

Open-weight models are inspectable. You can study the architecture, analyse the attention patterns, and explain why a model arrived at a particular output.

Closed-source cloud AI models are by definition less transparent — the provider does not share the internal workings.

---

### Art. 14 — Human oversight

### The literal text

> "High-risk AI systems shall be designed and developed, including with appropriate human-machine interface tools, in such a way that they can be effectively overseen by natural persons during the period in which the AI system is in use."

And:

> "The natural persons to whom the human oversight task is assigned shall be able to:
> (a) fully understand the capacities and limitations of the high-risk AI system [...];
> (b) monitor the operation of the high-risk AI system, in particular in order to detect and address signs of anomalies, dysfunctions and unexpected performance;
> (c) where appropriate, intervene in the operation of the high-risk AI system or interrupt it through a 'stop' button or a similar procedure."

### The translation

A human must always be able to understand, monitor and stop the AI system.

"Stop button" is literally a requirement. Not metaphorically — there must be a mechanism to stop the system immediately.

The human overseer must also be genuinely able to understand the system. Not just theoretically — in practice.

### The implication for local AI versus cloud AI

With cloud AI, the "stop button" is an API cancellation to an external server. In practice, this means you can stop the system for new inputs — but not running processes on the provider's server.

With local AI: you can literally switch the system off. The stop button is physically present. Human oversight is entirely in your own hands.

---

### Art. 15 — Accuracy, robustness and cybersecurity

### The literal text

> "High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness and cybersecurity, and perform consistently in those respects throughout their lifecycle."

### The translation

The system must work well, withstand errors and attacks, and be secure. And throughout its entire lifespan, not just at launch.

---

## Part 6 — AI literacy (Art. 4)

This article has been in force since 2 February 2025.

### The literal text

> "Providers and deployers of AI systems shall take measures to ensure, to their best extent, a sufficient level of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf, taking into account their technical knowledge, experience, education and training and the context the AI systems are to be used in."

### The translation

Everyone in your organisation who uses AI — or oversees it — must sufficiently understand what AI is, how it works, and what its limitations are.

"Sufficient level" is not defined — it depends on the context and the risk level.

For an employee using ChatGPT for emails: basic knowledge of what AI can and cannot do, and awareness of what you may and may not have AI process.

For a manager responsible for a high-risk AI system: deeper knowledge of the risks, the obligations, and the human oversight requirements.

### The implication for consultancy

This article is the direct entry point for AI literacy workshops and consultancy. The law requires it — but gives you the freedom to determine how.

---

## Part 7 — GPAI models (Art. 51-56)

### The literal text (Art. 51)

> "A provider of a general-purpose AI model [...] shall ensure the performance of the obligations set out in Article 53."

The obligations for GPAI models include:
- Draw up and maintain technical documentation
- Provide information and documentation to downstream providers
- Establish a policy for copyright compliance
- Publish a summary of training data

### The open-source exemption (Art. 53(2))

> "The obligations [...] shall not apply to providers of general-purpose AI models that are released under a free and open-source licence."

Exceptions to the exemption: systemic risk models (more than 10^25 FLOP training compute) and models deployed in high-risk applications.

### The translation

Open-source GPAI models — Llama, Mistral, Gemma, Qwen — are largely exempt from the GPAI obligations.

This is the legal opening that makes local AI possible. You can download an open-source model, run it locally, and do not need to comply with the GPAI obligations that apply to closed-source models such as GPT-4.

**But:** if you deploy that open-source model in a high-risk application, the high-risk obligations of Art. 8-15 do apply. The exemption applies to the model, not to the application.

---

## Part 8 — Rights of affected persons (Art. 86)

### The literal text

> "Any affected person subject to a decision taken by the deployer on the basis of the output of the high-risk AI systems listed in Annex III [...] shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken."

### The translation

If an AI system contributes to a decision that affects you — your job application is rejected, your credit request is denied, your benefit application is processed — you have the right to know how that system influenced the decision.

The organisation must be able to explain it. In plain language. Not "the algorithm decided" — but what the main factors were.

### The implication for local AI versus cloud AI

Open-weight models are interpretable. You can analyse attention patterns, reconstruct the reasoning, and give an honest explanation.

Closed-source cloud models are black boxes. You can explain the output, but the internal reasoning of the model is invisible — even to the provider itself.

---

## Part 9 — Fines (Art. 99)

### The literal text

Art. 99(3):
> "Non-compliance with the prohibition of the AI practices referred to in Article 5 shall be subject to administrative fines of up to EUR 35 000 000 or, if the offender is an undertaking, up to 7% of its total worldwide annual turnover."

Art. 99(4):
> "Non-compliance with any other obligation of this Regulation [...] shall be subject to administrative fines of up to EUR 15 000 000 or, if the offender is an undertaking, up to 3% of its total worldwide annual turnover."

Art. 99(5):
> "The supply of incorrect, incomplete or misleading information to notified bodies and national competent authorities [...] shall be subject to administrative fines of up to EUR 7 500 000 or, if the offender is an undertaking, up to 1% of its total worldwide annual turnover."

### The translation

Three fine categories:

- Violating prohibited practices: up to €35 million or 7% of turnover
- Non-compliance with other obligations: up to €15 million or 3% of turnover
- Providing incorrect information: up to €7.5 million or 1% of turnover

The heaviest fines in the European regulatory landscape. Higher than GDPR (4%), higher than NIS2 (2%), higher than DORA (2%).

---

## Part 10 — The AI Act and local AI: the full picture

Now everything together.

### Why local AI is the path of least resistance

**Art. 10 data governance:** with local AI you know the data. With cloud AI you do not.

**Art. 11 technical documentation:** with local AI you can fully document the system. With cloud AI you depend on what the provider shares.

**Art. 12 logging:** with local AI you have the logs. With cloud AI you have them on request, in the provider's format.

**Art. 13 transparency:** open-weight models are inspectable. Closed-source models are black boxes.

**Art. 14 human oversight:** with local AI the stop button is literally in your hands. With cloud AI it is an API call to an external server.

**Art. 86 right to explanation:** with local open-weight models you can reconstruct the reasoning. With closed-source cloud models you cannot.

### The open-source key

The combination of two elements makes local AI legally attractive:

1. **Open-source GPAI exemption (Art. 53(2)):** open-weight models are exempt from the heavy GPAI obligations.

2. **High-risk obligations still apply:** but those obligations are much easier to fulfil with local deployment.

The result: local AI with open-weight models is both technically feasible and legally the most manageable route for high-risk applications.

### The summary in one table

| Requirement | Cloud AI | Local AI |
|---|---|---|
| Data governance (Art. 10) | Dependent on provider | Fully in own hands |
| Technical documentation (Art. 11) | Partial, provider-dependent | Fully self-produced |
| Logging (Art. 12) | At provider, on request | With you, fully manageable |
| Transparency (Art. 13) | Limited for closed-source | Full for open-weight |
| Stop button (Art. 14) | API cancellation | Physically present |
| Right to explanation (Art. 86) | Limited | Full |
| Open-source exemption | Not applicable | Applicable |

---

## Part 11 — Practical scenarios

### Scenario 1: Accountancy firm with AI-driven VAT analysis

An accountant uses an AI system to analyse VAT returns and detect anomalies.

**Does this fall under high-risk?**
Possibly — if the system contributes to decisions about clients' creditworthiness (Annex III, point 5b) or influences tax filings with essential financial consequences.

**With cloud AI:** technical documentation about training data is not available. Logging is limited. The right to explanation for clients is difficult to fulfil.

**With local AI:** fully documented system, own logs, open-weight model whose workings can be explained to clients and regulators.

---

### Scenario 2: Therapist with AI-driven session note processing

A therapist uses an AI to structure session notes and draw up treatment plans.

**Does this fall under high-risk?**
Health data is Art. 9 GDPR data. If the AI system contributes to treatment decisions, it may be high-risk (healthcare, Annex I sector). If it only summarises without a decision component, possibly not.

**With cloud AI:** session notes — Art. 9 GDPR data — go to an external server. GDPR violation + potential AI Act violation.

**With local AI:** data does not leave the practice. No GDPR problem. If it is high-risk: all obligations are fulfillable because the system is entirely under own management.

---

### Scenario 3: HR department with AI for CV screening

A company uses AI to screen applications and rank candidates.

**Does this fall under high-risk?**
Yes. Annex III, point 4(a) is explicit: AI for screening or filtering applications is high-risk.

**With cloud AI:** all obligations of Art. 8-15 apply, but are difficult to fulfil because the training data and model are not fully accessible.

**With local AI:** all obligations are fulfillable. And: you can give a fair explanation to rejected candidates (Art. 86).

---

## Glossary

**AI system** — a machine-based system that processes input to generate output (predictions, recommendations, decisions) with a degree of autonomy.

**Provider** — the one who develops and brings an AI system to market. OpenAI for ChatGPT, Meta for Llama.

**Deployer** — the one who deploys an AI system for professional purposes. The accountant using ChatGPT. The hospital deploying a diagnostic AI.

**GPAI model** — a large language model that can be deployed for general purposes. ChatGPT, Gemini, Claude, Llama, Mistral.

**High-risk AI system** — an AI system deployed in a context with significant risks to people's rights and safety. Defined in Annex III.

**Conformity assessment** — the process by which it is demonstrated that a high-risk AI system meets all requirements of the AI Act.

**Open-source exemption** — the provision (Art. 53(2)) that providers of open-source GPAI models are largely exempt from GPAI obligations.

**AI literacy** — the level of understanding of AI technology, capabilities and risks required of employees who use or manage AI. Mandatory to promote under Art. 4.

**Stop button** — the mechanism by which a human overseer can immediately interrupt or stop a high-risk AI system (Art. 14).

**Logging** — the automatic recording of the operation of an AI system, including inputs, outputs and decisions, for traceability (Art. 12).

**Human oversight** — the requirement that a high-risk AI system can be effectively monitored by a human who understands the system and can intervene (Art. 14).

**Systemic risk** — the risk that a GPAI model with more than 10^25 FLOP training compute has systemic consequences for society. Models with systemic risk have heavier obligations.

**AI Office** — the European office supervising GPAI models and coordinating the implementation of the AI Act. Established in 2024 within the European Commission.

**National supervisory authority** — per member state designated authority for AI Act supervision. In Belgium designated but not yet fully operational in March 2026. In the Netherlands: role distributed across multiple regulators.

---

## Checklist for a client conversation

**Initial screening:**
- [ ] Does your organisation use AI systems for professional purposes?
- [ ] In what context? (HR, finance, healthcare, education, government?)
- [ ] Does the AI system make decisions affecting people, or does it only support?

**If high-risk is possible:**
- [ ] Do you have a risk management system documented? (Art. 9)
- [ ] Do you know what data the system uses and how it is composed? (Art. 10)
- [ ] Do you have technical documentation of the system? (Art. 11)
- [ ] Are the system's actions logged and traceable? (Art. 12)
- [ ] Can your employees explain the output of the system? (Art. 13)
- [ ] Is a human overseer designated? Can they stop the system? (Art. 14)
- [ ] Can you explain to affected persons how the system influenced their case? (Art. 86)

**AI literacy (for everyone):**
- [ ] Do your employees know what AI can and cannot do?
- [ ] Do they know which data they may not enter into an AI system?
- [ ] Is there a policy for responsible AI use?

---

_Previous document: 04-data-act.md_
_This is the last regulatory document in the series._
_Next step: sector dossiers per target audience_
_Last updated: March 2026_
