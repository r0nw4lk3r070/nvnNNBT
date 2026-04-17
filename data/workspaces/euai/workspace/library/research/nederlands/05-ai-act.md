# 05 — EU AI Act
### LocAI Bibliotheek · Diepgang
_Verordening (EU) 2024/1689 · Verwachte deadline hoog-risico systemen: 2 december 2027_
_Versie 0.2 · maart 2026 — bijgewerkt na EP-commissiestemming 18 maart 2026_

---

## Wat dit document is

De AI Act is de eerste bindende AI-wet ter wereld. Ze is complex, uitgebreid, en direct relevant voor elke organisatie die AI inzet. Dit document volgt dezelfde structuur als de vorige documenten: letterlijke tekst, vertaling, implicatie voor lokale AI versus cloud AI.

Maar de AI Act verdient ook extra aandacht voor de begrippen — want de wet introduceert een volledig nieuw vocabulaire dat je moet kennen om zinvol over de wet te kunnen praten.

---

## De kern in één zin

De AI Act classificeert AI-systemen op risiconiveau, legt zware verplichtingen op aan organisaties die hoog-risico AI ontwikkelen of inzetten, en maakt lokale deployment de architectureel eenvoudigste weg naar compliance.

---

## Deel 1 — Waarom de AI Act bestaat

### De letterlijke tekst (Overweging 1)

> "Artificiële intelligentie is een snel evoluerende familie van technologieën die kan bijdragen aan een breed scala aan economische en maatschappelijke voordelen in de gehele economie en samenleving. [...] Tegelijkertijd kan AI, afhankelijk van de context van de toepassing en het gebruik, risico's met zich meebrengen en schade veroorzaken aan openbare belangen en grondrechten die worden beschermd door het Unierecht."

### De vertaling

AI is krachtig en nuttig. Maar het kan ook schade aanrichten — aan mensen, aan democratische processen, aan grondrechten. Europa kiest ervoor die risico's te reguleren voordat ze realiteit worden, in plaats van achteraf te reageren.

Dit is het Europese model: proactieve regulering op basis van risico's. Hetzelfde principe zit in GDPR, NIS2 en DORA — maar nu toegepast op intelligente systemen zelf.

### De historische context

De AI Act bouwt direct voort op alles wat eraan voorafging:
- GDPR regelt de data waarop AI traint en werkt
- NIS2 regelt de beveiliging van de systemen waarop AI draait
- DORA regelt de weerbaarheid van financiële AI-systemen
- De Data Act regelt de data die AI-systemen genereren

De AI Act sluit de cirkel: het reguleert de intelligentie zelf.

---

## Deel 2 — Het vocabulaire van de AI Act

Voordat we de artikelen ingaan, moeten de sleutelbegrippen helder zijn. De AI Act heeft een eigen taal die je moet kennen.

### AI-systeem

### De letterlijke tekst (Art. 3 lid 1)

> "'AI-systeem': een op een machine gebaseerd systeem dat is ontworpen om met verschillende niveaus van autonomie te werken en dat na ingebruikstelling aanpassingsvermogen kan vertonen, en dat voor expliciete of impliciete doelstellingen, uit de ontvangen invoer afleidt hoe uitvoer te genereren zoals voorspellingen, inhoud, aanbevelingen of besluiten die van invloed kunnen zijn op fysieke of virtuele omgevingen."

### De vertaling

Een AI-systeem is elk systeem dat:
- Op een machine draait
- Met een zekere mate van autonomie werkt
- Input verwerkt om output te genereren (voorspellingen, content, aanbevelingen, beslissingen)

ChatGPT is een AI-systeem. Een spamfilter is een AI-systeem. Een creditscoringsalgoritme is een AI-systeem. Een routeplanner die AI gebruikt is een AI-systeem.

Wat géén AI-systeem is: gewone software die puur op regels werkt zonder leren of inferentie. Een rekenmachine is geen AI-systeem. Een Excel-formule is geen AI-systeem.

---

### Aanbieder (Provider)

### De letterlijke tekst (Art. 3 lid 3)

> "'aanbieder': een natuurlijke of rechtspersoon, autoriteit, agentschap of andere instantie die een AI-systeem of een AI-model voor algemene doeleinden ontwikkelt of laat ontwikkelen en dit op de markt brengt of het AI-systeem in gebruik stelt onder zijn eigen naam of handelsmerk, al dan niet tegen betaling."

### De vertaling

De aanbieder is degene die het AI-systeem maakt en op de markt brengt. OpenAI is de aanbieder van ChatGPT. Google is de aanbieder van Gemini. Meta is de aanbieder van Llama.

Als jij een AI-systeem bouwt voor intern gebruik en het niet op de markt brengt, ben je ook aanbieder — maar dan van een intern systeem, met bijbehorende verplichtingen.

---

### Deployer (Gebruiker)

