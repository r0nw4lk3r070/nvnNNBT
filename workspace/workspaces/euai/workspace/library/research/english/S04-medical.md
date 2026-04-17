# S04 — Medical & Dental Practices
### LocAI Library · Sector Dossier
_Version 0.1 · 25 March 2026_

---

## Who they are

Doctors and dentists stand daily at the beginning of the most personal thing that exists: the health of their patients. They know bodies and lives like nobody else. They hear complaints that people dare not voice at home. They see vulnerabilities hidden from family and friends.

The trust patients place in them is the foundation of medicine itself — and that trust demands absolute discretion.

**Typical profile:**
- General practitioner (GP) practice of 1-5 doctors
- Dental practice of 1-4 dentists
- 1,500-2,500 active patients per general practitioner (GP)
- High administrative burden: consultation reports, medical certificates, referrals, correspondence with specialists
- Working with an Electronic Medical Record (EMR) — mandatory in Belgium and the Netherlands

**Specific professional groups:**
- General practitioners (GPs) — broad patient base, gatekeeper role
- Dentists — combination of medical and technical work
- Specialists — deeper expertise, often hospital-based but also independent
- Physiotherapists — treatment plans, progress reports
- Nurses in independent practice

---

## What data they process

**Per patient file:**
- Medical history — all conditions, operations, hospital admissions
- Medication list — all current and past medication
- Consultation report — what was discussed at each consultation
- Laboratory results — blood values, urine, biopsies
- Imaging — X-rays, ultrasounds, scans
- Referrals — to which specialist and why
- Medical certificates and reports — for employer, insurer, school, court
- Psychosocial context — family situation, work, stress, addiction
- Sexual health — contraception, STIs, sexually transmitted infections
- Psychiatric information — depression, anxiety disorders, psychoses
- Genetic information — familial conditions, hereditary risks

**What makes this data specific:**
Medical data is the most sensitive special category of personal data that exists. A leaked medical file can affect someone's insurance, damage their career, harm their relationships, and violate their dignity. Cancer, HIV, psychiatric diagnoses, addictions — information that someone carefully shields from those around them.

---

## Which laws apply

### GDPR Art. 9 — Health data as a special category

All medical data is special category data under GDPR Art. 9. Processing is in principle prohibited, unless the healthcare exception applies (Art. 9(2)(h)).

That exception applies to the doctor themselves and to care providers under their supervision — not automatically to external tools and services they use.

**Crucial point:** a cloud AI tool processing patient data is an external processor. The transfer of medical data to that processor requires a valid GDPR basis. The healthcare exception covers the doctor — but does it also cover their cloud AI tool?

Legal answer: no. The exception applies to the healthcare professional, not to their suppliers. External processors require an explicit Data Processing Agreement and a valid legal basis.

### Medical professional secrecy

**Belgium:** Art. 458 Penal Code [1]. Medical professional secrecy is absolute — apart from statutory exceptions. Violation is a criminal offence.

**Netherlands:** Art. 7:457 BW (WGBO — the Medical Treatment Contracts Act) [2] and Art. 88 BIG-wet (Individual Healthcare Professions Act) [3]. The duty of confidentiality applies to all BIG-registered care providers.

**The question for cloud AI:** if a doctor enters patient data into a cloud AI tool — even for administrative use — is that a violation of medical professional secrecy?

Legally: it is a serious risk. The data leaves the direct sphere of control of the doctor and is processed by a third party that is not a care provider and is not bound by medical professional secrecy.

### Law on Patient Rights (Belgium) / WGBO (Netherlands)

**Belgium:** Law of 22 August 2002 on the rights of the patient. Patients have the right of access to their file, the right to privacy, and the right to correction of inaccurate data.

**Netherlands:** Medical Treatment Contracts Act (WGBO). Comparable rights. Retention period: 20 years after last treatment.

### AI Act — High risk

Medical AI is explicitly high-risk if it contributes to diagnosis or treatment decisions [4].

**What is high-risk:**
- AI analysing symptoms and suggesting diagnoses
- AI drawing up or adapting treatment plans
- AI calculating medication dosages
- AI analysing imaging (radiology AI)

**What is probably not high-risk:**
- AI dictating and structuring consultation reports
- AI generating standard letters and referrals
- AI managing the diary and scheduling appointments

**But:** even administrative AI processing patient data falls under GDPR Art. 9 — regardless of the AI Act risk level.

### eHealth regulation

**Belgium:** the eHealth platform Belgium [5] regulates the digital exchange of medical data. Access to patient data via the MyCareNet network requires authentication and authorisation.

