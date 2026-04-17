# S13 — Bouw & Aannemers
### LocAI Bibliotheek · Sectordossier
_Versie 0.1 · 25 maart 2026_

---

## Wie zijn ze

De bouwsector omvat iedereen die verantwoordelijk is voor het ontwerpen, bouwen, renoveren en onderhouden van gebouwen en infrastructuur — van de aannemer die een woonproject leidde tot de loodgieter die een ketel vervangt. Het is een sector van kmo’s: de overgrote meerderheid van de bouw- en renovatiebedrijven in België en Nederland telt minder dan tien medewerkers.

AI heeft een duidelijke toepassingsruimte in de bouw: offertes opstellen kost tijd, werfverslagen schrijven is repetitief werk, aanbestedingsdossiers zijn omvangrijke documenten met vaste structuur. Tegelijk is de sector relatief laat gedigitaliseerd, werken veel bedrijven nog met papieren werfadministratie, en is het bewustzijn over data governance beperkt. Dat combineert tot een sector waar AI snel waarde kan leveren — en waar de risico’s onderschat worden.

**Typisch profiel:**
- Algemene aannemers — nieuwbouw en renovatie, woning en utiliteitsbouw
- Gespecialiseerde vaklui — elektriciens, loodgieters, schilders, tegelzetters, schrijnwerkers
- Architectenbureaus — ontwerp, bouwbegeleiding, vergunningsbeheer
- Projectontwikkelaars — grotere woningbouwprojecten en commercieel vastgoed
- Infrabedrijven — wegenbouw, nutsinfrastructuur, grondwerken

**Wat hen onderscheidt:** bouwbedrijven verwerken data van drie verschillende partijen tegelijk — opdrachtgevers, onderaannemers en werknemers. Die driehoek maakt het databeheer complexer dan het er op eerste gezicht uitziet.

---

## Welke data verwerken ze

**Opdrachtgevers- en projectdata:**
- Persoonsgegevens van particuliere opdrachtgevers — naam, adres, contactdata
- Eigendomsgegevens en bouwvergunningen
- Offertes, bouwtekeningen en technische specificaties
- Contracten en wijzigingsbeheer
- Facturen en betalingshistorie

**Onderaannemer- en leveranciersdata:**
- Bedrijfsgegevens en contactpersonen
- Prijsafspraken en inkoopcontracten
- Prestatiebeoordeling bij terugkerende samenwerking
- Kwalificaties en vergunningsbewijzen (VCA, erkenningsbewijzen)

**Werknemersdata:**
- Persoonsgegevens, arbeidscontracten, functieclassificaties
- Werfpresentielijsten en tijdregistratie
- Veiligheidsopleidingen en certificaten (VCA, triltool, hoogwerker)
- Medische geschiktheidsverklaringen voor specifieke functies

**Werfregistratie en LIMOSA (BE):**
- Registratie van buitenlandse werknemers op de werf (verplicht in België via LIMOSA)
- Subcontractorketens — wie staat er op de werf, voor wie, wanneer
- Uurregistratie voor sociale inspectie en aanbestedingsverplichtingen

**Veiligheids- en omgevingsdata:**
- Veiligheidsplannen (VGP) en risico-inventarisaties
- Camerabeelden op beveiligde werven (potentieel hoog-risico AI Act)
- Incidentregistraties en bijna-ongevallenrapportages

**Wat dit specifiek maakt:** de keten is lang en onzichtbaar voor de meeste bedrijven. Een aannemer die een offerte maakt met AI, voert klantpersoonsdata in. Een aannemer die zijn werftijden registreert met een app, verwerkt werknemersdata. Een architect die AI gebruikt voor bouwverslagen, werkt met projectspecifieke informatie die opdrachtgevers vertrouwelijk beschouwen.

---

## Welke wetten zijn van toepassing

### GDPR — Drie data-lagen tegelijk

De GDPR is van toepassing op alle persoonsdata die bouwbedrijven verwerken: klantdata, werknemersdata en in sommige gevallen data van derde partijen op de werf [1]. Voor de meeste kmo-aannemers is het goed nieuws dat hun datatypes relatief gewoon zijn — geen artikel 9 bijzondere gegevens in de dagelijkse werking. De discipline zit in het bewaarbeleid (hoe lang bewaart u offertes van afgewezen klanten?) en de verwerkersverhoudingen (welke apps en tools verwerken werknemersdata?).

