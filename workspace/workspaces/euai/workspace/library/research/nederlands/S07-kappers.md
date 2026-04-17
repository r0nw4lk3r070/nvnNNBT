# S07 — Kappers & Beauty
### LocAI Bibliotheek · Sectordossier
_Versie 0.1 · maart 2026_

---

## Wie zijn ze

Kappers en beautyspecialisten zijn misschien wel de meest onderschatte verwerkingsverantwoordelijken van de GDPR. Iedereen denkt aan ziekenhuizen en advocatenkantoren als het over gevoelige data gaat. Maar een kapper die bijhoudt dat een vaste klant allergisch is voor PPD (para-fenylenediamine — een veelgebruikte kleurstof) bewaart medische informatie. Een schoonheidsspecialiste die huidaandoeningen registreert voor behandeladvies: hetzelfde.

Het gaat om kleine bedrijven — een eenmanszaak of een salon met twee of drie medewerkers. Geen juridische afdeling. Geen functionaris voor gegevensbescherming. Maar de wet maakt geen uitzondering op basis van bedrijfsgrootte.

**Typisch profiel:**
- Kapperszaak: 1-5 medewerkers, vaste klantenbasis, hoog herhaalbezoek
- Nagelstudio, schoonheidssalon, wenkbrauwbar: overwegend zelfstandigen
- Tattoo- en piercingstudio: vaste klanten + eenmalige bezoekers
- Barbershop: groeiend segment, vaak jongere ondernemers

**Specifieke beroepsgroepen:**
- Kappers (haarverzorging, kleurbehandeling)
- Schoonheidsspecialisten (gezichtsbehandeling, ontharing, huidverzorging)
- Nagelstylisten
- Tattoo-artiesten en piercers
- Permanent make-up specialisten

---

## Welke data verwerken ze

**Afspraakdata:**
- Naam, telefoonnummer, e-mailadres
- Afspraakhistorie — wanneer, welke behandeling, bij welke medewerker
- No-show en annulatiedata

**Behandelhistorie:**
- Gebruikte producten en kleurnummers
- Resultaten van vorige behandelingen
- Klantvoorkeuren — "wil altijd dezelfde kleur", "neemt nooit conditioner"

**Gezondheidsdata — het kritieke punt:**
- Allergieën voor haarkleurproducten (PPD, ammonia, peroxide) [1]
- Huidaandoeningen relevant voor behandeling (eczeem, psoriasis, couperose)
- Zwangerschap (relevant voor bepaalde chemische behandelingen)
- Medicatiegebruik (sommige medicatie beïnvloedt haarkleur of huidreactie)

Dit is GDPR Art. 9 gezondheidsdata. Dezelfde categorie als een medisch dossier. De verwerkingsgrondslag: Art. 9 lid 2(a) — expliciete toestemming van de betrokkene (wat een behandelformulier bij het eerste bezoek juridisch verankert), of Art. 9 lid 2(c) — bescherming van vitale belangen (van toepassing bij een ernstige allergie waarbij de klant zichzelf niet adequaat kan beschermen). Praktisch: de informatie is nodig om de klant geen schade toe te brengen.

**Visuele data:**
- Foto's voor of na behandeling — steeds vaker gebruikt voor portfolioopbouw en sociale media
- Dit zijn persoonsgegevens. Publicatie vereist expliciete toestemming [2].

**Betaaldata:**
- Kassa-aanslagen, tikkie-betalingen, cadeaubon-gebruik

---

## Welke wetten zijn van toepassing

### GDPR — Gezondheidsdata en toestemming

Het allergie- en behandeldossier vereist een expliciete verwerkingsgrondslag [1]. "De klant heeft het mondeling gezegd" is geen grondslag. Een papieren kaart in een lade is geen gedocumenteerde toestemming.

**Wat wel werkt:** een eenvoudig behandelformulier bij het eerste bezoek — allergie-anamnese, toestemming voor gebruik van de gegevens voor toekomstige behandelingen, en apart: toestemming voor foto's. Twee handtekeningen, bewaard bij het klantdossier.

**Bewaartermijn:** er is geen wettelijk vastgelegde termijn voor kappersdata. De vuistregel: zo lang als nodig voor het doel. Voor allergie-informatie is dat zolang de klant komt. Bij stopzetting van de relatie: verwijderen.

**Foto's en sociale media:** een foto posten op Instagram vereist expliciete toestemming van de afgebeelde persoon [2]. "De klant vond het goed" is onvoldoende — het moet schriftelijk of digitaal aantoonbaar zijn. De toestemming moet ook de specifieke platforms vermelden.

### AI Act — Minimaal risico met één uitzondering

Afsprakenbeheer, klantcommunicatie, productaanbevelingen — minimaal risico [3].