### De letterlijke tekst (Art. 3 lid 4)

> "'gebruiker': een natuurlijke of rechtspersoon, autoriteit, agentschap of andere instantie die een AI-systeem gebruikt onder zijn eigen verantwoordelijkheid, tenzij het AI-systeem wordt gebruikt in het kader van een persoonlijke niet-beroepsmatige activiteit."

### De vertaling

De deployer is degene die het AI-systeem inzet voor beroepsmatige doeleinden. Een accountant die ChatGPT gebruikt voor zijn werk is een deployer. Een ziekenhuis dat een AI-diagnostiek systeem inzet is een deployer.

Belangrijk: de deployer heeft ook verplichtingen onder de AI Act — niet alleen de aanbieder. Als je een hoog-risico AI-systeem inzet, ben jij verantwoordelijk voor correct gebruik, menselijk toezicht, en transparantie naar betrokkenen.

---

### GPAI-model (General Purpose AI Model)

### De letterlijke tekst (Art. 3 lid 63)

> "'AI-model voor algemene doeleinden': een AI-model, met inbegrip van een AI-model dat is getraind met grote hoeveelheden gegevens met behulp van zelfsupervisie op grote schaal, dat een aanzienlijke algemene bruikbaarheid vertoont en in staat is een breed scala aan afzonderlijke taken competent uit te voeren."

### De vertaling

Een GPAI-model is een groot taalmodel dat voor van alles ingezet kan worden. GPT-4, Gemini, Llama, Claude, Mistral — allemaal GPAI-modellen.

GPAI-modellen hebben hun eigen verplichtingen in de AI Act, los van de risicoclassificatie van het systeem waarin ze gebruikt worden.

---

### Systeem met hoog risico

De kern van de AI Act. We behandelen dit uitgebreid in Deel 4.

---

### Conformiteitsbeoordeling

### De letterlijke tekst (Art. 3 lid 20)

> "'conformiteitsbeoordeling': het proces van verificatie of aan de vereisten van hoofdstuk III, afdeling 2 van deze verordening voor een AI-systeem met een hoog risico is voldaan."

### De vertaling

Voordat een hoog-risico AI-systeem in gebruik genomen wordt, moet aangetoond worden dat het voldoet aan alle vereisten van de AI Act. Dit is de conformiteitsbeoordeling. Denk aan het CE-keurmerk voor producten, maar dan voor AI.

---

## Deel 3 — De tijdlijn

### De letterlijke tekst (Art. 113)

| Datum | Wat |
|---|---|
| 1 augustus 2024 | AI Act in werking getreden |
| 2 februari 2025 | Verboden praktijken (Art. 5) + AI-geletterdheid (Art. 4) van kracht |
| 2 augustus 2025 | GPAI-modelverplichtingen + boetekader actief |
| ~~2 augustus 2026~~ | ~~Alle verplichtingen voor hoog-risico AI-systemen~~ _(originele deadline — zie update)_ |
| **2 december 2027** | **Verwachte nieuwe deadline hoog-risico systemen (Annex III/Bijlage III)** |
| **2 augustus 2028** | **Hoog-risico AI als veiligheidscomponent in producten onder sectorale wetgeving** |

> **Update maart 2026:** Het Europees Parlement (IMCO + LIBE commissies) stemde op 18 maart 2026 met 101 stemmen voor en 9 tegen voor uitstel van de hoog-risico deadline. De plenaire stemming is gepland op 26 maart, waarna triloogonderhandeling met de Raad volgt. Tot de wet officieel gewijzigd is geldt augustus 2026 juridisch nog als operationele deadline — maar de richting is duidelijk.

### De vertaling

We zitten nu in maart 2026. Dat betekent:

- De verboden praktijken gelden al — depuis februari 2025
- GPAI-verplichtingen gelden al — desde augustus 2025
- De hoog-risico deadline schuift naar verwachting op naar 2 december 2027

Het uitstel haalt de directe tijdsdruk weg — maar niet de verplichting. Organisaties die wachten tot 2027 verliezen anderhalf jaar voorbereiding.

---

## Deel 4 — De risicoclassificatie

Dit is de architectuur van de hele wet. Alles hangt af van in welke risicocategorie een AI-systeem valt.

### Niveau 1 — Onaanvaardbaar risico (Art. 5) — VERBODEN

### De letterlijke tekst (Art. 5 lid 1, selectie)

