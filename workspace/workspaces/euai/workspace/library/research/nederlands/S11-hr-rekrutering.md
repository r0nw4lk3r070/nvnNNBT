# S11 — HR & Rekrutering
### LocAI Bibliotheek · Sectordossier
_Versie 0.1 · 25 maart 2026_

---

## Wie zijn ze

HR-professionals en rekruteringsbureaus staan aan het begin van elke arbeidsrelatie. Ze verwerken de meest persoonlijke informatie die mensen delen: hun carrièregeschiedenis, hun motivaties, hun salarisverleden, hun assessmentresultaten — en ze doen dat in een context van expliciete besluitvorming over wie mag doorstromen en wie niet. Die combinatie van dataintensiteit en beslissingsgewicht maakt HR tot de sector die het hardst geraakt wordt door de AI Act.

AI wordt al breed ingezet in rekrutering: cv-screening, matching, chatbots voor eerste gesprekken, assessmentanalyse. Maar veel van die tools worden ingezet zonder dat de gebruikers beseffen dat ze juridisch als hoog-risico AI worden geclassificeerd — met alle documentatie- en transparantieverplichtingen van dien.

**Typisch profiel:**
- Intern HR-team bij een kmo of grote onderneming
- Gespecialiseerd rekruteringsbureau of interimkantoor
- Headhuntingbureau voor executive en specialistenprofielen
- Uitzend- of selectiekantoor dat werkt voor meerdere opdrachtgevers

**Specifieke beroepsgroepen:**
- HR Business Partners en HR Managers — interne rekrutering, people management
- Rekruteringsconsultants — externe selectieprocedures voor opdrachtgevers
- Interimconsultants — plaatsing van tijdelijk personeel
- Assessment- en loopbaanspecialisten — testen, outplacement, loopbaanbegeleiding
- Talent acquisition teams bij grotere organisaties

---

## Welke data verwerken ze

**Kandidatendata:**
- Cv's — naam, adres, contactdata, werkhistorie, opleiding, vaardigheden
- Motivatiebrieven en persoonlijke verklaringen
- LinkedIn-profielen en online aanwezigheid
- Assessmentresultaten — cognitieve tests, persoonlijkheidstests, vaardigheidsproeven
- Gespreksverslagen en evaluatienotes van interviewers
- Referenties en feedback van eerdere werkgevers
- Salarisexpectaties en huidig loon
- Foto's, indien door kandidaat verstrekt (juridisch gevoelig)

**Werknemersdata (intern HR):**
- Loongegevens, functieclassificaties en voordelen
- Functioneringsgesprekken en beoordelingsresultaten
- Verzuimregistraties en re-integratiedossiers
- Opleidingshistorie en competentieprofielen
- Disciplinaire dossiers

**Opdrachtgeversdata (externe bureaus):**
- Vacatureprofielen en functieclassificaties
- Loonschalen en budgetinformatie
- Interne organisatiestructuur en teamdynamiek
- Vertrouwelijke informatie over uitbreidings- of reorganisatieplannen

**Wat dit specifiek maakt:**
Een cv is een samenstelling van persoonsdata die de kandidaat heeft verstrekt in de hoop op een baan. Die data wordt beoordeeld, vergeleken, gerangschikt — en bij afwijzing: verwijderd of bewaard. De machtsongelijkheid tussen kandidaat en rekruteerder is enorm. Als die beoordeling geheel of deels door AI wordt uitgevoerd, stijgt het juridische risico exponentieel: discriminatierisico in getrainde modellen, gebrek aan transparantie, onmogelijkheid voor de kandidaat om de redenering te begrijpen of te betwisten.

---

## Welke wetten zijn van toepassing

### GDPR — Kandidatendata en bewaarbeleid

Kandidatendata is persoonsdata die voor een specifiek doel is verstrekt: deelname aan een selectieprocedure [1]. Dat doel begrenst het gebruik: de data mag niet worden hergebruikt voor andere vacatures zonder nieuwe toestemming, mag niet worden verkocht of gedeeld met andere partijen, en moet worden verwijderd als de bewaartermijn verstreken is.

**Bewaartermijnen:** voor afgewezen kandidaten is de standaard doorgaans zes maanden — lang genoeg voor eventuele klachtprocedures, kort genoeg om proportioneel te zijn. Voor "talentpoels" waar kandidaten actief toestemming geven voor langere bewaring, is die toestemming specifiek en herroepbaar.

