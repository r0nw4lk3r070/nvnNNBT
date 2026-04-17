# S12 — Insurance Brokers
### LocAI Library · Sector Dossier
_Version 0.1 · 25 March 2026_

---

## Who they are

Insurance brokers are independent intermediaries who find the best insurance solutions for their clients across multiple insurers. They are not agents of a single insurer — they work in their client's interest. That position is distinctive: they process comprehensive personal and financial information within a relationship of trust, and they carry a duty of care enshrined in law.

The sector is already accustomed to strict regulation via the FSMA (BE) and the AFM/DNB (NL), sectoral conduct rules, and special categories of personal data under the GDPR. But the real challenge is AI: premium calculation, claims assessment, and client advice are increasingly supported by systems that may or may not be high-risk under the AI Act.

**Typical profiles:**
- Independent insurance offices — household, motor, fire, liability
- Specialist brokers — life, pension, income protection
- Comparison platforms — multi-insurer, online or hybrid
- Corporate brokers — professional indemnity, credit, trade, major risks

**What distinguishes them:** brokers hold a combination of financial profiles, claims history, and health information. That combination makes their data processing risk fundamentally different from most other sectors. Health questions on life insurance policies fall under Article 9 of the GDPR — the highest category of sensitive personal data.

---

## What data they process

**Client data:**
- Personal details — name, address, date of birth, national registry number (BE) / BSN (NL)
- Financial profile — income, assets, liabilities, family situation
- Policy and product data — active policies, premium history, coverage summaries
- Claims history — previous claims, rejections, fraud registrations

**Special categories of personal data (Art. 9 GDPR):**
- Health information on life and hospitalisation policies — medical history, conditions, medication
- Disability and incapacity for work status
- In some niches: genetic data for specific risk assessment

**Business data (commercial portfolio):**
- Annual accounts and financial reports of commercial clients
- Insurable properties and risk addresses
- Business-specific exposures — product liability, professional risks, cyber risk

**Compliance and AML data:**
- KYC documents — identity records, source of funds
- FATF screenings and PEP checks (politically exposed persons)
- Transaction records for anti-money laundering purposes

**What makes this distinctive:** it is the combination that amplifies the risk. A financial profile is sensitive. Claims history is sensitive. Health information is Article 9 — the most restricted category. When all three sit in a single client file and are analysed by an AI system, a thorough data governance framework is not optional.

---

## Which laws apply

### GDPR — Article 9 and the health question

Health information is special category personal data under Article 9 of the GDPR [1]. Processing it is in principle prohibited unless a specific exception applies. For insurance brokers, the most relevant exceptions are Article 9(2)(b) — processing necessary for employment and social security obligations — or, for life and income insurance: Article 9(2)(a), explicit consent of the data subject.

**In practice:** clients who complete a medical questionnaire for a life insurance application give consent for that specific processing activity. That consent does not automatically extend to loading those same answers into an AI system that uses them to calculate premiums or model risk at a third party.

### AI Act — Risk classification for insurance AI

High-risk or not, depending on the application:

- **High-risk (Annex III):** AI systems used to assess creditworthiness or insurance risk of individuals, especially those that determine whether someone is insured and at what premium [2]. In practice this category covers AI-driven insurance risk assessment.
- **Limited risk:** AI that simulates advisory conversations or generates documents but does not make acceptance or premium decisions.
- **Minimal risk:** internal administrative automation without decision-making weight.

### FSMA — Belgian Financial Services and Markets Authority

Insurance brokers in Belgium must be registered with the FSMA [3] and comply with the conduct rules in the Insurance Act of 4 April 2014 and MiFID-equivalent provisions for financial products. The FSMA has published statements on AI use in financial services.

### Wft — Financial Supervision Act (Netherlands)

In the Netherlands, insurance brokers are subject to the Financial Supervision Act (Wft) [4], supervised by the AFM (conduct) and DNB (prudential). The Wft sets requirements for duty of care, advisory process, and client file management — all directly relevant to how AI tools may be used in the advisory process.

### AMLD5 — Anti-Money Laundering Directive