**Uitzondering:** als AI wordt ingezet voor roostering van medewerkers op basis van prestatiedata (wie krijgt welke klant, wie wordt ingeroosterd voor drukke periodes) is dat potentieel hoog-risico arbeids-AI (Bijlage III, punt 4) [3]. Menselijk toezicht verplicht.

### Sectorregulering

**België:** PC 314 — Paritair Comité voor het kappersbedrijf [4]. Regelt arbeidsovereenkomsten, lonen, en werktijden. Vlaamse Kappersfederatie als sectorvertegenwoordiger.

**Nederland:** ANKO — Algemene Nederlandse Kappers Organisatie [5]. Cao Kappersbedrijf regelt arbeidsvoorwaarden. Branchevereniging voor schoonheidsspecialisten: ANBOS.

---

## Concrete use cases voor AI

### 1. Afsprakenbeheer en herinneringen

**Wat het is:** AI stuurt automatische herinneringen, beheert de agenda, en vult vrije plekken op basis van klanthistorie en voorkeurstijden.

**Waarde:** no-shows kosten de gemiddelde kapperszaak 10-15% van de omzet. Automatische herinneringen reduceren dit significant.

**Met lokale AI:** agenda + klantcontactdata blijft intern. Geen externe afspraakplatformen die je klantenbestand opbouwen en analyseren.

---

### 2. Behandelformulier en allergie-anamnese

**Wat het is:** AI helpt bij het digitaliseren en structureren van behandelformulieren. Bij terugkerende klanten: herinnering aan relevante allergie-informatie voor de behandeling.

**Waarde:** veiligheidswinst én juridische dekking. Als een behandeling verkeerd gaat en er geen allergie-registratie is, staat de behandelaar juridisch zwak.

**Met lokale AI:** gezondheidsdata verlaat de salon niet. Een cloud-afspraken-app die ook allergie-notities opslaat stuurt die data naar een server waarover jij geen controle hebt.

---

### 3. Klantcommunicatie en seizoensaanbiedingen

**Wat het is:** AI genereert gepersonaliseerde berichten op basis van behandelhistorie — klanten die lang niet geweest zijn, seizoensgebonden aanbiedingen, verjaardagsbericht.

**Waarde:** herhalingsbezoek is de kern van het kappersbedrijf. Een klant die zes weken na de vorige knipbeurt een herinnering krijgt, komt sneller terug.

**Met lokale AI:** de behandelhistorie en persoonlijke notities zijn de input. Die horen niet op een extern e-mailplatform dat ze commercieel inzet.

---

### 4. Productsuggesties en voorraadbeheer

**Wat het is:** AI analyseert welke producten goed verkopen, welke klanten welke producten kopen, en wanneer bijbesteld moet worden.

**Waarde:** retail (producten verkopen) is voor veel salons een winstgevend neveninkomsten. Betere voorspelling = minder overstock.

**Met lokale AI:** jouw verkoopdata per product en per klant is bedrijfsinformatie. Hoeft niet op een cloudplatform van een groothandel.

---

### 5. Portfolio en sociale media contentplanning

**Wat het is:** AI helpt bij het plannen en beschrijven van posts — welke foto's wanneer te posten, welke hashtags, welke seizoensthema's.

**Opgelet GDPR:** de foto's zelf zijn persoonsgegevens als ze herkenbare klanten tonen. AI mag de planning doen — maar de toestemmingsdocumentatie is mensenwerk en is verplicht [2].

---

## Het concrete risico met cloud-AI

**Het behandeldossier-scenario:**

Een kapper gebruikt een populaire cloud-afspraken-app — Treatwell, Fresha, of vergelijkbaar. Handig: online boeken, herinneringen, betaling. Wat er ook gebeurt:

1. Alle klantdata — naam, contactgegevens, behandelhistorie, en eventuele notities over allergieën of huidaandoeningen — staat op de servers van het platform.
2. De platformvoorwaarden geven het bedrijf het recht die data te gebruiken voor "verbetering van de dienst" — wat betekent: trainen van modellen, analyseren van patronen, verkopen van inzichten aan partners.
3. Als het platform failliet gaat, overgenomen wordt, of gehackt wordt: jouw klantdata, inclusief gezondheidsdata, is in andere handen.
4. De kapper is als verwerkingsverantwoordelijke aansprakelijk voor wat er met die data gebeurt — ook bij een verwerker.

De klant die jou vertelde dat ze allergisch is voor PPD heeft dat in vertrouwen gedaan. Niet aan een Amerikaans SaaS-platform.

---

## De kernboodschap voor het eerste gesprek

Begin niet bij de wet. Begin bij de relatie.

> "Jouw klanten komen bij jou omdat ze jou vertrouwen. Ze vertellen jou dingen — over hun haar, hun huid, hun gezondheid — die ze aan niemand anders vertellen. Als jij die informatie doorgeeft aan een cloud-platform, geef je dat vertrouwen weg. Niet bewust. Maar het staat in de kleine lettertjes."

