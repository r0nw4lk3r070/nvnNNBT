# 03 — DORA
### LocAI Bibliotheek · Diepgang
_Verordening (EU) 2022/2554 · Van kracht 17 januari 2025_
_Versie 0.1 · maart 2026_

---

## Wat dit document is

DORA staat voor Digital Operational Resilience Act. Het is een verordening — direct bindend in alle lidstaten, geen nationale implementatie nodig. Specifiek gericht op de financiële sector. Dit document volgt dezelfde structuur: letterlijke tekst, vertaling, implicatie voor lokale AI versus cloud AI.

---

## De kern in één zin

DORA verplicht financiële instellingen om hun digitale weerbaarheid serieus te nemen — inclusief de weerbaarheid van alle ICT-diensten die ze afnemen van derde partijen.

---

## Deel 1 — Waarom DORA bestaat

De financiële sector is volledig afhankelijk geworden van digitale systemen en externe ICT-leveranciers. Banken draaien op cloud-infrastructuur van Amazon, Microsoft en Google. Betalingssystemen zijn verweven met tientallen derde partijen. Een storing bij één grote leverancier kan het hele financiële systeem raken.

De Europese toezichthouders — ECB, EBA, ESMA, EIOPA — zagen dit risico groeien en concludeerden dat de bestaande regelgeving onvoldoende was. DORA is het antwoord.

Wat nieuw is ten opzichte van wat er al was: de focus op operationele veerkracht als geheel, inclusief de volledige keten van ICT-leveranciers. Niet alleen "is je eigen systeem veilig" maar "ben je bestand tegen uitval van de systemen waar je van afhankelijk bent."

---

## Deel 2 — Voor wie geldt DORA?

### De letterlijke tekst (Art. 2)

DORA geldt voor:

> "a) kredietinstellingen; b) betalingsinstellingen; c) instellingen voor elektronisch geld; d) beleggingsondernemingen; e) aanbieders van cryptoactivadiensten; f) centrale effectenbewaarinstellingen; g) centrale tegenpartijen; h) handelsplatformen; i) transactieregisters; j) beheerders van alternatieve beleggingsfondsen; k) beheermaatschappijen; l) aanbieders van datarapporteringsdiensten; m) verzekeringsondernemingen en herverzekeringsondernemingen; n) verzekeringstussenpersonen, herverzekeringstussenpersonen en nevenverzekeringstussenpersonen; o) instellingen voor bedrijfspensioenvoorziening; p) ratingbureaus; q) beheerders van kritieke benchmarks; r) crowdfundingdienstverleners; s) securitisatieregisters; t) ICT-derde-dienstverleners."

### De vertaling

In gewone taal: alles wat met financiële dienstverlening te maken heeft.

De meest relevante categorieën voor onze doelgroep:

**Kredietinstellingen:** banken, spaarbanken, kredietcoöperaties.

**Betalingsinstellingen:** bedrijven die betalingstransacties verwerken.

**Beleggingsondernemingen:** vermogensbeheerders, beursvennootschappen.

**Verzekeringsondernemingen:** alle vormen van verzekering.

**Verzekeringstussenpersonen:** makelaars, agenten — ook de kleine zelfstandige verzekeringsmakelaar.

**ICT-derde-dienstverleners:** dit is de categorie die alles verandert. Een cloudprovider die diensten levert aan een bank valt zelf ook onder DORA. Een software-as-a-service bedrijf dat HR-software levert aan een verzekeringsmaatschappij: ook onder DORA.

**De drempelwaarden:**
Voor kleine financiële instellingen gelden vereenvoudigde verplichtingen. Maar "vereenvoudigd" betekent niet "geen verplichtingen."

### Wat dit betekent voor onze doelgroep

Een accountantskantoor dat de boekhouding doet voor een verzekeringsmakelaar: de makelaar valt onder DORA. Die makelaar moet de ICT-leveranciers van zijn accountant beoordelen als die ICT-diensten leveren die de financiële dienstverlening raken.

