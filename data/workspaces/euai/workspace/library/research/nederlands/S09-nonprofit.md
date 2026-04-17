# S09 — Non-profit & Vzw
### LocAI Bibliotheek · Sectordossier
_Versie 0.1 · 25 maart 2026_

---

## Wie zijn ze

Non-profitorganisaties worden gedreven door een missie, niet door winstoogmerk. Toch verwerken ze dagelijks grote hoeveelheden persoonsdata — van donoren die de werking financieren tot begunstigden die afhankelijk zijn van de zorg of dienstverlening die de organisatie biedt. Die combinatie maakt het sector die qua data-intensiteit weinig onderdoet voor de gezondheidszorg of financiële diensten, maar die er zelden als zodanig wordt behandeld.

Een sociale vzw die thuiszorg coördineert kent de medische situatie, woonsituatie en financiële kwetsbaarheid van tientallen of honderden mensen. Een jeugdorganisatie bewaart niet alleen ledendata maar ook uittreksels uit het strafregister van haar vrijwilligers. Een fondsenwervende NGO combineert IBAN-nummers van donoren met informatie over de doelgroepen waarvoor ze werkt — informatie die in het verkeerde handen disproportioneel veel schade kan aanrichten.

**Typisch profiel:** klein tot middelgroot, sterk afhankelijk van vrijwilligers, gefinancierd door een mix van subsidies, donaties en lidgelden. Compliance-bewustzijn is er vaak minder uitgesproken aanwezig dan in commerciële sectoren — niet door onwil, maar door beperkte middelen en schaarse juridische expertise.

**Specifieke beroepsgroepen:**
- Sociale vzw's — thuiszorg, maatschappelijk werk, hulpverlening, crisisopvang
- Culturele organisaties — musea, theaterfederaties, amateurkunstverenigingen
- Sportclubs en -federaties
- Welzijnsorganisaties en OCMW-verwante initiatieven
- Fondsen en filantropische instellingen
- Religieuze organisaties
- Buurtorganisaties en wijkcomités
- Internationale NGO's met een Belgisch of Nederlands kantoor

---

## Welke data verwerken ze

**Ledendata:**
- Naam, contactdata, lidmaatschapshistorie
- Betalingsgegevens — lidgelden, bijdragen
- Communicatievoorkeuren en betrokkenheid bij activiteiten

**Donordata:**
- Naam, adres, IBAN (voor fiscale attesten en domiciliëring)
- Financiële bijdragen — bedragen, frequentie, aanwervingskanaal
- Communicatiegeschiedenis en campagnerespons
- Vastgelegde contactmomenten — telefoongesprekken, e-mailuitwisseling, evenementen

**Vrijwilligersdata:**
- Identiteitsgegevens en contactinformatie
- Beschikbaarheid, taken en vaardigheden
- Opleidingen en certificaten
- Uittreksel uit het strafregister — met name bij jeugdwerk, werk met kwetsbare personen of kinderen (bijzonder gevoelig)

**Begunstigdendata:**
- Identiteitsgegevens en gezinssituatie
- Sociale situatie — inkomen, huisvesting, werksituatie
- Zorgdossiers en begeleidingshistorie
- Gezondheidsgegevens, mentale gezondheid, verslavingsproblematiek
- Dit is de gevoeligste categorie — GDPR Art. 9 [1]

**Wat dit specifiek maakt:** de combinatie van donordata (financieel en gedragsmatig) en begunstigdendata (mogelijk gezondheids- of sociale kwetsbaarheidsgegevens) op hetzelfde digitale platform is uitzonderlijk gevoelig. Een datalek raakt niet alleen de privacy van individuen, maar ook de vertrouwensrelatie die de absolute kern is van de werking van elke non-profitorganisatie. Donoren moeten erop kunnen vertrouwen dat hun bijdragen discreet beheerd worden. Begunstigden moeten erop kunnen vertrouwen dat hun situatie nooit de weg vindt naar onbevoegden — inclusief de donoren die de organisatie financieren.

---