**Verwerkersovereenkomsten:** elk ATS (Applicant Tracking System), elke AI-screener, elk assessmentplatform of HR-cloudtool die kandidatendata verwerkt namens het bedrijf, vereist een verwerkersovereenkomst.

### AI Act — Bijlage III punt 4: arbeidsgerelateerde AI als expliciet hoog-risico

AI-systemen voor rekrutering en personeelsselectie staan expliciet in Bijlage III van de AI Act als hoog-risico [2]. Dat is een bewuste beleidskeuze: het beslissingsgewicht op arbeidsgebied — wie mag werken, wie niet — vereist de hoogste beschermingsnormen.

**Wat valt eronder:** AI-tools voor cv-screening en -rangschikking, matching-algoritmen, assessmentanalysetools, AI-gestuurde videogespreksanalyse, chatbots die selectiebeslissingen meedelen — al deze systemen vallen in de hoog-risico categorie als ze kandidaten beoordelen, vergelijken of rangschikken.

**Verplichtingen:** technische documentatie, logging van beslissingen, transparantie tegenover betrokkenen, menselijk toezicht en override, en conformiteitsbeoordeling [2]. Een rekruteringsbureau dat een SaaS-tool inkoopt voor cv-screening, is als deployer verantwoordelijk voor de naleving — ook als de tool door een derde wordt aangeleverd.

### Antidiscriminatiewetgeving

AI-modellen getraind op historische recruitmentdata reproduceren structureel de vooroordelen die in die data zitten. Een model getraind op tien jaar aanwervingsbeslissingen van een sector die traditioneel homogeen was, zal die homogeniteit versterken — tenzij actief gecorrigeerd.

In België verbiedt de **Wet van 10 mei 2007** [4] discriminatie op basis van geslacht, afkomst, leeftijd, seksuele oriëntatie en andere beschermde kenmerken. In Nederland regelt de **Algemene wet gelijke behandeling (AWGB)** [5] hetzelfde. AI-systemen die niet actief op discriminatierisico geëvalueerd worden, zijn een juridisch aansprakelijkheidsrisico.

---

## Concrete use cases voor AI

### 1. Vacatureteksten

**Wat het is:** AI genereert vacatureteksten op basis van een functiebeschrijving, gewenst profiel en de tone of voice van het bedrijf.

**Waarde:** snellere productie van kwalitatieve vacatures, consistente stijl, en — als het systeem daarvoor geconfigureerd is — neutraler taalgebruik dat meer diverse kandidaten aanspreekt.

**Met lokale AI:** functiebeschrijvingen en organisatiecultuurinformatie zijn intern gevoelig. Een vervangingsvacature tijdens een lopend dienstverband, een uitbreiding in een strategisch nieuw marktsegment — dat is informatie die niet via een cloud AI-platform mag lekken.

---

### 2. Cv-verwerking en samenvatting

**Wat het is:** AI leest en structureert inkomende cv's, trekt relevante informatie eruit en presenteert een gestandaardiseerde samenvatting aan de recruiter.

**Waarde:** tijdsbesparing bij hoge volumes. Een recruiter die honderd cv's per week ontvangt, doorloopt de eerste selectiefase sneller.

**Opgelet AI Act:** cv-verwerking voor selectie is hoog-risico AI [2]. Het systeem mag kandidaten niet automatisch uitsluiten zonder menselijke controle. De recruiter beslist — AI structureert en ondersteunt.

---

### 3. Gespreksverslagen en evaluatienotes

**Wat het is:** AI transcribeert en structureert gespreksverslagen van selectiegesprekken, vat evaluatienotes samen en bewaakt consistentie in de beoordeling.

**Waarde:** minder administratieve last voor recruiters, betere documentatie voor GDPR-doeleinden, consistentere evaluatieprocessen.

**Met lokale AI:** gespreksverslagen bevatten directe quotes, emotionele indrukken en persoonlijke informatie die kandidaten in vertrouwen hebben gedeeld. Die data hoort niet in een cloud AI-platform.

---

### 4. Onboarding-documenten

