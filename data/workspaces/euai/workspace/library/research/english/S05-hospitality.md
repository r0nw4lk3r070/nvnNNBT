# S05 — Hospitality
### LocAI Library · Sector Briefing
_Version 0.1 · 25 March 2026_

---

## Who they are

The hospitality industry is different from the other sectors in this library. No professional secrecy, no special categories of data, no statutory conformity assessments. But it is a sector that runs on margins, people, and momentum — and where AI can make a visible, tangible difference in day-to-day operations.

A restaurant, a café, a boutique hotel — these are businesses where the owner is simultaneously chef, manager, marketer, buyer, and host. Where a bad week can make the difference between profit and loss. Where personal service is the only real differentiator.

AI that supports that — without sending data anywhere else — fits perfectly into that picture.

**Typical profile:**
- Independent owner-operator or small group of 2–5 locations
- 5–30 employees
- Seasonal peaks, fluctuating staffing levels
- Thin margins — food costs 28–35%, labour costs 30–40%
- Little time for administration
- Strong personal character — the operator IS the brand

**Specific business types:**
- Restaurant owners — from chip shops to gastronomic restaurants
- Café owners — from traditional brown cafés to cocktail bars
- Hoteliers — boutique hotels, B&Bs, aparthotels
- Caterers — events, corporate canteens, school cafeterias
- Food trucks and pop-ups

---

## What data they process

The data in the hospitality industry is less sensitive than in the previous sectors — but still relevant.

**Guest data:**
- Reservation details — name, phone number, email, number of guests
- Preferences and allergies — dietary restrictions, favourite dishes
- Loyalty data — visit frequency, spending, special occasions
- Payment data — credit card details (via payment terminal, rarely stored directly)

**Employee data:**
- Employment contracts and payroll data
- Schedules and availability
- Sick leave and holiday

**Operational data:**
- Sales figures per dish, per day, per shift
- Inventory management — incoming goods, consumption, waste
- Supplier data — contacts, prices, delivery times
- Energy consumption and costs

**What makes this data distinctive:**
Allergy data is a special category under GDPR [1] — it is health data. A guest who indicates they are gluten-intolerant or have a nut allergy is sharing medical information. That warrants extra care.

Beyond that, data in the hospitality industry is less sensitive than in the previous sectors — but its operational value is enormous. Knowing who your best customers are, which dishes sell best, when peak periods occur — that is gold for a small hospitality business owner.

---

## Which laws apply

### GDPR — Applicable but less intensive

Reservation data, loyalty data, employee data — all personal data. The basic principles of GDPR apply.

**Allergy data — special category:**
Health data requires additional protection. A reservation system that stores and processes allergy data is processing special category data. The legal basis: Art. 9(2)(c) (protection of vital interests) [1] — the allergy information is necessary to protect the health of the guest.

**Retention periods:**
Reservation data may not be retained longer than necessary. A guest who makes a single reservation and never returns has, after a reasonable period, the right to be forgotten.

**Employee data:**
Payroll data, schedules, sick leave — personal data of employees. Legal basis: performance of an employment contract (Art. 6(b)).

### AI Act — Minimal risk for most applications

Menu recommendations, inventory management, scheduling — all minimal risk. No high-risk AI in the typical hospitality context.

**Exception:** if AI is used for staffing decisions (who gets which shift, who is dismissed) — then it may be high-risk (Annex III, point 4) [2]. Human oversight remains mandatory.

### Employment law

The hospitality industry has specific employment legislation — flexible contracts, overtime, night work, student employment. AI that generates schedules must take these rules into account.

**Belgium:** joint labour committee 302 (paritair comité 302) [4] with specific collective labour agreements (CLAs).
**Netherlands:** cao Horeca (hospitality CLA) with specific provisions on working hours.

---

## Concrete AI use cases

This is where hospitality differs fundamentally from the other sectors. The use cases are not primarily aimed at compliance — they are aimed at operational efficiency and guest experience.

### 1. Menu recommendations and allergy guide

**What it is:** a local AI assistant that helps guests choose dishes based on their preferences and dietary restrictions.