## Welke wetten zijn van toepassing

### GDPR — Doelbinding, bijzondere categorieën en dataminimalisatie

Non-profitorganisaties verzamelen data van meerdere stakeholdergroepen voor fundamenteel verschillende doeleinden [1]. Donordata mag niet worden ingezet voor begunstigdenbeheer. Vrijwilligersdata mag niet worden gedeeld met donoren. Ledendata van een sportclub mag niet worden gebruikt voor politieke communicatie. Dit principe van doelbinding — persoonsdata wordt uitsluitend verwerkt voor het doel waarvoor ze verzameld is — is in de non-profit bijzonder kritisch omdat de organisatie meerdere rollen tegelijk vervult.

Voor ledencommunicatie en donorwerving speelt de keuze tussen toestemming (Art. 6(1)(a)) en gerechtvaardigd belang (Art. 6(1)(f)) een centrale rol [1]. Bestaande leden en donoren kunnen op basis van gerechtvaardigd belang worden benaderd, mits met duidelijke opt-out. Nieuwe contacten vereisen in de meeste gevallen expliciete toestemming. Fiscale attesten voor giften zijn gekoppeld aan een wettelijke bewaarplicht van zeven jaar — donordata mag dus niet zomaar worden gewist. Dit creëert een spanning met het recht op wissing onder GDPR.

Elke externe CRM, fundraisingplatform of e-mailtool waarmee persoonsdata worden gedeeld, vereist een verwerkersovereenkomst (Data Processor Agreement). De non-profit blijft te allen tijde verwerkingsverantwoordelijke — en daarmee aansprakelijk voor wat haar verwerkers doen.

### GDPR Art. 9 — Bijzondere categorieën persoonsgegevens

Sociale non-profits die werken met gezondheidsdata, mentale gezondheidsdata, gegevens over sociale kwetsbaarheid of informatie over verslavingsproblematiek van begunstigden verwerken "bijzondere categorieën" in de zin van Art. 9 GDPR [1]. Dit is het hoogste beschermingsniveau binnen de verordening. Verwerking is in principe verboden, tenzij een expliciete uitzonderingsgrond van Art. 9(2) van toepassing is — doorgaans expliciete toestemming van de betrokkene, of aanzienlijk openbaar belang met passende waarborgen.

Elke cloud-omgeving die begunstigdendata verwerkt — intake-formulieren, dossierbeheersoftware, casemanagementtools — moet over een robuuste verwerkersovereenkomst beschikken die specifiek de Art. 9-verplichtingen adresseert. Art. 9-data op US-gebaseerde fundraising- of CRM-platforms vertegenwoordigt een significante juridische kwetsbaarheid: de combinatie van een zwakke rechtsbasis, transatlantische datatransfers, en commerciële gebruiksvoorwaarden die ruimte laten voor modeltraining creëert een risicoprofiel dat moeilijk te verdedigen is tegenover de toezichthouder.

### WVV — Wetboek van Vennootschappen en Verenigingen (België)

De Wet van 23 maart 2019 betreffende het Wetboek van Vennootschappen en Verenigingen [2] regelt de werking van vzw's in België. De WVV legt verplichtingen op inzake bestuur — algemene vergadering, raad van bestuur, jaarrekening — en vereist dat beslissingen en financiële gegevens traceerbaar en controleerbaar zijn.

Digitale tools die worden ingezet voor bestuurlijke processen — verslaggeving van vergaderingen, financieel beheer, subsidiedossiers — moeten die traceerbaarheid ondersteunen. Een AI-tool die bestuursvergaderingen samenvat of financiële rapportages genereert, maakt deel uit van het officiële besluitvormingsdossier van de vzw. Als die output wordt gegenereerd via een externe clouddienst, stelt zich de vraag welke controle de vzw heeft over de integriteit en duurzaamheid van die gegevens.

### WBTR — Wet bestuur en toezicht rechtspersonen (Nederland)