> "De volgende AI-praktijken zijn verboden:
> a) het in de handel brengen, in gebruik stellen of gebruiken van een AI-systeem dat subliminale technieken gebruikt die buiten het bewustzijn van een persoon vallen [...] met als doel het gedrag van een persoon wezenlijk te verstoren;
> b) het in de handel brengen, in gebruik stellen of gebruiken van een AI-systeem dat gebruikmaakt van kwetsbaarheden van een specifieke groep personen [...];
> c) het in de handel brengen, in gebruik stellen of gebruiken van AI-systemen voor de evaluatie of classificatie van natuurlijke personen [...] op basis van hun sociale gedrag of bekende of voorspelde persoonlijke of persoonlijkheidskenmerken (sociale scores);
> d) het in de handel brengen, in gebruik stellen of gebruiken van AI-systemen voor risicobeoordeling van natuurlijke personen teneinde de kans te beoordelen dat een natuurlijke persoon een strafbaar feit pleegt;
> e) het [...] aanleggen van databanken voor gezichtsherkenning door het [...] scrapen van gezichtsafbeeldingen van internet of van beeldmateriaal van bewakingscamera's;
> f) het [...] afleiden van emoties van een natuurlijke persoon op de werkplek en in het onderwijs [...];
> g) biometrische categorisering van natuurlijke personen [...] om gevoelige of beschermde kenmerken [...] af te leiden;
> h) het gebruik van 'real-time' biometrische identificatiesystemen op afstand in openbare ruimten voor rechtshandhavingsdoeleinden."

### De vertaling

Acht categorieën die simpelweg verboden zijn. Geen uitzonderingen voor goede bedoelingen, geen overgangsperiode.

In gewone taal:
- **Geen social scoring:** je mag mensen niet rangschikken op basis van hun gedrag of persoonlijkheid
- **Geen manipulatie:** je mag AI niet gebruiken om mensen onbewust te beïnvloeden
- **Geen emotieherkenning op het werk of in de klas:** je mag niet meten hoe medewerkers of studenten zich voelen
- **Geen biometrische massa-identificatie in openbare ruimten:** gezichtsherkenning voor surveillance is verboden (met zeer beperkte uitzonderingen voor rechtshandhaving)
- **Geen predictive policing:** AI mag niet voorspellen of iemand een misdaad gaat begaan

---

### Niveau 2 — Hoog risico (Art. 6 + Bijlage III) — ZWARE VERPLICHTINGEN

Dit is de kern van de wet. Hoog-risico AI-systemen zijn toegestaan, maar alleen als je aan alle vereisten voldoet.

### De letterlijke tekst (Bijlage III — selectie)

> "Hoog-risico AI-systemen als bedoeld in artikel 6, lid 2:
> 1. Biometrie [...]
> 2. Kritieke infrastructuur [...]
> 3. Onderwijs en beroepsopleiding:
>    a) AI-systemen die worden gebruikt om toegang tot of toelating van of de toewijzing van natuurlijke personen aan onderwijs- en beroepsopleidingsinstellingen te bepalen of de toelatingsprocedures voor die instellingen te beïnvloeden;
>    b) AI-systemen die worden gebruikt om leerresultaten of de leerresultaten van studenten te evalueren [...];
> 4. Werkgelegenheid, beheer van werknemers en toegang tot zelfstandige arbeid:
>    a) AI-systemen die worden gebruikt voor het werven of selecteren van natuurlijke personen, met name voor het bekendmaken van vacatures [...], voor het screenen of filteren van sollicitaties, voor het beoordelen van kandidaten;
>    b) AI-systemen die worden gebruikt voor het nemen van besluiten die van invloed zijn op de arbeidsomstandigheden, [...] inclusief de taakverdeling [...];
> 5. Toegang tot en genot van essentiële particuliere diensten en essentiële overheidsdiensten en -uitkeringen:
>    a) AI-systemen die worden gebruikt door of namens overheidsinstanties [...] voor het beoordelen van de geschiktheid van natuurlijke personen voor essentiële uitkeringen [...];
>    b) AI-systemen die worden gebruikt om de kredietwaardigheid van natuurlijke personen te beoordelen [...];
>    c) AI-systemen die worden gebruikt voor risicobeoordeling en -tariefstelling ten behoeve van levensverzekering en ziektekostenverzekering;
> 6. Rechtshandhaving [...]
> 7. Migratie, asiel en grenstoezicht [...]
> 8. Rechtsbedeling en democratische processen [...]"

### De vertaling

Hoog-risico AI-systemen zijn systemen die gebruikt worden in contexten waar fouten ernstige gevolgen hebben voor mensen.

De sectoren die voor onze doelgroep het meest relevant zijn:

**Onderwijs:** een AI die bepaalt of een student wordt toegelaten, of die leerresultaten beoordeelt. Een school die AI gebruikt voor leerlingbegeleiding moet dit als hoog-risico behandelen.

**HR en werving:** een AI die cv's screent, kandidaten rankt, of arbeidsomstandigheden bepaalt. Een bedrijf dat AI gebruikt in zijn recruitmentproces heeft een hoog-risico systeem.

**Krediet en verzekering:** een AI die kredietwaardigheid beoordeelt of verzekeringstarieven bepaalt. Banken en verzekeraars die AI gebruiken voor deze beslissingen zitten zwaar in de hoog-risico categorie.

