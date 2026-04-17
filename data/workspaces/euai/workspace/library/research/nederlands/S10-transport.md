# S10 — Transport & Logistiek
### LocAI Bibliotheek · Sectordossier
_Versie 0.1 · 25 maart 2026_

---

## Wie zijn ze

Transport- en logistiekbedrijven draaien op data. Elke vracht die verplaatst wordt, laat een digitale stroom achter: wie rijdt waar, hoe snel, hoe lang, met welke lading, voor welke klant. Tegelijk werken de meeste bedrijven in de sector met werknemers en zelfstandige chauffeurs wier bewegingen continu worden geregistreerd — locatiedata die juridisch tot de meest gevoelige categorie van arbeidsrechtelijke gegevensverzameling behoort.

De sector is groot, operationeel gedreven en weinig bewust van zijn eigen datavorming. Een koeriersbedrijf van twaalf chauffeurs verwerkt dagelijks honderden adressen van particulieren, continue GPS-tracking van zijn personeel, rijgedragdata en commerciële vrachtinformatie van zijn klanten — maar beschouwt zichzelf zelden als een gegevensverwerkende entiteit.

**Typisch profiel:**
- Klein tot middelgroot transportbedrijf — 5 tot 100 voertuigen
- Sterk operationeel karakter: ritplanning, klantcommunicatie, compliance
- Mix van vaste chauffeurs en zelfstandige onderaannemers
- Afhankelijk van real-time data voor efficiënte werking

**Specifieke beroepsgroepen:**
- Wegvervoerders — stukgoed, groupage, vol- en deelladingen
- Koeriersdiensten — pakket- en expreslevering, last-mile
- Logistieke dienstverleners — warehousing, supply chain management
- Tankwagenvervoer — gevaarlijke stoffen, ADR-reglementering
- Personenvervoer — touringcar, leerlingenvervoer, zorgvervoer
- Zelfstandige chauffeurs en owner-operators

---

## Welke data verwerken ze

**Werknemers- en chauffeurdata:**
- Continue GPS-locatiedata — positie, snelheid, route, stops
- Rijtijdenregistratie — rij-, pauze- en rusttijden conform Verordening 561/2006 [3]
- Tachograafdata — digitale rijtijdenregistratie, snelheidsprofielen
- Rijgedragdata — hard remmen, scherp bochten nemen, stationair draaien
- Persoonlijke gegevens — naam, rijbewijsgegevens, ADR-certificaten, medische attesten
- Salarisdata en contractgegevens

**Klant- en vrachtdata:**
- Naam, adres en contactdata van opdrachtgevers en ontvangers
- Vrachtomschrijvingen, gewicht, volume, bijzondere instructies
- Leveringsadressen — ook particulieren bij last-mile levering
- Vrachtbrieven en CMR-documenten
- Tijdvensters en leveringsbevestigingen
- Klachten en incidentenregistratie

**Voertuig- en operationele data:**
- Voertuiggegevens — kentekens, onderhoudshistorie, kilometerstand
- Brandstofverbruik en CO₂-registratie (toenemend voor duurzaamheidsrapportage)
- Koeltemperatuurdata bij gekoelde transporten (farma, vers)
- Laad- en lostijden, laadplaatsen en magazijncodes

**Wat dit specifiek maakt:**
GPS-tracking van werknemers die hen de gehele werkdag volgt is arbeidsrechtelijk en privacyrechtelijk bijzonder gevoelig. De werknemer kan die registratie niet ontwijken — het is een structurele, permanente verwerking van zijn bewegingen, gedrag en prestaties. Dat vergt een duidelijke rechtsgrondslag, transparante informatieverstrekking, en strikte begrenzing van het gebruik: verkeersregels handhaven is iets anders dan rijgedragscores inzetten als beoordelingsinstrument voor loononderhandelingen of ontslag.

---

## Welke wetten zijn van toepassing

### GDPR — Locatietracking en werknemersmonitoring

Continue GPS-tracking van werknemers en chauffeurs is verwerking van persoonsdata — en vereist een geldige rechtsgrondslag [1]. Voor werkgevers is die rechtsgrondslag doorgaans gerechtvaardigd belang (Art. 6(1)(f)) — operationele efficiëntie, veiligheid en contractuele verplichtingen tegenover klanten. Die rechtsgrond is niet onbeperkt: het gebruik van locatiedata moet proportioneel zijn aan het doel waarvoor ze verzameld wordt.

**Proportionaliteit en gebruik:** locatiedata die verzameld wordt voor ritplanning en klantenservice mag niet worden gebruikt voor disciplinaire procedures of prestatiebeoordeling zonder expliciete informatie aan de werknemer. In veel cao's in de transport- en logistieke sector bestaan specifieke bepalingen over het gebruik van GPS-data voor beoordelingsdoeleinden.

