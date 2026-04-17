# S05 — Horeca
### LocAI Bibliotheek · Sectordossier
_Versie 0.1 · 25 maart 2026_

---

## Wie zijn ze

Horeca is anders dan de andere sectoren in deze bibliotheek. Geen beroepsgeheim, geen bijzondere categorieën data, geen wettelijke conformiteitsbeoordelingen. Maar wel een sector die draait op marges, mensen, en momentum — en waar AI een zichtbaar, tastbaar verschil kan maken in de dagelijkse operatie.

Een restaurant, een café, een boetiekhotel — dat zijn bedrijven waar de eigenaar tegelijk kok, manager, marketeer, inkoper, en gastheer is. Waar een slechte week het verschil kan maken tussen winst en verlies. Waar persoonlijke service het enige echte onderscheidende vermogen is.

AI die dat ondersteunt — zonder data ergens anders naartoe te sturen — past perfect in dat plaatje.

**Typisch profiel:**
- Zelfstandige uitbater of kleine groep van 2-5 locaties
- 5-30 medewerkers
- Seizoensgebonden drukte, wisselende bezetting
- Dunne marges — voedselkosten 28-35%, personeelskosten 30-40%
- Weinig tijd voor administratie
- Sterk persoonlijk karakter — de uitbater IS het merk

**Specifieke beroepsgroepen:**
- Restauranthouders — van frituur tot gastronomisch restaurant
- Caféhouders — van bruine kroeg tot cocktailbar
- Hoteliers — boetiekhotels, B&B's, aparthotels
- Cateraars — events, bedrijfslunchrooms, schoolkantines
- Foodtrucks en pop-ups

---

## Welke data verwerken ze

De data in horeca is minder gevoelig dan bij de vorige sectoren — maar toch relevant.

**Gastdata:**
- Reservatiegegevens — naam, telefoonnummer, e-mail, aantal personen
- Voorkeuren en allergieën — dieetbeperkingen, favoriete gerechten
- Loyaliteitsdata — bezoekfrequentie, uitgaven, speciale gelegenheden
- Betalingsdata — creditcardgegevens (via betaalterminal, zelden direct opgeslagen)

**Personeelsdata:**
- Arbeidscontracten en loongegevens
- Uurroosters en beschikbaarheid
- Ziekteverzuim en verlof

**Operationele data:**
- Verkoopcijfers per gerecht, per dag, per shift
- Voorraadbeheer — inkomende goederen, verbruik, afval
- Leveranciersdata — contacten, prijzen, levertijden
- Energieverbruik en kosten

**Wat dit data specifiek maakt:**
Allergieëndata is een bijzondere categorie onder GDPR [1] — het is gezondheidsdata. Een gast die aangeeft glutenintolerant te zijn of een notenallergie heeft, deelt medische informatie. Dat verdient extra zorgvuldigheid.

Verder is de data in horeca minder explosief dan in de vorige sectoren — maar de operationele waarde ervan is enorm. Wie zijn beste klanten zijn, welke gerechten het best verkopen, wanneer de drukte piekt — dat is goud voor een kleine horecaondernemer.

---

## Welke wetten zijn van toepassing

### GDPR — Van toepassing maar minder intensief

Reservatiegegevens, loyaliteitsdata, personeelsdata — allemaal persoonsgegevens. De basisprincipes van GDPR gelden.

**Allergieëndata — bijzondere categorie:**
Gezondheidsdata vereist extra bescherming. Een reservatiesysteem dat allergieëndata opslaat en verwerkt, verwerkt bijzondere categorie data. De verwerkingsgrondslag: Art. 9 lid 2c (bescherming van vitale belangen) [1] — de allergie-informatie is noodzakelijk om de gezondheid van de gast te beschermen.

**Bewaartermijnen:**
Reservatiedata mag niet langer bewaard worden dan noodzakelijk. Een gast die één keer reserveert en nooit terugkomt, heeft na een redelijke termijn het recht om vergeten te worden.

**Personeelsdata:**
Loongegevens, roosters, ziekteverzuim — persoonsgegevens van medewerkers. Verwerkingsgrondslag: uitvoering van arbeidsovereenkomst (Art. 6b).