**Wat het is:** AI genereert gepersonaliseerde onboardingpakketten — welkomstbrieven, introductiedocumenten, takenlijsten voor de eerste weken — op basis van het profiel en de functie van de nieuwe medewerker.

**Waarde:** betere onboardingervaringen, minder handmatig werk voor HR, snellere integratie.

**Met lokale AI:** onboarding vereist verwerking van persoonsdata van de werknemer, contractinformatie en organisatiegevoelige informatie.

---

### 5. Loonbenchmarking en HR-analytics

**Wat het is:** AI analyseert interne loonstructuren en vergelijkt ze met marktdata om loonbandbreedtes en functieclassificaties te ondersteunen.

**Waarde:** betere onderbouwing voor loonbeslissingen, vroege signalering van loonkloven.

**Met lokale AI:** interne loondata van individuele medewerkers mag niet worden gedeeld met externe platforms — ook niet geanonimiseerd als heridentificatie bij kleine groepen mogelijk is.

---

## Het concrete risico met cloud-AI

**Het ATS-SaaS-scenario:**

Een rekruteringsbureau stapt over op een modern cloud ATS met ingebouwde AI-screening, videogespreksanalyse en candidate matching.

1. Duizenden cv's per jaar — naam, adres, werkhistorie, opleidingen — worden geüpload naar servers buiten de EU.
2. De videogespreksanalyse analyseert toon, mimiek en woordkeus — hoog-risico AI onder Bijlage III [2]. De vereiste documentatie levert het platform niet standaard.
3. Het platform traint zijn matchingmodellen op geaggregeerde data van alle aangesloten bureaus — inclusief jouw kandidatendatabase en beoordelingshistorie.
4. Een kandidaat vraagt om inzage in de redenering bij afwijzing (GDPR Art. 22). Jij hebt geen uitleg die je kunt geven.
5. De GBA of AP onderzoekt een klacht. Jij — als deployer — bent verantwoordelijk voor de AI Act-conformiteit, ook als je het systeem als dienst hebt afgenomen.

Lokale cv-verwerking en gespreksverslaggeving: kandidatendata op een eigen server, zonder dat persoonsdata de bedrijfsomgeving verlaat, en met volledige controle over documentatie en transparantie.

---

## De kernboodschap voor het eerste gesprek

Begin niet bij de AI Act. Begin bij aansprakelijkheid.

> "AI in rekrutering is expliciet hoog-risico onder de AI Act. Dat staat letterlijk in Bijlage III. Als jij een SaaS-tool gebruikt die cv's screent of kandidaten rangschikt, ben jij als deployer verantwoordelijk voor de conformiteit van dat systeem. Niet de leverancier. Jij."

Vervolg:

> "Lokale AI lost dat op een elegante manier op: je ondersteunt recruiters met AI die cv's structureert, gespreksverslagen samenvat en onboarding-documenten genereert — zonder dat kandidatendata een externe server bereikt, en zonder dat je afhankelijk bent van de AI Act-conformiteit van een cloudprovider."

---

## Vragen die ze stellen en hoe je antwoordt

**"Wij gebruiken al een gekende tool — die zijn toch GDPR-compliant?"**

GDPR-compliant zijn en AI Act-compliant zijn is niet hetzelfde. Een tool kan een geldig privacybeleid hebben en toch een hoog-risico AI-systeem inzetten dat niet voldoet aan de documentatie- en transparantieverplichtingen van de AI Act. Als deployer draag jij de verantwoordelijkheid. "De leverancier heeft het ons verzekerd" is geen juridische verdediging.

**"Cv-screening door AI is toch neutraal — het kijkt niet naar geslacht of afkomst?"**

AI-modellen zijn zo neutraal als de data waarop ze getraind zijn. Als historische aanwervingsbeslissingen overwegend mannen selecteerden, leert het model dat mannen betere kandidaten zijn. Bepaalde woordkeuzen gecorreleerd met een bepaalde achtergrond worden meegewogen. Dat is structurele bias in een algoritmisch jasje — juridisch net zo problematisch als bewuste discriminatie.

**"We bewaren cv's altijd — voor de volgende keer dat er iets past."**

Dat mag — als kandidaten daarvoor expliciet toestemming hebben gegeven bij indiening, als die toestemming specifiek is voor die bewaarduur, en als kandidaten ze kunnen intrekken. "Altijd bewaren" zonder expliciete toestemming en actief bewaarbeheer is een GDPR-overtreding.

