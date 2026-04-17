# S03 — Lawyers & Legal Advisors
### LocAI Library · Sector Dossier
_Version 0.1 · 25 March 2026_

---

## Who They Are

Lawyers and legal advisors are the guardians of the law. They represent clients in disputes, advise businesses on risks, and protect individuals against the power of institutions. Their effectiveness depends on one thing: trust. A client must be able to tell their lawyer everything — including what they would rather tell no one — in the knowledge that it stays within the attorney-client relationship.

That trust is not merely ethical — it is legally enshrined in professional secrecy and the legal privilege / right to refuse testimony. It is one of the most absolute protections in the legal system.

**Typical profile:**
- Solo lawyer or small firm of 2–15 lawyers
- Specialised in one or more areas of law
- Operating under strict deontological rules of the bar
- High document load: contracts, procedural documents / court filings, legal opinions, correspondence
- Time pressure: deadlines, hearings, time limits that must not be missed

**Specific professional groups:**
- Lawyers (registered at the bar — legal privilege / right to refuse testimony)
- In-house counsel (more limited protection)
- Notaries (separate profession, own professional secrecy)
- Bailiffs (own professional secrecy)
- Legal advisors (not bar-registered — less protection)

---

## What Data They Process

**Per client file:**
- Correspondence between lawyer and client — fully protected by professional secrecy
- Contracts and agreements — often confidential business information
- Procedural documents / court filings — strategic information about cases
- Evidence — sometimes sensitive or confidential
- Clients' financial information — for proceedings or tax advice
- Personal circumstances — family law, criminal law, labour law
- Trade secrets — in mergers, acquisitions, commercial disputes
- Medical information — in personal injury or incapacity cases
- Criminal information — in criminal cases

**What makes this data special:**
In a criminal file, a single leaked document can destroy a defence. In a commercial case, a single leaked contract clause can sink an acquisition. In a family case, a single leaked email can decide a custody proceedings. The damage from a data breach in the legal sector is not only legal — it is irreversible.

---

## Applicable Laws

### Professional Secrecy and Legal Privilege — The Absolute Core

**Belgium:**
The professional secrecy of lawyers is enshrined in Art. 458 of the Criminal Code (violation is a criminal offence), the Law on the Legal Profession, and the deontological code of the OVB (Flemish Bar Association) [1] and the Ordre des barreaux francophones et germanophone (OBFG — French/German-speaking Bar).

The legal privilege / right to refuse testimony gives lawyers the right to refuse to testify about what their clients have entrusted to them. It is one of the most absolute rights in the Belgian legal system.

**Netherlands:**
The professional secrecy of lawyers is enshrined in Art. 11a of the Advocatenwet (Lawyers Act) and Art. 218 of the Code of Criminal Procedure (right to refuse testimony). The NOvA (Netherlands Bar Association) enforces strict deontological rules [2].

**The critical question for cloud AI:**
The legal privilege protects communication between lawyer and client. If that communication is routed through a cloud AI server — even for internal administration — is the protection still absolute?

Legal answer: it is a serious grey area. Courts have not yet delivered a definitive ruling on cloud AI and legal privilege. But the direction of legal doctrine is clear: any transfer of confidential communication to a third party — even a processor — is a potential weakening of legal privilege.

### GDPR — Applicable to Personal Data in Files

Name, address, financial situation, family circumstances, criminal record — all personal data. Sometimes special categories (health, criminal data).

**Legal basis for processing:** Art. 6b (performance of a contract) or Art. 6f (legitimate interest — legal defence).

**Criminal data (Art. 10 GDPR):** [3] an additional layer of protection. Processing of criminal data may only be carried out by public authorities or under the supervision of public authorities — unless an exception applies.

### AI Act — When Applicable

AI that contributes to decisions in legal proceedings is high-risk (Annex III, point 8 — administration of justice and democratic processes) [5].

**Nuance:** an AI that analyses contracts or conducts legal research is probably not high-risk. An AI that contributes to a judge's decision — that is high-risk.

For lawyers: most AI applications fall under minimal or limited risk. But if AI is used to assess the chances of a case or to present evidence — proceed with caution.

### Anti-Money Laundering Regulation (AML)

Lawyers in certain domains (real estate, corporate law, tax law) are subject to anti-money laundering obligations [4]. They must screen clients and report suspicious transactions.

If AI is used for AML screening — that is potentially high-risk and requires extra diligence.

---

## Concrete Use Cases for AI

### 1. Contract Analysis and Review

**What it is:** uploading a contract and having AI identify which clauses are risky, missing, or deviate from the standard.

**Time saving:** reading and analysing a 50-page contract takes hours. AI produces an initial analysis in minutes.