**Bewaring:** locatiedata mag niet langer worden bewaard dan strikt noodzakelijk. Operationele ritdata van zes maanden geleden heeft geen waarde meer voor planningsdoeleinden — zes jaar bewaren voor "statistische doeleinden" is niet proportioneel.

**Verwerkersovereenkomsten:** elke telematics-provider, fleetmanagementsoftware of AI-analyseplatform dat locatie- of tachograafdata verwerkt namens het bedrijf, is een verwerker en vereist een verwerkersovereenkomst.

### AI Act — Werknemersmonitoring als hoog-risico

AI-systemen die worden ingezet voor de monitoring van werknemers — inclusief bewaking van gedrag, prestaties of locatie — zijn expliciet opgenomen in **Bijlage III, punt 4** (Werkgelegenheid, beheer van werknemers en toegang tot zelfstandige arbeid) van de AI Act als hoog-risico systemen [2]. Een AI-platform dat rijgedrag analyseert, chauffeurs een score geeft, of rijtijdencompliance automatisch controleert en rapporteert, valt in die categorie.

Dit heeft concrete gevolgen: hoog-risico AI-systemen moeten gedocumenteerd zijn, transparant zijn tegenover de betrokken werknemers, en menselijke controle waarborgen. Rijgedragscores die automatisch worden doorgestuurd naar HR zonder menselijke tussenkomst zijn problematisch. Een AI-systeem dat op basis van rijgedragdata prestatiescores genereert die worden gebruikt in functioneringsgesprekken, vereist volledige documentatie, transparantie en toetsing op discriminatierisico.

### Verordening 561/2006 — Rijtijdenwetgeving

De Europese rijtijdenverordening [3] legt maximale rij- en minimale rusttijden op voor chauffeurs van vrachtvoertuigen boven 3,5 ton. Tachografen — digitaal of analoog — registreren die tijden en zijn wettelijk verplicht. De data uit de tachograaf is persoonsgebonden: ze koppelt rijgedrag aan een specifieke bestuurder.

AI-analyse van tachograafdata voor compliance-controle is waardevol — maar de data is gevoelig: ze toont niet alleen of een chauffeur de regels naleeft, maar ook zijn pauzegedrag, zijn werkritme en eventuele overtredingen. Die data behoort op een goed beveiligde, gecontroleerde omgeving.

### NIS2 — Grote logistieke operators

Logistieke dienstverleners die als essentiële of belangrijke entiteit worden geclassificeerd onder NIS2 [4] — doorgaans grotere operators of operators in kritieke supply chains — hebben aanvullende cybersecurityverplichtingen. Voor de meeste kmo-transporteurs speelt NIS2 niet rechtstreeks, maar de keteneis — grote opdrachtgevers die hun leveranciers NIS2-compliance opleggen — wordt al voelbaar.

---

## Concrete use cases voor AI

### 1. Routeoptimalisatie

**Wat het is:** AI berekent optimale routes op basis van adressen, tijdvensters, voertuigkenmerken, verkeersdata en historische rijtijden.

**Waarde:** minder kilometers, kortere levertijden, lagere brandstofkosten. Een verbetering van 5–10% in ritefficiëntie is realistisch voor bedrijven die nog handmatig plannen.

**Met lokale AI:** klantadressen, leveringstijdvensters en historische ritdata zijn operationeel gevoelig. Klantadressen omvatten ook particuliere afleveradressen. Die data hoort op een eigen server, niet in een externe cloudplanner die ook de data van concurrenten verwerkt.

---

### 2. Rijgedraganalyse en veiligheidscoaching

**Wat het is:** AI analyseert tachograafdata en telematics om rijgedragspatronen te identificeren — hard remmen, scherpe bochten, overschreden snelheden — en genereert gerichte coachingfeedback.

**Waarde:** minder ongelukken, lagere verzekeringskosten, langere voertuiglevensduur.

**Opgelet AI Act én arbeidsrecht:** rijgedraganalyse die wordt ingezet als beoordelingsinstrument voor loon of ontslag is hoog-risico AI [2] en vereist transparantie, documentatie en menselijk toezicht. Cao-bepalingen over het gebruik van GPS-data voor beoordelingsdoeleinden moeten worden geëerbiedigd. De analyse moet worden gebruikt voor veiligheidsverbetering, niet als disciplinair mechanisme.

---

### 3. Predictief onderhoud

**Wat het is:** AI analyseert voertuigdata — kilometerstand, motordata, storingscodes — om onderhoudsbehoeften te voorspellen vóór ze tot een panne leiden.

**Waarde:** minder onverwachte uitval, lagere totale onderhoudskosten, betere vlootbeschikbaarheid.