Een softwarebedrijf dat facturatiesoftware levert aan een bank: direct onder DORA als ICT-derde-dienstverlener.

De grens is niet altijd scherp — maar de richting is duidelijk: DORA werkt door in de hele keten.

---

## Deel 3 — De vijf pijlers van DORA

DORA is opgebouwd rond vijf kerngebieden. Samen vormen ze een raamwerk voor digitale operationele weerbaarheid.

### Pijler 1 — ICT-risicobeheer (Art. 5-16)

### De letterlijke tekst (Art. 5 lid 1)

> "Financiële entiteiten beschikken over een solide, alomvattend en goed gedocumenteerd ICT-risicobeheerkader als onderdeel van hun algehele risicobeheersysteem, dat hen in staat stelt ICT-risico's snel, efficiënt en alomvattend aan te pakken en een hoog niveau van digitale operationele veerkracht te waarborgen."

### De vertaling

Je moet een raamwerk hebben voor het beheren van ICT-risico's. Niet een document dat in een la ligt — een werkend systeem dat je kunt aantonen aan een toezichthouder.

Wat dat raamwerk minimaal moet bevatten:
- Identificatie van alle ICT-activa (hardware, software, data, netwerken)
- Bescherming van die activa
- Detectie van anomalieën en incidenten
- Respons op incidenten
- Herstel na incidenten
- Leren van incidenten

### De implicatie voor lokale AI versus cloud AI

Een cloud AI-dienst is een ICT-actief. Het staat in je register. Je moet het risico ervan beoordelen. Je moet een exit-strategie hebben.

Bij lokale AI: de AI-component staat op je eigen hardware. Het is een intern ICT-actief dat je volledig beheert. Geen externe afhankelijkheid om te registreren en te bewaken.

---

### Pijler 2 — Beheer van ICT-gerelateerde incidenten (Art. 17-23)

### De letterlijke tekst (Art. 17 lid 1)

> "Financiële entiteiten stellen een beheersproces voor ICT-gerelateerde incidenten vast, documenteren en implementeren dit, teneinde ICT-gerelateerde incidenten op te sporen, te beheren en te melden."

Met meldingstermijnen (Art. 19):

> "Financiële entiteiten melden ernstige ICT-gerelateerde incidenten [...] aan de bevoegde autoriteit [...]:
> a) een eerste melding, zo spoedig mogelijk en uiterlijk vier uur na de classificatie van het incident als ernstig;
> b) een tussentijds verslag [...] uiterlijk 72 uur na de eerste melding;
> c) een eindverslag [...] uiterlijk één maand na de indiening van de tussentijdse melding."

### De vertaling

Als er een ernstig ICT-incident is, heb je:

- 4 uur voor een eerste melding aan de toezichthouder
- 72 uur voor een tussentijds rapport
- 1 maand voor een eindrapport

Dat is sneller dan NIS2 (24 uur eerste melding) en GDPR (72 uur). De financiële sector wordt harder aangepakt.

"Ernstig" incident betekent: significant aantal klanten getroffen, langdurige uitval, data-integriteit aangetast, reputatieschade, of financiële impact boven een bepaalde drempel.

### De implicatie voor lokale AI versus cloud AI

Als een cloud AI-dienst uitvalt of gehackt wordt en dat impact heeft op je financiële dienstverlening, begint de 4-uur klok te lopen op het moment dat jij het weet.

Maar als de cloud AI-provider pas na 6 uur communiceert over het incident, heb je al een probleem met je meldplicht.

Bij lokale AI: het incident is in je eigen omgeving. Je detecteert het zelf. Je bepaalt zelf de communicatiestrategie. Geen afhankelijkheid van de communicatiesnelheid van een externe provider.

---

### Pijler 3 — Testen van digitale operationele veerkracht (Art. 24-27)

### De letterlijke tekst (Art. 24 lid 1)