**Essentiële overheidsdiensten:** een AI die bepaalt of iemand recht heeft op een uitkering of een dienst.

---

### Niveau 3 — Beperkt risico — TRANSPARANTIEPLICHT

Chatbots en systemen die tekst genereren die mensen kunnen lezen, moeten duidelijk maken dat het AI is. Deepfakes moeten gelabeld worden.

Een klantenservicebot die zichzelf niet identificeert als AI — dat is een overtreding.

---

### Niveau 4 — Minimaal risico — GEEN VERPLICHTINGEN

Spamfilters, aanbevelingssystemen voor streaming, AI in videogames. De overgrote meerderheid van AI-toepassingen valt hier.

---

## Deel 5 — Verplichtingen voor hoog-risico AI (Art. 8-15)

Dit zijn de artikelen die het meest direct relevant zijn voor organisaties die hoog-risico AI inzetten.

### Art. 9 — Risicobeheersysteem

### De letterlijke tekst

> "Voor AI-systemen met een hoog risico wordt een risicobeheersysteem opgezet, uitgevoerd, gedocumenteerd en onderhouden."

> "Het risicobeheersysteem wordt beschouwd als een continu iteratief proces dat gedurende de gehele levenscyclus van een AI-systeem met een hoog risico wordt gepland en uitgevoerd."

### De vertaling

Je moet weten welke risico's je AI-systeem met zich meebrengt. En je moet dat documenteren. En bijhouden. Niet eenmalig — continu, gedurende de hele levensduur van het systeem.

### De implicatie voor lokale AI versus cloud AI

Bij een cloud AI-systeem zijn de risico's deels afhankelijk van hoe de provider het systeem beheert. Je hebt beperkt zicht op modelupdates, trainingsdata-wijzigingen, of wijzigingen in de inferentie-infrastructuur.

Bij lokale AI: je beheert het systeem volledig. Je weet welke modelversie draait, wanneer het geüpdatet is, en wat er veranderd is. Het risicobeheersysteem is volledig in eigen handen.

---

### Art. 10 — Data en databeheer

### De letterlijke tekst

> "AI-systemen met een hoog risico die technieken gebruiken waarbij modellen worden getraind met gegevens, worden ontwikkeld op basis van trainingsgegevens, validatiegegevens en testgegevens die voldoen aan de kwaliteitscriteria als bedoeld in de leden 2 tot en met 5."

> "Trainingsgegevens, validatiegegevens en testgegevens zijn relevant, voldoende representatief en zoveel mogelijk vrij van fouten en volledig met betrekking tot het beoogde doel."

En cruciaal:

> "De gegevensreeksen worden onderworpen aan passende gegevensbeheersingspraktijken en -procedures, met name wat betreft de keuze van de relevante trainingsgegevens [...], de mogelijke vertekeningen [...], en de vaststelling van eventuele lacunes of tekortkomingen in de gegevens."

### De vertaling

Als je een hoog-risico AI-systeem gebruikt, moet je kunnen aantonen dat de data waarop het getraind is van goede kwaliteit is, representatief, en zo vrij mogelijk van bias.

### De implicatie voor lokale AI versus cloud AI

Dit is het artikel dat cloud AI fundamenteel problematisch maakt voor hoog-risico toepassingen.

Als je ChatGPT gebruikt voor een hoog-risico toepassing — zeg, het screenen van sollicitaties — moet je kunnen aantonen dat de trainingsdata van GPT-4 representatief en vrij van bias is. Dat kun je niet. OpenAI publiceert die informatie niet in de mate die Art. 10 vereist.

Bij een lokaal open-weight model dat je zelf fine-tunet op jouw eigen data: je kent de trainingsdata. Je kunt de bias-analyse uitvoeren. Je kunt Art. 10 invullen.

---

### Art. 11 — Technische documentatie

### De letterlijke tekst

> "Alvorens een AI-systeem met een hoog risico in de handel te brengen of in gebruik te stellen, stelt de aanbieder de technische documentatie op overeenkomstig artikel 11 en Bijlage IV."

Bijlage IV specificeert onder meer:
- Algemene beschrijving van het systeem
- Beschrijving van de componenten en het ontwikkelproces
- Gedetailleerde informatie over de trainingsgegevens
- Beschrijving van de monitoringprocedures
- Beschrijving van de validatie- en testprocedures

### De vertaling

Er moet een uitgebreid technisch dossier zijn dat het AI-systeem volledig documenteert. Dit dossier moet beschikbaar zijn voor toezichthouders.

### De implicatie voor lokale AI versus cloud AI

Bij cloud AI: je bent afhankelijk van de documentatie die de aanbieder verstrekt. Als die onvolledig is of niet voldoet aan Bijlage IV, heb je een compliance-probleem — terwijl het niet jouw fout is.

