# S06 — Retail & E-commerce
### LocAI Library · Sector Dossier
_Version 0.1 · 25 March 2026_

---

## Who they are

Retail is the sector everyone knows, yet few regard as "data-driven". And yet a modern shop or online store is one of the most data-intensive environments for a small business owner — especially once a loyalty programme, a webshop, or any digital touchpoint enters the picture.

A clothing retailer with a loyalty card knows more about the purchasing behaviour of its regular customers than those customers themselves realise. A webshop with Google Analytics and a Meta Pixel sends data to servers in the United States with every pageview — without the owner having consciously decided to do so.

**Typical profile:**
- Physical shop, pure online store, or mixed (omnichannel)
- Independent trader to SME of 5–50 employees
- Seasonal (fashion, garden centre, gift shop) or year-round (supermarket, pharmacy)
- Strongly dependent on customer recognition and retention

**Specific business types:**
- Clothing shops and fashion chains
- Electronics retailers
- Specialist shops — bookshops, pet shops, sports retailers
- Online stores without a physical presence
- Omnichannel retailers — shop + webshop + app

---

## What data they process

**Customer data:**
- Name, e-mail address, delivery address, telephone number
- Purchase history — what, when, how much
- Browsing behaviour on the webshop — which pages visited, how long, what was placed in the basket but not purchased
- Loyalty data — points, visit frequency, customer lifetime value
- Returns data — what is sent back and why

**Technical tracking data:**
- Cookies — session, preference, analytical, marketing
- Pixel data — Meta Pixel, Google Tag — behaviour on the site forwarded to external platforms [1]
- IP addresses and device information

**Operational data:**
- Stock levels per product
- Sales data per SKU, per day, per channel
- Supplier data and purchase prices

**What makes this specific:**
Retail data appears innocuous — someone buys a pair of shoes. But purchasing patterns over time tell a story. Medical devices, maternity products, bereavement items, gambling-related purchases — a purchase history is a window into someone's life. Combined with browsing behaviour and demographic data, it becomes a profile that extends far beyond "customer".

---

## Which laws apply

### GDPR — Consent, profiling and retention periods

Every webshop that places cookies, sends newsletters, or maintains a customer database falls under the GDPR [2].

**Cookies and consent:** non-functional cookies — analytical, marketing — require freely given, specific, informed and unambiguous consent [3]. Pre-ticked boxes are invalid. A cookie banner that makes "accept" more prominent than "decline" is misleading. Both the Belgian DPA (Gegevensbeschermingsautoriteit) and the Dutch DPA (Autoriteit Persoonsgegevens) have issued enforcement decisions on this matter [4].

**Profiling and automated decision-making:** where AI is used to segment customers and automatically link actions to those segments (different price, different offer, access refused), GDPR Art. 22 applies [2]. The customer has the right not to be subject to fully automated decisions with significant consequences.

**E-mail marketing:** existing customers may be contacted on the basis of legitimate interest (Art. 6(1)(f)) — but only for similar products, with an easy opt-out. New contacts require explicit consent.

**Retention periods:** customer data may not be retained longer than necessary. For accounting documents, a statutory period of 7 years applies. For marketing profiles, the permissible period is considerably shorter.

### ePrivacy — Cookies and electronic communications

The ePrivacy Directive specifically governs the use of cookies and electronic communications [5]. Implemented in Belgium via the law on electronic communications, in the Netherlands via the Telecommunications Act. The practical implication: every cookie without a strictly functional role requires prior consent.

### AI Act — Low risk with exceptions

Product recommendations, customer service chatbots, inventory management — these fall under minimal-risk classifications under the AI Act [6].

**Note:** where AI is used for fraud detection in refunds or for refusing customers on the basis of profiles, the risk level increases. AI that applies price discrimination to vulnerable groups may fall under higher risk categories.

---

## Concrete AI use cases

### 1. Product recommendations

**What it is:** AI analyses purchase history and browsing behaviour to generate relevant product recommendations — "also viewed", "pairs well with", "others also bought".

**Value:** on average 10–30% of a webshop's revenue comes from recommendation engines.

**With local AI:** the purchasing patterns of your customers remain on your server. A cloud recommendation engine does not only learn from your data — it learns from all customers of all shops using the platform. Your bestsellers, your customer profiles, your seasonal patterns — all of these feed a model that also benefits your competitors.

---

### 2. Customer service chatbot

**What it is:** AI answers standard questions — opening hours, order status, returns policy, product information — without human intervention.

**Value:** 60–80% of customer service queries at webshops are repetitive and fully automatable.

**With local AI:** complaints, order issues and returns requests contain personal data. A local AI processes these without sending the data to an external server.

---

### 3. Demand forecasting and inventory management

**What it is:** AI analyses historical sales data, seasonal patterns, and external factors (weather, public holidays, promotions) to forecast stock requirements.

**Value:** overstock costs money, understock costs revenue. A good forecast saves an average of 15–25% on inventory costs.

**With local AI:** your sales data, your purchase prices, your suppliers — that is commercially sensitive business information. Not something that belongs on an external platform.

---

### 4. Personalised e-mail communications

**What it is:** AI generates personalised e-mails based on purchase history and customer behaviour — birthday offers, reactivation of inactive customers, post-purchase follow-up.

**Value:** personalised e-mails achieve on average 6× higher conversion than generic newsletters.

**With local AI:** the customer profiles and purchasing behaviour remain internal. No external e-mail platforms analysing that data and deploying it commercially.

---

### 5. Returns and fraud analysis

