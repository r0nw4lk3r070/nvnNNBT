# S13 — Construction & Contractors
### LocAI Library · Sector Dossier
_Version 0.1 · 25 March 2026_

---

## Who they are

The construction sector covers everyone responsible for designing, building, renovating, and maintaining buildings and infrastructure — from the general contractor running a housing project to the plumber replacing a boiler. It is a sector of SMEs: the vast majority of construction and renovation companies in Belgium and the Netherlands employ fewer than ten people.

AI has clear applications in construction: writing quotes is time-consuming, site reports are repetitive work, and tender documents are large files with standardised structures. At the same time, the sector has been relatively slow to digitise, many companies still run paper-based site administration, and awareness of data governance is limited. That combination means AI can deliver value quickly — and where risks tend to be underestimated.

**Typical profiles:**
- General contractors — new-build and renovation, residential and commercial
- Specialist tradespeople — electricians, plumbers, painters, tilers, carpenters
- Architecture firms — design, site supervision, permit management
- Property developers — larger residential and commercial projects
- Civil engineering firms — roads, utilities infrastructure, groundworks

**What distinguishes them:** construction companies simultaneously process data from three different parties — clients, subcontractors, and employees. That triangle makes data management more complex than it first appears.

---

## What data they process

**Client and project data:**
- Personal details of private clients — name, address, contact information
- Property details and building permits
- Quotes, architectural drawings, and technical specifications
- Contracts and change order management
- Invoices and payment history

**Subcontractor and supplier data:**
- Company details and contact persons
- Pricing agreements and purchase contracts
- Performance assessments for repeat collaborations
- Qualifications and certification records (VCA, recognition certificates)

**Employee data:**
- Personal details, employment contracts, job classifications
- Site attendance records and time registration
- Safety training and certificates (VCA, vibration tools, elevated platforms)
- Medical fitness declarations for specific roles

**Site registration and LIMOSA (BE):**
- Registration of foreign workers on site (mandatory in Belgium via LIMOSA)
- Subcontractor chains — who is on site, for whom, when
- Hourly records for social inspectorate and tendering obligations

**Safety and environmental data:**
- Safety plans (VGP) and risk inventories
- CCTV footage on secured sites (potentially high-risk under AI Act)
- Incident records and near-miss reports

**What makes this distinctive:** the chain is long and invisible to most companies. A contractor writing a quote with AI inputs client personal data. A contractor logging site hours via an app processes employee data. An architect using AI for site reports works with project-specific information that clients consider confidential.

---

## Which laws apply

### GDPR — Three data layers simultaneously

The GDPR applies to all personal data processed by construction companies: client data, employee data, and in some cases data from third parties on site [1]. For most SME contractors, the good news is that their data types are relatively standard — no Article 9 special categories in day-to-day operations. The discipline lies in retention policy (how long do you keep quotes from rejected clients?) and processor relationships (which apps and tools process employee data?).

### AI Act — Site security cameras as a high-risk boundary

AI systems that analyse camera footage for the purpose of identifying individuals, monitoring access, or observing behaviour potentially fall in the high-risk category of AI Act Annex III [2]. A CCTV camera on a building site that only records is not AI. A system that analyses footage to detect unauthorised persons, monitor evacuation routes, or log site access using facial recognition — that is AI Act-relevant.

**Practical message:** most construction SMEs do not deploy AI-driven camera systems. But as site management software integrates more intelligent features, it is relevant to know when an application crosses into the high-risk category.

### NIS2 — Large contractors and construction services

Large civil engineering firms and contractors working on critical infrastructure (energy, water, transport) may be classified as operators of essential services under the NIS2 Directive [3]. This brings cybersecurity risk management obligations for their operational IT systems.

### LIMOSA — Foreign worker registration (Belgium)