**Two forms:**
- Internal (for staff): a member of staff asks "which dishes are gluten-free and nut-free?" and receives an immediate answer.
- External (for guests): a tablet or QR code where guests enter their allergies themselves and receive tailored menu suggestions.

**Value:** fewer errors with allergies (avoiding life-threatening risk), faster service, better guest experience.

**With local AI:** guests' allergy data does not leave the restaurant. No cloud server storing guests' health data.

---

### 2. Inventory management and order prediction

**What it is:** AI analyses sales data, seasonal patterns, and weather forecasts to predict how much of each product needs to be ordered.

**Time savings and cost savings:** ordering too much leads to food waste. Ordering too little leads to "sold out" on the menu — lost revenue and disappointed guests. AI optimises this.

**Concrete example:** a restaurant knows that on warm summer Friday evenings, rosé wine sales rise by 40%. A local AI that recognises this pattern warns in good time to reorder.

**With local AI:** sales data and ordering patterns — commercially sensitive information — remain internal. No competitor gaining insight into your best-sellers via a cloud platform.

---

### 3. Staff scheduling

**What it is:** AI generates an optimal schedule based on expected occupancy, employee availability, CLA rules, and costs.

**Time savings:** creating a schedule for 15 employees over 4 weeks takes hours. AI produces a first draft in minutes.

**Value:** less over- and understaffing, more satisfied employees, lower labour costs.

**With local AI:** schedules and employee availability data remain internal. Employee data does not go to an external server.

---

### 4. Multilingual guest communication

**What it is:** a local AI that assists with communication with guests in different languages — translating menus, answering emails, drafting reservation confirmations.

**Value:** in tourist areas, guests come from dozens of countries. AI enables professional multilingual communication without an external translation service.

**With local AI:** guest communication — including any personal information in emails — remains internal.

---

### 5. Daily financial summary

**What it is:** AI generates a concise summary of the financial results at the end of each day — revenue, costs, margin per category, comparison with the previous week.

**Value:** an operator who knows how their day went without spending an hour in Excel can course-correct faster.

**With local AI:** revenue figures and cost data — commercially sensitive — remain internal.

---

### 6. Recipes and cost price calculation

**What it is:** AI helps calculate the cost price of dishes, adjust recipes when purchase prices change, and suggest menu changes to improve margins.

**Value:** in hospitality, the margin on every dish is critical. AI that automatically calculates what a dish costs when ingredient prices rise saves time and prevents loss-making items.

**With local AI:** recipes and cost price data — sometimes knowledge developed over many years — remain internal.

---

## The argument for hospitality: different from the other sectors

With accountants, therapists, lawyers, and doctors, the primary argument is: professional secrecy and GDPR risk.

With hospitality, the primary argument is different: **operational value and competitive advantage.**

A restaurant owner who sends their sales data, their recipes, and their customer preferences to a cloud platform is giving away valuable business intelligence. Not to a regulator — but to a tech platform that uses that data to improve, analyse, and potentially monetise its services.

Local AI keeps that knowledge internal. Your best-sellers, your margins, your customer patterns — those stay yours.

And there is a second argument that makes hospitality different: **visibility.**

An allergy assistant on a tablet at the table is visible to guests. An AI that provides menu tips in multiple languages is noticeable. That is a differentiating factor — a way to stand out from the competitor still working with a paper menu.

---

## The core message for the first conversation

Don't start with GDPR or the AI Act — these are less urgent in this sector. Start with the operational pain.

> "How much time do you spend each week on schedules, orders, and administration? And how much of that time comes at the expense of your guests?"

Follow-up:

> "Local AI handles those tasks faster — schedules, inventory management, financial summaries. And everything stays internal. Your sales data, your recipes, your customer information does not go to an external platform."

For the more tech-savvy operator:

> "Imagine: a tablet at the table where guests enter their allergies and immediately receive tailored menu suggestions. Fully in your own style, on your own hardware. No subscription, no platform storing your guest data."

---

## Questions they ask and how to answer

**"I already have a POS system (point-of-sale) that does this."**

POS systems handle transaction management. They do not analyse, they do not advise, and they do not communicate with guests. Local AI is a layer on top of your POS system — it makes the data actionable.