**Met lokale AI:** voertuigdata is bedrijfseigen operationele informatie. Predictieve onderhoudsmodellen die getraind zijn op jouw vloothistorie zijn preciezer dan generieke cloud-modellen — en de data verlaat jouw omgeving niet.

---

### 4. Klantenservice en leveringscommunicatie

**Wat het is:** AI genereert automatische leveringsmeldingen, behandelt eenvoudige klantvragen over status en levertijden, en stelt antwoorden op klachten op.

**Waarde:** minder telefoon- en e-mailload op het planningsteam, betere klantenervaring bij last-mile levering.

**Met lokale AI:** klantcommunicatie bevat adressen, bestelgegevens en klanthistorie. Een lokale assistent verwerkt die informatie net zo goed, zonder dat klantdata de bedrijfsomgeving verlaat.

---

### 5. Rijtijdencompliance en rapportage

**Wat het is:** AI controleert tachograafdata automatisch op compliance met Verordening 561/2006, signaleert afwijkingen en genereert rapportages voor de sociale inspectie.

**Waarde:** minder handmatig controlewerk, vroege signalering van overtredingen, betere voorbereiding op controles.

**Met lokale AI:** tachograafdata is persoonsgebonden werknemersdata. Compliance-analyse op een lokale server betekent dat die data niet bij een externe provider staat die ook wetshandhavingsinstanties bedient of wiens beveiligingsniveau onbekend is.

---

## Het concrete risico met cloud-AI

**Het telematics-platform-scenario:**

Een transportbedrijf van dertig chauffeurs stapt over op een modern cloud fleet management platform met ingebouwde AI voor routeoptimalisatie, rijgedraganalyse en klantcommunicatie.

1. De GPS-locatie van elke chauffeur wordt continu gestreamd naar servers buiten de EU. Rijtijden, pauzelocaties, snelheidsprofielen en rijgedragscores worden opgeslagen op het platform van de aanbieder.
2. De AI van het platform gebruikt de gecombineerde data van alle aangesloten vloten om zijn optimalisatiemodellen te verbeteren — inclusief jouw klantadressen en leveringspatronen.
3. Bij een cyberaanval op de platformaanbieder liggen niet alleen klantgegevens bloot, maar ook de persoonlijke locatiedata en rijgedragprofielen van alle chauffeurs.
4. De verwerkersovereenkomst regelt de aansprakelijkheid in het voordeel van de aanbieder. Het transportbedrijf is de verwerkingsverantwoordelijke.
5. AI-functies voor rijgedragscoring kwalificeren als hoog-risico AI Act — documentatie en transparantie die het platform niet standaard levert, zijn jouw verantwoordelijkheid.

Lokale telematics-verwerking: locatiedata en tachograafdata op een eigen server, routeoptimalisatie en rijgedraganalyse zonder dat werknemersdata de onderneming verlaat.

---

## De kernboodschap voor het eerste gesprek

Begin niet bij GDPR of de AI Act. Begin bij de waarde van jouw operationele data.

> "Jouw klantadressen, jouw leveringspatronen, jouw rijtijden — dat is operationele kennis die jij over jaren hebt opgebouwd. Als je die verwerkt via een cloud platform, draag je die kennis over aan een systeem dat ook de data van je concurrent verwerkt. Jouw routeoptimalisatiemodel wordt gedeeld inzicht."

Vervolg over werknemersdata:

> "Tegelijk zijn je chauffeurs mensen, geen data-objecten. Continue locatietracking en rijgedragscores die bij een externe provider staan, kunnen juridisch terugslaan — bij sociale inspectie, bij arbeidsrechtelijke geschillen, of gewoon bij een datalek. Lokale verwerking geeft jou de controle die je wettelijk al moet hebben."

---

## Vragen die ze stellen en hoe je antwoordt

**"Onze telematics-provider zorgt al voor de compliance — dat is hun probleem."**

De provider is een verwerker. Jij bent de verwerkingsverantwoordelijke. Als de servers van de provider worden gehackt en de locatiedata van jouw chauffeurs uitlekt, ben jij meldingsplichtig. Als de Sociale Inspectie vraagt wie toegang heeft tot de tachograafdata van jouw bestuurders, ben jij verantwoordelijk voor het antwoord. Een verwerkersovereenkomst verdeelt de verantwoordelijkheid — ze heft ze niet op.

**"Mijn chauffeurs weten toch dat ze gevolgd worden. Wat is het probleem?"**

Wetenschap is niet hetzelfde als rechtmatige verwerking. GDPR vereist dat werknemers geïnformeerd worden over welke data verzameld wordt, voor welk doel, hoe lang die bewaard wordt en wie er toegang toe heeft. Weten dat er een GPS in de truck zit is niet hetzelfde als weten dat hun locatiedata zes jaar bewaard wordt op een server in Ierland en gebruikt wordt voor AI-modeltraining. Dat onderscheid is juridisch relevant.