**Netherlands:** the National Switching Point (LSP) and the National Health Information Point (Nuts) govern data exchange between care providers.

**Implication:** medical data processed via cloud AI leaves the regulated eHealth ecosystem. That is an additional compliance risk on top of GDPR.

---

## Concrete use cases for AI

### 1. Dictating and structuring consultation reports

**What it is:** the doctor dictates their findings after a consultation. AI converts the spoken text into a structured consultation report in the EMR.

**Time saving:** a general practitioner (GP) with 30 consultations per day spends an average of 3-5 minutes per consultation on record-keeping. That is 90-150 minutes per day. AI can halve this.

**The risk with cloud AI:** the spoken consultation — name of the patient, complaint, findings, diagnosis, medication — goes as audio file or text to an external server. Art. 9 GDPR. Medical professional secrecy.

**With local AI + whisper.cpp:** speech-to-text processed locally. The audio does not leave the consulting room. The consultation report is generated locally.

---

### 2. Drawing up referral letters

**What it is:** AI generates a draft letter for referral to a specialist based on the consultation information.

**Time saving:** referral letters are time-consuming but largely standardised. AI saves 5-10 minutes per referral.

**The risk with cloud AI:** medical history, diagnosis, reason for referral — all going to an external server.

**With local AI:** referrals generated locally. Nothing leaves the consulting room.

---

### 3. Generating medical certificates and reports

**What it is:** medical certificates for employer, school, insurer, or court. AI generates the correct format based on the available medical information.

**Time saving:** medical certificates are repetitive. AI saves significant time for frequently requested certificates.

**The risk with cloud AI:** medical information contained in a medical certificate is by definition sensitive — otherwise the certificate would not be needed.

**With local AI:** medical certificate generation internally. Sensitive medical information stays internal.

---

### 4. Medication check and interactions

**What it is:** AI checks whether a newly prescribed medication has interactions with the patient's existing medication.

**Time saving and safety:** medication interactions are one of the greatest risks in medicine. A local AI systematically checking this is a safety tool.

**AI Act attention:** this is potentially high-risk if the AI contributes to the medication decision. Human oversight (Art. 14) is mandatory — the doctor always confirms.

**With local AI:** medication check internally, based on a local pharmacological database.

---

### 5. Patient communication

**What it is:** AI helps with producing understandable explanations for patients — what does this diagnosis mean, how does this medication work, what are the side effects.

**Value:** medical communication in understandable language improves treatment adherence and patient satisfaction.

**The risk with cloud AI:** the diagnosis and the medication — linked to the context of the patient — go to an external server.

**With local AI:** patient communications generated internally.

---

## The concrete risk with cloud AI

**Scenario — The GP with speech-to-text:**
A general practitioner (GP) uses a cloud speech-to-text tool combined with an AI assistant to process their consultations. After each consultation they dictate: "Patient Jan Janssen, 52, smoker, type 2 diabetes, recent blood glucose 8.4, considering insulin..."

**What happens legally:**
1. Name, age, diagnosis, laboratory results — Art. 9 GDPR special category — go to an external server.
2. There is no valid processing basis for this transfer.
3. Medical professional secrecy has potentially been violated.
4. The patient has never given consent.
5. The data is on servers in the US, potentially subject to the CLOUD Act.

**What the patient would think:**
Most patients assume their medical information stays in the consulting room. If they knew that their HIV status, psychiatric diagnosis, or addiction was on an American server — they would change doctor.

---

## What local AI solves

**The architectural solution:**
A mini-PC or powerful laptop in the consulting room. whisper.cpp for local speech-to-text. Ollama with a medically-optimised open-weight model. Integration with the existing EMR via a local API.

**What changes legally:**
- No transfer of Art. 9 data to external servers
- Medical professional secrecy intact
- GDPR compliant by architecture
- eHealth compliance: data stays within the organisation

**What changes practically:**
- Consultation report dictated and structured in seconds
- Referrals and medical certificates in minutes
- Medication check automated
- More time for patients, less for administration

---

## The core message for the first conversation

Start with the patient — not with technology.

> "Your patients trust you with the most personal information that exists. If today you use AI for your record-keeping — are you certain that information stays on your own systems?"

Follow up:

> "Local AI processes everything in your consulting room. The medical data of your patients does not leave your practice. You are compliant with GDPR, with medical professional secrecy, and with eHealth regulations. And you save significant time on administration."

---

## Questions they ask and how you answer

**"My EMR software is also in the cloud — isn't that the same problem?"**

