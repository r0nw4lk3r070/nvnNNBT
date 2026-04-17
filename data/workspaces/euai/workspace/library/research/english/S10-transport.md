# S10 — Transport & Logistics
### LocAI Library · Sector Dossier
_Version 0.1 · 25 March 2026_

---

## Who they are

Transport and logistics companies handle the physical movement of goods and people — and they do so through a dense network of connected systems: GPS trackers, tachographs, fleet management platforms, route optimisation software. That infrastructure generates continuous employee data. Before a single AI tool is even mentioned, these companies already process sensitive personal data in quantities and at a granularity that few other sectors match.

AI is genuinely useful in transport. Route optimisation, driving behaviour analysis, predictive maintenance scheduling, customer communication — these all have real efficiency value. But AI in transport operates in a sector where employee monitoring is the dominant data risk, and where category-specific regulations — EU Regulation 561/2006, the tachograph regulation — create a compliance environment that most cloud tools do not address.

**Typical profile:**
- Road haulage companies — domestic and cross-border freight
- Courier and last-mile delivery services
- Logistics service providers — warehousing, distribution, fulfilment
- Bus and coach operators — passenger transport
- Self-employed drivers and owner-operators working for larger fleets

**What distinguishes them:** the driver is the core asset — their time, location, rest breaks, fuel consumption, and driving behaviour are all data points. That data is legally required in some cases (tachograph) and commercially valuable in others (route efficiency). The GDPR and the AI Act both treat employee monitoring as a category requiring heightened care.

---

## What data they process

**Driver and employee data:**
- Continuous GPS location data during working hours
- Tachograph data — driving times, rest periods, speed readings
- Driving behaviour data — braking, acceleration, fuel consumption
- Rest and break records (legally required under Regulation 561/2006)
- Personal details — name, address, driving licence, professional certifications

**Fleet and operational data:**
- Vehicle positions and route histories
- Maintenance schedules and service records
- Fuel consumption and efficiency metrics
- Route planning data and client delivery schedules

**Customer and shipment data:**
- Delivery addresses (including private individuals)
- Shipment contents, weights, and handling requirements
- Customer contacts and communication history
- Commercial agreements and pricing arrangements

**What makes this distinctive:** location data is continuous and linked to an individual. Track someone's location at 30-second intervals for a year and you have information about their home, their routines, their personal stops. The GDPR treats continuous employee location tracking as sensitive processing requiring lawful basis, proportionality, and transparency — and the AI Act classifies tools that monitor employees as high-risk.

---

## Which laws apply

### GDPR — Employee location tracking and proportionality

The GDPR requires a lawful basis for processing employee location data [1]. Legitimate interest is the most commonly cited basis — but it has conditions: the processing must be necessary, proportionate, and the employee's fundamental rights must not override the employer's interest. Continuous 24/7 tracking without clear operational justification does not meet the proportionality test.

Employees must be informed — what is tracked, why, for how long, who has access. Works councils and union representatives in both Belgium and the Netherlands have consultation rights before monitoring systems are introduced.

### AI Act — Annex III: employee monitoring as high-risk AI

The AI Act explicitly classifies AI systems used to monitor or evaluate workers as high-risk under **Annex III, Point 4** (Employment, workers management and access to self-employment) [2]. This includes systems that analyse driving behaviour to rate or rank drivers, systems that identify anomalies in working patterns, and any AI that makes or influences employment-related decisions based on monitored data.

High-risk obligations include: technical documentation, logging and auditability, human oversight with override capability, and — critically — transparency toward the affected employees. A driver has the right to know that an AI system is analysing their driving behaviour and how that analysis influences decisions about them.

### EU Regulation 561/2006 and the tachograph regulation

Driving time, rest period, and break records are legally mandated data under EU Regulation 561/2006 [3]. This creates a specific compliance obligation around data that partially overlaps with GDPR: you must collect it, and you must store it correctly. Any AI system that processes tachograph data for compliance purposes operates at the intersection of employment law, road safety law, and data protection.

