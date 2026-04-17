# S02 — Therapists & Psychologists
### LocAI Library · Sector Dossier
_Version 0.1 · 25 March 2026_

---

## Who they are

Therapists and psychologists work with people at their most vulnerable moments. They hear things no one else hears. They keep secrets that would tear families apart. They know the deepest fears, the darkest thoughts, the most intimate details of their clients' lives.

That trust is not merely the foundation of their profession — it is the therapeutic effectiveness itself. Without trust, therapy does not work.

**Typical profile:**
- Solo practice or small group practice of 2–5 therapists
- 20–50 active clients per therapist
- Sessions of 50–90 minutes, 1–2 times per week per client
- Working under professional duty of confidentiality and ethical codes of professional associations
- High administrative burden: session notes, treatment plans, progress reports, correspondence with other care providers

**Specific professional groups:**
- Clinical psychologists (recognised by VVKP in Belgium, NIP in the Netherlands)
- Psychotherapists (recognised profession in Belgium, BIG Act in the Netherlands)
- Counsellors and coaches (less regulated, but professional duty of confidentiality applies here too)
- Psychiatrists (medical specialists — additional mental health care regulations)

---

## What data they process

This is the most sensitive category of data that exists — special categories under GDPR Art. 9 [1].

**Per client file:**
- Session notes — detailed records of what was discussed
- Treatment plans — diagnosis, objectives, interventions
- Progress reports — how the client is doing
- Correspondence with GP, psychiatrist, school, or employer
- Test results and assessments — intelligence tests, personality tests
- Crisis situations — suicidal thoughts, self-harm, psychoses
- Medication information
- Family history and trauma history

**What makes this data special:**
Session notes are not neutral medical data. They contain the inner world of a person — thoughts, feelings, memories that have often never been spoken aloud before. They may contain information about sexual orientation, religious doubts, political views, illegal activities, relationship problems, financial stress.

A leaked session file can destroy someone's life. Career, relationships, reputation — everything is at stake.

---

## Which laws apply

### GDPR Art. 9 — Special categories, additional protection

Health data is a special category. That means:
- Processing is in principle prohibited
- Exception: necessary for healthcare by a health professional bound by professional secrecy / duty of confidentiality (Art. 9(2)(h))
- That exception applies to the therapist themselves — not automatically to every tool the therapist uses

**The critical question:** does a cloud AI tool that processes session notes fall under the healthcare exception?

Legal answer: no. The exception applies to the health professional. An external AI service is not a health professional. The transfer of health data to a cloud AI requires an explicit legal basis for processing — and client consent is problematic in a therapeutic relationship (see below).

### GDPR — Consent in a therapeutic relationship

Art. 7(4) provides that consent is not freely given where there is a clear imbalance of power between the controller and the data subject.

A client seeking help from their therapist is in a dependent position. If the therapist says "I use AI for my notes, do you agree?" — is that consent truly free? Legally, this is a grey area. Ethically, it is more problematic.

### GDPR — Minors (Recital 38)

Many therapists work with children and young people. GDPR gives minors additional protection. Consent for the processing of data relating to minors must be given by parents or legal representatives — and requires extra care.

### Professional secrecy / duty of confidentiality — Law and ethics

In Belgium: the professional duty of confidentiality for psychologists and psychotherapists is enshrined in Art. 458 of the Criminal Code [2]. Breach of professional secrecy is a criminal offence.

In the Netherlands: the professional duty of confidentiality for BIG-registered healthcare providers is laid down in the BIG Act [3] and the Civil Code.

**The question:** does the use of a cloud AI tool constitute a breach of professional secrecy?

Legal assessment: it is at the very least a serious risk. Transferring session data to an external server — even with a DPA — is a transfer to a third party. The client has not been made aware of this, let alone given consent.

### AI Act — High risk

If an AI system contributes to decisions about the health or treatment of a patient, it is high-risk under the AI Act (Annex III — healthcare sector, critical infrastructure).

**Nuance:** purely administrative AI (summarising notes, managing schedules) is probably not high-risk. AI that makes treatment suggestions or categorises clients — that is high-risk.

**AI literacy (Art. 4):** the obligation for AI literacy also applies to therapists who use AI for administration.

### Mental health care-specific regulations

In the Netherlands, additional rules apply to mental health care institutions via the Medical Treatment Contracts Act (WGBO) [4] and the Quality Standard ROM. Record-keeping obligations, retention periods, and patient rights are extensively regulated.

In Belgium, the law on patients' rights and the accreditation standards for psychological practices apply.

---

## Concrete use cases for AI