De WBTR (2021) [3] regelt de governance van verenigingen en stichtingen in Nederland. Bestuurders hebben individuele aansprakelijkheid en zijn verantwoordelijk voor een deugdelijk bestuur. Digitale dossiers — inclusief AI-gegenereerde outputs die worden gebruikt voor bestuursbeslissingen of externe verantwoording — moeten auditeerbaar zijn.

Een AI-systeem dat subsidieaanvragen genereert, impactrapportages opstelt of begunstigdenstatistieken verwerkt en daarvoor gebruikmaakt van een externe cloudinfrastructuur buiten de controle van de organisatie, creëert een traceerbaarheidsprobleem dat botst met de individuele bestuurdersverantwoordelijkheid onder de WBTR.

### AI Act — Donorscore- en toelatingsmodellen

AI-modellen die worden ingezet voor donorscoring — wie gaat hoeveel geven, wie is het meest vatbaar voor een wervingscampagne — of voor het prioriteren van begunstigden bij toelatingsprocessen kunnen kwalificeren als hoog-risico onder de AI Act [4]. Bijlage III van de AI Act omschrijft systemen die de toegang tot essentiële diensten of ondersteuning significant beïnvloeden als potentieel hoog-risico. Een intake-systeem dat automatisch bepaalt wie in aanmerking komt voor zorg of ondersteuning, of dat aanvragers rangschikt op basis van een algoritme, valt in principe onder die categorie.

Voor hoog-risico AI-systemen zijn transparantievereisten en menselijk toezicht verplicht [4]. De non-profit die zo'n systeem inzet — ook als ze het afneemt als dienst — draagt de verantwoordelijkheid voor correcte implementatie en documentatie.

---

## Concrete use cases voor AI

### 1. Donorcommunicatie en -segmentatie

**Wat het is:** AI analyseert geefgeschiedenis, communicatierespons en betrokkenheidspatronen om donorcommunicatie te personaliseren — gepaste aansprekingstoon, relevant campagnemoment, passend donatiebedrag als voorstel in een aanvraagbrief.

**Waarde:** donorretentie is voor de meeste non-profits goedkoper dan nieuwe donorwerving. Gepersonaliseerde communicatie verhoogt retentie significant. Campagnes die aansluiten bij het bewezen engagement van een donor presteren structureel beter dan generieke mailings.

**Met lokale AI:** donorprofielen bevatten financiële data (IBAN, bijdragehistorie), communicatiegeschiedenissen en soms persoonlijke aantekeningen over contactmomenten. Die data thuishouden op de eigen server betekent dat ze niet wordt ingezet voor modeltraining op een commercieel fundraisingplatform dat ook de concurrerende fondsen van dezelfde donoren bedient.

---

### 2. Vrijwilligersplanning

**Wat het is:** AI matcht beschikbaarheid, vaardigheden en voorkeuren van vrijwilligers aan concrete taken en planningen — evenementen, dagelijkse werking, noodinterventies.

**Waarde:** no-shows en inefficiënte inzet zijn chronische problemen bij vrijwilligersorganisaties. Een slimme planningsassistent die rekening houdt met eerdere inzet, trainingsniveau en persoonlijke omstandigheden vermindert de coördinatielast voor de vrijwilligerscoördinator.

**Met lokale AI:** vrijwilligersprofielen bevatten soms bijzonder gevoelige data — beschikbaarheid door persoonlijke omstandigheden, achtergrondchecks, gezondheidsbelemmeringen. Die informatie hoort op de eigen server, niet op een extern platform.

---

### 3. Subsidie- en rapportageondersteuning

**Wat het is:** AI ondersteunt het opstellen van subsidiedossiers, impactrapporten en jaarverslagen — structurering van informatie, taalkundige verfijning, consistentiecheck tussen verschillende rapportagemomenten.

**Waarde:** voor kleine organisaties met beperkte stafcapaciteit is de administratieve last van subsidieaanvragen en -rapportages een van de grootste drempels. AI kan die last substantieel verlichten.