Bij lokale AI: jij maakt de documentatie. Je hebt volledige toegang tot alle componenten. Je kunt Bijlage IV invullen op basis van jouw eigen kennis van het systeem.

---

### Art. 12 — Logging en traceerbaarheid

### De letterlijke tekst

> "AI-systemen met een hoog risico zijn technisch in staat om automatisch gebeurtenissen ('logs') te registreren gedurende de werking van het AI-systeem."

> "De logboekmogelijkheden zorgen voor een traceerbaar niveau dat aansluit bij het beoogde doel van het AI-systeem."

### De vertaling

Een hoog-risico AI-systeem moet bijhouden wat het doet. Elke beslissing, elke output, elke interactie — gelogd, met tijdstempel, traceerbaar.

Als er later een vraag is over waarom het systeem een bepaalde beslissing nam, moet je dat kunnen reconstrueren.

### De implicatie voor lokale AI versus cloud AI

Bij cloud AI: de logs zijn bij de provider. Je kunt ze opvragen, maar de provider bepaalt wat er gelogd wordt, hoe lang het bewaard wordt, en in welk formaat je het krijgt.

Bij lokale AI: de logs staan bij jou. Je beheert het logformat, de bewaartermijn, en de toegang. Je kunt elke output traceren naar de exacte modelversie, de exacte input, en het exacte tijdstip.

---

### Art. 13 — Transparantie en informatieverstrekking

### De letterlijke tekst

> "AI-systemen met een hoog risico worden zodanig ontworpen en ontwikkeld dat de werking ervan voldoende transparant is om de gebruikers in staat te stellen de output van het systeem te interpreteren en op de juiste wijze te gebruiken."

### De vertaling

De deployer moet de output van het AI-systeem kunnen begrijpen en uitleggen. Een zwarte doos die beslissingen neemt die niemand kan verklaren — dat voldoet niet.

### De implicatie voor lokale AI versus cloud AI

Open-weight modellen zijn inspecteerbaar. Je kunt de architectuur bestuderen, de aandachtspatronen analyseren, en verklaren waarom een model tot een bepaalde output is gekomen.

Closed-source cloud AI-modellen zijn per definitie minder transparant — de provider deelt de interne werking niet.

---

### Art. 14 — Menselijk toezicht

### De letterlijke tekst

> "AI-systemen met een hoog risico worden zodanig ontworpen en ontwikkeld, met inbegrip van met passende menselijk-machine-interface-hulpmiddelen, dat deze effectief kunnen worden gecontroleerd door de natuurlijke personen aan wie het systeem is toegewezen tijdens de periode dat het AI-systeem in gebruik is."

En:

> "De aan het toezicht toegewezen natuurlijke personen zijn in staat:
> a) de mogelijkheden en beperkingen van het AI-systeem met een hoog risico volledig te begrijpen [...];
> b) de werking van het AI-systeem met een hoog risico te bewaken, met name met het oog op tekenen van anomalieën, storingen en onverwachte prestaties;
> c) wanneer van toepassing, tussenbeide te komen in de werking van het AI-systeem met een hoog risico of het systeem te onderbreken via een stop-knop of gelijkaardige procedure."

### De vertaling

Een mens moet altijd in staat zijn het AI-systeem te begrijpen, te monitoren, en te stoppen.

"Stop-knop" is letterlijk een vereiste. Niet metaforisch — er moet een mechanisme zijn om het systeem onmiddellijk te stoppen.

De menselijke toezichthouder moet ook daadwerkelijk in staat zijn het systeem te begrijpen. Niet alleen theoretisch — in de praktijk.

### De implicatie voor lokale AI versus cloud AI

Bij cloud AI is de "stop-knop" een API-annulering naar een externe server. In de praktijk betekent dit dat je het systeem kunt stoppen voor nieuwe inputs — maar lopende processen op de server van de provider niet.

Bij lokale AI: je kunt het systeem letterlijk uitzetten. De stop-knop is fysiek aanwezig. Menselijk toezicht is volledig in eigen handen.

---

### Art. 15 — Accuraatheid, robuustheid en cybersecurity

### De letterlijke tekst

> "AI-systemen met een hoog risico worden zodanig ontworpen en ontwikkeld dat zij gedurende hun levenscyclus een passend niveau van accuraatheid, robuustheid en cybersecurity bereiken, en consistent presteren met betrekking tot die aspecten."

### De vertaling

Het systeem moet goed werken, bestand zijn tegen fouten en aanvallen, en veilig zijn. En dat moet gedurende de hele levensduur, niet alleen bij lancering.

---

## Deel 6 — AI-geletterdheid (Art. 4)

Dit artikel is al van kracht sinds 2 februari 2025.

### De letterlijke tekst