### AI Act — Minimaal risico voor de meeste toepassingen

Menurecommendaties, voorraadbeheer, roostering — allemaal minimaal risico. Geen hoog-risico AI in de typische horecacontext.

**Uitzondering:** als AI gebruikt wordt voor personeelsbeslissingen (wie krijgt welke shift, wie wordt ontslagen) — dan is het mogelijk hoog-risico (Bijlage III, punt 4) [2]. Menselijk toezicht blijft verplicht.

### Arbeidswetgeving

Horeca heeft specifieke arbeidswetgeving — flexibele contracten, overuren, nachtarbeid, studentenarbeid. AI die roosters genereert, moet rekening houden met deze regels.

**België:** paritair comité 302 (horeca) [4] met specifieke cao's.
**Nederland:** cao Horeca met specifieke bepalingen over arbeidstijden.

---

## Concrete use cases voor AI

Hier verschilt horeca fundamenteel van de andere sectoren. De use cases zijn niet primair gericht op compliance — ze zijn gericht op operationele efficiëntie en gastbeleving.

### 1. Menurecommendaties en allergieëngids

**Wat het is:** een lokale AI-assistent die gasten helpt bij het kiezen van gerechten op basis van hun voorkeuren en dieetbeperkingen.

**Twee vormen:**
- Intern (voor personeel): een medewerker vraagt "welke gerechten zijn glutenvrij én zonder noten?" en krijgt direct een antwoord.
- Extern (voor gasten): een tablet of QR-code waarbij gasten zelf hun allergieën invoeren en aangepaste menusuggesties krijgen.

**Waarde:** minder fouten bij allergieën (levensbedreigend risico vermijden), snellere bediening, betere gastervaring.

**Met lokale AI:** de allergieëndata van gasten verlaat het restaurant niet. Geen cloud-server die gezondheidsdata van gasten opslaat.

---

### 2. Voorraadbeheer en bestelpredictie

**Wat het is:** AI analyseert verkoopdata, seizoenspatronen, en weersvoorspellingen om te voorspellen hoeveel van elk product besteld moet worden.

**Tijdsbesparing en kostenbesparing:** te veel bestellen leidt tot voedselverspilling. Te weinig bestellen leidt tot "uitverkocht" op de kaart — verloren omzet en teleurgestelde gasten. AI optimaliseert dit.

**Concreet voorbeeld:** een restaurant weet dat op warme zomerse vrijdagavonden de verkoop van rosé met 40% stijgt. Een lokale AI die dat patroon herkent, waarschuwt tijdig voor bijbestelling.

**Met lokale AI:** verkoopdata en bestelpatronen — bedrijfsvertrouwelijke informatie — blijven intern. Geen concurrent die via een cloud-platform inzicht krijgt in jouw bestsellers.

---

### 3. Personeelsroostering

**Wat het is:** AI genereert een optimaal rooster op basis van verwachte bezetting, beschikbaarheid van medewerkers, cao-regels, en kosten.

**Tijdsbesparing:** een rooster maken voor 15 medewerkers over 4 weken kost uren. AI doet een eerste versie in minuten.

**Waarde:** minder over- en onderbezetting, tevredenere medewerkers, lagere personeelskosten.

**Met lokale AI:** roosters en beschikbaarheidsdata van medewerkers blijven intern. Personeelsdata gaat niet naar een externe server.

---

### 4. Meertalige gastcommunicatie

**Wat het is:** een lokale AI die helpt bij communicatie met gasten in verschillende talen — menukaarten vertalen, e-mails beantwoorden, reservatiebevestigingen opstellen.

**Waarde:** in toeristische gebieden zijn gasten uit tientallen landen. AI maakt professionele meertalige communicatie mogelijk zonder externe vertaaldienst.

**Met lokale AI:** gastcommunicatie — inclusief eventuele persoonlijke informatie in e-mails — blijft intern.

---

### 5. Dagelijkse financiële samenvatting

**Wat het is:** AI genereert aan het einde van elke dag een beknopte samenvatting van de financiële resultaten — omzet, kosten, marge per categorie, vergelijking met vorige week.