**Met lokale AI:** subsidiedossiers en impactrapporten bevatten organisatieprestaties, begunstigdenstatistieken en financiële overzichten. Dat is strategische organisatie-informatie die niet toebehoort aan een externe clouddienst.

---

### 4. Begunstigdenintake en -dossiers

**Wat het is:** AI helpt intakeformulieren te structureren, onvolledige dossiers te signaleren en casenotes samen te vatten voor snelle raadpleging.

**Waarde:** snellere en consistentere intake, minder administratieve vertraging in de zorgverlening, betere overdracht tussen medewerkers.

**Opgelet AI Act:** als AI automatisch beslist over toegang tot zorg of ondersteuning — of individuen rangschikt in een wachtlijst op basis van een model — is menselijk toezicht verplicht [4]. Dit kan kwalificeren als hoog-risico AI onder Bijlage III. Bovendien: begunstigdendata is Art. 9-data [1] — verwerking vereist een expliciete juridische grondslag die verder gaat dan de standaardverwerking van gewone persoonsdata.

---

### 5. Impact monitoring en verslaggeving

**Wat het is:** AI aggregeert en visualiseert programmaresultaten — bereik, uitkomsten, trends over tijd — voor bestuur, subsidiënten en het publiek.

**Waarde:** betere onderbouwing van de maatschappelijke impact, efficiëntere rapportage aan donoren en overheden, sterkere positie in subsidieaanvragen.

**Met lokale AI:** geaggregeerde begunstigdendata — ook geanonimiseerd — bevat gevoelige informatie over de populaties die de organisatie bedient. Die data intern verwerken en visualiseren is niet alleen juridisch correcter, het is ook organisatorisch zuiverder.

---

## Het concrete risico met cloud-AI

**Het CRM-fundraisingplatform-scenario:**

Een sociale welzijnsvzw kiest voor een US-gebaseerd cloud-CRM met ingebouwde AI voor donorbeheer en begunstigdenbeheer — een veelgebruikt platform in de filantropiesector.

1. Donorprofielen — inclusief IBAN, geefgeschiedenissen en persoonlijke communicaties — worden opgeslagen op servers in de Verenigde Staten.
2. Intakeformulieren voor begunstigden — inclusief sociale kwetsbaarheidsdata en gezondheidsinformatie (Art. 9 GDPR) — worden opgeslagen op hetzelfde platform, soms in hetzelfde systeem.
3. De ingebouwde AI van het platform gebruikt alle data om donorscoringsmodellen en engagementvoorspellingen te trainen — inclusief data over de kwetsbare begunstigden van de organisatie.
4. De gebruiksvoorwaarden van het platform staan de provider toe geaggregeerde data te gebruiken voor "productverbetering" — een clausule die breed geïnterpreteerd kan worden.
5. Een datalek of een eenzijdige wijziging van de gebruiksvoorwaarden legt tegelijk de financiële data van donoren en de zorgdata van begunstigden bloot.
6. De vzw is de verwerkingsverantwoordelijke — volledig aansprakelijk — en verliest in één klap het vertrouwen van zowel haar donoren als haar begunstigden. De reputatieschade overtreft de directe financiële kosten.

Donorbeheer, vrijwilligerscoördinatie en begunstigdenintake kunnen alle drie draaien op een lokale server. Volledige controle over Art. 9-data. Geen afhankelijkheid van platforms die commerciële belangen hebben bij het hergebruik van die data.

---

## De kernboodschap voor het eerste gesprek

Begin niet bij de GDPR. Begin bij vertrouwen.

> "Jullie werking is gebouwd op vertrouwen. Donoren vertrouwen jullie met hun geld en hun naam. Begunstigden vertrouwen jullie met hun meest kwetsbare momenten. Een cloud AI-platform dat die data gebruikt om modellen te trainen — en wiens gebruiksvoorwaarden ruimte laten voor 'productverbetering' — zet dat vertrouwen op het spel. Niet theoretisch. Concreet, contractueel, vandaag."

Vervolg:

> "Lokale AI beschermt dat vertrouwen. Donorcommunicatie, vrijwilligersplanning, subsidiedossiers, impactrapportage — dat kan allemaal op jullie eigen server. Dezelfde efficiëntie, zonder dat jullie data de organisatie verlaat. Dat is wat jullie aan donoren en begunstigden kunnen uitleggen — en dat is wat telt."

---

## Vragen die ze stellen en hoe je antwoordt

**"We gebruiken al [bekend fundraisingplatform] — moeten we dat nu vervangen?"**

Niet noodzakelijk. Je kunt lokale AI inzetten voor de taken waarbij persoonsdata de input is — donoranalyse, vrijwilligersplanning, begunstigdendossiers — en het bestaande platform laten doen wat het doet voor campagnebeheer of online betalingen. De sleutel is: wat verwerk je lokaal, wat geef je door aan externe systemen? Die keuze bewust maken is het begin.

**"We zijn een kleine vzw — niemand viseert ons."**

De GBA en de AP werken niet alleen op basis van doelgerichte onderzoeken. Klachten van individuele leden, donoren of begunstigden kunnen een procedure in gang zetten. En bij een datalek — ook bij een klein platform — ben je als verwerkingsverantwoordelijke verplicht te melden. De kosten van een datalek voor een kleine non-profit beginnen bij tienduizenden euro's, los van de reputatieschade bij de doelgroep die jullie werking financiert.

**"Onze vrijwilligers regelen alles manueel toch al."**

Dat is precies waarom AI zo waardevol is voor jullie: vrijwilligers zijn kostbaar, hun tijd is beperkt, en administratieve overlast is een van de hoofdredenen voor uitval. Een lokale AI die de planningslogistiek en de rapportageondersteuning overneemt, geeft vrijwilligers meer ruimte voor de eigenlijke missie. En omdat ze lokaal draait, hoeft er geen data gedeeld te worden met externe platforms.

**"Kan AI echt helpen bij subsidieaanvragen?"**

Ja. AI is bijzonder sterk in het structureren van complexe dossiers, het consistent formuleren van impactdata, en het bewaken van de rode draad door lange aanvraagdocumenten. Een subsidiebeheerder met toegang tot een goed geconfigureerde lokale AI-assistent werkt sneller, consistenter en met minder fouten. De menselijke expertise — de kennis van de organisatie, de relatie met de subsidiënt — blijft essentieel. AI neemt het schrijfwerk niet over, maar maakt het draaglijker.

**"Wat is het verschil tussen lokale AI en ChatGPT gebruiken voor onze communicatie?"**

ChatGPT en vergelijkbare tools zijn cloud-diensten: alles wat je invoert wordt verwerkt op externe servers en kan worden gebruikt voor modelverbetering. Als je er begunstigdeninfo, donornamen of interne organisatiedata in plakt — bewust of onbewust — verlaat die data je organisatie. Lokale AI draait op je eigen infrastructuur. De input gaat nergens naartoe. Dat is het verschil.

---

## Belgische en Nederlandse context

### België

**VZW-rechtsvorm onder de WVV.** Vzw's zijn de meest voorkomende rechtsvorm voor non-profits in België. De WVV [2] legt specifieke bestuurs- en rapportageverplichtingen op die digitale traceerbaarheid van beslissingen veronderstellen.

**Fiscale attesten voor giften via FOD Financiën.** Vzw's die fiscale attesten afleveren aan donoren voor giften van meer dan €40 zijn verplicht die te registreren en jaarlijks door te geven aan FOD Financiën [7]. Dit vereist een betrouwbaar en auditeerbaar donatiebeheersysteem. Donordata die hiervoor wordt bijgehouden heeft een wettelijke bewaartermijn van zeven jaar.

**Platform voor Vrijwilligerswerk.** Het Vlaams Platform voor Vrijwilligerswerk en equivalenten in de andere gewesten publiceren richtlijnen over vrijwilligersbeleid, ook inzake privacybescherming van vrijwilligers.