### AI Act — Camerabeveiliging op werf als hoog-risico grensgebied

AI-systemen die camerabeelden analyseren met als doel personen te identificeren, toegang te bewaken of gedrag te monitoren, vallen potentieel in de hoog-risico categorie van AI Act Bijlage III [2]. Een bewakingscamera op een werf die alleen opneemt, is geen AI. Een systeem dat camerabeelden analyseert om onbevoegden te detecteren, vluchtwegen te monitoren of werftoegang te loggen op basis van gezichtsherkenning — dat is AI Act-relevant.

**Praktische boodschap:** de meeste bouwkmo’s zetten geen AI-gedreven camerasystemen in. Maar naarmate werfsoftware meer intelligente functies integreert, is het relevant om te weten wanneer een toepassing in de hoog-risico categorie terechtkomt.

### NIS2 — Grote aannemers en aanneemdiensten

Grote infrabedrijven en aannemers die werken aan kritieke infrastructuur (energie, water, transport) kunnen als exploitant van essentiële diensten worden geclassificeerd onder de NIS2-richtlijn [3]. Dat brengt cybersecurityverplichtingen mee voor hun operationele IT-systemen.

### LIMOSA — Registratie van buitenlandse werknemers (België)

Een aannemer in België die buitenlandse werkne mers of onderaannemers inschakelt, is verplicht hen vooraf te melden via het LIMOSA-systeem [4]. Dat systeem genereert persoonsdata van werknemers die wettelijk verwerkt en bewaard moet worden. AI die werfpresentielijsten geneert of beheert op basis van LIMOSA-data, verwerkt werknemerspersoonsdata.

### Wkba — Wet keten aansprakelijkheid (Nederland)

In Nederland regelt de Wet keten aansprakelijkheid (Wkba) [5] de aansprakelijkheid in de bouwketen voor loonafdrachten en sociale premies. Aannemers die met onderaannemers werken moeten documenteren wie er op de werf werkt en voor wie. Dat documentatieproces is een administratieve last — en een toepassing waar AI efficiëntie kan brengen mits de onderliggende data correct wordt verwerkt.

---

## Concrete use cases voor AI

### 1. Offertes opstellen

**Wat het is:** AI genereert offertes op basis van projectbeschrijvingen, historische prijsdata, materiaalprijzen en de opdrachtgevercontext.

**Waarde:** snellere offertering, consistentere prijsopbouw, minder kans op vergeten posten. Voor aannemers die tientallen offertes per jaar schrijven, levert dit aanzienlijke tijdsbesparing.

**Met lokale AI:** offertes bevatten klantpersoonsdata (naam, adres, project) en bedrijfsvertrouwelijke prijsinformatie. Die combinatie hoort niet thuis op een cloud AI-platform. Marginale prijzen, onderaannemerkorting, en strategische projectkeuzes zijn informatie die niet naar een externe server mag.

---

### 2. Werfverslagen en dagelijkse rapportage

**Wat het is:** AI structureert en schrijft dagelijkse werfverslagen op basis van mondelinge of schriftelijke notities van de werfleider.

**Waarde:** minder schrijfwerk voor werfleiders, consistente documentatie, betere juridische bescherming bij geschillen over uitgevoerde werken.

**Met lokale AI:** werfverslagen zijn projectdocumentatie die opdrachtgevers vertrouwelijk beschouwen en die bij geschillen als juridisch bewijs dienen. Ze horen op een systeem dat de aannemer zelf beheert.

---

### 3. Planningsoptimalisatie

**Wat het is:** AI analyseert werftijdlijnen, materiaalleveringen, weersverwachtingen en personeelsbeschikbaarheid om de werfplanning te optimaliseren.

**Waarde:** minder stilstand, betere afstemming van onderaannemers, tijdige signalering van vertragingsrisico’s.

**Met lokale AI:** planningsdata bevat informatie over werknemers, onderaannemers en projectdeadlines. Bij grotere projecten is die data commercieel gevoelig.

---

### 4. Veiligheidsinstructies en toolbox talks

**Wat het is:** AI genereert gepe rsonaliseerde veiligheidsinstructies en toolbox talk-inhoud op basis van de specifieke werfrisico’s, het geplande werk en de betrokken werknemers.