**Waarde:** een uitbater die weet hoe zijn dag was zonder een uur in Excel te zitten, kan sneller bijsturen.

**Met lokale AI:** omzetcijfers en kostendata — bedrijfsvertrouwelijk — blijven intern.

---

### 6. Recepten en kostprijsberekening

**Wat het is:** AI helpt bij het berekenen van de kostprijs van gerechten, het aanpassen van recepten bij gewijzigde inkoopprijzen, en het suggereren van menuwijzigingen om de marge te verbeteren.

**Waarde:** in horeca is de marge op elk gerecht cruciaal. AI die automatisch berekent wat een gerecht kost als de ingrediëntenprijzen stijgen, bespaart tijd en voorkomt verlieslatende items.

**Met lokale AI:** recepten en kostprijsdata — soms jarenlang ontwikkelde kennis — blijven intern.

---

## Het argument voor horeca: anders dan de andere sectoren

Bij accountants, therapeuten, juristen, en artsen is het primaire argument: beroepsgeheim en GDPR-risico.

Bij horeca is het primaire argument anders: **operationele waarde en concurrentieel voordeel.**

Een restauranthouder die zijn verkoopdata, zijn recepten, en zijn klantvoorkeuren naar een cloud-platform stuurt, geeft waardevolle bedrijfsinformatie weg. Niet aan een toezichthouder — maar aan een tech-platform dat die data gebruikt om zijn diensten te verbeteren, te analyseren, en mogelijk te monetariseren.

Lokale AI houdt die kennis intern. Jouw bestsellers, jouw marges, jouw klantpatronen — dat blijft van jou.

En er is een tweede argument dat horeca anders maakt: **de zichtbaarheid.**

Een allergieën-assistent op een tablet aan tafel is voor gasten zichtbaar. Een AI die menutips geeft in meerdere talen is merkbaar. Dat is een differentiatiefactor — een manier om je te onderscheiden van de concurrent die nog met een papieren kaart werkt.

---

## De kernboodschap voor het eerste gesprek

Niet beginnen met GDPR of de AI Act — die zijn minder urgent in deze sector. Beginnen met de operationele pijn.

> "Hoeveel tijd besteedt u per week aan roosters, bestellingen, en administratie? En hoeveel van die tijd gaat ten koste van de gasten?"

Vervolg:

> "Lokale AI doet die taken sneller — roosters, voorraadbeheer, financiële samenvattingen. En alles blijft intern. Uw verkoopdata, uw recepten, uw klantinformatie gaat niet naar een extern platform."

Voor de meer tech-savvy uitbater:

> "Stel u voor: een tablet aan tafel waarop gasten hun allergieën invoeren en direct aangepaste menusuggesties krijgen. Volledig in uw eigen stijl, op uw eigen hardware. Geen abonnement, geen platform dat uw gastdata opslaat."

---

## Vragen die ze stellen en hoe je antwoordt

**"Ik heb al een kassasysteem dat dit doet."**

Kassasystemen doen transactiebeheer. Ze analyseren niet, ze adviseren niet, en ze communiceren niet met gasten. Lokale AI is een laag bovenop uw kassasysteem — het maakt de data bruikbaar.

**"Mijn marge is te dun voor extra investeringen."**

De investering in hardware is eenmalig. Wat terugkomt: minder voedselverspilling, optimaler rooster, minder overuren. De terugverdientijd is typisch 6-18 maanden, afhankelijk van de schaal.

**"Ik heb geen IT-kennis."**

Dat hoeft niet. De interface is zo eenvoudig als een smartphone. De installatie en configuratie wordt voor u gedaan. Daarna gebruikt u het als elk ander apparaat.

**"Wat als het systeem uitvalt tijdens de drukte?"**

Lokale AI werkt offline. Geen internetafhankelijkheid. Als het systeem uitvalt, herstart u het — en u bent er weer. Geen afhankelijkheid van een cloud-provider die misschien ook juist op zaterdagavond problemen heeft.

**"Mijn personeel is niet technisch."**

Een menurecommendatietool of een voorraadassistent hoeft niet technisch te zijn. Als uw personeel een smartphone kan bedienen, kunnen ze dit gebruiken.

