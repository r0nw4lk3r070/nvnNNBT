# 01 — GDPR
### LocAI Library · Deep Dive
_Regulation (EU) 2016/679 · In force 25 May 2018_
_Version 0.1 · March 2026_

---

## What this document is

The GDPR is 99 articles long and spans hundreds of recitals. This document is not a complete legal analysis — it is a working document. We take the articles most relevant to us, cite the literal text, translate it into plain language, and draw the implications for local AI versus cloud AI.

Everything here is based on the official text of the regulation as published in the Official Journal of the European Union.

---

## The core in one sentence

The GDPR gives European citizens control over their personal data and imposes extensive obligations on organisations that process that data — with real penalties for non-compliance.

---

## Part 1 — The Basic Principles (Art. 5)

### The literal text

Article 5(1) states that personal data shall:

> a) "be processed lawfully, fairly and in a transparent manner in relation to the data subject ('lawfulness, fairness and transparency')"

> b) "be collected for specified, explicit and legitimate purposes and not further processed in a manner that is incompatible with those purposes ('purpose limitation')"

> c) "be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed ('data minimisation')"

> d) "be accurate and, where necessary, kept up to date ('accuracy')"

> e) "be kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed ('storage limitation')"

> f) "be processed in a manner that ensures appropriate security of the personal data, including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organisational measures ('integrity and confidentiality')"

Article 5(2):

> "The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1 ('accountability')."

### The translation

Six principles that every organisation must comply with when processing personal data.

**Lawfulness, fairness and transparency:** you may only process personal data if you have a legal basis for doing so, you do it in a fair manner, and you are open about it.

**Purpose limitation:** you collect data for a specific purpose. You may not simply use that data for something else. If you collect an email address to send an invoice, you may not use it for a newsletter — unless the person has given separate consent.

**Data minimisation:** collect only what you genuinely need. Do not fill in extra fields "just in case." If name and email address are sufficient, do not ask for a date of birth.

**Accuracy:** keep data current. Outdated information can cause harm.

**Storage limitation:** do not retain data longer than necessary. If a customer has not purchased anything for three years, there is no point retaining their personal data indefinitely.

**Integrity and confidentiality:** secure the data you store. Both technically (encryption, access control) and organisationally (who has access, how are staff trained).

**Accountability:** you cannot simply say you are compliant — you must also be able to demonstrate it. Documentation, processing registers, policies.

### The implication for local AI versus cloud AI

With cloud AI you send data to an external server. You have no control over what happens to it afterwards. Is it used for model training? Is it stored? For how long? Can an American court demand access to it?

With local AI the data remains on your own device or server. You decide what happens to it. You can fulfil the accountability obligation — because you are the only data controller.

The principle of data minimisation takes on a new dimension with AI: if you have a language model summarise a patient record, you are potentially sending the entire record to the processor. With local AI, that "processor" is yourself. With cloud AI, it is a third party.

---

## Part 2 — Legal Basis for Processing (Art. 6)

### The literal text

> "Processing shall be lawful only if and to the extent that at least one of the following applies:
> a) the data subject has given consent to the processing of his or her personal data for one or more specific purposes;
> b) processing is necessary for the performance of a contract to which the data subject is party;
> c) processing is necessary for compliance with a legal obligation to which the controller is subject;
> d) processing is necessary in order to protect the vital interests of the data subject or of another natural person;
> e) processing is necessary for the performance of a task carried out in the public interest;
> f) processing is necessary for the purposes of the legitimate interests pursued by the controller or by a third party."

### The translation

You may only process personal data if you have one of these six legal bases. No basis = no processing. Full stop.

The most commonly used bases in practice:

**Consent (a):** the person has explicitly said yes. Note: consent must be freely given, specific, informed and unambiguous. A pre-ticked box is not consent. "By using our service you agree" is not consent.

**Contract (b):** you process data because it is necessary to perform a contract. An accountant processes financial data of a client because that is necessary for the bookkeeping. That is basis b.

**Legitimate interests (f):** the most flexible basis, and therefore the most misused. You have a legitimate interest, and that outweighs the privacy interests of the data subject. Requires a balancing test — and that test must be documented.

### The implication for local AI versus cloud AI

If you process personal data via a cloud AI service, you technically need a data processing agreement with that service (see Art. 28). But the legal basis for the processing must be your own.

Problem: many cloud AI services process data in ways that fall outside the original legal basis. They use conversations for model improvement, for analytical purposes, or retain them longer than necessary. That is a violation of purpose limitation (Art. 5b) — even if you yourself have a valid basis for the initial processing.

With local AI there is no third party doing anything with the data outside your legal basis.

---

