# S09 — Non-profit & Associations
### LocAI Library · Sector Dossier
_Version 0.1 · 25 March 2026_

---

## Who they are

Non-profit organisations are driven by a mission, not by profit. Yet they process large volumes of personal data every day — from donors who finance their work to beneficiaries who depend on the care or services the organisation provides. That combination makes the sector as data-intensive as healthcare or financial services, even if it is rarely treated as such.

A social welfare charity coordinating home care knows the medical situation, living circumstances and financial vulnerability of tens or hundreds of people. A youth organisation holds not only member data but also criminal record extracts for its volunteers. A fundraising NGO combines donor IBANs with information about the populations it serves — information that, in the wrong hands, could cause disproportionate harm.

**Typical profile:** small to mid-sized, heavily dependent on volunteers, funded by a mix of subsidies, donations and membership fees. Compliance awareness is often less developed than in commercial sectors — not through unwillingness, but through limited resources and scarce legal expertise.

**Specific professional groups:**
- Social welfare associations — home care, social work, crisis support, community care
- Cultural organisations — museums, theatre federations, amateur arts associations
- Sports clubs and federations
- Welfare organisations and social services
- Foundations and philanthropic institutions
- Religious organisations
- Neighbourhood and community groups
- International NGOs with a Belgian or Dutch office

---

## What data they process

**Member data:**
- Name, contact data, membership history
- Payment details — membership fees, contributions
- Communication preferences and activity engagement

**Donor data:**
- Name, address, IBAN (for tax certificates and direct debit)
- Financial contributions — amounts, frequency, acquisition channel
- Communication history and campaign response
- Recorded contact moments — calls, email exchanges, events

**Volunteer data:**
- Identity details and contact information
- Availability, tasks and skills
- Training certificates and qualifications
- Criminal record extract — especially for youth work, work with vulnerable persons or children (particularly sensitive)

**Beneficiary data:**
- Identity details and family situation
- Social situation — income, housing, employment
- Care files and support history
- Health data, mental health, addiction issues
- This is the most sensitive category — GDPR Art. 9 [1]

**What makes this distinctive:** the combination of donor data (financial and behavioural) and beneficiary data (potentially health or social vulnerability data) on the same digital platform is exceptionally sensitive. A data breach damages not just individual privacy, but the trust relationship that is the absolute core of every non-profit's work. Donors must be able to trust that their contributions are managed discreetly. Beneficiaries must be able to trust that their situation will never reach unauthorised parties — including the donors who fund the organisation.

---

## Which laws apply

### GDPR — Purpose limitation, special categories and data minimisation

Non-profits collect data from multiple stakeholder groups for fundamentally different purposes [1]. Donor data may not be used for beneficiary management. Volunteer data may not be shared with donors. Member data of a sports club may not be used for political communications. This principle of purpose limitation — personal data is processed solely for the purpose for which it was collected — is particularly critical in the non-profit context because the organisation simultaneously fulfils multiple roles.

For member communications and donor outreach, the choice between consent (Art. 6(1)(a)) and legitimate interest (Art. 6(1)(f)) plays a central role [1]. Existing members and donors can be approached on the basis of legitimate interest, provided there is a clear opt-out. New contacts generally require explicit consent. Tax certificates for donations are linked to a statutory retention obligation of seven years — donor data may therefore not simply be erased. This creates a tension with the right to erasure under GDPR.

Every external CRM, fundraising platform or email tool with which personal data is shared requires a data processing agreement. The non-profit remains controller at all times — and is therefore liable for what its processors do.

### GDPR Art. 9 — Special categories of personal data

Social non-profits working with health data, mental health data, social vulnerability data or information about beneficiaries' addiction issues process "special categories" within the meaning of Art. 9 GDPR [1]. This is the highest protection level within the regulation. Processing is in principle prohibited, unless an explicit exemption under Art. 9(2) applies — typically explicit consent from the data subject, or substantial public interest with appropriate safeguards.