**"My margins are too thin for additional investment."**

The hardware investment is a one-off. What comes back: less food waste, a more optimal schedule, less overtime. The payback period is typically 6–18 months, depending on scale.

**"I don't have any IT knowledge."**

You don't need it. The interface is as simple as a smartphone. Installation and configuration is done for you. After that, you use it like any other device.

**"What if the system goes down during a busy period?"**

Local AI works offline. No internet dependency. If the system goes down, you restart it — and you're back. No dependency on a cloud provider that might also be having problems on a Saturday evening.

**"My staff aren't technical."**

A menu recommendation tool or an inventory assistant doesn't need to be technical. If your staff can operate a smartphone, they can use this.

---

## Special attention: hotels and B&Bs

Hotels process more data than restaurants — passport details, payment data, stay history.

**Passport details:** in Belgium and the Netherlands, hotels are legally required to register the identity details of guests (aliens legislation). That data may not be retained longer than legally required.

**AI use cases specific to hotels:**
- Personalised welcome communication
- Remembering room preferences for returning guests
- Dynamic pricing based on occupancy rate
- Local recommendations for guests

**Privacy consideration:** hotel data is more sensitive than restaurant data. Stay history can contain sensitive information — who someone travels with, how often, when. Local storage is the safest choice.

---

## Special attention: the food truck and pop-up

Smallest scale, most limited resources. But local AI is relevant here too.

A food truck owner who operates at different locations benefits from AI that analyses which locations are most profitable, which dishes sell best at which location, and when purchasing needs to happen.

For this scale, a powerful laptop is sufficient — no separate mini-PC needed.

---

## Belgian and Dutch context

### Belgium

**Federatie Horeca Vlaanderen** [3] — sector organisation for the Flemish hospitality industry.

**Joint labour committee 302 (Paritair comité 302)** [4] — specific collective labour agreements (CLAs) for hospitality, including arrangements for flexi-jobs (a Belgian system allowing employees with a primary job to work extra hours in hospitality), student employment, and overtime.

**Flexi-jobs:** a Belgian system whereby employees with a primary job can work additional hours in the hospitality industry. AI scheduling must take flexi-job regulations into account.

**Cash register systems:** the use of a certified cash register system (GKS/SCE) is mandatory in the Belgian hospitality industry for restaurants. Local AI can integrate with GKS data.

### Netherlands

**KHN** [5] — Royal Dutch Hospitality Association (Koninklijke Horeca Nederland). Sector organisation.

**Cao Horeca** — collective labour agreement (CLA) with specific provisions on working hours, supplements, and holiday entitlement.

**Tourist tax:** hotels are required to register and remit tourist tax. AI can assist with calculation and reporting.

---

## Sector figures (reference)

- Number of hospitality businesses in Belgium: approximately 50,000
- Number of hospitality businesses in the Netherlands: approximately 40,000
- Average margin in restaurant hospitality: 3–9% net
- Staff turnover in hospitality: 70–80% per year (one of the highest of all sectors)
- Food waste as a percentage of revenue: average 4–10%
- Potential savings via AI inventory optimisation: 1–3% of revenue

---

## References

1. **GDPR — Regulation (EU) 2016/679, Art. 9 — Special categories (health data)**  
   EUR-Lex, Official Journal of the European Union  
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/nld>

2. **AI Act — Regulation (EU) 2024/1689, Annex III — High-risk employment AI**  
   EUR-Lex, Official Journal of the European Union  
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

3. **Federatie Horeca Vlaanderen — Sector representation and employment conditions**  
   <https://www.horeca.be>

4. **PC 302 — Joint Labour Committee for the hotel industry (Belgium)**  
   Federatie Horeca Vlaanderen  
   <https://www.horeca.be/nl/sociaal-recht/paritair-comite>

5. **KHN — Royal Dutch Hospitality Association (Koninklijke Horeca Nederland)**  
   <https://www.khn.nl>

---

_Part of: LocAI Library · Sector Briefings_
_Previous: S04 — Medical & Dental Practices_
_Next: S06 — Other Sectors_
_Last updated: 25 March 2026_