> "Financiële entiteiten stellen, onderhouden en herzien een degelijk en alomvattend programma voor het testen van digitale operationele veerkracht als integraal onderdeel van het in artikel 6 bedoelde ICT-risicobeheerkader."

### De vertaling

Je mag niet alleen zeggen dat je systemen veilig zijn — je moet het testen. En documenteren.

Basisniveau: jaarlijkse tests van alle ICT-systemen en -toepassingen.

Gevorderd niveau (verplicht voor grote financiële instellingen): Threat-Led Penetration Testing (TLPT) — gesimuleerde aanvallen op productiesystemen door gecertificeerde externe testers, minimaal elke drie jaar.

### De implicatie voor lokale AI versus cloud AI

Een cloud AI-dienst testen op veerkracht is complex: je hebt beperkte toegang tot de infrastructuur, en de provider bepaalt in grote mate wat je mag testen.

Lokale AI-systemen zijn volledig toegankelijk voor penetratietests. Je kunt de volledige stack testen — hardware, software, netwerk, toegangscontrole — zonder toestemming van een externe partij.

---

### Pijler 4 — Beheer van risico's van ICT-derde-dienstverleners (Art. 28-44)

Dit is de pijler die het meeste impact heeft op de dagelijkse praktijk.

### De letterlijke tekst (Art. 28 lid 1)

> "Financiële entiteiten beheren het risico van ICT-derde-dienstverleners als integraal onderdeel van ICT-risico's binnen hun ICT-risicobeheerkader en in overeenstemming met de volgende beginselen:
> a) financiële entiteiten die contractuele regelingen aangaan voor het gebruik van ICT-diensten dienen te handelen met de nodige zorgvuldigheid [...];
> b) financiële entiteiten gaan uitsluitend contractuele regelingen aan met ICT-derde-dienstverleners die passende normen voor informatiebeveiliging hanteren."

En (Art. 28 lid 2):

> "Financiële entiteiten houden een register bij van alle contractuele regelingen met betrekking tot het gebruik van door ICT-derde-dienstverleners verleende ICT-diensten."

### De letterlijke tekst (Art. 30 — verplichte contractinhoud)

Contracten met ICT-leveranciers moeten minimaal bevatten:

> "a) een duidelijke en volledige beschrijving van alle te verlenen functies en ICT-diensten;
> b) de locaties waar de contractuele functies en ICT-diensten worden verleend [...];
> c) bepalingen inzake de beschikbaarheid, authenticiteit, integriteit en vertrouwelijkheid [...];
> d) bepalingen inzake toegang tot, herstel en retournering van gegevens [...];
> e) volledige serviceniveaubeschrijvingen [...];
> f) de relevante bepalingen inzake exitstrategieën."

### De vertaling

Elke cloudprovider, elke SaaS-leverancier, elke externe ICT-dienst moet:

1. In een register staan
2. Een contract hebben dat aan DORA-eisen voldoet
3. Beoordeeld worden op hun cybersecuritypraktijken
4. Een exit-strategie hebben

**Het register:** je moet kunnen aantonen welke ICT-diensten je afneemt, van wie, voor welk doel, en hoe kritiek ze zijn voor je dienstverlening.

**De exit-strategie:** als een leverancier wegvalt, failliet gaat, of je contract opzegt — wat doe je dan? Je moet een plan hebben. En dat plan moet werken.

**De locatie:** je moet weten waar je data staat. "In de cloud" is geen antwoord. Welk datacenter, in welk land, onder welke jurisdictie?

### De implicatie voor lokale AI versus cloud AI

Dit is het artikel dat cloud AI duur maakt voor financiële instellingen — niet financieel, maar administratief.

Een cloud AI-dienst vereist:
- Een vermelding in het DORA-register
- Een contract dat voldoet aan Art. 30 (inclusief locatie van data, exit-strategie, SLA)
- Een beoordeling van de beveiligingspraktijken van de provider
- Periodieke herziening van die beoordeling
- Een gedocumenteerde exit-strategie