### NIS2 Directive

Large logistics operators are increasingly recognised as operators of essential services [4]. The NIS2 Directive mandates cybersecurity risk management and incident reporting. Fleet management systems, route planning platforms, and logistics execution systems are all potential attack surfaces.

---

## Concrete use cases for AI

### 1. Route optimisation

**What it is:** AI analyses historical route data, real-time traffic, delivery windows, and vehicle capacities to generate optimal route plans.

**Value:** significant fuel savings, better delivery reliability, lower CO₂ emissions, and reduced driver stress from unrealistic scheduling.

**With local AI:** route planning involves customer addresses, delivery windows, and commercially sensitive logistics data. Route history also reveals fleet capacity, client concentrations, and operational patterns that competitors would value.

---

### 2. Driving behaviour analysis

**What it is:** AI analyses tachograph and telematics data to detect patterns — harsh braking, excessive speed, fatigue indicators — and flags them for fleet managers.

**Value:** improved road safety, reduced accident costs, lower insurance premiums, and fuel efficiency gains.

**AI Act classification:** this is employee monitoring AI under Annex III [2]. Full high-risk obligations apply: documentation, logging, human review of AI-generated risk ratings, and transparency to drivers. A driver who receives a safety warning generated by an AI system must be able to understand the basis for that assessment.

---

### 3. Predictive maintenance

**What it is:** AI analyses service history, mileage, usage patterns, and sensor data to predict when components need attention before they fail.

**Value:** less unplanned downtime, lower repair costs, better roadworthiness compliance, and extended vehicle lifespan.

**With local AI:** vehicle maintenance data is commercially sensitive. Fleet age, reliability profile, and maintenance costs inform competitive positioning and insurance premiums.

---

### 4. Customer communication

**What it is:** AI drafts delivery notifications, delay communications, and responses to customer queries based on route status and shipment data.

**Value:** reduced manual communication burden on dispatchers, more consistent customer experience, faster exception handling.

**With local AI:** customer communications involve names, addresses, and shipment details. Consumer delivery addresses are personal data under the GDPR.

---

### 5. Tachograph compliance assistance

**What it is:** AI reviews tachograph data for compliance with Regulation 561/2006 — identifying potential rest period violations before social inspectors do.

**Value:** proactive compliance management, reduced risk of fines, better documentation for labour inspections.

**Note:** this is a legal compliance tool operating on mandatory data. Output must be reviewed by a human — AI flags potential violations, but the compliance decision remains with the transport manager.

---

## The concrete risk with cloud AI

**The telematics platform scenario:**

A transport company switches to a modern cloud fleet management platform with built-in AI driving behaviour scoring.

1. Every driver's GPS position is transmitted every 30 seconds to servers outside the EU.
2. The driving behaviour AI scores each driver daily — braking, cornering, speed adherence — and generates a driver risk rating. This is high-risk AI under Annex III [2]. The platform cannot provide the required technical documentation.
3. The scoring model was trained on aggregated data from all platform users — including your drivers' historical data, which now trains a model shared with competitors.
4. A union representative requests access to the AI scoring model on behalf of a driver who received a poor rating. You cannot provide it.
5. The Belgian or Dutch social inspectorate requests the data trail for a rest period investigation. The data is on servers you do not control.

Local AI for route planning and maintenance scheduling: operational intelligence stays on your own servers, driver data does not leave the company environment, and AI Act compliance remains within your control.

---

## The core message for the first conversation

Start with the monitoring obligation — not the AI regulation.

> "Your vehicles generate continuous location and behaviour data for every driver, every shift. That data has a legal basis — but it also has GDPR boundaries. And if you use AI to analyse it, the AI Act classifies that as high-risk. That is not theoretical. It means documentation, transparency to drivers, and human oversight of every AI-generated assessment."

Follow with:

> "Local AI gives you the efficiency — route optimisation, maintenance alerts, compliance checks — without your drivers' continuous location data leaving your network. That is the architecture that makes both GDPR and AI Act compliance manageable."