Insurance brokers are obligated entities under the Fifth Anti-Money Laundering Directive [5]. This entails KYC obligations, transaction monitoring for unusual payment flows, and documentation requirements. AI that screens client profiles for AML risk potentially falls in the high-risk category of the AI Act.

### IDD — Insurance Distribution Directive (2016/97)

The IDD [6] regulates the distribution of insurance products in the EU. It obliges brokers to be transparent about their remuneration, to conduct an advisory process in the client's best interest, and to demonstrate adequate product knowledge. AI tools used in the advisory process must comply with the IDD duty of care: the tool may not generate advice that is not in the client's best interest.

---

## Concrete use cases for AI

### 1. Policy analysis and gap detection

**What it is:** AI analyses a client's existing insurance portfolio and identifies coverage gaps, overlaps, and potential optimisations.

**Value:** brokers can advise faster and more thoroughly, clients gain a clearer picture of their risks, and the quality of the advisory process improves.

**With local AI:** the full client profile — financial, insurance-related, sometimes including health information — stays on the broker's own system. No transfer to a cloud analytics platform.

---

### 2. Claims support and correspondence

**What it is:** AI assists with the claims management process by drafting correspondence with insurers, summarising status updates, and keeping clients informed.

**Value:** reduced administrative burden for brokers, faster turnaround for clients, better file documentation.

**With local AI:** claims data may include medical context alongside financial information (disability claims, health insurance). That data does not leave the office.

---

### 3. Client advisory preparation

**What it is:** AI helps the broker prepare for an advisory meeting — summarising the client file, identifying relevant risk factors, suggesting questions to ask, and presenting product options.

**Value:** better meeting preparation, more client-centred conversations, more consistent advisory quality across the office.

**Note on IDD:** the advisory process must be documented and demonstrably in the client's interest. AI that drives the advice but is not auditable does not satisfy IDD requirements.

---

### 4. Compliance and AML support

**What it is:** AI screens newly onboarded clients against AML risk profiles, consolidates KYC information, and generates a compliance summary for the file manager.

**Value:** faster onboarding, less manual research, consistent documentation levels.

**Note on AI Act:** AML screening systems potentially fall in the high-risk category. Documentation and human oversight requirements apply.

---

### 5. Document processing and premium overviews

**What it is:** AI processes incoming policy documents, premium notices, and insurer correspondence — extracts key data and updates the client file.

**Value:** administrative time savings, fewer data entry errors, up-to-date files.

**With local AI:** policy documents contain the client's personal data and sometimes the insurer's financial data. Processing via a cloud OCR service is a processor relationship that must be contractually established.

---

## The concrete risk with cloud AI

**The health data scenario:**

A life insurance brokerage uses a cloud AI platform for client advisory support and risk analysis.

1. A client completes a medical questionnaire for a life insurance quote. Their answers are loaded into the AI platform together with their financial profile and claims history.
2. The Article 9 data — health information — leaves the office's secure environment and is processed on the cloud provider's servers, potentially outside the EU.
3. The platform trains its risk models on aggregated client data from all connected brokers. Your clients' health information contributes to a model shared with competitors.
4. A client requests access to how their health information was used. You cannot give an answer that covers the cloud provider's processing chain.
5. The DPA opens an investigation following a complaint. The data processing agreement for the AI platform does not explicitly cover Article 9 processing. That is a violation.

Local processing of policy analysis and client advisory: Article 9 data remains within the office, processing purposes are controllable and demonstrable, and the advisory process satisfies IDD documentation requirements.

---

## The core message for the first conversation

Start with the special character of the data.

> "You process health information. That is Article 9 GDPR — the most restricted category. You cannot send that data to a cloud AI platform without an explicit lawful basis and a watertight data processing agreement. And almost no one gets that right."

Follow with:

> "Local AI processes the client file, prepares advisory meetings, and generates documentation — without health data, financial profiles, or claims history leaving the office environment. That is the only architecture that supports both GDPR Article 9 compliance and the IDD duty of care at the same time."

---