Bij lokale AI: geen externe ICT-derde-dienstverlener voor de AI-component. Geen registervermelding, geen DORA-conform contract, geen exit-strategie nodig. De AI-functionaliteit zit in de eigen infrastructuur.

De exit-strategie bij lokale AI is eenvoudig: de hardware staat bij jou. De modellen zijn open-source. Als de leverancier van het hardware-onderhoud wegvalt, koop je een nieuwe leverancier. Je data blijft bij jou.

---

### Pijler 5 — Informatiedeling (Art. 45)

### De letterlijke tekst

> "Financiële entiteiten kunnen onderling informatie en inlichtingen over cyberdreigingen uitwisselen, met inbegrip van indicatoren van compromittering, tactieken, technieken en procedures, cyberbeveiligingswaarschuwingen en configuratietools."

### De vertaling

DORA moedigt financiële instellingen aan om dreigingsinformatie te delen. Dit is optioneel, niet verplicht. Maar het creëert een ecosysteem van gedeelde intelligentie over cyberdreigingen.

---

## Deel 4 — DORA en cloud AI: de praktische consequentie

Laten we het concreet maken voor een typische klant.

**Scenario: een verzekeringsmakelaar met 12 medewerkers**

Hij valt onder DORA als verzekeringstussenpersoon (Art. 2n). Hij gebruikt ChatGPT Team voor het opstellen van polisadviezen en het samenvatten van verzekeringsvoorwaarden.

Wat hij nu moet doen onder DORA:

1. ChatGPT/OpenAI opnemen in zijn ICT-register als derde-dienstverlener
2. Zijn contract met OpenAI beoordelen op DORA-conformiteit (locatie data, exit-strategie, SLA — deze staan niet standaard in de ChatGPT Team voorwaarden)
3. Een beoordeling maken van OpenAI's cybersecuritypraktijken
4. Een exit-strategie documenteren: wat doet hij als OpenAI zijn dienst stopt, de prijs vertienvoudigt, of een datalek heeft?
5. Dit periodiek herzien

Dat is aanzienlijk werk voor een kantoor van 12 mensen.

**Met lokale AI:**

De AI draait op een mini-PC in het kantoor. OpenAI staat niet in het register. Er is geen DORA-conform contract nodig voor de AI-component. De exit-strategie is simpel: de hardware staat er, de modellen zijn open-source.

Compliance-last: significant lager.

---

## Deel 5 — DORA, NIS2 en GDPR samen

De drie wetten overlappen voor financiële instellingen.

| | GDPR | NIS2 | DORA |
|---|---|---|---|
| **Primaire focus** | Persoonsgegevens | Cybersecurity systemen | Operationele weerbaarheid finance |
| **Meldplicht** | 72u bij datalek | 24u waarschuwing, 72u melding | 4u eerste melding, 72u tussentijds |
| **Supply chain** | Via verwerkersovereenkomst | Art. 21d | Art. 28-44 (uitgebreid) |
| **Bestuurlijke aansprakelijkheid** | Impliciet | Expliciet Art. 20 | Impliciet via verantwoordingsplicht |
| **Testen verplicht** | Nee | Impliciet | Expliciet Art. 24-27 |
| **Register verplicht** | Verwerkingsregister | Niet specifiek | ICT-derde-dienstverleners register |

Voor een bank of verzekeraar gelden alle drie tegelijk. Dat is een complexe compliance-omgeving waarbij elke externe ICT-dienst — inclusief cloud AI — meervoudige juridische verplichtingen triggert.

---

## Deel 6 — DORA en de kleine financiële instelling

DORA erkent dat niet alle financiële instellingen even groot zijn. Art. 16 voorziet in "vereenvoudigde ICT-risicobeheerregelingen" voor kleine en niet-verweven instellingen.

Maar "vereenvoudigd" betekent niet "vrijgesteld." De basisverplichtingen blijven:
- ICT-risicobeheer documenteren
- Incidenten registreren en melden
- Contracten met ICT-leveranciers beoordelen
- Exit-strategie voor kritieke diensten

