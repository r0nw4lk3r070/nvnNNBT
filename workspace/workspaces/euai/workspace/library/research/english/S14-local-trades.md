# S14 — Local Retail & Trades
### LocAI Library · Sector Dossier
_Version 0.1 · 25 March 2026_

---

## Who they are

Local retail and trades form the backbone of the Belgian and Dutch high street. Bakers, butchers, florists, bookshops, bicycle repair shops, cheese specialists, local clothing boutiques — sole traders and small partnerships with one or two employees who know their neighbourhood, know their customers by name, and have built supplier relationships over years.

This is the most accessible entry point for LocAI. Not because the data protection challenges are large — but precisely because they are small and recognisable. The baker immediately understands why their customer list is their own property. The florist sees the value of AI that quickly drafts a seasonal promotion. The bicycle mechanic saves time when AI places an order with a regular supplier.

**Typical profiles:**
- Food retail — bakers, butchers, delicatessens, cheese specialists, fishmongers
- Flowers and plants — florists, garden centres
- Leisure and culture — bookshops, toy shops, hobby stores
- Services — bicycle repair, shoe repair, key cutting, tailoring
- Fashion retail — local clothing shops, fashion boutiques

**What distinguishes them:** they are not IT companies. They have no DPO, no compliance department, no legal team. They do have a customer list, an invoice history, supplier contacts, and sometimes a loyalty card. That is already enough to fall within the GDPR — and enough for AI to be useful.

---

## What data they process

**Customer data:**
- Names and contact details of regular customers
- Orders and order history (phone, email, WhatsApp)
- Loyalty card data — name, purchases, points balance
- Email addresses for newsletters or promotions

**Accounting data:**
- Invoices to private customers (name, address, VAT number if commercial)
- Cash and payment history
- Supplier invoices and contracts

**Supplier data:**
- Contact persons at suppliers
- Order history and pricing agreements
- Delivery schedules

**Employee data (where applicable):**
- Name, address, employment contract of the few staff members
- Work schedule and hours worked
- Salary data

**What makes this distinctive:** the scale is small but the principles are identical to those of larger businesses. A name and email address in an order list are personal data. A loyalty card is a processing activity that requires explanation. The GDPR makes no exceptions based on turnover or headcount.

---

## Which laws apply

### GDPR — Basic principles for everyone

The GDPR applies to every processing of personal data by every business, regardless of size [1]. For small retailers and tradespeople, the essential obligations are:

- **Transparency:** customers must know what data you collect and why. A short privacy notice on a poster or website is sufficient for most activities.
- **Purpose limitation:** data collected for orders may not be used for marketing without consent.
- **Retention:** invoice data must be kept for 7 years for tax purposes. Orders from customers who have not bought in two years: those can go.
- **Security:** a customer list on an unsecured laptop is a risk. A password and disk encryption are minimal measures.

**Exception for small processors:** businesses with fewer than 250 employees are in certain cases exempt from the processing records obligation (Article 30(5) GDPR) — but that exemption does not apply to regular processing activities or processing of special categories of data. A loyalty card programme is a regular processing activity.

### AI Act — Minimal risk for most applications

Most AI applications for local retail fall in the minimal risk category [2]. Text generation for promotions, assistance with order lists, social media content — these are AI systems without decision-making weight over individuals and without special data processing. They require only honesty: if you use AI to respond to a review, you respond as yourself — not as a robot.

**Where it can differ:** a loyalty programme that uses AI to generate personalised offers based on purchase behaviour starts moving toward an AI system with a profiling component. That is not legally prohibited, but requires attention to the purpose limitation principle and transparency.

### VAT legislation

Keeping invoices is not just a GDPR question — it is also a fiscal obligation. In Belgium, a 7-year retention obligation applies to accounting documents [3]. In the Netherlands the same: 7 years (General Tax Act) [4]. AI supporting accounting processes therefore works with data that must already be retained for tax reasons.

---

## Concrete use cases for AI

### 1. Customer communication

**What it is:** AI writes responses to customer emails, WhatsApp messages, and order confirmations in the trader's own tone of voice.

**Value:** less time at the screen, more consistent communication, more professional appearance even for a small business.

**With local AI:** customer communications contain names and contact details. That data does not leave the workplace.

---

### 2. Order lists and inventory management

**What it is:** AI analyses sales history and generates weekly order lists or restocking suggestions.

**Value:** less waste, better anticipation of seasonal variations, fewer forgotten orders.

**With local AI:** sales data and supplier information is commercially confidential and does not need to be on an external platform.

---

### 3. Social media content

**What it is:** AI generates posts for Instagram, Facebook, or newsletters — seasonal promotions, product introductions, opening hours.

**Value:** regular social media presence without spending hours per week on it. A well-written post about fresh strawberries takes the baker two minutes.

**Practical note:** social media content rarely contains personal data. This is the cleanest AI application for local retail: no data risk, direct value.

---

### 4. Basic accounting support

**What it is:** AI helps categorise expenses, structure invoice overviews, or prepare VAT return summaries for the accountant.

**Value:** less time on administration, fewer errors when submitting documents to the monthly accountant.

**With local AI:** accounting information contains the business's financial data and client data (in invoices). That data does not belong in a cloud accounting system from a third party without an explicit processing agreement.

---

### 5. Inventory tracking and supplier orders

