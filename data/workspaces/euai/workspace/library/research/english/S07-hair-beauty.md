# S07 — Hair & Beauty
### LocAI Library · Sector Dossier
_Version 0.1 · 25 March 2026_

---

## Who they are

Hairdressers and beauty specialists are perhaps the most underestimated data controllers under the GDPR. Everyone thinks of hospitals and law firms when it comes to sensitive data. But a hairdresser who records that a regular client is allergic to PPD (para-phenylenediamine — a commonly used dye) is storing medical information. A beauty therapist who registers skin conditions for treatment advice: the same applies.

These are small businesses — a sole trader or a salon with two or three employees. No legal department. No data protection officer. But the law makes no exception based on business size.

**Typical profile:**
- Hairdressing salon: 1–5 employees, loyal client base, high repeat visits
- Nail studio, beauty salon, eyebrow bar: predominantly sole traders
- Tattoo and piercing studio: regular clients + one-off visitors
- Barbershop: growing segment, often younger entrepreneurs

**Specific occupational groups:**
- Hairdressers (hair care, colour treatments)
- Beauty therapists (facials, hair removal, skin care)
- Nail stylists
- Tattoo artists and piercers
- Permanent make-up specialists

---

## What data they process

**Appointment data:**
- Name, telephone number, e-mail address
- Appointment history — when, which treatment, with which employee
- No-show and cancellation data

**Treatment history:**
- Products used and colour references
- Results of previous treatments
- Client preferences — "always wants the same colour", "never takes conditioner"

**Health data — the critical point:**
- Allergies to hair colouring products (PPD, ammonia, peroxide) [1]
- Skin conditions relevant to treatment (eczema, psoriasis, rosacea)
- Pregnancy (relevant for certain chemical treatments)
- Medication use (some medications affect hair colour or skin reaction)

This is GDPR Art. 9 health data. The same category as a medical record. The legal basis for processing: Art. 9(2)(a) — explicit consent from the data subject (which a treatment form at the first visit legally anchors), or Art. 9(2)(c) — protection of vital interests (applicable in the case of a serious allergy where the client cannot adequately protect themselves). In practice: the information is necessary to avoid causing harm to the client.

**Visual data:**
- Before or after treatment photographs — increasingly used for portfolio building and social media
- These are personal data. Publication requires explicit consent [2].

**Payment data:**
- Till receipts, payment requests, gift voucher use

---

## Which laws apply

### GDPR — Health data and consent

The allergy and treatment record requires an explicit legal basis for processing [1]. "The client mentioned it verbally" is not a legal basis. A paper card in a drawer is not documented consent.

**What does work:** a simple treatment form at the first visit — an allergy questionnaire, consent for use of the data for future treatments, and separately: consent for photographs. Two signatures, retained with the client file.

**Retention period:** there is no statutory retention period for hairdressing data. The rule of thumb: for as long as necessary for the purpose. For allergy information, that is for as long as the client visits. Upon termination of the relationship: delete.

**Photographs and social media:** posting a photograph on Instagram requires explicit consent from the person depicted [2]. "The client was fine with it" is insufficient — it must be demonstrable in writing or digitally. The consent must also specify the platforms concerned.

### AI Act — Minimal risk with one exception

Appointment management, client communication, product recommendations — minimal risk [3].

**Exception:** if AI is used for scheduling employees on the basis of performance data (who gets which client, who is rostered for busy periods), this is potentially high-risk employment AI (Annex III, point 4) [3]. Human oversight is mandatory.

### Sector regulation

**Belgium:** PC 314 — joint committee for the hairdressing industry [4]. Governs employment contracts, wages, and working hours. The Flemish Hairdressers Federation acts as sector representative.

**The Netherlands:** ANKO — Algemene Nederlandse Kappers Organisatie [5]. The collective labour agreement (CLA) for the hairdressing industry governs employment conditions. Trade association for beauty therapists: ANBOS.

---

## Concrete AI use cases

### 1. Appointment management and reminders

**What it is:** AI sends automatic reminders, manages the diary, and fills vacant slots based on client history and preferred times.

**Value:** no-shows cost the average hairdressing salon 10–15% of turnover. Automatic reminders reduce this significantly.

**With local AI:** diary and client contact data stays in-house. No external booking platforms building and analysing your client database.

---

### 2. Treatment form and allergy questionnaire

**What it is:** AI assists with digitalising and structuring treatment forms. For returning clients: a reminder of relevant allergy information prior to the treatment.

**Value:** a safety gain and legal protection. If a treatment goes wrong and there is no allergy record, the practitioner is in a legally weak position.

**With local AI:** health data does not leave the salon. A cloud booking app that also stores allergy notes sends that data to a server over which you have no control.

---

### 3. Client communication and seasonal offers

**What it is:** AI generates personalised messages based on treatment history — clients who have not visited for a while, seasonal offers, birthday messages.

**Value:** repeat visits are the core of the hairdressing business. A client who receives a reminder six weeks after the previous cut is more likely to return sooner.