Vervolg:

> "Lokale AI betekent: die notities, die behandelhistorie, die allergie-informatie — dat blijft tussen jou en je klant. Zoals het altijd al was. Alleen nu geordend, doorzoekbaar, en bruikbaar."

---

## Vragen die ze stellen en hoe je antwoordt

**"Ik gebruik gewoon een papieren klantenkaart — is dat niet veiliger?"**

Voor GDPR-aansprakelijkheid maakt het medium niet uit — papier valt ook onder de GDPR. Maar papier gaat verloren, is niet doorzoekbaar, en als er brand is in de salon ben je alles kwijt. Een lokaal digitaal systeem is veiliger én compliant.

**"Ik zet toch geen medische dingen op — alleen 'geen ammonia'."**

"Geen ammonia" vanwege een allergie is gezondheidsdata onder Art. 9. Niet omdat de wet streng wil zijn, maar omdat een allergische reactie op een haarkleur levensgevaarlijk kan zijn. De wet beschermt de klant en jou tegelijk.

**"Mijn klanten vinden het niet erg als ik hun foto op Instagram zet."**

Mondeling "niet erg vinden" is geen geldige toestemming onder GDPR. Je hebt schriftelijke of digitale toestemming nodig, specifiek voor elk platform. Één formulier bij het eerste bezoek regelt dit voor altijd.

**"Ik ben te klein — niemand kijkt naar een kapper."**

De GBA en AP controleren op klachten. Een klant die een foto terugziet die hij nooit heeft goedgekeurd, kan een klacht indienen. Dat kost jou meer tijd en geld dan een goed formulier ooit zou kosten.

---

## Belgische en Nederlandse context

### België

**Coiffure EU / Nationaal Verbond van Kappers** [4] — sectororganisatie voor kappers in België. Biedt modelcontracten en sectoradvies.

**PC 314** — Paritair Comité voor het kappersbedrijf. Regelt cao's en arbeidsvoorwaarden. Flexi-jobs zijn gangbaar in de sector.

**GBA** — Gegevensbeschermingsautoriteit. Heeft aandacht voor kleine ondernemers die persoonsdata verwerken zonder bewerkersovereenkomst met hun software-leverancier.

### Nederland

**ANKO** — Algemene Nederlandse Kappers Organisatie. Branchevereniging voor kappers, biedt praktische GDPR-templates aan leden [5].

**ANBOS** — Branchevereniging voor schoonheidsspecialisten in Nederland.

**AP** — Autoriteit Persoonsgegevens. Heeft specifieke guidance gepubliceerd over foto's en portretrecht in de context van sociale media.

---

## Sectorcijfers (referentie)

- Aantal kapperszaken in België: ca. 12.000 [4]
- Aantal kapperszaken in Nederland: ca. 14.000 [5]
- Gemiddeld klantbezoek per jaar: 5-8 keer (haar), 12+ keer (nagels)
- Percentage salons dat digitale afsprakensoftware gebruikt: ca. 60-70% (2024)
- PPD-allergie prevalentie in de bevolking: ca. 5-10% — onderschat risico

---

## Bronnen

1. **GDPR — Verordening (EU) 2016/679, Art. 9 — Bijzondere categorieën persoonsgegevens**
   EUR-Lex, Publicatieblad van de Europese Unie
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/nld>

2. **GDPR Art. 6 & 7 — Rechtmatigheid van verwerking en toestemmingsvoorwaarden**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/nld>

3. **AI Act — Verordening (EU) 2024/1689, Bijlage III — Hoog-risico AI-systemen**
   EUR-Lex, Publicatieblad van de Europese Unie
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

4. **Nationaal Verbond van Kappers van België (Coiffure EU) — Sectorinformatie en arbeidsregelgeving PC 314**
   <https://www.coiffure.be>

5. **ANKO — Algemene Nederlandse Kappers Organisatie**
   <https://www.anko.nl>

---

_Onderdeel van: LocAI Bibliotheek · Sectordossiers_
_Vorige: S06 — Retail & Webshops_
_Volgende: S08 — Makelaars & Vastgoed_
_Laatste update: 25 maart 2026_

## Belgische en Nederlandse context

_[ in te vullen — PC 314 kappersbedrijven (BE), ANKO (NL), hygiënewetgeving ]_

---

## Sectorcijfers (referentie)

_[ in te vullen ]_

---

## Bronnen

_[ referenties volgen bij uitwerking ]_

---

_Onderdeel van: LocAI Library · Sectordossiers_
_Vorige: S06 — Retail & Webshops_
_Volgende: S08 — Vastgoedmakelaars_
_Laatste update: maart 2026_
