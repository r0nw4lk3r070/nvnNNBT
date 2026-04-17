# S01 — Accountants & Bookkeepers
### LocAI Library · Sector Dossier
_Version 0.1 · 25 March 2026_

---

## Who they are

Accountants and bookkeepers are the financial conscience of SMEs. They work for small and medium-sized enterprises, sole traders, non-profits and individuals. They often know their clients for years — sometimes decades. They know what a business is worth, how healthy it is, and what keeps the owner awake at night.

**Typical profile:**
- Self-employed bookkeeper or small firm of 2-10 people
- 30-100 active client files
- Working in a heavily regulated profession with statutory professional secrecy
- Member of ITAA (Institute of Accountants and Tax Consultants) in Belgium or the NBA (Dutch Professional Organisation of Accountants) in the Netherlands
- Accustomed to compliance — but not always digital compliance

**Work rhythm:**
- Peak periods around quarterly returns, year-end closing and tax returns
- Much repetitive work: categorising transactions, checking invoices, producing reports
- Increasingly time spent on client communication about complex tax questions

---

## What data they process

This is the heart of the risk. An accountant processes the most sensitive financial data of their clients.

**Per client file:**
- Bank statements — full view of all income and expenditure
- Invoices and receipts — suppliers, clients, amounts
- Payslips and personnel data — salaries, social security, premiums
- Tax returns — VAT, corporate tax, personal income tax
- Annual accounts — complete financial picture of the business
- Contracts and agreements
- Correspondence with tax authorities and social security

**For private clients:**
- Personal bank statements
- Property information
- Investment portfolios
- Inheritances and gifts

**Why this is so sensitive:**
A bank statement of a client contains more than financial information. It tells the full story of someone's life — medical expenditure, political donations, religious gifts, relationship problems, addictions. An accountant with access to bank statements has more insight into the private life of their clients than those clients themselves realise.

---

## Which laws apply

### GDPR — Primary law

Bank statements, payslips, tax data — all personal data. The full GDPR regime applies to private clients.

**Legal basis:** Art. 6(b) GDPR (performance of a contract) [2] — the accountant processes data because it is necessary to provide the accounting service.

**Retention obligation vs. storage limitation:** accounting documents must by law be retained for 7 years (Belgian and Dutch accounting law). This creates tension with the GDPR principle of storage limitation — but the statutory retention obligation is a valid basis for longer retention.

**Data Processing Agreement:** every piece of software the accountant uses to process client data — accounting package, cloud storage, AI tool — requires a DPA.

### DORA — Indirectly applicable

Accountants are not financial institutions in the DORA sense [3]. But:

1. Many of their clients are — banks, insurers, investment funds.
2. Those clients fall under DORA and must assess the ICT suppliers in their supply chain.
3. The accountant of a bank is a supplier to that bank.
4. If the accountant uses cloud AI to process bank data, that triggers DORA questions at their client.

**Practical consequence:** an accountant working for financial institutions will increasingly be asked to document and demonstrate their ICT practices.

### ITAA professional rules — Professional secrecy

The ITAA regulations impose extensive professional secrecy. Article 58 of the ITAA Act [1]:

> "Members of the Institute are bound to keep secret everything that is entrusted to them or comes to their knowledge in the exercise of their profession."

This professional secrecy is not merely an ethical obligation — it is legally enforceable. An accountant who shares client data with a third party without the client's consent violates their professional secrecy.

**The question:** is the use of a cloud AI tool "sharing with a third party"?

Legally the answer is nuanced but the direction is clear: if the cloud AI provider processes data on its servers, that is technically a transfer to a third party. The Data Processing Agreement regulates the legal relationship — but professional secrecy requires more than a contractual clause.

### AI Act — When applicable

Most accounting AI applications fall under minimal risk or limited risk. But note:

**High-risk trigger:** if an AI system contributes to decisions about the creditworthiness of a client (Annex III, point 5b), or if it is used for tax returns with essential financial consequences — it may be high-risk.

**AI literacy (Art. 4, already in force):** every accountant using AI for their work must have sufficient AI literacy. That is not optional — it is a legal obligation.

---

## Concrete use cases for AI

These are the tasks for which an accountant would want to use AI.

### 1. Transaction classification

**What it is:** importing bank statements and automatically categorising each transaction into the correct accounting entry.