### 1. Structuring session notes

**What it is:** the therapist dictates or types raw notes after a session. AI structures these into the correct format — SOAP note (Subjective, Objective, Assessment, Plan) or DAP format (Data, Assessment, Plan).

**Time saving:** a therapist with 30 sessions per week spends an average of 10–15 minutes per session on notes. That is 5–7.5 hours of administration per week. AI can halve this.

**The risk with cloud AI:** the raw session notes — the most sensitive data imaginable — go to an external server. Art. 9 GDPR. Professional secrecy. Criminal offence.

**With local AI:** notes are processed on the therapist's own laptop or office server. No data leaves the practice. The client does not even need to know.

---

### 2. Drawing up a treatment plan

**What it is:** generating a treatment plan as a first draft based on the intake and initial sessions, which the therapist then adjusts and finalises.

**Time saving:** drawing up a treatment plan takes 30–60 minutes. AI generates a draft in minutes.

**The risk with cloud AI:** the diagnosis, the problem formulation, the therapeutic objectives — everything goes to an external server.

**With local AI:** treatment plan generation on the practice's own hardware. Nothing leaves the practice.

---

### 3. Progress reporting

**What it is:** periodic reports for the GP, school, employer, or insurer. AI generates the first draft based on session notes.

**Time saving:** significant — especially for reports that go to third parties and must be written formally.

**The risk with cloud AI:** progress reports contain a summary of the treatment trajectory — all sensitive information compressed into one document, sent to an external server.

**With local AI:** report generation locally. Internal document, internal processing.

---

### 4. Client communication

**What it is:** AI assists with drafting letters and emails to clients — appointment confirmations, reminders, informational texts about the therapy process.

**Time saving:** limited per message, but cumulatively significant.

**The risk with cloud AI:** the name and contact details of clients go to an external server — although this is less sensitive than session data.

**With local AI:** communication is also processed locally.

---

### 5. Internal knowledge base

**What it is:** a local AI that helps the therapist look up therapeutic techniques, DSM criteria, medication information, or professional literature.

**Time saving:** less searching, faster answers to clinical questions.

**The risk with cloud AI:** if the therapist provides context about a client when asking a question ("my client has symptoms X and Y..."), that context is confidential.

**With local AI:** knowledge base consultation entirely internal. Even informal clinical questions can be asked without leaking data.

---

## The concrete risk with cloud AI

**The scenario:**
A therapist uses a speech-to-text tool followed by ChatGPT to structure their session notes. After each session, they dictate: "Today I spoke with [name], 34 years old, about his anxiety around his marriage, his sexual problems, and his thoughts about self-harm..."

**What happens legally:**
1. The name, age, and most intimate details of the client — Art. 9 GDPR special category data — are transferred to OpenAI.
2. There is no valid legal basis for this transfer.
3. Professional secrecy has been breached — a criminal offence under Art. 458 of the Criminal Code [2] (Belgium).
4. The client has never given consent.
5. If the client ever discovers that their session notes are stored on American servers, the trust — and the therapeutic relationship — is irreparably damaged.

**What else can happen:**
- A data breach at OpenAI in which clients' session data leaks
- A complaint to VVKP or NIP that can lead to suspension
- Criminal prosecution for breach of professional secrecy
- A GDPR complaint to the Belgian DPA with fines

---

## What local AI solves

**The architectural solution:**
A local server or powerful laptop. Ollama with an open-weight model. A simple interface for note input. All processing internal.

**Optional: whisper.cpp for speech-to-text:**
whisper.cpp is an open-source speech-to-text model that runs locally. The therapist dictates — the text is generated locally. No audio goes to external servers.

**What changes legally:**
- No transfer of Art. 9 data to a third party
- Professional secrecy intact
- GDPR compliant by architecture
- No data processing agreement required for the AI component

**What changes practically:**
- Structuring notes in seconds instead of minutes
- Treatment plans as a draft in minutes
- More time for clients, less time for administration
- No concern that session data is stored somewhere on a server

---

## The core message for the first conversation

Start with the therapeutic relationship — not with technology.

> "Your clients tell you things they tell no one else. That trust is the foundation of your work. If you are using AI today for your notes or treatment plans, can you be certain that data does not leave your practice?"

Follow-up:

> "Local AI processes everything on your own device. Your clients' session notes do not leave your practice. You have the same functionality — structuring notes, drawing up treatment plans, writing reports — but without the legal and ethical risk."

---

## Questions they ask and how to respond

**"But I use anonymised notes?"**