**GBA-aanbevelingen voor non-profits.** De Gegevensbeschermingsautoriteit heeft specifieke aanbevelingen gepubliceerd voor verenigingen en vzw's over de rechtmatige verwerking van ledenen donordata, toestemming versus gerechtvaardigd belang, en de bescherming van gevoelige data van begunstigden [5].

### Nederland

**Stichtingen en verenigingen onder het Burgerlijk Wetboek.** De juridische grondslagen voor non-profits in Nederland zijn het BW (Boek 2) en de WBTR [3], met nadruk op bestuurdersverantwoordelijkheid en transparantie.

**CBF — Centraal Bureau Fondsenwerving.** Het CBF-keurmerk [6] is de kwaliteitsstandaard voor fondsenwervende organisaties in Nederland. CBF-gecertificeerde organisaties moeten voldoen aan strenge eisen rond governance, transparantie en omgang met donordata. Een datalek of privacyschending kan leiden tot verlies van het keurmerk — met directe impact op het donatieinkomen.

**ANBI-status.** Organisaties met ANBI-status (Algemeen Nut Beogende Instelling) genieten fiscale voordelen voor zichzelf en hun donoren, maar zijn verplicht tot transparantie over bestuur, doelstellingen en financiën — ook via publicatie op de website. Dat veronderstelt een degelijk digitaal registratie- en rapportagesysteem.

**AP — Autoriteit Persoonsgegevens.** De AP heeft aanbevelingen gepubliceerd voor verenigingen over de verwerking van ledendata, met specifieke aandacht voor toestemmingsvereisten en bewaartermijnen [8].

---

## Sectorcijfers (referentie)

- Aantal actieve vzw's in België: ca. 80.000 (Statbel, 2024)
- Aantal stichtingen en verenigingen in Nederland: ca. 200.000+ (CBS, 2024)
- Vrijwilligers in België: ca. 1,1 miljoen actieve vrijwilligers in georganiseerd verband
- Vrijwilligers in Nederland: ca. 4,5 miljoen actieve vrijwilligers
- Gemiddeld aandeel donorfinanciering bij Belgische sociale vzw's: 15–30% van het totaalbudget
- Gemiddeld aandeel subsidies bij Nederlandse non-profits: 40–60% van het totaalbudget
- Gemiddelde kosten van een datalek voor een kmo of kleine non-profit: €15.000–50.000 (IBM Cost of Data Breach Report 2024, gecorrigeerd voor kmo-schaal) — met reputatieschade bij donateurs en begunstigden potentieel een veelvoud

---

## Bronnen

1. **GDPR — Verordening (EU) 2016/679 (incl. Art. 9 bijzondere categorieën persoonsgegevens)**
   EUR-Lex, volledig geconsolideerde tekst
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/nld>

2. **WVV — Wet van 23 maart 2019 betreffende het Wetboek van Vennootschappen en Verenigingen**
   Belgisch Staatsblad via e-Justice
   <https://www.ejustice.just.fgov.be>

3. **WBTR — Wet bestuur en toezicht rechtspersonen (2021)**
   Overheid.nl — Nationale wettenbank
   <https://wetten.overheid.nl/BWBR0044286/>

4. **AI Act — Verordening (EU) 2024/1689 — Risicoklassificatie en hoog-risico systemen**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

5. **GBA — Gegevensbeschermingsautoriteit — aanbevelingen voor non-profits en verenigingen**
   <https://www.gegevensbeschermingsautoriteit.be>

6. **CBF — Centraal Bureau Fondsenwerving — keurmerk en normen**
   <https://www.cbf.nl>

7. **FOD Financiën — Fiscale attesten voor giften aan vzw's**
   <https://financien.belgium.be>

8. **AP — Autoriteit Persoonsgegevens — aanbevelingen voor verenigingen**
   <https://www.autoriteitpersoonsgegevens.nl>

---

_Onderdeel van: LocAI Bibliotheek · Sectordossiers_
_Vorige: S08 — Vastgoedmakelaars_
_Volgende: S10 — Onderwijs & Scholen_
_Laatste update: 25 maart 2026_