A contractor in Belgium that engages foreign workers or subcontractors is required to register them in advance via the LIMOSA system [4]. That system generates personal data of employees that must be processed and retained in accordance with the law. AI that generates or manages site attendance records based on LIMOSA data processes employee personal data.

### Wkba — Chain liability act (Netherlands)

In the Netherlands, the Chain Liability Act (Wkba) [5] regulates liability in the construction chain for wage tax and social security contributions. Contractors working with subcontractors must document who is on site and for whom. That documentation process is an administrative burden — and an application where AI can provide efficiency, provided the underlying data is processed correctly.

---

## Concrete use cases for AI

### 1. Writing quotes

**What it is:** AI generates quotations based on project descriptions, historical pricing data, material prices, and client context.

**Value:** faster tendering, more consistent cost structures, lower risk of missed line items. For contractors writing dozens of quotes per year, the time saving is significant.

**With local AI:** quotes contain client personal data (name, address, project) and commercially sensitive pricing information. That combination does not belong on a cloud AI platform. Margin rates, subcontractor discounts, and strategic project preferences are information that must not leave the company environment.

---

### 2. Site reports and daily logging

**What it is:** AI structures and writes daily site reports from verbal or written notes by the site manager.

**Value:** less writing work for site managers, consistent documentation, better legal protection in disputes about work performed.

**With local AI:** site reports are project documentation that clients consider confidential and that serve as legal evidence in disputes. They belong on a system the contractor controls directly.

---

### 3. Planning optimisation

**What it is:** AI analyses project timelines, material deliveries, weather forecasts, and staff availability to optimise the site schedule.

**Value:** less downtime, better subcontractor coordination, early identification of delay risks.

**With local AI:** planning data contains information about employees, subcontractors, and project deadlines. On larger projects, that data is commercially sensitive.

---

### 4. Safety instructions and toolbox talks

**What it is:** AI generates personalised safety briefings and toolbox talk content based on specific site risks, planned work, and the people involved.

**Value:** stronger safety culture, less preparation time for safety briefings, demonstrated compliance with the Wellbeing Code (BE) / Working Conditions Act (NL).

**Practical note:** safety instructions describe the nature of risks on site. That informs external parties about the state of the project. Local storage is the obvious choice.

---

### 5. Tender documents and public procurement

**What it is:** AI drafts tender documentation — technical notes, reference lists, quality assurance documents — based on project history and the requirements of the specification.

**Value:** less time spent assembling large dossiers, better consistency, higher success rate when repeatedly bidding on similar contracts.

**With local AI:** tender documents contain the project references and competency profiles that form the competitive advantage of the construction company. That information is commercially sensitive.

---

## The concrete risk with cloud AI

**The site management app scenario:**

A contractor migrates to a modern site management app with integrated AI for planning optimisation and reporting.

1. Workers clock in and out via the app. Their attendance and location data is continuously transmitted to the app provider's servers.
2. Site managers dictate daily reports into the app. That voice input — project details, supplier conversations, problem descriptions — is processed by cloud-based speech recognition on external servers.
3. Client personal data and project descriptions entered into quoting modules are absorbed into the provider's AI training process.
4. A worker representative requests access to the location data processed via the app. The contractor has no direct access to that data at the cloud provider.
5. In a tender procedure, the client asks for the data processing agreement for tools managing project data. That agreement does not exist.

Local AI for quoting, site reporting, and planning documentation: project data, client information, and employee data stay on your own system. Compliance is demonstrable. Competitively sensitive information does not leak.

---

## The core message for the first conversation

Start with practical value, not regulation.

> "Writing quotes takes time you'd rather spend on site. Site reports are repetitive. Tender documents follow the same structure every time. AI handles all of that — quickly and reliably."

Follow with the data point:

> "The one thing we avoid is sending that data to an external server. Client addresses, project details, employee attendance — that's your information. A local system keeps it with you."

---

## Questions they ask and how you answer

**"We still work with Word and Excel — why would I need AI?"**