**Waarde:** betere veiligheidscultuur, minder tijdverlies bij de voorbereiding van veiligheidsmomenten, aangetoonde compliance met Codex Welzijn op het Werk (BE) / Arbowet (NL).

**Praktisch:** veiligheidsinstructies bevatten de aard van de risico’s op de werf. Dat informeert externe partijen over de staat van het project. Lokale opslag is logisch.

---

### 5. Aanbestedingsdossiers en overheidsopdrachten

**Wat het is:** AI stelt aanbestedingsdocumentatie op — technische nota’s, refrentielijsten, kwaliteitsborgingsdocumenten — op basis van de projectgeschiedenis en de vereisten van het lastenboek.

**Waarde:** minder tijd besteed aan het samenstellen van omvangrijke dossiers, betere consistentie, hogere slagingskans bij herhaald inschrijven op gelijkaardige opdrachten.

**Met lokale AI:** aanbestedingsdossiers bevatten de projectreferenties en competentieprofielen die het concurrentievoordeel van het bouwbedrijf vormen. Die informatie is bedrijfsvertrouwelijk.

---

## Het concrete risico met cloud-AI

**Het werfapp-scenario:**

Een aannemer stapt over op een moderne werfbeheersapp met geïntegreerde AI voor planningsoptimalisatie en rapportage.

1. Werknemers klokken in en uit via de app. Hun aanwezigheids- en locatiedata wordt continu doorgestuurd naar servers van de app-aanbieder.
2. Werfleiders dicteren dagelijkse verslagen in de app. Die spraakinput — projectdetails, leveranciersgesprekken, probleembeschrijvingen — wordt verwerkt door cloudgebaseerde spraakherkenning op externe servers.
3. Klantpersoonsdata en projectbeschrijvingen die in offertemodules worden ingevoerd, worden meegezogen in het AI-trainingsproces van de aanbieder.
4. Een werknemersvertegenwoordiger vraagt inzage in de locatiedata die via de app is verwerkt. De aannemer heeft geen directe toegang tot die gegevens bij de cloudaanbieder.
5. Bij een aanbestedingsprocedure vraagt de opdrachtgever naar de verwerkersovereenkomst voor tools die projectdata beheren. Die overeenkomst bestaat niet.

Lokale AI voor offertering, werfrapportage en planningsdocumentatie: projectdata, klantinfo en werknemersdata blijven op het eigen systeem. Compliance is aantoonbaar. Concurrentiegevoelige informatie lekt niet.

---

## De kernboodschap voor het eerste gesprek

Begin bij de praktische waarde, niet bij de regelgeving.

> "Offertes schrijven kost je tijd die je liever op de werf besteedt. Werfverslagen zijn repetitief werk. Aanbestedingsdossiers zijn telkens opnieuw hetzelfde stramien. Dat lost AI op — snel en degelijk."

Vervolg met het datapunt:

> "Het enige wat we vermijden, is die data naar een externe server sturen. Klantadressen, projectdetails, werknemerspresences — dat is jouw informatie. Een lokaal systeem houdt die bij jou."

---

## Vragen die ze stellen en hoe je antwoordt

**"Wij werken nog gewoon met Word en Excel — waarom zou ik AI nodig hebben?"**

Dat is een eerlijk uitgangspunt. AI is geen verplichte upgrade — het is een efficiëntietool. Als je twintig offertes per maand schrijft en elk offerte je twee uur kost, en AI brengt dat terug naar twintig minuten: dat is veertig uur per maand vrijgemaakt voor werk op de werf. De vraag is niet "moet ik AI gebruiken" maar "welke taken kost me nu onnodige tijd?"

**"Onze klantdata is gewoon een naam en adres — dat is toch niet gevoelig?"**

Naam en adres zijn persoonsdata onder de GDPR. Ze mogen niet zonder meer worden doorgegeven aan een cloudprovider zonder verwerkersovereenkomst en transparantie tegenover de klant. Dat is geen horror-scenario — het is de basisregel die voor iedereen geldt, ook voor de kmo.

**"Onze werfapp heeft alles centraal staan — makkelijk."**

Centraliseren bij een externe aanbieder is gemakkelijk — totdat de aanbieder failliet gaat, zijn tarieven verdrievoudigt, of de data om een andere reden niet meer toegankelijk is. Lokale opslag met lokale AI geeft je dezelfde centrale toegankelijkheid én eigenaarschap over je eigen data.