**With local AI:** the treatment history and personal notes are the input. These do not belong on an external e-mail platform that exploits them commercially.

---

### 4. Product suggestions and stock management

**What it is:** AI analyses which products sell well, which clients buy which products, and when to reorder.

**Value:** retail (selling products) is a profitable secondary revenue stream for many salons. Better forecasting = less overstock.

**With local AI:** your sales data per product and per client is business information. It does not need to sit on a wholesaler's cloud platform.

---

### 5. Portfolio and social media content planning

**What it is:** AI assists with planning and describing posts — which photographs to post when, which hashtags, which seasonal themes.

**GDPR note:** the photographs themselves are personal data if they show identifiable clients. AI may handle the planning — but the consent documentation is human work and is mandatory [2].

---

## The concrete cloud-AI risk

**The treatment record scenario:**

A hairdresser uses a popular cloud booking app — Treatwell, Fresha, or similar. Convenient: online booking, reminders, payment. What also happens:

1. All client data — name, contact details, treatment history, and any notes on allergies or skin conditions — resides on the platform's servers.
2. The platform terms and conditions give the company the right to use that data for "service improvement" — meaning: training models, analysing patterns, selling insights to partners.
3. If the platform goes bankrupt, is acquired, or is hacked: your client data, including health data, is in other hands.
4. The hairdresser, as data controller, is liable for what happens with that data — including when processed by a processor.

The client who told you she is allergic to PPD did so in confidence. Not to an American SaaS platform.

---

## The core message for the first conversation

Do not start with the law. Start with the relationship.

> "Your clients come to you because they trust you. They tell you things — about their hair, their skin, their health — that they tell no one else. When you hand that information to a cloud platform, you are giving away that trust. Not deliberately. But it is in the small print."

Continue:

> "Local AI means: those notes, that treatment history, that allergy information — it stays between you and your client. As it always has been. Only now organised, searchable, and usable."

---

## Questions they ask and how to answer

**"I just use a paper client card — isn't that safer?"**

For GDPR liability, the medium does not matter — paper also falls under the GDPR. But paper gets lost, cannot be searched, and if there is a fire in the salon you lose everything. A local digital system is both safer and compliant.

**"I don't record any medical things — just 'no ammonia'."**

"No ammonia" due to an allergy is health data under Art. 9. Not because the law wants to be strict, but because an allergic reaction to a hair dye can be life-threatening. The law protects the client and you simultaneously.

**"My clients don't mind me putting their photo on Instagram."**

Verbally "not minding" is not valid consent under the GDPR. You need written or digitally demonstrable consent, specific to each platform. One form at the first visit resolves this permanently.

**"I'm too small — nobody looks at a hairdresser."**

The Belgian DPA (Gegevensbeschermingsautoriteit) and the Dutch DPA (Autoriteit Persoonsgegevens) investigate on the basis of complaints. A client who sees a photograph they never approved can file a complaint. That will cost you more time and money than a proper form ever would.

---

## Belgian and Dutch context

### Belgium

**Coiffure EU / National Association of Hairdressers (Nationaal Verbond van Kappers)** [4] — sector organisation for hairdressers in Belgium. Provides model contracts and sector advice.

**PC 314** — joint committee for the hairdressing industry. Governs collective labour agreements (CLAs) and employment conditions. Flexi-jobs are common in the sector.

**Belgian DPA (Gegevensbeschermingsautoriteit)** — has focused attention on small businesses that process personal data without a data processing agreement with their software supplier.

### The Netherlands

**ANKO** — Algemene Nederlandse Kappers Organisatie. Trade association for hairdressers; provides practical GDPR templates to members [5].

**ANBOS** — Trade association for beauty therapists in the Netherlands.

**Dutch DPA (Autoriteit Persoonsgegevens)** — has published specific guidance on photographs and portrait rights in the context of social media.

---

## Sector figures (reference)

- Number of hairdressing salons in Belgium: approx. 12,000 [4]
- Number of hairdressing salons in the Netherlands: approx. 14,000 [5]
- Average client visits per year: 5–8 times (hair), 12+ times (nails)
- Percentage of salons using digital booking software: approx. 60–70% (2024)
- PPD allergy prevalence in the population: approx. 5–10% — an underestimated risk

---

## References

1. **GDPR — Regulation (EU) 2016/679, Art. 9 — Special categories of personal data**
   EUR-Lex, Official Journal of the European Union
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/nld>

2. **GDPR Art. 6 & 7 — Lawfulness of processing and conditions for consent**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/nld>

3. **AI Act — Regulation (EU) 2024/1689, Annex III — High-risk AI systems**
   EUR-Lex, Official Journal of the European Union
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

4. **National Association of Hairdressers of Belgium (Coiffure EU) — Sector information and labour regulations PC 314**
   <https://www.coiffure.be>

5. **ANKO — Algemene Nederlandse Kappers Organisatie**
   <https://www.anko.nl>

---

_Part of: LocAI Library · Sector Dossiers_
_Previous: S06 — Retail & E-commerce_
_Next: S08 — Estate Agents & Property_
_Last updated: 25 March 2026_