**What it is:** AI helps track stock levels and automates repeat orders to regular suppliers.

**Value:** less stockout, less overstock, time savings on the weekly supplier round.

**Practical note:** for local retail, this is the most direct time saving AI can deliver — with no data governance complications whatsoever.

---

## The concrete risk with cloud AI

**The free tool scenario:**

A baker uses a free AI writing tool to draft his weekly promotions and reply to customer emails.

1. He regularly pastes customer names and addresses into the tool for personalised messages. Those names go to the cloud provider's servers and train the model.
2. The tool saves his complete order list when he includes it as context for a supplier email. His supplier information and pricing agreements are now at an external party.
3. The tool is acquired by another company. The terms of service he never read permit use of his data for model training.
4. A customer asks him how their name ended up in promotional emails from a third-party company. He has no answer.

A local AI tool running on his own laptop or server: he types his content, the AI generates the text, nothing leaves the workplace. Free tools are rarely truly free — the price is the data.

---

## The core message for the first conversation

Never start with compliance. Start with recognition.

> "You have a customer list. That list is yours — built through years of good work. AI can help you use it efficiently for promotions, orders, and communication. What we avoid is leaving that list with an external provider."

Follow with:

> "The GDPR applies to you too — but for a small business the obligations are very manageable: a short privacy notice, knowing what data you hold, and a password on your laptop. That's it. AI that runs locally fits perfectly into that picture."

---

## Questions they ask and how you answer

**"GDPR is for big companies, isn't it?"**

No. The GDPR applies to every organisation that processes personal data, regardless of turnover or size. A name in an order book is personal data. That said, the obligations for a small business are relatively light — the challenge is not the weight of the rules but awareness that they exist.

**"I just use ChatGPT — is that a problem?"**

As long as you don't enter customer data, payment information, or personal details: no. The moment you include names, email addresses, or customer-specific information, you are sending personal data to an OpenAI server in the US. That is technically a transfer of data to a third party — which requires either a processing agreement or an applicable exception. A local AI tool has no such problem.

**"My customer list is just in Excel on my laptop."**

That is a perfectly fine starting point. The question is: does your laptop have a password? Is the drive encrypted? Do you back up regularly? Those three things are the basic security the GDPR asks of you — nothing more, nothing less for a list of customer names and email addresses.

**"I don't have time for all these rules — I have a business to run."**

Fair point. That's exactly why the entry level is simple. You don't need a DPO. You don't need an extensive register. You need a short privacy notice (half an A4, available as a template), a password on your customer data, and awareness that you don't share customer information carelessly. AI that helps you with that rather than creating obstacles: that's precisely the point.

**"My loyalty card — do I need to ask permission for that?"**

Yes. A loyalty card processes personal data (name, purchase history) for a marketing purpose. That processing requires either legitimate interest or consent at sign-up. In practice: a short form at registration explaining what you record and how the points work. That is sufficient.

---

## Belgian and Dutch context

### Belgium

**UNIZO** [5] is the Union of Self-Employed Entrepreneurs — the largest interest group for self-employed people and SMEs in Belgium. UNIZO publishes practical GDPR guides for self-employed people and operates an enterprise desk that answers legal questions.

**The GBA — Data Protection Authority** [6] has published simplified tools specifically for small businesses: a model register, a privacy notice generator, and a checklist. These are available free of charge on their website.

**Business registration offices** (Unizo, UCM, Securex, Acerta) also offer GDPR guidance for people starting a business.

### The Netherlands

**MKB-Nederland** [7] is the main business organisation for small and medium-sized enterprises in the Netherlands. MKB-Nederland has GDPR tools and sector-specific guides for small business owners.

**The AP — Data Protection Authority** [8] has a dedicated SME section on its website with practical tools, model contracts, and FAQs. The AP also recognises that small businesses deserve a proportionate approach.

**KvK ondernemersplein** also offers a free GDPR starter pack for sole traders and small businesses.

---

## Sector figures (reference)

- Number of self-employed persons and small businesses in Belgian retail: approx. 55,000 (Statbel, 2024)
- Number of sole traders and micro-businesses in Dutch retail: approx. 80,000 (CBS, 2024)
- Share of Belgian SMEs with a documented GDPR approach: estimated 35% (GBA survey, 2023)
- Number of GBA complaints per year from consumers: approx. 3,500 (GBA, 2023) — predominantly involving larger players, but trend rising for retail

---

## References

1. **GDPR — Regulation (EU) 2016/679**
   EUR-Lex, full consolidated text
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj>

2. **AI Act — Regulation (EU) 2024/1689 — risk classification**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

3. **Belgian accounting retention obligation — Code of Economic Law Art. III.86**
   <https://economie.fgov.be>

4. **Dutch retention obligation — General Tax Act Art. 52**
   <https://wetten.overheid.nl>

5. **UNIZO — Union of Self-Employed Entrepreneurs**
   <https://www.unizo.be>

6. **GBA — Data Protection Authority (Belgium)**
   <https://www.gegevensbeschermingsautoriteit.be>

7. **MKB-Nederland**
   <https://www.mkb.nl>

8. **AP — Autoriteit Persoonsgegevens (Netherlands)**
   <https://www.autoriteitpersoonsgegevens.nl>

---

_Part of: LocAI Library · Sector Dossiers_
_Previous: S13 — Construction & Contractors_
_Last updated: March 2026_