**"Wij werken met buitenlandse onderaannemers — LIMOSA is toch hun verantwoordelijkheid?"**

LIMOSA-aanmelding is mede de verantwoordelijkheid van de hoofdaannemer. Als de buitenlandse onderaannemer niet aangemeld is en er is een sociale inspectie, is de hoofdaannemer aansprakelijk. AI die helpt bij het bijhouden van de onderaannemersketen en de LIMOSA-status is een compliancetool die concrete boeterisico’s vermijdt.

**"Camerabeveiliging op de werf — heb ik daar toestemming voor nodig?"**

Voor gewone bewakingscamera’s gelden de standaard GDPR- en CAO 68-regels (BE) / Wet particuliere beveiligingsorganisaties (NL): informatieplicht, registratie, bewaarperiode van maximaal dertig dagen. Als die camera’s gekoppeld zijn aan AI-analyse — bewegingsdetectie, toegangsherkenning — stap je in een hoog-risico categorie die aanvullende verplichtingen meebrengt.

---

## Belgische en Nederlandse context

### België

**Confederatie Bouw** [6] is de sectorale werkgeversorganisatie voor de Belgische bouwnijverheid. Confederatie Bouw vertegenwoordigt meer dan 13.000 bouwbedrijven en publiceert sectorstandaarden en arbeidsrechtelijke updates.

**PC 124 — Paritair Comité voor het Bouwbedrijf** is het paritair comité voor bouw- en aanverwante activiteiten in België. De collectieve arbeidsovereenkomsten van PC 124 regelen onder andere tijdregistratie en werftoegang — direct relevant voor data verwerkt via werfbeheersapps.

**LIMOSA** [4] is het systeem voor aanmelding van buitenlandse werknemers bij tewerkstelling in België. De aanmelding is verplicht en genereert een LIMOSA-bewijs dat op de werf beschikbaar moet zijn.

### Nederland

**Bouwend Nederland** [7] is de brancheorganisatie voor aannemers en gespecialiseerde bouwbedrijven in Nederland. Bouwend Nederland publiceert leden informatie over arbeidsrecht, wettelijke verplichtingen en sectorontwikkelingen.

**De Wkba — Wet keten aansprakelijkheid** [5] verplicht aannemers in Nederland tot ketendocumentatie voor loonbetalingsketen en sociale premies. Dat creîrt een administratieve stroom die AI efficiënt kan ondersteunen.

**Inspectie SZW** (thans onderdeel van NLA — Nederlandse Arbeidsinspectie) controleert de naleving van arbeids- en veiligheidswetgeving op Nederlandse bouwwerven.

---

## Sectorcijfers (referentie)

- Aantal bouwbedrijven in België: ca. 78.000 (Statbel, 2024)
- Aantal bouwbedrijven in Nederland: ca. 90.000 (CBS, 2024)
- Aandeel kmo’s (< 10 medewerkers) in de Belgische bouwsector: >85%
- Gemiddeld aantal offertes per aannemer per jaar (kmo): 30–120
- Aandeel bouwbedrijven met een formele GDPR-verwerkersovereenkomst voor hun werfapps: geschat < 20% (Confederatie Bouw interne inschatting, 2023)

---

## Bronnen

1. **GDPR — Verordening (EU) 2016/679**
   EUR-Lex, volledig geconsolideerde tekst
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj>

2. **AI Act — Verordening (EU) 2024/1689 — Bijlage III**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

3. **NIS2-richtlijn — Richtlijn (EU) 2022/2555**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/dir/2022/2555/oj>

4. **LIMOSA — Limosa.be — Melding buitenlandse werknemers (België)**
   <https://www.limosa.be>

5. **Wkba — Wet keten aansprakelijkheid (Nederland)**
   Overheid.nl
   <https://wetten.overheid.nl>

6. **Confederatie Bouw (België)**
   <https://www.confederatiebouw.be>

7. **Bouwend Nederland**
   <https://www.bouwendnederland.nl>

---

_Onderdeel van: LocAI Bibliotheek · Sectordossiers_
_Vorige: S12 — Verzekeringsmakelaars_
_Volgende: S14 — Lokale Middenstand_
_Laatste update: 25 maart 2026_