**Time saving:** an accountant with 50 clients each having 200 transactions per month — that is 10,000 transactions per month to classify. With AI: significant time saving.

**The risk with cloud AI:** the complete bank statement of the client — with all transactions, all counterparties, all amounts — goes to an external server. The client has not given consent for that. Professional secrecy is at stake.

**With local AI:** the bank statement is processed on the office's local server. No data leaves the building. The client need not even know that AI is being used.

---

### 2. Invoice processing and OCR

**What it is:** automatically reading and processing photos or scans of receipts and invoices.

**Time saving:** manual entry of invoices is time-consuming and error-prone. AI OCR is faster and more accurate.

**The risk with cloud AI:** invoices contain supplier names, VAT numbers, amounts, and sometimes personal information. All that data goes to an external server.

**With local AI:** invoice processing on own hardware. No external server, no risk.

---

### 3. Report generation

**What it is:** automatically producing monthly or quarterly reports based on accounting data.

**Time saving:** producing a report takes hours. An AI generating the first draft saves significant time.

**The risk with cloud AI:** the complete financial picture of the client — turnover, costs, margins, cash flows — goes as input to a cloud model.

**With local AI:** report generation on own hardware. The client's financial data stays in the office.

---

### 4. Tax question answering

**What it is:** a local AI model trained on Belgian/Dutch tax legislation that can answer tax questions from clients or employees.

**Time saving:** many client questions are repetitive. "Can I deduct my car?" "What is the deadline for my VAT return?" A local tax assistant saves time.

**The risk with cloud AI:** the question often contains context about the specific situation of the client — and that context is confidential.

**With local AI:** tax questions answered on own hardware. The context stays internal.

---

### 5. Anomaly detection

**What it is:** AI that flags deviations in financial data — unusual transactions, inconsistencies, potential fraud indicators.

**Value:** accountants are legally obliged to detect and report fraud. AI can do this more systematically and quickly than manual checking.

**High-risk trigger:** if anomaly detection leads to decisions about clients (creditworthiness, tax returns), it may be high-risk under the AI Act.

**With local AI:** anomaly detection on own data, without sensitive financial patterns of clients going to an external server.

---

## The concrete risk with cloud AI

Let us sketch the scenario an accountant should fear.

**The scenario:**
A 6-person accountancy firm uses ChatGPT Team to categorise bank statements. They copy the transactions into the chat and ask: "categorise these transactions for my accounting software."

**What happens legally:**
1. The bank statements of the client — personal data — are transferred to OpenAI as processor.
2. No DPA has been signed with OpenAI specifically for this processing (the standard ChatGPT Team DPA may not explicitly cover this).
3. The data is on servers in the US, subject to the CLOUD Act.
4. The ITAA professional secrecy may have been violated.
5. If the client ever asks "have you shared my bank data with third parties?" — the answer is yes.

**What can happen:**
- A client files a complaint with the ITAA about violation of professional secrecy
- The Belgian DPA (Data Protection Authority) receives a report of GDPR violation
- In the worst case: a data breach at OpenAI causing the client's financial data to leak

**The chance this happens tomorrow:** small. The chance that the legal landscape becomes stricter over the next two years and this type of use becomes increasingly risky: large.

---

## What local AI solves

**The architectural solution:**
A mini-PC in the office. Ollama running locally. An open-weight model — Llama 3.3, Mistral, or a fine-tuned tax model — processing the data.

**What changes legally:**
- No transfer to a third party: the data does not leave the office
- No DPA needed for the AI component: no external processor
- Professional secrecy intact: the data is processed by the accountant themselves, on their own hardware
- GDPR compliant by architecture: no cross-border data transfer, no external logging

**What changes practically:**
- Same functionality as cloud AI for most tasks
- No per-token costs: after the hardware investment, marginal costs are zero
- Works offline: no internet dependency for confidential processing
- Full control over which model version is running

---

## The core message for the first conversation

Do not start with technology. Start with professional secrecy.

> "You have professional secrecy. That is not just an ethical obligation — it is legally enforceable. If today you process bank statements of your clients via a cloud AI tool, that data leaves your office. That is a tension with your professional secrecy that you need to know about and make a conscious choice about."

Follow up if they ask further:

> "Local AI solves this architecturally. The data does not leave the office. Your professional secrecy is not at stake. And the functionality — transaction classification, report generation, tax questions — is comparable to what cloud AI offers."

---

## Questions they ask and how you answer

**"But I have a DPA with my cloud provider?"**

A DPA regulates the legal relationship but guarantees nothing technically. You cannot verify whether the provider is honouring the agreements. With local AI there is no external provider — you are the only data controller.

**"Isn't it much more expensive?"**

Hardware is a one-off investment of €2,300-€3,500. No monthly subscriptions, no per-token costs. Over a 3-5 year period, local AI is typically cheaper than an equivalent cloud subscription — especially when you factor in the compliance overhead.

**"Aren't local models less good than ChatGPT?"**

For most accounting tasks — transaction classification, report generation, tax question answering — modern 70B-parameter models perform comparably to GPT-4. For reading the latest tax circulars you will always need a human specialist. That does not change.

**"What if it breaks down?"**

Local systems are maintainable. The software is stable. If something happens, there is a service contract. And: if your cloud provider has an outage tomorrow, you also come to a standstill. Local AI works offline.

**"Do I have to retrain my staff?"**

The interface resembles ChatGPT. The learning curve is minimal. What changes is the policy: which data may go through the AI, which may not. That is half a day of training.

**"What does the ITAA say about this?"**

The ITAA has not yet issued specific guidelines on AI use and professional secrecy. That does not mean it is not a risk — it means the responsibility lies with you. Local AI is the most conservative and defensible choice.

---

## Timing and urgency

**December 2027** is the expected new deadline for AI Act compliance for high-risk systems (EP committee vote 18 March 2026, plenary vote expected 26 March). The urgency remains — those who wait until 2027 lose eighteen months of preparation.

The strongest argument is professional secrecy — and that applies now.

Every day an accountant uses cloud AI for confidential client data is a day when their professional secrecy is potentially at stake. That is not a future risk. That is the present.

The AI Act adds urgency for accountants using AI for tasks that may be high-risk. But the professional secrecy argument works regardless of the AI Act.

---

## Belgian and Dutch context

### Belgium

**ITAA** — Institute of Accountants and Tax Consultants. Professional regulation for certified bookkeepers and accountants. Professional secrecy anchored in the ITAA Act.

**Belgian DPA (Data Protection Authority)** — GDPR supervision in Belgium. Active in handling complaints and issuing recommendations.

**Relevant accounting software:** Isabel, Winbooks, Wolters Kluwer, Exact, Silverfin. Many of these systems are cloud-based. The accountant must have a DPA for each system.

### Netherlands

**NBA** — Dutch Professional Organisation of Accountants. Regulation for registered accountants (RA) and accounting officers (AA) [4]. Comparable professional secrecy to ITAA.

**AFM** — Netherlands Authority for the Financial Markets. Supervision of the accountancy sector. Active on quality and independence.

**Relevant software:** Exact, AFAS, Twinfield, SnelStart. Same DPA obligation as in Belgium.

---

## Sector figures (reference)

- Number of certified bookkeepers and accountants in Belgium (ITAA): approximately 17,000
- Number of accountancy firms in the Netherlands (NBA): approximately 5,000 firms
- Estimated Benelux market for local AI in accountancy: not yet quantified but substantial
- Average time saving with AI for transaction classification: 40-60% of manual processing time (industry estimate)

---

## References

1. **ITAA Act 17 March 2019, Art. 58 — Professional secrecy**  
   Act on the professions of accountant and tax adviser, Belgian Official Gazette / FPS Economy  
   <https://economie.fgov.be/nl/legislation/wet-van-17-maart-2019>

2. **GDPR — Regulation (EU) 2016/679, Art. 6(b) — Legal basis**  
   EUR-Lex, Official Journal of the European Union  
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng>

3. **DORA — Regulation (EU) 2022/2554 — Digital operational resilience**  
   EUR-Lex, Official Journal of the European Union  
   <https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng>

4. **NBA — Regulation on conduct and professional rules for accountants (VGBA)**  
   Royal Dutch Institute of Chartered Accountants  
   <https://www.nba.nl/regelgeving>

---

_Part of: LocAI Library · Sector Dossiers_
_Next: S02 — Therapists & Psychologists_
_Last updated: 25 March 2026_