---

## Bijzondere aandacht: hotels en B&B's

Hotels verwerken meer data dan restaurants — paspoortgegevens, betalingsdata, verblijfshistoriek.

**Paspoortgegevens:** in België en Nederland zijn hotels wettelijk verplicht de identiteitsgegevens van gasten te registreren (vreemdelingenwet). Die data mag niet langer bewaard worden dan wettelijk vereist.

**AI-use cases specifiek voor hotels:**
- Gepersonaliseerde welkomstcommunicatie
- Kamerpreferenties onthouden voor terugkerende gasten
- Dynamische prijsstelling op basis van bezettingsgraad
- Lokale aanbevelingen voor gasten

**Privacy-aandacht:** hoteldata is gevoeliger dan restaurantdata. Verblijfshistoriek kan gevoelige informatie bevatten — met wie iemand reist, hoe vaak, wanneer. Lokale opslag is de meest veilige keuze.

---

## Bijzondere aandacht: de foodtruck en pop-up

Kleinste schaal, meest beperkte resources. Maar ook hier is lokale AI relevant.

Een foodtruck-eigenaar die op verschillende locaties staat, heeft baat bij AI die analyseert welke locaties het meest renderen, welke gerechten het beste verkopen op welke locatie, en wanneer de inkoop moet gebeuren.

Voor deze schaal is een krachtige laptop voldoende — geen aparte mini-PC nodig.

---

## Belgische en Nederlandse context

### België

**Federatie Horeca Vlaanderen** [3] — sectororganisatie voor de Vlaamse horeca.

**Paritair comité 302** [4] — specifieke cao's voor horeca, inclusief regelingen voor flexi-jobs, studentenarbeid, en overuren.

**Flexi-jobs:** een Belgisch systeem waarbij werknemers met een hoofdbetrekking extra uren kunnen werken in horeca. AI-roostering moet rekening houden met flexi-job regelgeving.

**Kassasystemen:** het gebruik van een gecertificeerd kassasysteem (GKS/SCE) is verplicht in de Belgische horeca voor restaurants. Lokale AI kan koppelen met GKS-data.

### Nederland

**KHN** [5] — Koninklijke Horeca Nederland. Sectororganisatie.

**Cao Horeca** — collectieve arbeidsovereenkomst met specifieke bepalingen over arbeidstijden, toeslagen, en vakantiedagen.

**Toeristenbelasting:** hotels zijn verplicht toeristenbelasting te registreren en af te dragen. AI kan helpen bij de berekening en rapportage.

---

## Sectorcijfers (referentie)

- Aantal horecabedrijven in België: circa 50.000
- Aantal horecabedrijven in Nederland: circa 40.000
- Gemiddelde marge in restauranthoreca: 3-9% netto
- Personeelsverloop in horeca: 70-80% per jaar (een van de hoogste van alle sectoren)
- Voedselverspilling als percentage van omzet: gemiddeld 4-10%
- Potentiële besparing via AI-voorraadoptimalisatie: 1-3% van omzet

---

## Bronnen

1. **GDPR — Verordening (EU) 2016/679, Art. 9 — Bijzondere categorieën (gezondheidsdata)**  
   EUR-Lex, Publicatieblad van de Europese Unie  
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/nld>

2. **AI Act — Verordening (EU) 2024/1689, Bijlage III — Hoog-risico arbeids-AI**  
   EUR-Lex, Publicatieblad van de Europese Unie  
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

3. **Federatie Horeca Vlaanderen — Sectorvertegenwoordiging en arbeidsvoorwaarden**  
   <https://www.horeca.be>

4. **PC 302 — Paritair Comité voor het hotelbedrijf (België)**  
   Federatie Horeca Vlaanderen  
   <https://www.horeca.be/nl/sociaal-recht/paritair-comite>

5. **KHN — Koninklijke Horeca Nederland**  
   <https://www.khn.nl>

---

_Onderdeel van: LocAI Bibliotheek · Sectordossiers_
_Vorige: S04 — Medische & Tandartspraktijken_
_Volgende: S06 — Overige sectoren_
_Laatste update: 25 maart 2026_