Voor een kleine verzekeringsmakelaar of een kleine beleggingsadviseur: de vereenvoudigde regels zijn van toepassing, maar de kernlogica van DORA — weet van wie je afhankelijk bent en zorg dat je kunt overleven als die afhankelijkheid wegvalt — blijft onverminderd gelden.

---

## Begrippenlijst

**Financiële entiteit** — elk bedrijf dat financiële diensten verleent en onder de scope van DORA valt (banken, verzekeraars, beleggingsondernemingen, betalingsinstellingen, etc.).

**ICT-derde-dienstverlener** — een externe partij die ICT-diensten levert aan een financiële entiteit. Cloudproviders, softwareleveranciers, datacenters, maar ook AI-diensten.

**Kritieke ICT-derde-dienstverlener** — een ICT-leverancier die zo belangrijk is voor de financiële sector dat hij rechtstreeks onder toezicht van Europese toezichthouders (ESAs) valt. Amazon AWS, Microsoft Azure en Google Cloud zijn aangewezen als kritieke leveranciers.

**Digitale operationele veerkracht** — het vermogen van een financiële entiteit om haar ICT-gerelateerde capaciteiten op te bouwen, te waarborgen en te herzien om de integriteit en betrouwbaarheid van haar dienstverlening te garanderen, ook bij ICT-gerelateerde storingen of incidenten.

**ICT-risico** — elk redelijkerwijs identificeerbaar risico met betrekking tot het gebruik van netwerk- en informatiesystemen, inclusief storingen, uitval, cyberaanvallen en dataverlies.

**TLPT (Threat-Led Penetration Testing)** — een geavanceerde vorm van penetratietest waarbij echte aanvalstactieken gesimuleerd worden op productiesystemen. Verplicht voor grote financiële instellingen minimaal elke drie jaar.

**ESAs (European Supervisory Authorities)** — de drie Europese financiële toezichthouders: EBA (banken), ESMA (effectenmarkten), EIOPA (verzekeringen en pensioenen). Zij houden toezicht op de kritieke ICT-derde-dienstverleners.

**EBA** — European Banking Authority. Toezicht op banken en betalingsinstellingen.

**ESMA** — European Securities and Markets Authority. Toezicht op beleggingsondernemingen en effectenmarkten.

**EIOPA** — European Insurance and Occupational Pensions Authority. Toezicht op verzekeraars en pensioenfondsen.

**Exit-strategie** — een gedocumenteerd plan voor het beëindigen van de afhankelijkheid van een ICT-leverancier, zonder significante verstoring van de dienstverlening.

**Operationele continuïteit** — het vermogen om kritieke bedrijfsfuncties voort te zetten tijdens en na een verstoring.

---

## Checklist voor een klantgesprek (financiële sector)

- [ ] Valt uw organisatie onder DORA? (type financiële instelling)
- [ ] Heeft u een register van alle ICT-derde-dienstverleners?
- [ ] Staan uw cloudleveranciers — inclusief AI-diensten — in dat register?
- [ ] Voldoen uw contracten met ICT-leveranciers aan de DORA-eisen? (locatie data, SLA, exit-strategie)
- [ ] Heeft u een gedocumenteerde exit-strategie voor kritieke ICT-diensten?
- [ ] Heeft u een ICT-risicobeheerkader gedocumenteerd?
- [ ] Heeft u een incidentresponsplan met de juiste meldingstermijnen? (4u, 72u, 1 maand)
- [ ] Test u uw digitale weerbaarheid regelmatig?
- [ ] Weet u waar uw data staat — in welk datacenter, in welk land?
- [ ] Heeft u als bestuurder de ICT-risicomaatregelen formeel goedgekeurd?

---

_Vorige document: 02-nis2.md_
_Volgende document: 04-data-act.md_
_Laatste update: maart 2026_
