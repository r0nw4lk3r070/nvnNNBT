# S11 — HR & Recruitment
### LocAI Library · Sector Dossier
_Version 0.1 · 25 March 2026_

---

## Who they are

HR professionals and recruitment agencies sit at the start of every employment relationship. They process the most personal information people share: their career history, their motivations, their salary expectations, their assessment results — and they do so in a context of explicit decision-making about who progresses and who does not. That combination of data intensity and decision weight makes HR the sector most directly in the sights of the AI Act.

AI is already widely used in recruitment: CV screening, matching algorithms, chatbots for initial candidate interactions, assessment analysis. But many of these tools are deployed without awareness that they are legally classified as high-risk AI — with all the documentation, transparency, and oversight requirements that entails.

**Typical profiles:**
- Internal HR teams at SMEs and large enterprises
- Specialist recruitment agencies and search firms
- Temporary staffing and interim management agencies
- Executive search and headhunting firms
- Assessment and career guidance specialists

---

## What data they process

**Candidate data:**
- CVs — name, address, contact details, employment history, education, skills
- Cover letters and personal statements
- LinkedIn profiles and online presence
- Assessment results — cognitive tests, personality assessments, skills evaluations
- Interview records and evaluator notes
- References and feedback from previous employers
- Salary expectations and current compensation
- Photographs, if provided by the candidate (legally sensitive)

**Employee data (internal HR):**
- Salary data, job classifications, and benefits
- Performance reviews and appraisal results
- Absence records and reintegration files
- Training history and competency profiles
- Disciplinary records

**Client data (external agencies):**
- Vacancy profiles and role specifications
- Salary bands and budget information
- Internal organisational structure and team dynamics
- Confidential expansion or restructuring plans

**What makes this distinctive:** a CV is a collection of personal data shared by a candidate in the hope of employment. That data is assessed, compared, ranked — and upon rejection: deleted or retained. The power imbalance between candidate and recruiter is significant. When that assessment is wholly or partly conducted by AI, the legal risk rises sharply: discrimination risk in trained models, lack of transparency, and the candidate's inability to understand or contest the reasoning.

---

## Which laws apply

### GDPR — Candidate data and retention

Candidate data is personal data collected for a specific purpose: participation in a selection process [1]. That purpose limits its use — it may not be repurposed for other vacancies without new consent, may not be shared with third parties, and must be deleted when the retention period expires.

**Retention periods:** for rejected candidates, the standard is typically six months — long enough for potential complaint proceedings, short enough to be proportionate. For talent pools where candidates actively consent to longer retention, that consent must be specific and revocable.

**Data processing agreements:** every ATS (Applicant Tracking System), AI screening tool, assessment platform, or HR cloud service that processes candidate data on the company's behalf requires a data processing agreement.

### AI Act — Annex III point 4: employment AI as explicitly high-risk

AI systems used in recruitment and personnel selection are explicitly listed in Annex III of the AI Act as high-risk [2]. This is a deliberate policy choice: the weight of employment decisions — who gets to work, who does not — demands the highest standards of protection.

**What is covered:** AI tools for CV screening and ranking, matching algorithms, assessment analysis tools, AI-driven video interview analysis, chatbots that communicate selection decisions — all fall in the high-risk category when they evaluate, compare, or rank candidates.

**Obligations:** technical documentation, decision logging, transparency toward data subjects, human oversight with override capability, and conformity assessment [2]. A recruitment agency that purchases a SaaS CV screening tool is, as deployer, responsible for compliance — even if the tool is supplied by a third party.

### Anti-discrimination law

AI models trained on historical recruitment data structurally reproduce the biases present in that data. A model trained on ten years of selection decisions from a historically homogeneous sector will reinforce that homogeneity — unless actively corrected.

In Belgium, the **Act of 10 May 2007** [4] prohibits discrimination on grounds of sex, origin, age, sexual orientation, and other protected characteristics. In the Netherlands, the **General Equal Treatment Act (AWGB)** [5] covers the same ground. AI systems not actively evaluated for bias are a legal liability.

---

## Concrete use cases for AI

### 1. Vacancy texts

**What it is:** AI generates vacancy postings based on a role description, desired profile, and the employer's tone of voice.

**Value:** faster production of quality vacancies, consistent house style, and — if configured for it — more neutral language that attracts a broader and more diverse candidate pool.

**With local AI:** role descriptions and organisational culture information are internally sensitive. A replacement vacancy during an ongoing employment relationship, an expansion into a new market segment — this is information that must not flow through a cloud AI platform.

---

### 2. CV processing and summarisation

**What it is:** AI reads and structures incoming CVs, extracts relevant information, and presents a standardised summary to the recruiter.

**Value:** time savings at high volume. A recruiter handling a hundred CVs per week processes the initial screening phase faster.

**AI Act classification:** CV processing for selection purposes is high-risk AI [2]. The system may not automatically exclude candidates without human review. The recruiter decides — AI structures and supports.

---

### 3. Interview records and evaluation notes

**What it is:** AI transcribes and structures records of selection interviews, summarises evaluator notes, and monitors consistency in assessment criteria.

**Value:** reduced administrative burden for recruiters, better documentation for GDPR purposes, more consistent evaluation processes.

**With local AI:** interview records contain direct quotes, emotional impressions, and personal information shared by candidates in confidence. That data does not belong on a cloud AI platform.

---

### 4. Onboarding documents

**What it is:** AI generates personalised onboarding packages — welcome letters, introductory materials, first-week task lists — based on the new employee's profile and role.

**Value:** better onboarding experiences, less manual work for HR, faster integration.

**With local AI:** onboarding requires processing the new employee's personal data, contract information, and organisationally sensitive information.

---

### 5. Salary benchmarking and HR analytics