## Part 3 — Special Categories (Art. 9)

### The literal text

> "Processing of personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, and the processing of genetic data, biometric data for the purpose of uniquely identifying a natural person, data concerning health or data concerning a natural person's sex life or sexual orientation shall be prohibited."

Followed by exceptions — but these are limited and specific.

### The translation

Some data is so sensitive that the GDPR places an extra layer of protection on it. These "special categories" are in principle prohibited from processing, unless you can demonstrate an explicit exception.

The categories most frequently encountered in practice:

**Health data:** everything that says something about a person's physical or mental health. Medical records, diagnoses, medication, but also absence records and session notes of a therapist.

**Biometric data:** fingerprints, facial recognition, voice recognition — if used to uniquely identify a person.

**Genetic data:** DNA information.

**Racial or ethnic origin, political opinions, religious beliefs, sexual orientation:** categories deserving extra protection due to the risk of discrimination.

The exceptions relevant in practice:
- Explicit consent of the data subject
- Processing necessary for healthcare by a health professional subject to professional secrecy
- Processing necessary to protect vital interests
- Processing for archiving in the public interest or scientific research

### The implication for local AI versus cloud AI

This is the article that makes the difference for sectors such as healthcare, social work and youth care.

A therapist who has session notes processed by cloud AI is processing special category data (health, possibly also sexual orientation or religious beliefs) via a third party. The exception for healthcare applies to the therapist themselves — not automatically to the cloud provider running the AI.

A youth care organisation processing client data works with data of minors (extra protection via Recital 38) that also contains health and behavioural information. Art. 9 data on an American cloud server is a compliance nightmare.

With local AI: the data does not leave the organisation. The exception for health professionals subject to professional secrecy applies to the organisation itself. There is no third party that needs its own legal basis.

---

## Part 4 — Rights of Data Subjects (Art. 12-22)

### The literal text (summary per article)

**Art. 13-14 — Information obligation:** data subjects must be informed about who processes their data, why, for how long, and what their rights are.

**Art. 15 — Right of access:** data subjects have the right to know which personal data about them is being processed.

**Art. 16 — Right to rectification:** inaccurate data must be correctable.

**Art. 17 — Right to erasure ("right to be forgotten"):**
> "The data subject shall have the right to obtain from the controller the erasure of personal data concerning him or her without undue delay."

**Art. 18 — Right to restriction of processing:** in certain situations a data subject can request that processing be temporarily suspended.

**Art. 20 — Right to data portability:** data subjects have the right to receive their data in a machine-readable format and transfer it to another service.

**Art. 21 — Right to object:** data subjects can object to processing based on legitimate interests.

**Art. 22 — Automated decision-making:**
> "The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her."

### The translation

**Right to erasure:** if someone requests deletion of their data, you must be able to do it. And demonstrate that you did.

**Right to data portability:** a patient may request their file in a format that another healthcare provider can read. A customer may export their transaction history.

**Automated decision-making:** AI may not make decisions affecting someone's life without human intervention. An AI system assessing credit applications, screening job applications, or making benefit decisions — that always requires a human check.

### The implication for local AI versus cloud AI

The right to erasure is technically feasible with local AI: you know exactly which database contains the data, you can delete it, and you can demonstrate it.

With cloud AI this is structurally more complex: the data may be cached, used for model improvement, stored in backups you do not manage. Even if the provider promises deletion, you cannot verify it.

Art. 22 on automated decision-making is crucial for the AI Act — it is the GDPR article most directly connected to the AI Act's requirement for human oversight (Art. 14 AI Act). The two laws reinforce each other here: GDPR prohibits fully automated decisions with legal effects, the AI Act mandates human oversight for high-risk AI.

---

## Part 5 — Data Processing Agreement (Art. 28)

### The literal text

> "Where processing is to be carried out on behalf of a controller, the controller shall use only processors providing sufficient guarantees to implement appropriate technical and organisational measures in such a manner that processing will meet the requirements of this Regulation and ensure the protection of the rights of the data subject."

And:

> "The processor shall process the personal data only on documented instructions from the controller."

### The translation

If you engage a third party to process personal data — accounting software, an HR system, a cloud AI service — you must conclude a Data Processing Agreement (DPA).

That agreement must establish:
- What the processor may do with the data
- That the processor only processes data on your instructions
- What security measures the processor takes
- That the processor informs you in the event of a data breach
- That the processor deletes or returns the data when the partnership ends

### The implication for local AI versus cloud AI

Every cloud AI service is a processor. You need a DPA. It must comply with Art. 28. And you must be able to demonstrate that the processor is honouring the commitments.