**The risk with cloud AI:** the entire contract — including confidential business information, commercial terms, strategic clauses — goes to an external server. Trade secrets, intellectual property, acquisition price — everything.

**With local AI:** contract analysis on your own hardware. The contract never leaves the office.

---

### 2. Legal Research

**What it is:** AI searches for relevant case law, legislation, and legal doctrine based on a query.

**Time saving:** legal research is time-consuming. A well-trained local model can significantly accelerate the starting point of research.

**The risk with cloud AI:** if the lawyer provides context ("my client is on trial for fraud and…"), that context is confidential.

**With local AI:** research with full context, internally. No risk to the file.

---

### 3. Drafting Procedural Documents

**What it is:** AI generates a first draft of a legal brief, petition, or legal opinion based on the facts and the legal framework.

**Time saving:** significant — especially for standard documents such as summonses, standard letters, or routine legal opinions.

**The risk with cloud AI:** the facts of the case, the legal strategy, the weak points of the defence — all go to an external server.

**With local AI:** procedural documents / court filings drafted on your own hardware. Strategic information stays internal.

---

### 4. Summarising Files

**What it is:** summarising a large file — hundreds of pages of correspondence, evidence, procedural documents / court filings — into a manageable overview.

**Time saving:** enormous. Going through a 500-page file takes days. AI generates a summary in minutes.

**The risk with cloud AI:** the entire file — including all confidential information — goes to an external server.

**With local AI:** file summary on your own hardware. The complete file stays internal.

---

### 5. Client Communication

**What it is:** AI helps draft letters and emails to clients — explaining legal concepts, status updates, advice in plain language.

**Time saving:** limited per letter, but cumulatively significant — and it raises the quality of communication.

**The risk with cloud AI:** name, file information, and legal strategy go to an external server.

**With local AI:** communication processed internally.

---

## The Concrete Risk with Cloud AI

**Scenario 1 — The Merger Acquisition:**
A lawyer is guiding an acquisition transaction. He uses Claude or ChatGPT to analyse the acquisition contract and identify risks. The acquisition price, the warranties, the break-up fees, the confidentiality clauses — everything is in the contract he uploads.

If that information leaks — via a data breach at the provider, via a CLOUD Act request, or through any other channel — the transaction can fail, share prices can move, and his clients can lose billions.

**Scenario 2 — The Criminal Defence:**
A lawyer is preparing the defence in a criminal case. He uses AI to identify the weak points in the evidence and refine his strategy. He provides the AI with context: the facts as his client describes them, the evidence, the witness statements.

If the prosecutor ever gains access to that analysis — through whatever channel — the defence is compromised.

**Scenario 3 — The Family Dispute:**
A lawyer is handling a divorce. He uses AI to summarise correspondence and prepare arguments. That correspondence contains the deepest vulnerabilities of his client — financial situation, psychological problems, relationship issues.

If that information reaches the other party — the consequences are immediate and personal.

---

## What Local AI Solves

**The architectural solution:**
A local server or powerful laptop. Ollama with a large open-weight model — preferably 70B for complex legal analysis. An interface that can load and analyse documents.

**Optional: RAG (Retrieval-Augmented Generation):**
A local vector database filled with the complete text of Belgian or Dutch law, relevant case law, and the firm's legal knowledge base. The AI searches that database for every query — without a single query going to an external server.

**What changes legally:**
- No transfer of confidential client information to a third party
- Legal privilege / right to refuse testimony and professional secrecy intact
- GDPR compliant
- No DPA required for the AI component

**What changes practically:**
- Contract analysis in minutes
- File summary in minutes
- Legal research accelerated
- More time for the client, less for administration

---

## The Core Message for the First Conversation

Start with legal privilege — the most sacred principle in the legal profession.

> "Legal privilege is one of the most absolute rights in our legal system. It protects everything your clients entrust to you. If you use AI today for contract analysis, file summaries, or research — and you provide context about your file — where does that information go?"

Continue:

> "Local AI processes everything on your own server. Not a single piece of a file leaves your office. You have the same functionality — contract analysis, research, drafting documents — but without any risk to your professional secrecy or the legal privilege of your clients."

---

## Questions They Ask and How to Answer

**"I don't pass names to the AI — I anonymise."**

Full anonymisation of legal documents is virtually impossible. A contract contains company names, amounts, dates, and specific clauses that are identifiable. A criminal file contains facts that are directly traceable. And if you later link the anonymous version to the file, the connection is there regardless.

**"My bar association hasn't said anything about this."**