> "Aanbieders en gebruikers van AI-systemen nemen maatregelen om, naar beste vermogen, te zorgen voor een voldoende niveau van AI-geletterdheid bij hun personeel en andere personen die namens hen AI-systemen bedienen en gebruiken, rekening houdend met hun technische kennis, ervaring, opleiding en onderwijs, en de context waarin de AI-systemen zullen worden gebruikt."

### De vertaling

Iedereen in je organisatie die AI gebruikt — of er toezicht op houdt — moet voldoende begrijpen wat AI is, hoe het werkt, en wat de beperkingen zijn.

"Voldoende niveau" is niet gedefinieerd — het hangt af van de context en het risiconiveau.

Voor een medewerker die ChatGPT gebruikt voor e-mails: basiskennis van wat AI kan en niet kan, en bewustzijn van wat je wel en niet door AI mag laten verwerken.

Voor een manager die verantwoordelijk is voor een hoog-risico AI-systeem: diepere kennis van de risico's, de verplichtingen, en de menselijke toezichtsvereisten.

### De implicatie voor consultancy

Dit artikel is de directe ingang voor AI-geletterdheidsworkshops en consultancy. De wet verplicht je het — maar geeft je de vrijheid te bepalen hoe.

---

## Deel 7 — GPAI-modellen (Art. 51-56)

### De letterlijke tekst (Art. 51)

> "Een aanbieder van een AI-model voor algemene doeleinden [...] zorgt voor de uitvoering van de in artikel 53 bedoelde verplichtingen."

De verplichtingen voor GPAI-modellen omvatten:
- Technische documentatie opstellen en bijhouden
- Informatie en documentatie verstrekken aan downstream-aanbieders
- Beleid voor naleving van het auteursrecht opstellen
- Samenvatting van trainingsdata publiceren

### De open-source vrijstelling (Art. 53 lid 2)

> "De verplichtingen [...] zijn niet van toepassing op aanbieders van AI-modellen voor algemene doeleinden die onder een vrije en open-source licentie worden vrijgegeven."

Uitzonderingen op de vrijstelling: systemic risk modellen (meer dan 10^25 FLOP trainingscompute) en modellen die als hoog-risico ingezet worden.

### De vertaling

Open-source GPAI-modellen — Llama, Mistral, Gemma, Qwen — zijn grotendeels vrijgesteld van de GPAI-verplichtingen.

Dit is de juridische opening die lokale AI mogelijk maakt. Je kunt een open-source model downloaden, lokaal draaien, en hoeft niet aan de GPAI-verplichtingen te voldoen die gelden voor closed-source modellen zoals GPT-4.

**Maar:** als je dat open-source model inzet in een hoog-risico toepassing, gelden de hoog-risico verplichtingen van Art. 8-15 wél. De vrijstelling geldt voor het model, niet voor de toepassing.

---

## Deel 8 — Rechten van betrokkenen (Art. 86)

### De letterlijke tekst

> "Elke betrokkene die onderworpen is aan een beslissing die door de gebruiker wordt genomen op basis van de output van de in bijlage III genoemde AI-systemen met een hoog risico [...] heeft het recht van de desbetreffende gebruiker duidelijke en betekenisvolle uitleg te verkrijgen over de rol van het AI-systeem in de besluitvormingsprocedure en over de voornaamste elementen van het genomen besluit."

### De vertaling

Als een AI-systeem bijdraagt aan een beslissing die jou raakt — je sollicitatie wordt afgewezen, je kredietaanvraag wordt geweigerd, je uitkeringsaanvraag wordt afgehandeld — dan heb je het recht te weten hoe dat systeem die beslissing heeft beïnvloed.

De organisatie moet dat kunnen uitleggen. In heldere taal. Niet "het algoritme heeft beslist" — maar wat de voornaamste factoren waren.

### De implicatie voor lokale AI versus cloud AI

Open-weight modellen zijn interpreteerbaar. Je kunt aandachtspatronen analyseren, je kunt de redenering reconstrueren, je kunt een eerlijke uitleg geven.

Closed-source cloud modellen zijn zwarte dozen. Je kunt de output uitleggen, maar de interne redenering van het model is onzichtbaar — ook voor de aanbieder zelf.

---

## Deel 9 — Boetes (Art. 99)

### De letterlijke tekst

Art. 99 lid 3:
> "Inbreuken op de verboden praktijken van artikel 5 [...] worden bestraft met administratieve geldboeten van maximaal 35 000 000 EUR of, indien de overtreder een onderneming is, van maximaal 7 % van de totale wereldwijde jaarlijkse omzet."

Art. 99 lid 4:
> "Niet-naleving van andere verplichtingen [...] wordt bestraft met administratieve geldboeten van maximaal 15 000 000 EUR of, indien de overtreder een onderneming is, van maximaal 3 % van de totale wereldwijde jaarlijkse omzet."