In practice: Microsoft, Google and OpenAI offer standard DPAs. These are written by their lawyers, in their favour, with limited negotiating room for a small organisation.

Two problems:
1. The DPA protects you legally but guarantees nothing technically. You cannot verify whether the processor is complying with the agreements.
2. If the processor engages sub-processors — and they all do — you have a chain of processing relationships you cannot oversee.

With local AI: no processor. No DPA required. The data is processed by the organisation itself, on its own hardware, under its own control.

---

## Part 6 — Data Breaches (Art. 33-34)

### The literal text

Art. 33(1):
> "In the case of a personal data breach, the controller shall without undue delay and, where feasible, not later than 72 hours after having become aware of it, notify the personal data breach to the supervisory authority."

Art. 34(1):
> "When the personal data breach is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall communicate the personal data breach to the data subject without undue delay."

### The translation

If there is a data breach — data stolen, lost, or inadvertently made public — you must report it to the supervisory authority within 72 hours (in Belgium: the GBA; in the Netherlands: the AP).

If the breach poses a high risk to data subjects — think medical data, financial data, or data of minors — you must also inform the data subjects themselves.

The 72-hour clock starts running when you become aware that there is a breach. Not when you have fully investigated it. Not when your lawyer is back from holiday.

### The implication for local AI versus cloud AI

With cloud AI: a data breach at the provider is also your data breach. You are the data controller — the notification obligation rests with you, not the provider. But you depend on the provider to inform you in a timely manner. And "timely" in a cloud environment with millions of customers can mean you as a small organisation are at the back of the queue.

With local AI: you manage the data yourself. A breach is immediately visible in your own systems. You do not depend on the communication speed of an external provider.

---

## Part 7 — Privacy by Design and Privacy by Default (Art. 25)

### The literal text

> "Taking into account the state of the art, the cost of implementation and the nature, scope, context and purposes of processing as well as the risks of varying likelihood and severity for rights and freedoms of natural persons posed by the processing, the controller shall, both at the time of the determination of the means for processing and at the time of the processing itself, implement appropriate technical and organisational measures [...] to implement data-protection principles [...] in an effective manner."

And:

> "The controller shall implement appropriate technical and organisational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed."

### The translation

**Privacy by design:** build privacy in from the start. Not as a layer you add on afterwards. When designing a system, ask yourself: how do we process as little data as possible, as securely as possible, in a way that respects the rights of data subjects?

**Privacy by default:** the default settings of your system must always be the most privacy-friendly option. If a user configures nothing, they share as little as possible. Not as much as possible.

### The implication for local AI versus cloud AI

Privacy by design is the architectural principle that local AI embodies.

A system that processes data locally, without external API calls, without data transfers to third parties, without logging on foreign servers — that is privacy by design in its most direct form.

A system that by default sends all data to a cloud unless the user actively opts out — that is the opposite of privacy by default.

SPOREN is built on this principle: no cloud, no external processing, data remains on the organisation's own server. That is not a marketing choice — it is an architectural choice that directly flows from Art. 25.

---

## Part 8 — Penalties (Art. 83)

### The literal text

Art. 83(4):
> "Infringements of the following provisions shall [...] be subject to administrative fines up to 10,000,000 EUR, or in the case of an undertaking, up to 2% of the total worldwide annual turnover."

Art. 83(5):
> "Infringements of the following provisions shall [...] be subject to administrative fines up to 20,000,000 EUR, or in the case of an undertaking, up to 4% of the total worldwide annual turnover."

The heaviest fines (4%) apply to violations of: the basic principles (Art. 5), legal bases for processing (Art. 6), special categories (Art. 9), and rights of data subjects (Art. 12-22).

### The translation

There are two penalty categories. The lighter: up to €10 million or 2% of turnover. The heavier: up to €20 million or 4% of turnover.

For an SME of 10 people with €500,000 turnover, 4% = €20,000. That sounds less dramatic than the headline figures about million-euro fines for big tech companies. But it is still an existential amount for a small practice.

And the financial fine is not the only risk. Reputational damage is greater for many small organisations: a therapist who must inform their patients about a data breach loses trust they can never recover.

### Documented fines in Europe (selection)

- **Meta (Ireland, 2023):** €1.2 billion for transferring personal data to the US without adequate protection. Largest GDPR fine ever at that time.
- **Google (France, 2022):** €150 million for cookie consent violation.
- **H&M (Germany, 2020):** €35 million for unlawful surveillance of employees.
- **Clearview AI (multiple countries, 2022):** fines in Italy, Greece, France for illegal processing of biometric data.

Pattern: large tech companies receive the large fines. SMEs receive smaller fines — but they exist, including in Belgium and the Netherlands.