**What it is:** AI analyses internal salary structures and compares them to market data to support salary band decisions and job classifications.

**Value:** better-evidenced salary decisions, early identification of pay gaps.

**With local AI:** internal salary data of individual employees must not be shared with external platforms — even anonymised, where re-identification is possible in small groups.

---

## The concrete risk with cloud AI

**The ATS SaaS scenario:**

A recruitment agency migrates to a modern cloud ATS with built-in AI screening, video interview analysis, and candidate matching.

1. Thousands of CVs per year — names, addresses, employment histories, qualifications — are uploaded to servers outside the EU.
2. The video interview analysis analyses tone, facial expressions, and word choice — high-risk AI under Annex III [2]. The platform does not provide the required technical documentation as standard.
3. The platform trains its matching models on aggregated data from all connected agencies — including your candidate database and historical assessment decisions.
4. A candidate requests access to the reasoning behind their rejection (GDPR Art. 22). You have no explanation you can give.
5. The DPA investigates a complaint. You — as the deployer — are responsible for AI Act compliance, even though you took the system as a managed service.

Local CV processing and interview summarisation: candidate data stays on your own server, personal data does not leave the company environment, and documentation and transparency obligations are within your control.

---

## The core message for the first conversation

Do not start with the AI Act. Start with liability.

> "AI in recruitment is explicitly high-risk under the AI Act. That is written directly in Annex III. If you use a SaaS tool that screens CVs or ranks candidates, you as the deployer are responsible for that system's compliance. Not the vendor. You."

Follow with:

> "Local AI solves this cleanly: you support recruiters with AI that structures CVs, summarises interview notes, and generates onboarding documents — without candidate data reaching an external server, and without depending on a cloud provider's AI Act compliance."

---

## Questions they ask and how you answer

**"We already use a well-known tool — surely they're GDPR compliant?"**

Being GDPR compliant and being AI Act compliant are different things. A tool can have a valid privacy policy and still deploy a high-risk AI system that does not meet the documentation and transparency requirements of the AI Act. As the deployer, you carry the responsibility. "The vendor assured us" is not a legal defence.

**"Surely AI screening is neutral — it doesn't look at gender or origin?"**

AI models are as neutral as the data on which they were trained. If historical hiring decisions predominantly selected men, the model learns that men are stronger candidates. Certain word choices correlated with a particular background get weighted into the score. That is structural bias in algorithmic form — legally just as problematic as deliberate discrimination.

**"We always keep CVs — for when something suitable comes up."**

That is permitted — if candidates explicitly consented to that retention period at the time of submission, if that consent is specific, and if candidates can withdraw it. Retaining CVs indefinitely without explicit consent and active retention management is a GDPR violation.

**"How am I supposed to explain why a candidate was rejected if AI decided it?"**

That is exactly the problem. GDPR Art. 22 gives individuals the right not to be subject to solely automated decision-making with significant consequences. If you cannot provide that explanation, you risk enforcement action. Local AI that supports the recruiter without replacing them solves this: the decision remains human and explicable.

**"Our candidates sign a consent declaration anyway."**

Consent to participate in a selection process is not consent to every use of their data. Consent to AI screening requires specific information about which system is being used and what consequences it has. A generic clause is not sufficient.

---

## Belgian and Dutch context

### Belgium

**Federgon** [5] is the Belgian federation of HR service providers. Federgon publishes sector guidelines for recruitment and data management and has a code of conduct for its members.

**Unia — Interfederal Centre for Equal Opportunities** [6] handles discrimination complaints in Belgium, including complaints about discriminatory selection procedures. Unia has specific focus on algorithmic discrimination.

The **Social Inspectorate** oversees compliance with anti-discrimination law and labour law. AI tools used in selection procedures can form part of an inspection file.

### The Netherlands

**ABU and NBBU** [7] are the sector organisations for temporary staffing and recruitment agencies in the Netherlands. They publish codes of conduct and sector standards for handling candidate data.

**College voor de Rechten van de Mens** [8] handles discrimination complaints in the Netherlands. The College has issued opinions on AI and discrimination in selection procedures.

**FNV** and **CNV** have active positions on AI use in recruitment and the protection of candidates and workers.

---

## Sector figures (reference)

- Number of Belgian interim and recruitment agencies: approx. 700 (Federgon, 2024)
- Share of Belgian companies using AI in recruitment: growing, estimated 20–30% for 2025
- Average number of CVs per vacancy in the Benelux: 40–120 depending on sector and seniority level
- Average cost of a data breach for an SME: €15,000–50,000 (IBM Cost of Data Breach Report 2024, adjusted for SME scale)

---

## References

1. **GDPR — Regulation (EU) 2016/679 (incl. Art. 22 — automated decision-making)**
   EUR-Lex, full consolidated text
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj>

2. **AI Act — Regulation (EU) 2024/1689 — Annex III point 4 (employment AI = high-risk)**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

3. **GDPR Art. 22 — Automated individual decision-making**
   EUR-Lex (see source 1)

4. **Act of 10 May 2007 combating discrimination — Belgium**
   Belgian Official Gazette via e-Justice
   <https://www.ejustice.just.fgov.be>

5. **Federgon — Federation of HR service providers**
   <https://www.federgon.be>

6. **Unia — Interfederal Centre for Equal Opportunities**
   <https://www.unia.be>

7. **ABU / NBBU — Sector organisations for temporary staffing in the Netherlands**
   <https://www.abu.nl> / <https://www.nbbu.nl>

8. **College voor de Rechten van de Mens**
   <https://www.mensenrechten.nl>

---

_Part of: LocAI Library · Sector Dossiers_
_Previous: S10 — Transport & Logistics_
_Next: S12 — Insurance Brokers_
_Last updated: March 2026_