Every cloud environment processing beneficiary data — intake forms, case management software, file handling tools — must have a robust data processing agreement specifically addressing Art. 9 obligations. Art. 9 data on US-based fundraising or CRM platforms represents a significant legal vulnerability: the combination of a weak legal basis, transatlantic data transfers, and commercial terms of use that leave room for model training creates a risk profile that is difficult to defend before the regulator.

### Companies and Associations Code / CAC (Belgium)

The Act of 23 March 2019 on the Code of Companies and Associations [2] governs the operation of non-profit associations (VZW/ASBL) in Belgium. The CAC imposes governance obligations — general assembly, board of directors, annual accounts — and requires that decisions and financial data are traceable and auditable.

Digital tools deployed for governance processes — meeting minutes, financial management, grant files — must support that traceability. An AI tool that summarises board meetings or generates financial reports becomes part of the official decision-making record of the association. If that output is generated via an external cloud service, the question arises of what control the organisation retains over the integrity and durability of those records.

### Act on Governance and Oversight of Legal Entities / WBTR (Netherlands)

The WBTR (2021) [3] governs the governance of associations and foundations in the Netherlands. Directors bear individual liability and are responsible for proper governance. Digital records — including AI-generated outputs used for board decisions or external accountability — must be auditable.

An AI system that generates grant applications, compiles impact reports or processes beneficiary statistics using external cloud infrastructure outside the organisation's control creates a traceability problem that conflicts with individual director liability under the WBTR.

### AI Act — Donor scoring and admission models

AI models deployed for donor scoring — who will give how much, who is most responsive to a campaign — or for prioritising beneficiaries at intake may qualify as high-risk under the AI Act [4]. Annex III describes systems that significantly influence access to essential services or support as potentially high-risk. An intake system that automatically determines who qualifies for care or support, or that ranks applicants based on an algorithm, falls in principle within that category.

For high-risk AI systems, transparency requirements and human oversight are mandatory [4]. The non-profit deploying such a system — even if procured as a service — bears responsibility for correct implementation and documentation.

---

## Concrete use cases for AI

### 1. Donor communications and segmentation

**What it is:** AI analyses giving history, communication response and engagement patterns to personalise donor communications — appropriate tone, relevant campaign timing, suitable donation amount as a suggested ask.

**Value:** donor retention is cheaper than new donor acquisition for most non-profits. Personalised communications significantly improve retention. Campaigns that match a donor's proven engagement consistently outperform generic mailings.

**With local AI:** donor profiles contain financial data (IBAN, giving history), communication histories and sometimes personal notes about contact moments. Keeping that data on your own server means it is not being used for model training on a commercial fundraising platform that also serves competing funds approaching the same donors.

---

### 2. Volunteer scheduling

**What it is:** AI matches availability, skills and preferences of volunteers to specific tasks and schedules — events, daily operations, emergency interventions.

**Value:** no-shows and inefficient deployment are chronic problems in volunteer-based organisations. A smart scheduling assistant that accounts for prior deployment, training level and personal circumstances reduces the coordination burden on the volunteer coordinator.

**With local AI:** volunteer profiles sometimes contain particularly sensitive data — availability driven by personal circumstances, background checks, health limitations. That information belongs on your own server, not on an external platform.

---

### 3. Grant application and reporting support

**What it is:** AI supports the drafting of grant applications, impact reports and annual accounts — structuring information, linguistic refinement, consistency checks across different reporting periods.

**Value:** for small organisations with limited staff capacity, the administrative burden of grant applications and reporting is one of the greatest barriers. AI can substantially reduce that burden.

**With local AI:** grant files and impact reports contain organisational performance data, beneficiary statistics and financial overviews. That is strategic organisational information that does not belong to an external cloud service.

---

### 4. Beneficiary intake and file management

**What it is:** AI helps structure intake forms, flag incomplete files and summarise case notes for quick reference.

**Value:** faster and more consistent intake, less administrative delay in service delivery, better handover between staff.

**Caution — AI Act:** if AI automatically decides on access to care or support — or ranks individuals on a waiting list based on a model — human oversight is mandatory [4]. This can qualify as high-risk AI under Annex III. Moreover: beneficiary data is Art. 9 data [1] — processing requires an explicit legal basis beyond standard processing of ordinary personal data.