Your EMR has a specific Data Processing Agreement and is certified for medical data. That is different from using a generic cloud AI tool. Moreover: more and more EMR providers offer on-premise versions precisely to avoid this problem.

**"I only use the first name or a patient number, don't I?"**

Medical data with age, diagnosis, and medication is traceable to an individual — even without a name. And in practice nobody consistently uses pseudonyms in a spoken dictation.

**"RIZIV/NIHDI (National Institute for Health and Disability Insurance)/the health insurer requires digital files, doesn't it?"**

Digital files and cloud AI are two different things. Your EMR can be digital and compliant while your AI tools run locally. The requirement for digital files does not require cloud AI.

**"Isn't local AI too slow for daily use?"**

For consultation reports and medical certificates — tasks of seconds to minutes — modern local AI is more than adequate. Speed does not need to compete with cloud AI. It only needs to be fast enough for the task — and it is.

**"My patients are elderly — they don't understand AI, do they?"**

You don't need to explain to your patients how your dictation software works. You only need to know that their data is secure. That is your responsibility, not theirs.

---

## Special attention: dental practice

Dentists process not only medical data but also imaging (X-rays, CBCT scans) and financial data (treatment costs, insurance claims).

**AI use cases specific to dentists:**
- Analysis of X-rays for caries detection — this is high-risk under the AI Act
- Generating treatment plans based on findings
- Invoice processing and insurance claims
- Patient communication about treatments

**High-risk attention:** AI analysing X-rays and making diagnoses is explicitly high-risk. Human oversight by the dentist is always mandatory — the AI is a tool, not a replacement.

---

## Special attention: physiotherapists

Physiotherapists work with treatment plans, progress reports and referrals from doctors.

**AI use cases:**
- Drawing up treatment plans based on diagnosis and objectives
- Generating progress reports
- Suggesting exercise programmes

**GDPR attention:** treatment plans contain medical diagnoses (referred by the doctor) — special category data.

---

## Belgian and Dutch context

### Belgium

**RIZIV/NIHDI** (National Institute for Health and Disability Insurance) — Regulates reimbursement of medical services and sets requirements for electronic record-keeping.

**eHealth platform Belgium** [5] — Belgian platform for digital exchange of medical data. Required for collaboration between care providers.

**Domus Medica** — Professional organisation for general practitioners (GPs) in Flanders.

**BVGG** — Belgian Association for Mental Health. Relevant for psychiatrists and psychologists with a medical background.

### Netherlands

**KNMG** (Royal Dutch Medical Association) — Professional organisation for doctors.

**NZa** (Dutch Healthcare Authority) — Supervision of the healthcare market and tariffs.

**IGJ** (Healthcare and Youth Inspectorate) — Supervision of quality and safety of care.

**LSP** — National Switching Point. Digital exchange of medical data between care providers.

---

## Sector figures (reference)

- Number of GPs in Belgium: approximately 12,000
- Number of GPs in the Netherlands: approximately 14,000
- Number of dentists in Belgium: approximately 8,500
- Number of dentists in the Netherlands: approximately 9,000
- Average administrative burden GP: 2-3 hours per day
- Potential time saving with AI for record-keeping: 40-60%
- Waiting times for new patients at GPs: average 2-4 weeks (NL), comparable (BE)

The combination of high administrative burden, patient shortage and increasing ageing makes the medical sector particularly receptive to AI support. The question is not whether — the question is how, and with whose data.

---

## References

1. **Art. 458 Belgian Penal Code — Medical professional secrecy**  
   Belgian Official Gazette / ejustice.just.fgov.be  
   <https://www.ejustice.just.fgov.be/eli/wet/1867/06/08/1867060801/justel>

2. **WGBO — Art. 7:457 BW — Duty of confidentiality**  
   wetten.overheid.nl  
   <https://wetten.overheid.nl/BWBR0005290/>

3. **BIG-wet — Art. 88 — Duty of confidentiality**  
   wetten.overheid.nl  
   <https://wetten.overheid.nl/BWBR0006251/>

4. **AI Act — Regulation (EU) 2024/1689, Annex III — High-risk medical AI**  
   EUR-Lex, Official Journal of the European Union  
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

5. **eHealth platform Belgium — Digital exchange of medical data**  
   Federal Public Service / eHealth  
   <https://www.ehealth.fgov.be/>

---

_Part of: LocAI Library · Sector Dossiers_
_Previous: S03 — Lawyers & Legal Advisors_
_Next: S05 — Hospitality_
_Last updated: 25 March 2026_