Art. 99 lid 5:
> "Het verstrekken van onjuiste, onvolledige of misleidende informatie aan aangemelde instanties en nationale bevoegde autoriteiten [...] wordt bestraft met administratieve geldboeten van maximaal 7 500 000 EUR of, indien de overtreder een onderneming is, van maximaal 1 % van de totale wereldwijde jaarlijkse omzet."

### De vertaling

Drie boetecategorieën:

- Verboden praktijken overtreden: tot €35 miljoen of 7% omzet
- Andere verplichtingen niet naleven: tot €15 miljoen of 3% omzet
- Onjuiste informatie geven: tot €7,5 miljoen of 1% omzet

De zwaarste boetes in het Europese regelgevingslandschap. Zwaarder dan GDPR (4%), zwaarder dan NIS2 (2%), zwaarder dan DORA (2%).

---

## Deel 10 — De AI Act en lokale AI: het volledige plaatje

Nu alles samen.

### Waarom lokale AI de weg van de minste weerstand is

**Art. 10 databeheer:** bij lokale AI ken je de data. Bij cloud AI niet.

**Art. 11 technische documentatie:** bij lokale AI kun je het systeem volledig documenteren. Bij cloud AI ben je afhankelijk van wat de provider deelt.

**Art. 12 logging:** bij lokale AI heb jij de logs. Bij cloud AI heb je ze op verzoek, in het formaat van de provider.

**Art. 13 transparantie:** open-weight modellen zijn inspecteerbaar. Closed-source modellen zijn zwarte dozen.

**Art. 14 menselijk toezicht:** bij lokale AI is de stop-knop letterlijk in jouw handen. Bij cloud AI is het een API-call naar een externe server.

**Art. 86 uitlegrecht:** bij lokale open-weight modellen kun je de redenering reconstrueren. Bij closed-source cloud modellen niet.

### De open-source sleutel

De combinatie van twee elementen maakt lokale AI juridisch aantrekkelijk:

1. **Open-source GPAI-vrijstelling (Art. 53 lid 2):** open-weight modellen zijn vrijgesteld van de zware GPAI-verplichtingen.

2. **Hoog-risico verplichtingen zijn wel van toepassing:** maar die verplichtingen zijn bij lokale deployment veel eenvoudiger te vervullen.

Het resultaat: lokale AI met open-weight modellen is zowel technisch mogelijk als juridisch de meest beheersbare route voor hoog-risico toepassingen.

### De samenvatting in één schema

| Vereiste | Cloud AI | Lokale AI |
|---|---|---|
| Databeheer (Art. 10) | Afhankelijk van provider | Volledig in eigen handen |
| Technische documentatie (Art. 11) | Gedeeltelijk, provider-afhankelijk | Volledig zelf te maken |
| Logging (Art. 12) | Bij provider, op verzoek | Bij jou, volledig beheerbaar |
| Transparantie (Art. 13) | Beperkt bij closed-source | Volledig bij open-weight |
| Stop-knop (Art. 14) | API-annulering | Fysiek aanwezig |
| Uitlegrecht (Art. 86) | Beperkt | Volledig |
| Open-source vrijstelling | Niet van toepassing | Wel van toepassing |

---

## Deel 11 — Praktische scenario's

### Scenario 1: Accountantskantoor met AI-gestuurde BTW-analyse

Een accountant gebruikt een AI-systeem om BTW-aangiftes te analyseren en afwijkingen te detecteren.

**Valt dit onder hoog-risico?**
Mogelijk — als het systeem bijdraagt aan beslissingen over de kredietwaardigheid van klanten (Bijlage III, punt 5b) of belastingaangiftes beïnvloedt die essentiële financiële gevolgen hebben.

**Met cloud AI:** technische documentatie over de trainingsdata is niet beschikbaar. Logging is beperkt. Uitlegrecht aan klanten is moeilijk te vervullen.

**Met lokale AI:** volledig gedocumenteerd systeem, eigen logs, open-weight model waarvan de werking uitgelegd kan worden aan klanten en toezichthouders.

---

### Scenario 2: Therapeut met AI-gestuurde sessienotenverwerking

Een therapeut gebruikt een AI om sessienotities te structureren en behandelplannen op te stellen.

**Valt dit onder hoog-risico?**
Gezondheidsdata is Art. 9 GDPR-data. Als het AI-systeem bijdraagt aan behandelbesluiten, is het mogelijk hoog-risico (gezondheidszorg, Bijlage I sector). Als het alleen samenvatting is zonder beslissingscomponent, mogelijk niet.

**Met cloud AI:** sessienotities — Art. 9 GDPR-data — gaan naar een externe server. GDPR-schending + mogelijke AI Act-schending.

**Met lokale AI:** data verlaat de praktijk niet. Geen GDPR-probleem. Als het hoog-risico is: alle verplichtingen zijn vervulbaar omdat het systeem volledig in eigen beheer is.

---

### Scenario 3: HR-afdeling met AI voor cv-screening

Een bedrijf gebruikt een AI om sollicitaties te screenen en kandidaten te rangschikken.