---

### 5. Impact monitoring and reporting

**What it is:** AI aggregates and visualises programme results — reach, outcomes, trends over time — for governance, funders and the public.

**Value:** stronger substantiation of social impact, more efficient reporting to donors and governments, stronger position in grant applications.

**With local AI:** aggregated beneficiary data — even anonymised — contains sensitive information about the populations the organisation serves. Processing and visualising that data internally is not only legally sounder, it is organisationally cleaner.

---

## The concrete risk with cloud AI

**The CRM fundraising platform scenario:**

A social welfare organisation chooses a US-based cloud CRM with built-in AI for donor management and beneficiary management — a widely used platform in the philanthropy sector.

1. Donor profiles — including IBAN, giving histories and personal communications — are stored on servers in the United States.
2. Beneficiary intake forms — including social vulnerability data and health information (Art. 9 GDPR) — are stored on the same platform, sometimes in the same system.
3. The platform's built-in AI uses all data to train donor scoring models and engagement predictions — including data about the organisation's vulnerable beneficiaries.
4. The platform's terms of use permit the provider to use aggregated data for "product improvement" — a clause that can be interpreted broadly.
5. A data breach or unilateral change to the terms of use simultaneously exposes the financial data of donors and the care data of beneficiaries.
6. The organisation is the data controller — fully liable — and loses at a stroke the trust of both its donors and its beneficiaries. Reputational damage exceeds the direct financial costs.

Donor management, volunteer coordination and beneficiary intake can all run on a local server. Full control over Art. 9 data. No dependence on platforms with commercial interests in reusing that data.

---

## The core message for the first conversation

Do not start with GDPR. Start with trust.

> "Your work is built on trust. Donors trust you with their money and their name. Beneficiaries trust you with their most vulnerable moments. A cloud AI platform that uses that data to train models — and whose terms of use leave room for 'product improvement' — puts that trust at risk. Not theoretically. Concretely, contractually, today."

Continue:

> "Local AI protects that trust. Donor communications, volunteer scheduling, grant files, impact reporting — all of that can run on your own server. The same efficiency, without your data leaving the organisation. That is what you can explain to donors and beneficiaries — and that is what matters."

---

## Questions they ask and how you answer

**"We already use [well-known fundraising platform] — do we have to replace it now?"**

Not necessarily. You can deploy local AI for the tasks where personal data is the input — donor analysis, volunteer scheduling, beneficiary files — and let the existing platform continue handling campaign management or online payments. The key is: what do you process locally, what do you pass to external systems? Making that choice consciously is the starting point.

**"We are a small organisation — nobody is targeting us."**

The DPA (GBA in Belgium, AP in the Netherlands) does not only act on targeted investigations. Complaints from individual members, donors or beneficiaries can trigger a procedure. And in the event of a data breach — even at a small platform — you are legally required to notify as controller. The costs of a data breach for a small non-profit start at tens of thousands of euros, aside from the reputational damage with the audience that funds your work.

**"Our volunteers handle everything manually anyway."**

That is precisely why AI is so valuable for you: volunteers are precious, their time is limited, and administrative overload is one of the primary reasons for dropout. A local AI that takes over scheduling logistics and reporting support gives volunteers more space for the actual mission. And because it runs locally, no data needs to be shared with external platforms.

**"Can AI really help with grant applications?"**

Yes. AI is particularly strong at structuring complex files, formulating impact data consistently, and maintaining the thread through long application documents. A grant manager with access to a well-configured local AI assistant works faster, more consistently and with fewer errors. Human expertise — knowledge of the organisation, the relationship with the funder — remains essential. AI does not replace the writing; it makes it more manageable.

**"What is the difference between local AI and using ChatGPT for our communications?"**

ChatGPT and similar tools are cloud services: everything you enter is processed on external servers and may be used for model improvement. If you paste beneficiary information, donor names or internal organisational data — deliberately or accidentally — that data leaves your organisation. Local AI runs on your own infrastructure. The input goes nowhere. That is the difference.

---

## Belgian and Dutch context

### Belgium