---

## Questions they ask and how you answer

**"Our telematics provider handles GDPR — they're certified."**

Certification covers the provider's own processing. It does not make you compliant as the controller. You decided to collect this data, for this purpose, about these employees. That makes you the controller — and the controller's responsibilities are yours regardless of what the processor has certified.

**"Drivers know they're tracked. They signed a clause in their contract."**

Contractual acknowledgement of tracking is not a valid lawful basis under the GDPR. If tracking is genuinely necessary for operational purposes, a properly documented legitimate interest assessment is the more defensible basis. Knowing they are tracked is also different from understanding how AI uses that data to score them.

**"The AI system just shows us the data — the manager still decides."**

If the AI scores, ranks, or flags drivers — even if a manager has the final word — the AI is influencing employment-related decisions. That puts it in Annex III. Human oversight is required, but it does not remove the classification or the compliance obligations.

**"We're a small haulage company. Does this really apply to us?"**

Size does not create a GDPR exemption. If you track your drivers' locations — and most hauliers do — the GDPR obligations apply. The AI Act applies when you deploy an AI system. If your fleet management platform includes AI driving scoring, you are an AI deployer under the Act.

**"What about tachograph data — we have to keep that anyway."**

Yes. Mandatory retention under Regulation 561/2006 is a legal obligation — that is the lawful basis for that specific data. But the obligation to retain for compliance purposes does not extend to analysing it with AI without its own lawful basis and AI Act compliance. Tachograph data retained for inspectorate access and tachograph data fed into an AI scoring model are two different processing activities.

---

## Belgian and Dutch context

### Belgium

**FEBETRANS** [5] is the federation of Belgian road transport operators. FEBETRANS publishes guidance on labour relations, driving time compliance, and speaks primarily for small and medium-sized hauliers.

The **National Social Security Office (RSZ)** and the **Social Inspectorate** enforce driving time rules and labour law in the transport sector. Inspections are targeted and include tachograph data review.

**Joint Committee 140 (PC 140)** sets the collective labour agreement for road transport in Belgium. Any introduction of AI monitoring systems must be assessed against information and consultation obligations under social law.

### The Netherlands

**TLN — Transport en Logistiek Nederland** [6] is the largest Dutch transport sector organisation, representing road hauliers, logistics companies, and courier services.

**ILT — Inspectie Leefomgeving en Transport** enforces driving time regulations and transport licensing in the Netherlands. Tachograph data is a primary inspection tool.

**FNV Transport & Logistiek** and **CNV Vakmensen** hold active positions on driver monitoring and AI use in the sector.

---

## Sector figures (reference)

- Number of Belgian road transport companies: approx. 14,000 (Statbel, 2024)
- Number of Dutch transport and logistics companies: approx. 30,000 (CBS, 2024)
- Share of transport companies using telematics: >80% (Transporeon / TLN survey, 2023)
- Average cost of a tachograph violation per offence (BE): €1,800–3,600 (Social Inspectorate tariff table)
- Average cost of a data breach for an SME: €15,000–50,000 (IBM Cost of Data Breach Report 2024, adjusted for SME scale)

---

## References

1. **GDPR — Regulation (EU) 2016/679**
   EUR-Lex, full consolidated text
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj>

2. **AI Act — Regulation (EU) 2024/1689 — Annex III (employee monitoring = high-risk)**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

3. **EU Regulation 561/2006 — Driving times and rest periods**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2006/561/oj>

4. **NIS2 Directive — Directive (EU) 2022/2555**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/dir/2022/2555/oj>

5. **FEBETRANS — Federation of Belgian Road Transport**
   <https://www.febetrans.be>

6. **TLN — Transport en Logistiek Nederland**
   <https://www.tln.nl>

---

_Part of: LocAI Library · Sector Dossiers_
_Previous: S09 — Non-profit & Associations_
_Next: S11 — HR & Recruitment_
_Last updated: March 2026_