**Valt dit onder hoog-risico?**
Ja. Bijlage III, punt 4a is expliciet: AI voor het screenen of filteren van sollicitaties is hoog-risico.

**Met cloud AI:** alle verplichtingen van Art. 8-15 zijn van toepassing, maar moeilijk te vervullen omdat de trainingsdata en het model niet volledig toegankelijk zijn.

**Met lokale AI:** alle verplichtingen zijn vervulbaar. Én: je kunt een eerlijke uitleg geven aan afgewezen kandidaten (Art. 86).

---

## Begrippenlijst

**AI-systeem** — een op een machine gebaseerd systeem dat input verwerkt om output te genereren (voorspellingen, aanbevelingen, beslissingen) met een zekere mate van autonomie.

**Aanbieder (Provider)** — degene die een AI-systeem ontwikkelt en op de markt brengt. OpenAI voor ChatGPT, Meta voor Llama.

**Deployer (Gebruiker)** — degene die een AI-systeem inzet voor beroepsmatige doeleinden. De accountant die ChatGPT gebruikt. Het ziekenhuis dat een diagnostiek-AI inzet.

**GPAI-model** — een groot taalmodel dat voor algemene doeleinden ingezet kan worden. ChatGPT, Gemini, Claude, Llama, Mistral.

**Hoog-risico AI-systeem** — een AI-systeem dat ingezet wordt in een context met significante risico's voor rechten en veiligheid van mensen. Gedefinieerd in Bijlage III.

**Conformiteitsbeoordeling** — het proces waarbij aangetoond wordt dat een hoog-risico AI-systeem voldoet aan alle vereisten van de AI Act.

**Open-source vrijstelling** — de bepaling (Art. 53 lid 2) dat aanbieders van open-source GPAI-modellen grotendeels vrijgesteld zijn van GPAI-verplichtingen.

**AI-geletterdheid** — het niveau van begrip van AI-technologie, -mogelijkheden en -risico's dat vereist is van medewerkers die AI gebruiken of beheren. Verplicht te bevorderen onder Art. 4.

**Stop-knop** — het mechanisme waarmee een menselijke toezichthouder een hoog-risico AI-systeem onmiddellijk kan onderbreken of stoppen (Art. 14).

**Logging** — het automatisch registreren van de werking van een AI-systeem, inclusief inputs, outputs en beslissingen, voor traceerbaarheid (Art. 12).

**Menselijk toezicht** — de verplichting dat een hoog-risico AI-systeem effectief gecontroleerd kan worden door een mens die het systeem begrijpt en kan ingrijpen (Art. 14).

**Systeemrisico** — het risico dat een GPAI-model met meer dan 10^25 FLOP trainingscompute systemische gevolgen heeft voor de samenleving. Modellen met systeemrisico hebben zwaardere verplichtingen.

**AI Office** — het Europese bureau dat toezicht houdt op GPAI-modellen en de implementatie van de AI Act coördineert. Opgericht in 2024 binnen de Europese Commissie.

**Nationale toezichthoudende autoriteit** — per lidstaat aangewezen autoriteit voor AI Act-toezicht. In België aangewezen maar nog niet volledig operationeel in maart 2026. In Nederland: rol verdeeld over meerdere toezichthouders.

---

## Checklist voor een klantgesprek

**Eerste screening:**
- [ ] Gebruikt uw organisatie AI-systemen voor beroepsmatige doeleinden?
- [ ] In welke context? (HR, finance, zorg, onderwijs, overheid?)
- [ ] Neemt het AI-systeem beslissingen die mensen raken, of ondersteunt het alleen?

**Als hoog-risico mogelijk:**
- [ ] Heeft u een risicobeheersysteem gedocumenteerd? (Art. 9)
- [ ] Weet u welke data het systeem gebruikt en hoe die is samengesteld? (Art. 10)
- [ ] Heeft u technische documentatie van het systeem? (Art. 11)
- [ ] Worden de handelingen van het systeem gelogd en zijn die logs traceerbaar? (Art. 12)
- [ ] Kunnen uw medewerkers de output van het systeem uitleggen? (Art. 13)
- [ ] Is er een menselijke toezichthouder aangewezen? Kan die het systeem stoppen? (Art. 14)
- [ ] Kunt u betrokkenen uitleggen hoe het systeem hun dossier heeft beïnvloed? (Art. 86)

**AI-geletterdheid (voor iedereen):**
- [ ] Weten uw medewerkers wat AI wel en niet kan?
- [ ] Weten ze welke data ze niet mogen invoeren in een AI-systeem?
- [ ] Is er beleid voor verantwoord AI-gebruik?

---

_Vorige document: 04-data-act.md_
_Dit is het laatste wetgevingsdocument in de reeks._
_Volgende stap: sectordossiers per doelgroep_
_Laatste update: maart 2026_