Anonymisation is harder than it appears. A combination of age, profession, and complaints/symptoms can make a person identifiable. True anonymisation requires the systematic removal of all identifying elements — no one does that manually for every note. And if you later link the anonymous note back to the file, it is no longer anonymous anyway.

**"My clients will give consent if I ask them?"**

Consent in a therapeutic relationship is legally problematic — there is an imbalance of power. And ethically: do you want to ask your clients whether their most intimate thoughts may be stored on American servers? Local AI eliminates that question entirely.

**"Isn't it cumbersome to install locally?"**

One-time installation, after which it works like any other tool. The interface resembles ChatGPT. The only difference is that everything stays internal.

**"What if I only have one laptop?"**

A modern laptop with an NPU chip can run smaller models (7B–13B) locally — sufficient for structuring notes and drawing up treatment plans. For heavier tasks, a mini-server at the office is the solution.

**"My professional association says nothing about AI?"**

True — VVKP [5] and NIP have not yet issued specific AI guidelines. But the duty of confidentiality and the GDPR rules for special categories already apply. You are personally responsible for the choices you make. Local AI is the most conservative and defensible choice.

**"What does it cost?"**

Hardware: €2,300–€3,500 for a mini-PC with sufficient capacity. Setup and configuration once. After that, no monthly costs for the AI component itself. Compare that with €20–50 per month for a cloud AI subscription — plus the legal risk you cannot quantify.

---

## Special attention: crisis and suicidality

This is the most sensitive topic in therapeutic practice.

Session notes about suicidal thoughts, self-harm, or psychoses are the most protected data imaginable. If this information leaks, it can destroy lives — career, relationships, even insurance-related consequences.

A therapist who processes this type of notes through a cloud AI is taking a risk that no client would accept if they knew.

With local AI: even crisis notes are processed internally. The most sensitive information about the most vulnerable people remains where it belongs — in the practice, under professional secrecy / duty of confidentiality.

---

## Belgian and Dutch context

### Belgium

**VVKP** — Flemish Association of Clinical Psychologists. Professional association and ethical code.

**BFP-FBP** — Professional Federation for Psychologists. Umbrella federation.

**Accreditation:** clinical psychologist is a protected profession in Belgium (Act of 4 April 2014). Breach of professional rules can lead to suspension or removal from the register.

**Mental health care funding:** recognised psychologists work within the convention with health insurance (NIHDI). Files must comply with NIHDI requirements.

### Netherlands

**NIP** — Dutch Institute of Psychologists. Professional association.

**BIG-register** [3] — Professions in Individual Healthcare. Psychologists and psychotherapists are BIG-registered. Disciplinary proceedings via the Regional Disciplinary Board for Healthcare.

**WGBO** [4] — Medical Treatment Contracts Act. Regulates record-keeping obligations, retention periods (20 years), and patient rights.

**Care domain and EHR:** many therapists work with an Electronic Health Record (EHR). The integration between local AI and existing EHR software is a technical point of attention.

---

## Sector figures (reference)

- Number of recognised clinical psychologists in Belgium: approximately 10,000
- Number of BIG-registered psychologists in the Netherlands: approximately 28,000
- Number of psychotherapists in Belgium (recognised): approximately 3,500
- Waiting times in mental health care: average 3–6 months in the Netherlands, comparable in Belgium
- Administrative burden: therapists spend an average of 20–30% of their working time on administration

The high administrative burden combined with long waiting times creates a perfect context for AI adoption. The question is not whether therapists will use AI — the question is which AI.

---

## References

1. **GDPR — Regulation (EU) 2016/679, Art. 9(1) — Special categories**  
   EUR-Lex, Official Journal of the European Union  
   https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng

2. **Art. 458 Belgian Criminal Code — Professional secrecy**  
   Belgian Official Gazette / Ejustice  
   https://www.ejustice.just.fgov.be/eli/wet/1867/06/08/1867060850/justel

3. **BIG Act — Act on professions in individual healthcare**  
   wetten.overheid.nl  
   https://wetten.overheid.nl/BWBR0006251/

4. **WGBO — Medical Treatment Contracts Act, Art. 7:457 Civil Code**  
   wetten.overheid.nl  
   https://wetten.overheid.nl/BWBR0005290/

5. **VVKP — Professional ethics code for clinical psychologists**  
   Flemish Association of Clinical Psychologists  
   https://vvkp.be/klinisch-psychologen

---

_Part of: LocAI Library · Sector Dossiers_
_Previous: S01 — Accountants & Bookkeepers_
_Next: S03 — Lawyers & Legal Advisors_
_Last updated: 25 March 2026_