**VZW/ASBL legal form under the CAC.** Associations are the most common legal form for non-profits in Belgium. The CAC [2] imposes specific governance and reporting obligations that presuppose digital traceability of decisions.

**Tax certificates for donations via FPS Finance.** Associations issuing tax certificates to donors for gifts over €40 are required to register these and submit them annually to FPS Finance [7]. This requires a reliable and auditable donation management system. Donor data held for this purpose has a statutory retention period of seven years.

**Platform voor Vrijwilligerswerk.** The Flanders Platform for Volunteering and equivalents in other regions publish guidelines on volunteer policy, including privacy protection for volunteers.

**DPA recommendations for non-profits.** The Gegevensbeschermingsautoriteit (GBA) has published specific recommendations for associations on the lawful processing of member and donor data, consent versus legitimate interest, and the protection of sensitive beneficiary data [5].

### Netherlands

**Foundations and associations under the Dutch Civil Code.** The legal foundations for non-profits in the Netherlands are Book 2 of the Civil Code and the WBTR [3], with emphasis on director accountability and transparency.

**CBF — Centraal Bureau Fondsenwerving.** The CBF quality mark [6] is the standard for fundraising organisations in the Netherlands. CBF-certified organisations must meet strict requirements on governance, transparency and donor data handling. A data breach or privacy violation can result in loss of the mark — with direct impact on donation income.

**ANBI status.** Organisations with ANBI status (public benefit organisation) enjoy tax benefits for themselves and their donors, but are required to be transparent about governance, objectives and finances — including via website publication. This presupposes a solid digital registration and reporting system.

**AP — Autoriteit Persoonsgegevens.** The AP has published recommendations for associations on the processing of member data, with specific attention to consent requirements and retention periods [8].

---

## Sector figures (reference)

- Number of active VZW/ASBLs in Belgium: approx. 80,000 (Statbel, 2024)
- Number of foundations and associations in the Netherlands: approx. 200,000+ (CBS, 2024)
- Volunteers in Belgium: approx. 1.1 million active volunteers in organised settings
- Volunteers in the Netherlands: approx. 4.5 million active volunteers
- Average share of donor funding at Belgian social welfare VZWs: 15–30% of total budget
- Average share of subsidies at Dutch non-profits: 40–60% of total budget
- Average cost of a data breach for a small business or non-profit: €15,000–50,000 (IBM Cost of Data Breach Report 2024, adjusted for SME scale) — with reputational damage among donors and beneficiaries potentially a multiple of that

---

## Sources

1. **GDPR — Regulation (EU) 2016/679 (incl. Art. 9 special categories of personal data)**
   EUR-Lex, fully consolidated text
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj>

2. **CAC — Act of 23 March 2019 on the Code of Companies and Associations (Belgium)**
   Belgian Gazette via e-Justice
   <https://www.ejustice.just.fgov.be>

3. **WBTR — Act on Governance and Oversight of Legal Entities (2021, Netherlands)**
   Overheid.nl — National legislation database
   <https://wetten.overheid.nl/BWBR0044286/>

4. **AI Act — Regulation (EU) 2024/1689 — Risk classification and high-risk systems**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

5. **GBA — Gegevensbeschermingsautoriteit — recommendations for non-profits and associations**
   <https://www.gegevensbeschermingsautoriteit.be>

6. **CBF — Centraal Bureau Fondsenwerving — quality mark and standards**
   <https://www.cbf.nl>

7. **FPS Finance — Tax certificates for donations to associations (Belgium)**
   <https://financien.belgium.be>

8. **AP — Autoriteit Persoonsgegevens — recommendations for associations**
   <https://www.autoriteitpersoonsgegevens.nl>

---

_Part of: LocAI Library · Sector Dossiers_
_Previous: S08 — Estate Agents_
_Next: S10 — Transport & Logistics_
_Last updated: 25 March 2026_

---

## References

_[ references follow during research ]_

---

_Part of: LocAI Library · Sector Dossiers_
_Previous: S08 — Estate Agents_
_Next: S10 — Transport & Logistics_
_Last updated: March 2026_