That's a reasonable starting point. AI isn't a mandatory upgrade — it's an efficiency tool. If you write twenty quotes per month and each quote takes two hours, and AI brings that to twenty minutes: that's forty hours per month freed up for work on site. The question isn't "do I need AI" but "which tasks are currently costing me unnecessary time?"

**"Our client data is just a name and address — that's not sensitive, is it?"**

Name and address are personal data under the GDPR. They may not simply be passed to a cloud provider without a data processing agreement and transparency toward the client. That's not a horror scenario — it's the basic rule that applies to everyone, including SMEs.

**"Our site app centralises everything — convenient."**

Centralising at an external provider is convenient — until the provider goes bankrupt, triples its fees, or the data becomes inaccessible for another reason. Local storage with local AI gives you the same central accessibility — plus ownership of your own data.

**"We work with foreign subcontractors — LIMOSA is their responsibility, isn't it?"**

LIMOSA registration is also the responsibility of the main contractor. If the foreign subcontractor is not registered and the social inspectorate visits, the main contractor bears liability. AI that helps track the subcontractor chain and LIMOSA status is a compliance tool that prevents concrete fines.

**"CCTV on site — do I need permission for that?"**

For standard security cameras, the standard GDPR rules apply: information obligation, registration, maximum thirty-day retention — plus CAO 68 (BE) / Private Security Act (NL). If those cameras are connected to AI analysis — movement detection, access recognition — you enter a high-risk category that brings additional obligations.

---

## Belgian and Dutch context

### Belgium

**Confederatie Bouw** [6] is the sector employer organisation for the Belgian construction industry. Confederatie Bouw represents more than 13,000 construction companies and publishes sector standards and labour law updates.

**JC 124 — Joint Committee for the Construction Industry** is the joint committee for construction and related activities in Belgium. The collective labour agreements of JC 124 regulate, among other things, time registration and site access — directly relevant to data processed via site management apps.

**LIMOSA** [4] is the system for registering foreign workers employed in Belgium. Registration is mandatory and generates a LIMOSA certificate that must be available on site.

### The Netherlands

**Bouwend Nederland** [7] is the trade association for contractors and specialist construction companies in the Netherlands. Bouwend Nederland publishes member information on labour law, legal obligations, and sector developments.

**The Wkba** [5] obliges contractors in the Netherlands to maintain chain documentation for wage payment and social security contributions. This creates an administrative flow that AI can efficiently support.

**The Dutch Labour Inspectorate (NLA)** monitors compliance with labour and safety legislation on Dutch construction sites.

---

## Sector figures (reference)

- Number of construction companies in Belgium: approx. 78,000 (Statbel, 2024)
- Number of construction companies in the Netherlands: approx. 90,000 (CBS, 2024)
- Share of SMEs (< 10 employees) in the Belgian construction sector: >85%
- Average number of quotes per SME contractor per year: 30–120
- Share of construction companies with a formal GDPR processing agreement for their site apps: estimated <20% (Confederatie Bouw internal estimate, 2023)

---

## References

1. **GDPR — Regulation (EU) 2016/679**
   EUR-Lex, full consolidated text
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj>

2. **AI Act — Regulation (EU) 2024/1689 — Annex III**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

3. **NIS2 Directive — Directive (EU) 2022/2555**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/dir/2022/2555/oj>

4. **LIMOSA — Registration of foreign workers (Belgium)**
   <https://www.limosa.be>

5. **Wkba — Chain Liability Act (Netherlands)**
   Overheid.nl
   <https://wetten.overheid.nl>

6. **Confederatie Bouw (Belgium)**
   <https://www.confederatiebouw.be>

7. **Bouwend Nederland**
   <https://www.bouwendnederland.nl>

---

_Part of: LocAI Library · Sector Dossiers_
_Previous: S12 — Insurance Brokers_
_Next: S14 — Local Retail & Trades_
_Last updated: March 2026_