True — the OVB (Flemish Bar Association) and the NOvA (Netherlands Bar Association) have not yet issued specific AI guidelines. But professional secrecy and legal privilege already apply. The deontological code requires you to protect the confidentiality of client information. How you implement that technically is your responsibility. Local AI is the most defensible choice.

**"My clients sign a file agreement anyway."**

A file agreement governs the relationship between lawyer and client. It does not give the lawyer the right to transfer confidential information to third parties — including an AI provider — without the client's explicit consent.

**"Isn't a 70B model too slow for daily use?"**

On an AMD Ryzen AI Max+ mini-PC with 128GB unified memory, a 70B model runs at production speed. For contract analysis, file summaries, and draft texts, the speed is more than sufficient. For real-time chat, a smaller model (13B–34B) is faster and sufficient for most tasks.

**"What about cloud-based legal databases such as Westlaw or Jura?"**

Those databases contain published legislation and case law — not confidential client information. They are different from an AI tool that you feed with file content. The distinction is: what goes to the external server? Looking up public legal information is different from processing confidential file content.

**"My clients are large companies — surely they understand I use tools?"**

Large companies have their own legal teams and compliance departments. These are increasingly aware of the risks of data transfer to cloud AI. More and more in-house legal teams are imposing requirements on the external lawyers they hire regarding how they handle confidential data. Local AI is a competitive advantage — not just a compliance requirement.

---

## Special Attention: State Secrets and Classified Information

Lawyers working for governments, defence companies, or in cases with security classifications handle data that must absolutely not go to external servers.

For these categories, local AI is not just the best choice — it is the only choice. Cloud AI is categorically excluded.

---

## Special Attention: In-House Counsel

In-house counsel occupy a different position than bar-registered lawyers. In most European legal systems they do not have full legal privilege — their communications with their employer enjoy less protection than those of an external lawyer.

This makes the GDPR argument all the stronger for this group: if legal privilege is less absolute, the GDPR obligation to protect personal data is all the more clearly present.

---

## Belgian and Dutch Context

### Belgium

**OVB** — Orde van Vlaamse Balies (Flemish Bar Association). Regulates Dutch-speaking lawyers in Belgium.

**OBFG** — Ordre des barreaux francophones et germanophone (French/German-speaking Bar). Regulates French- and German-speaking lawyers.

**IBJ** — Instituut voor Bedrijfsjuristen (Institute for In-House Counsel). Professional organisation for in-house counsel — no full legal privilege.

**Relevant legal domains with high AI value:**
- Property law (many standard documents)
- Corporate law (articles of association, shareholders' agreements)
- Labour law (employment contracts, collective agreements)
- Debt collection and amicable settlement

### Netherlands

**NOvA** — Nederlandse Orde van Advocaten (Netherlands Bar Association). Regulates all lawyers in the Netherlands [2].

**Gedragsregels Advocatuur (Conduct Rules for the Legal Profession):** extensive deontological rules including a duty of confidentiality [2].

**Relevant legislation:** Advocatenwet (Lawyers Act), Art. 218 Sv (right to refuse testimony), WGBO (for medico-legal files).

---

## Sector Figures (Reference)

- Number of lawyers in Belgium: approximately 17,000 (registered at the bar)
- Number of lawyers in the Netherlands: approximately 18,000
- Number of notaries in Belgium: approximately 1,800
- Average hours per week on document management: 15–25 hours
- Potential time saving with AI for document work: 40–50%

---

## References

1. **OVB — Codex Deontologie voor Advocaten**  
   Orde van Vlaamse Balies  
   <https://www.ordevanvlaamsebalies.be/nl/kennisbank/deontologie/codex-deontologie-voor-advocaten>

2. **NOvA — Gedragsregels voor de Advocatuur**  
   Nederlandse Orde van Advocaten  
   <https://www.advocatenorde.nl/voor-advocaten/wet-en-regelgeving/gedragsregels/gedragsregels-advocatuur>

3. **GDPR — Regulation (EU) 2016/679, Art. 9 & 10 — Special categories & criminal data**  
   EUR-Lex, Official Journal of the European Union  
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng>

4. **Directive (EU) 2018/843 — Anti-Money Laundering Directive (AMLD5) — obligations for lawyers**  
   EUR-Lex, Official Journal of the European Union  
   <https://eur-lex.europa.eu/eli/dir/2018/843/oj>

5. **AI Act — Regulation (EU) 2024/1689, Annex III — High-risk AI systems**  
   EUR-Lex, Official Journal of the European Union  
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

---

_Part of: LocAI Library · Sector Dossiers_
_Previous: S02 — Therapists & Psychologists_
_Next: S04 — Medical & Dental Practices_
_Last updated: 25 March 2026_