**"AI-rijgedraganalyse is toch positief — het helpt chauffeurs veiliger te rijden."**

Dat klopt — als het zo gebruikt wordt. Zodra rijgedragscores worden ingezet voor loonbesprekingen, functioneringsgesprekken of ontslagprocedures, ben je in het domein van hoog-risico AI (AI Act Bijlage III) en arbeidsrechtelijke cao-verplichtingen. Die grens is gemakkelijk te overschrijden. Het gebruik van de scores bepaalt het juridische risico, niet het systeem zelf.

**"Routeplanning werkt toch beter in de cloud — meer data, betere modellen?"**

De meeste routeoptimalisatiemodellen zijn generiek. De bedrijfsspecifieke data — jouw klantadressen, jouw tijdvensters, jouw historische levertijden — is het waardevolle deel. Dat kun je lokaal verwerken en combineren met vrij beschikbare geografische data, zonder dat je operationele intelligence een extern platform voedt.

**"Moeten mijn chauffeurs ook geïnformeerd worden?"**

Ja. GDPR Art. 13 verplicht werkgevers om werknemers bij aanvang van de verwerking te informeren over de gegevensverwerking die op hen betrekking heeft. In België bestaan hier ook specifieke cao-verplichtingen en een informatieplicht aan het CPBW (Comité voor Preventie en Bescherming op het Werk).

---

## Belgische en Nederlandse context

### België

**FEBETRANS** [5] is de Federatie van Belgische Transporteurs en Logistieke Dienstverleners. FEBETRANS vertegenwoordigt Belgische wegtransporteurs en publiceert sectorrichtlijnen over operationele en sociale compliance. Tachograaf- en rijtijdenwetgeving wordt gehandhaafd door de Directie Wegverkeer en de Sociale Inspectie.

**Sociale Inspectie** controleert de naleving van rijtijdenwetgeving en registratievereisten. Overtredingen kunnen leiden tot boetes voor zowel het bedrijf als de chauffeur.

**GOCA** en **DIV** (Dienst Inschrijving Voertuigen) zijn relevante instanties voor voertuig- en rijbewijsadministratie.

### Nederland

**TLN — Transport en Logistiek Nederland** [6] is de grootste werkgeversorganisatie in de Nederlandse transport- en logistieke sector. TLN publiceert richtlijnen over arbeidsrecht, cao-verplichtingen en digitale tools. De cao Transport Nederlandse Ondernemingen bevat specifieke bepalingen over monitoring en GPS-gebruik.

**Inspectie Leefomgeving en Transport (ILT)** handhaaft rijtijdenwetgeving in Nederland, inclusief digitale tachograafdata.

**FNV Transport & Logistiek** en **CNV Vakmensen** nemen actief standpunten in over GPS-monitoring en het gebruik van werknemersdata voor beoordelingsdoeleinden.

---

## Sectorcijfers (referentie)

- Belgisch wegtransport: ca. 13.000 geregistreerde transportondernemingen (Statbel, 2024)
- Nederlandse transportsector: ca. 35.000 ondernemingen (CBS, 2024)
- Aandeel internationale ritten Belgisch transport: ca. 60% van de omzet
- Gemiddeld aantal chauffeurs per Belgisch transportkmo: 5–20
- Boetes sociale inspectie rijtijden: tot €1.800 per chauffeur per overtreding (BE)
- Gemiddelde kosten datalek kmo: €15.000–50.000 (IBM Cost of Data Breach Report 2024, gecorrigeerd voor kmo-schaal)

---

## Bronnen

1. **GDPR — Verordening (EU) 2016/679**
   EUR-Lex, volledig geconsolideerde tekst
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj>

2. **AI Act — Verordening (EU) 2024/1689 — Hoog-risico systemen en Bijlage III (werknemersmonitoring)**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

3. **Verordening (EG) 561/2006 — Rij- en rusttijden wegvervoer**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2006/561/oj>

4. **NIS2 — Richtlijn (EU) 2022/2555**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/dir/2022/2555/oj>

5. **FEBETRANS — Federatie van Belgische Transporteurs en Logistieke Dienstverleners**
   <https://www.febetrans.be>

6. **TLN — Transport en Logistiek Nederland**
   <https://www.tln.nl>

---

_Onderdeel van: LocAI Bibliotheek · Sectordossiers_
_Vorige: S09 — Non-profit & Vzw_
_Volgende: S11 — HR & Rekrutering_
_Laatste update: 25 maart 2026_

---

## Bronnen

_[ referenties volgen bij uitwerking ]_

---

_Onderdeel van: LocAI Library · Sectordossiers_
_Vorige: S09 — VZW & Non-profit_
_Volgende: S11 — HR & Rekrutering_
_Laatste update: maart 2026_