**"Hoe moet ik uitleggen waarom een kandidaat afgewezen is als AI dat beslist heeft?"**

Dat is precies het probleem. GDPR Art. 22 geeft individuen het recht om niet onderworpen te worden aan louter geautomatiseerde besluitvorming met significante gevolgen. Als jij die uitleg niet kunt geven, riskeert dat een handhavingstraject. Lokale AI die de recruiter ondersteunt maar niet vervangt, lost dit op: de beslissing blijft menselijk en uitlegbaar.

**"Onze kandidaten tekenen toch een toestemmingsverklaring?"**

Toestemming voor deelname is niet hetzelfde als toestemming voor elk gebruik van hun data. Toestemming voor AI-screening vereist specifieke informatie over welk systeem wordt ingezet en welke gevolgen het heeft. Een generieke clausule volstaat niet.

---

## Belgische en Nederlandse context

### België

**Federgon** [5] is de Belgische federatie van human resources dienstverleners. Federgon publiceert sectorrichtlijnen voor rekrutering en databeheer en heeft een deontologische code voor haar leden.

**Unia — Interfederaal Gelijkekansencentrum** [6] behandelt discriminatieklachten in België, inclusief klachten over discriminerende selectieprocedures. Unia heeft specifieke aandacht voor algoritmische discriminatie.

**Sociale Inspectie** controleert de naleving van antidiscriminatiewetgeving en arbeidsrecht. AI-tools in selectieprocedures kunnen onderdeel worden van een inspectiedossier.

### Nederland

**ABU en NBBU** [7] zijn de brancheorganisaties voor uitzend- en rekruteringsbureaus in Nederland. Zij publiceren gedragsregels en sectorstandaarden voor omgang met kandidatendata.

**College voor de Rechten van de Mens** [8] behandelt discriminatieklachten in Nederland. Het College heeft adviezen gepubliceerd over AI en discriminatie bij selectieprocedures.

**FNV** en **CNV** nemen actief standpunten in over AI in rekrutering en de bescherming van kandidaten en werknemers.

---

## Sectorcijfers (referentie)

- Aantal Belgische interimkantoren en rekruteringsbureaus: ca. 700 (Federgon, 2024)
- Aandeel Belgische bedrijven dat AI inzet in rekrutering: groeiend, schatting 20–30% voor 2025
- Gemiddeld aantal cv's per vacature in de Benelux: 40–120 afhankelijk van sector en functieniveau
- Gemiddelde kosten datalek kmo: €15.000–50.000 (IBM Cost of Data Breach Report 2024, gecorrigeerd voor kmo-schaal)

---

## Bronnen

1. **GDPR — Verordening (EU) 2016/679 (incl. Art. 22 — geautomatiseerde besluitvorming)**
   EUR-Lex, volledig geconsolideerde tekst
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj>

2. **AI Act — Verordening (EU) 2024/1689 — Bijlage III punt 4 (arbeidsgerelateerde AI = hoog-risico)**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

3. **GDPR Art. 22 — Geautomatiseerde individuele besluitvorming**
   EUR-Lex (zie bron 1)

4. **Wet van 10 mei 2007 ter bestrijding van discriminatie — België**
   Belgisch Staatsblad via e-Justice
   <https://www.ejustice.just.fgov.be>

5. **Federgon — Federatie van HR-dienstverleners**
   <https://www.federgon.be>

6. **Unia — Interfederaal Gelijkekansencentrum**
   <https://www.unia.be>

7. **ABU / NBBU — Brancheorganisaties uitzendbureau's Nederland**
   <https://www.abu.nl> / <https://www.nbbu.nl>

8. **College voor de Rechten van de Mens**
   <https://www.mensenrechten.nl>

---

_Onderdeel van: LocAI Bibliotheek · Sectordossiers_
_Vorige: S10 — Transport & Logistiek_
_Volgende: S12 — Verzekeringsmakelaars_
_Laatste update: 25 maart 2026_

---

## Bronnen

_[ referenties volgen bij uitwerking ]_

---

_Onderdeel van: LocAI Library · Sectordossiers_
_Vorige: S10 — Transport & Logistiek_
_Volgende: S12 — Verzekeringsmakelaars_
_Laatste update: maart 2026_