---

## Part 9 — The Supervisory Authorities

### Belgium — Data Protection Authority (GBA)

Website: gegevensbeschermingsautoriteit.be
Data breach notifications: via the online notification portal on the website
Complaints: also via the website

The GBA is relatively active compared to some other European supervisory authorities. It publishes recommendations, handles complaints, and conducts its own investigations.

### Netherlands — Dutch Data Protection Authority (AP)

Website: autoriteitpersoonsgegevens.nl
Similar structure to the GBA. Known for proactive communication on new developments, including AI.

### The one-stop-shop principle

If a company is active in multiple EU member states, it only needs to communicate with one supervisory authority — the supervisory authority in the country of its main establishment. For large tech companies this is often Ireland (where many American companies have their European headquarters).

---

## Part 10 — GDPR and AI: the Connection

This is the link to the AI Act.

The GDPR regulates how personal data may be processed. The AI Act regulates how intelligent systems that process personal data must be designed and deployed.

They overlap at multiple points:

| GDPR | AI Act | Common principle |
|---|---|---|
| Art. 5 — Data minimisation | Art. 10 — Data governance | Only use the data that is needed |
| Art. 22 — No fully automated decision-making | Art. 14 — Human oversight | Humans remain in the loop |
| Art. 25 — Privacy by design | Art. 9 — Risk management | Build it right from the start |
| Art. 17 — Right to erasure | Art. 12 — Logging and traceability | Data lifecycle management |
| Art. 83 — Fines | Art. 99 — Fines | Real consequences |

The AI Act explicitly references GDPR. An AI system that complies with the AI Act but violates the GDPR is not compliant. Both laws must be complied with together.

**The practical consequence:**
From December 2027 (expected new deadline) onwards, organisations deploying high-risk AI have a dual compliance burden: AI Act for the system, GDPR for the data. The easiest way to combine both: local processing, where the organisation itself has full control over both the system and the data.

---

## Glossary

**Controller** — the organisation or person who determines the purpose and means of personal data processing. You as an entrepreneur processing customer data. You are responsible — even if you engage a processor.

**Processor** — a party that processes personal data on behalf of the controller. A cloud AI service is a processor. An accounting package is a processor. You always need a data processing agreement.

**Data subject** — the natural person whose personal data is being processed. Your customer, your patient, your employee.

**Personal data** — any information that directly or indirectly identifies an identifiable person. Name, email address, IP address, location data, cookie IDs — all personal data.

**Special categories** — extra sensitive personal data requiring extra protection (see Art. 9): health, genetic, biometric, race, political, religion, trade union, sexuality.

**Data Processing Agreement (DPA)** — a contract between controller and processor that establishes how the processor may use the data. Mandatory under Art. 28.

**Legitimate interests** — a legal basis for processing where you argue that your legitimate interest outweighs the privacy interests of the data subject. Requires a documented balancing test.

**Consent** — a legal basis for processing where the data subject has freely, specifically, informedly and unambiguously said yes. Must be as easy to withdraw as to give.

**Data breach** — a security incident leading to accidental or unlawful destruction, loss, alteration, unauthorised disclosure of or access to personal data. Notification obligation within 72 hours to the supervisory authority.

**Privacy by design** — the principle that privacy protection is built into the design of a system from the outset, not added afterwards.

**Privacy by default** — the principle that the default settings are always the most privacy-friendly option.

**Profiling** — any automated processing of personal data used to evaluate certain aspects of a person, such as behaviour, preferences or reliability.

**DPO (Data Protection Officer)** — a mandatory role for certain organisations (public authorities, large-scale processing of special categories, large-scale monitoring). The DPO advises on GDPR compliance and is the point of contact for the supervisory authority.

---

## Checklist for SMEs

Use this as a quick audit for a client conversation.

- [ ] Do you have a register of processing activities? (Art. 30)
- [ ] Do you have a valid legal basis for each processing activity? (Art. 6)
- [ ] Do you have data processing agreements with all third parties? (Art. 28)
- [ ] Do you inform data subjects about their rights? (Art. 13-14)
- [ ] Can you respond to an access request within 30 days? (Art. 15)
- [ ] Can you delete data when someone requests it? (Art. 17)
- [ ] Do you know what to do in the event of a data breach? (Art. 33-34)
- [ ] Is your system built with privacy by design? (Art. 25)
- [ ] Do you process special categories — and do you have an explicit legal basis for that? (Art. 9)
- [ ] Do you transfer data outside the EU — and do you have adequate safeguards for that? (Art. 44-49)

---

_Previous document: 00-history.md_
_Next document: 02-nis2.md_
_Last updated: March 2026_