## Questions they ask and how you answer

**"We only ask what the insurer asks us — the responsibility is theirs."**

No. You ask the health questions to the client. That makes you the controller for that data. The insurer is a separate controller for what they do with it after you transfer it. Those two processing activities are legally separate — your responsibility does not end on transfer.

**"Our clients give consent on the application form."**

That consent covers the processing activity described on the form — typically submitting a quote request to an insurer. It does not cover loading that data into an external AI analytics platform. That use requires a separate lawful basis and a separate transparency obligation.

**"We're a small office — surely these rules are for the large players?"**

The GDPR has no size threshold for Article 9. Even a sole-trader office with ten life insurance policies processes special category personal data and is required to have an explicit lawful basis and adequate security. The FSMA expects registered brokers to have their data governance in order regardless of office size.

**"Our AI tool is GDPR certified."**

GDPR certification for a tool addresses the security measures for data storage. It does not confirm that you have a valid lawful basis for submitting Article 9 data to that tool. You must demonstrate that — the tool cannot do it for you.

**"Can we still use AI at all?"**

Absolutely. The question is where the AI runs. A locally deployed AI that processes Article 9 data on your own server — with you as the sole controller — is technically and legally sound. The architecture determines compliance, not the technology.

---

## Belgian and Dutch context

### Belgium

**FSMA — Financial Services and Markets Authority** [3] is the conduct supervisor for insurers and brokers in Belgium. The FSMA monitors AI use in financial services and publishes circulars on technology risks.

**Assuralia** [7] is the professional association of Belgian insurance companies. Assuralia publishes sector standards, market figures, and policy positions — relevant as context for the environment in which brokers operate.

**The GBA — Data Protection Authority** [8] enforces the GDPR in Belgium. The GBA has issued fines in the financial sector for inadequate processing of special categories of personal data.

### The Netherlands

**AFM — Authority for the Financial Markets** [4] supervises the conduct of insurance brokers. The AFM expects brokers to demonstrate their duty of care, including when AI tools are used in the advisory process.

**DNB — De Nederlandsche Bank** has supervisory responsibility for prudential oversight and publishes guidance on the use of AI models in the financial sector.

**Verbond van Verzekeraars** [9] is the trade association of Dutch insurance companies. Their conduct standards have indirect relevance for the broker market.

---

## Sector figures (reference)

- Number of FSMA-registered insurance intermediaries in Belgium: approx. 10,500 (FSMA, 2024)
- Number of AFM-registered insurance intermediaries in the Netherlands: approx. 5,000 (AFM, 2024)
- Share of offices with an active life insurance portfolio: approx. 65%
- Average cost of a data breach for financial services firms: €3.8 million (IBM Cost of Data Breach Report 2024, sector average)
- Share of financial sector data breaches involving external cloud providers: 24% (IBM, 2024)

---

## References

1. **GDPR — Regulation (EU) 2016/679 (incl. Art. 9 — special categories of personal data)**
   EUR-Lex, full consolidated text
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj>

2. **AI Act — Regulation (EU) 2024/1689 — Annex III (high-risk AI systems)**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

3. **FSMA — Financial Services and Markets Authority (Belgium)**
   <https://www.fsma.be>

4. **Wft / AFM — Financial Supervision Act / Authority for the Financial Markets (Netherlands)**
   <https://www.afm.nl>

5. **AMLD5 — Directive (EU) 2018/843 on anti-money laundering**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/dir/2018/843/oj>

6. **IDD — Insurance Distribution Directive (EU) 2016/97**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/dir/2016/97/oj>

7. **Assuralia — Professional Association of Belgian Insurers**
   <https://www.assuralia.be>

8. **GBA — Data Protection Authority (Belgium)**
   <https://www.gegevensbeschermingsautoriteit.be>

9. **Verbond van Verzekeraars (Netherlands)**
   <https://www.verzekeraars.nl>

---

_Part of: LocAI Library · Sector Dossiers_
_Previous: S11 — HR & Recruitment_
_Next: S13 — Construction & Contractors_
_Last updated: March 2026_