**What it is:** AI recognises patterns in returns behaviour that indicate misuse — serial returners, wardrobing (buy–wear–return), coordinated fraud.

**Value:** returns fraud costs European retail billions annually.

**AI Act note:** where AI automatically blocks or refuses customers based on returns behaviour, human oversight is mandatory. Automated decisions with significant consequences for the customer require an escalation path to a human.

---

## The concrete cloud-AI risk

**The Meta Pixel scenario:**

A webshop owner installs a Meta Pixel to track Facebook advertisements. Standard configuration. What actually happens:

1. Every visitor to the webshop sends an event to Meta's servers — including which products were viewed, what is in the basket, and the purchase amount.
2. If the customer also has a Facebook account, this is linked to their profile.
3. This constitutes a transfer of personal data to a third party (Meta) without most visitors being aware of it and without an adequate GDPR legal basis.
4. The Belgian DPA has carried out multiple enforcement actions against this practice [4].

Most webshop owners did not consciously configure this. It was embedded in their theme by default or installed by a marketing agency. They are responsible for it nonetheless.

**The local AI approach:** product recommendations, customer analysis and campaign planning based on data held exclusively on the business's own server. No pixels. No external trackers required.

---

## The core message for the first conversation

Do not start with GDPR. Start with the competition.

> "Your purchasing data — who your best customers are, what they buy, when they buy — is the most valuable information your business holds. If you process it via a cloud AI platform, you are contributing that information to a model used by hundreds of thousands of retailers. Your competitors included."

Continue:

> "Local AI turns that same data into an advantage for you alone. Recommendations, forecasts, communications — all based on your customers, on your server, without it going anywhere else."

---

## Questions they ask and how to answer

**"I already have an e-commerce platform with built-in recommendations — why would I replace that?"**

You don't need to replace it. You can use local AI for the tasks where your customer data is the input — analyses, communications, forecasts — and let the platform do what it does. They do not need to compete.

**"My customers consent to cookies anyway, don't they?"**

Consent for cookies is not the same as consent for sending detailed purchase data to Meta or Google. Most cookie banners do not cover that. And even if they did: as the data controller, you are responsible for what happens with that data, including what your processors do with it.

**"I'm too small for the Belgian DPA to pay attention to."**

The Belgian DPA has carried out enforcement actions against small webshops. Size does not protect you — conduct does. And beyond the Belgian DPA, customers can file complaints themselves.

**"I don't even know which pixels are on my site."**

That is precisely the problem. Open your site in a browser with the [Blacklight tool by The Markup](https://themarkup.org/blacklight) — it shows exactly which trackers are active. After that, you will know what is going on.

---

## Belgian and Dutch context

### Belgium

**Comeos** — Belgian federation for retail and e-commerce. One of the largest retail federations in Belgium, representing the majority of Belgian retail [7].

**Belgian DPA (Gegevensbeschermingsautoriteit)** — Has published specific recommendations on cookie consent and online tracking. The IAB Europe Transparency & Consent Framework (TCF) was declared invalid by the Belgian DPA in 2022 — a decision with implications for virtually all Belgian webshops [4].

**VAT and e-commerce:** since 1 July 2021, the OSS system (One Stop Shop) applies to VAT returns on cross-border B2C sales. Webshops selling to consumers in other EU countries must maintain thorough records of customer locations.

### The Netherlands

**INretail** — trade association for fashion, footwear, sports and related sectors in the Netherlands [8].

**Dutch DPA (Autoriteit Persoonsgegevens)** — Has carried out enforcement actions regarding cookies, tracking pixels and newsletter consent.

**Thuiswinkel Waarborg** — quality mark for webshops in the Netherlands. Membership requires, among other things, a GDPR-compliant privacy statement and cookie policy.

---

## Sector figures (reference)

- Number of retail outlets in Belgium: approx. 70,000 [7]
- Number of retail outlets in the Netherlands: approx. 90,000 [8]
- Share of e-commerce in total retail BE: approx. 15% (2024)
- Share of e-commerce in total retail NL: approx. 20% (2024) — one of the highest in Europe
- Average share of recommendation engines in webshop revenue: 10–30%
- Returns rate in Dutch e-commerce fashion: 30–50%
- Average cost of a data breach for an SME: €15,000–50,000 (including notification, investigation and customer communications — estimate based on IBM Cost of Data Breach Report 2024, adjusted for SME scale)

---

## References

1. **Meta Pixel — operation and data collection**
   Meta Business Help Centre documentation
   <https://www.facebook.com/business/help/742478679120153>

2. **GDPR — Regulation (EU) 2016/679**
   EUR-Lex, fully consolidated text
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/nld>

3. **GDPR Art. 7 — Conditions for consent**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/nld>

4. **Belgian DPA — IAB Europe TCF decisions (2022) — cookie consent**
   Gegevensbeschermingsautoriteit België
   <https://www.gegevensbeschermingsautoriteit.be/beslissingen>

5. **ePrivacy Directive 2002/58/EC — Electronic communications and privacy**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/dir/2002/58/oj/nld>

6. **AI Act — Regulation (EU) 2024/1689 — Risk classification**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

7. **Comeos — Retail in Belgium 2024 (sector facts)**
   <https://www.comeos.be/publicaties>

8. **INretail — Figures & trends in Dutch retail**
   <https://www.inretail.nl/kennis/cijfers-trends>

---

_Part of: LocAI Library · Sector Dossiers_
_Previous: S05 — Hospitality_
_Next: S07 — Hair & Beauty_
_Last updated: 25 March 2026_
