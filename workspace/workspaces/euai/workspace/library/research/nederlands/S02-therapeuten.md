# S02 — Therapeuten & Psychologen
### LocAI Bibliotheek · Sectordossier
_Versie 0.1 · 25 maart 2026_

---

## Wie zijn ze

Therapeuten en psychologen werken met mensen op hun meest kwetsbare momenten. Ze horen dingen die niemand anders hoort. Ze bewaren geheimen die families zouden verscheuren. Ze kennen de diepste angsten, de donkerste gedachten, de meest intieme details van het leven van hun cliënten.

Dat vertrouwen is niet alleen de basis van hun beroep — het is de therapeutische werkzaamheid zelf. Zonder vertrouwen werkt therapie niet.

**Typisch profiel:**
- Solo-praktijk of kleine groepspraktijk van 2-5 therapeuten
- 20-50 actieve cliënten per therapeut
- Sessies van 50-90 minuten, 1-2 keer per week per cliënt
- Werkzaam onder beroepsgeheim en ethische codes van beroepsorganisaties
- Hoge administratieve last: sessienotities, behandelplannen, voortgangsrapporten, correspondentie met andere zorgverleners

**Specifieke beroepsgroepen:**
- Klinisch psychologen (erkend door VVKP in België, NIP in Nederland)
- Psychotherapeuten (erkend beroep in België, Wet BIG in Nederland)
- Counselors en coaches (minder gereguleerd, maar beroepsgeheim geldt ook hier)
- Psychiaters (medisch specialisten — extra GGZ-regelgeving)

---

## Welke data verwerken ze

Dit is de meest gevoelige categorie data die bestaat — bijzondere categorieën onder GDPR Art. 9 [1].

**Per cliëntdossier:**
- Sessienotities — gedetailleerde verslagen van wat er besproken is
- Behandelplannen — diagnose, doelstellingen, interventies
- Voortgangsrapporten — hoe gaat het met de cliënt
- Correspondentie met huisarts, psychiater, school of werkgever
- Testresultaten en assessments — intelligentietests, persoonlijkheidstests
- Crisissituaties — suïcidale gedachten, zelfbeschadiging, psychoses
- Medicatie-informatie
- Familiegeschiedenis en traumageschiedenis

**Wat dit data specifiek maakt:**
Sessienotities zijn geen neutrale medische data. Ze bevatten de innerlijke wereld van een persoon — gedachten, gevoelens, herinneringen die vaak nooit eerder uitgesproken zijn. Ze kunnen informatie bevatten over seksuele geaardheid, religieuze twijfels, politieke opvattingen, illegale activiteiten, relatieproblemen, financiële stress.

Een gelekt sessiedossier kan iemands leven vernietigen. Carrière, relaties, reputatie — alles staat op het spel.

---

## Welke wetten zijn van toepassing

### GDPR Art. 9 — Bijzondere categorieën, extra bescherming

Gezondheidsdata is een bijzondere categorie. Dat betekent:
- Verwerking is in principe verboden
- Uitzondering: noodzakelijk voor gezondheidszorg door een zorgprofessional met beroepsgeheim (Art. 9 lid 2h)
- Die uitzondering geldt voor de therapeut zelf — niet automatisch voor elke tool die de therapeut gebruikt

**De kritieke vraag:** valt een cloud AI-tool die sessienotities verwerkt onder de uitzondering voor gezondheidszorg?

Juridisch antwoord: nee. De uitzondering geldt voor de zorgprofessional. Een externe AI-dienst is geen zorgprofessional. De doorgifte van gezondheidsdata aan een cloud AI vereist een expliciete verwerkingsgrondslag — en toestemming van de cliënt is in een therapeutische relatie problematisch (zie hieronder).

### GDPR — Toestemming in een therapeutische relatie

Art. 7 lid 4 stelt dat toestemming niet vrij is als er een duidelijke machtsongelijkheid bestaat tussen de verwerkingsverantwoordelijke en de betrokkene.

Een cliënt die zijn therapeut vraagt om hulp staat in een afhankelijke positie. Als de therapeut zegt "ik gebruik AI voor mijn notities, gaat u daarmee akkoord?" — is die toestemming dan echt vrij? Juridisch is dit een grijs gebied. Ethisch is het problematischer.

### GDPR — Minderjarigen (Overweging 38)

Veel therapeuten werken met kinderen en jongeren. GDPR geeft minderjarigen extra bescherming. Toestemming voor verwerking van data van minderjarigen moet gegeven worden door de ouders of wettelijke vertegenwoordigers — en vereist extra zorgvuldigheid.

### Beroepsgeheim — Wet en ethiek

In België: het beroepsgeheim voor psychologen en psychotherapeuten is verankerd in Art. 458 van het Strafwetboek [2]. Schending van beroepsgeheim is een strafbaar feit.

In Nederland: het beroepsgeheim voor BIG-geregistreerde zorgverleners is vastgelegd in de Wet BIG [3] en het Burgerlijk Wetboek.

**De vraag:** is het gebruik van een cloud AI-tool een schending van het beroepsgeheim?

Juridisch oordeel: het is op zijn minst een ernstig risico. Sessiedata overdragen aan een externe server — ook met een DPA — is een overdracht aan een derde partij. De cliënt heeft daar geen kennis van gegeven, laat staan toestemming.

### AI Act — Hoog risico

Als een AI-systeem bijdraagt aan beslissingen over de gezondheid of behandeling van een patiënt, is het hoog-risico onder de AI Act (Bijlage III — gezondheidszorg sector, kritieke infrastructuur).

**Nuance:** puur administratieve AI (notities samenvatten, agenda beheren) is waarschijnlijk niet hoog-risico. AI die behandelsuggesties doet of cliënten categoriseert — dat is hoog-risico.

**AI-geletterdheid (Art. 4):** ook voor therapeuten die AI gebruiken voor administratie geldt de plicht tot AI-geletterdheid.

### GGZ-specifieke regelgeving

In Nederland gelden voor GGZ-instellingen aanvullende regels via de Wet op de Geneeskundige Behandelingsovereenkomst (WGBO) [4] en de Kwaliteitsstandaard ROM. Dossierplicht, bewaartermijnen, en rechten van patiënten zijn uitgebreid geregeld.

In België gelden de wet op de rechten van de patiënt en de erkenningsnormen voor psychologische praktijken.

---

## Concrete use cases voor AI

### 1. Sessienotities structureren

**Wat het is:** de therapeut dicteert of typt ruwe notities na een sessie. AI structureert die in het juiste format — SOAP-notitie (Subjectief, Objectief, Analyse, Plan) of DAP-format (Data, Analyse, Plan).

**Tijdsbesparing:** een therapeut met 30 sessies per week besteedt gemiddeld 10-15 minuten per sessie aan notities. Dat is 5-7,5 uur per week administratie. AI kan dit halveren.

**Het risico bij cloud AI:** de ruwe sessienotities — de meest gevoelige data denkbaar — gaan naar een externe server. Art. 9 GDPR. Beroepsgeheim. Strafbaar feit.

**Met lokale AI:** notities worden verwerkt op de eigen laptop of kantoorserver. Geen data verlaat de praktijk. De cliënt hoeft het niet eens te weten.

---

### 2. Behandelplan opstellen

**Wat het is:** op basis van de intake en eerste sessies een behandelplan genereren als eerste concept dat de therapeut aanpast en finaliseert.

**Tijdsbesparing:** een behandelplan opstellen kost 30-60 minuten. AI genereert een concept in minuten.

**Het risico bij cloud AI:** de diagnose, de probleemformulering, de therapeutische doelstellingen — alles gaat naar een externe server.

**Met lokale AI:** behandelplangeneratie op eigen hardware. Niets verlaat de praktijk.

---

### 3. Voortgangsrapportage

**Wat het is:** periodieke rapporten voor huisarts, school, werkgever of verzekeraar. AI genereert het eerste concept op basis van sessienotities.

**Tijdsbesparing:** significant — zeker voor rapporten die naar derden gaan en formeel geschreven moeten zijn.

**Het risico bij cloud AI:** voortgangsrapporten bevatten een samenvatting van het behandeltraject — alle gevoelige informatie gecomprimeerd in één document, naar een externe server.

**Met lokale AI:** rapportgeneratie lokaal. Intern document, interne verwerking.

---

### 4. Cliëntcommunicatie

**Wat het is:** AI helpt bij het opstellen van brieven en e-mails aan cliënten — afspraakbevestigingen, herinneringen, informatieve teksten over het therapietraject.

**Tijdsbesparing:** beperkt per bericht, maar cumulatief significant.

**Het risico bij cloud AI:** naam en contactgegevens van cliënten gaan naar een externe server — al is dat minder gevoelig dan sessiedata.

**Met lokale AI:** ook communicatie lokaal verwerkt.

---

### 5. Interne kennisbank

**Wat het is:** een lokale AI die de therapeut helpt bij het opzoeken van therapeutische technieken, DSM-criteria, medicatie-informatie, of professionele literatuur.

**Tijdsbesparing:** minder zoekwerk, sneller antwoord op klinische vragen.

**Het risico bij cloud AI:** als de therapeut context geeft over een cliënt bij het stellen van een vraag ("mijn cliënt heeft symptomen X en Y..."), is die context vertrouwelijk.

**Met lokale AI:** kennisbankraadpleging volledig intern. Zelfs informele klinische vragen kunnen gesteld worden zonder data te lekken.

---

## Het concrete risico bij cloud AI

**Het scenario:**
Een therapeut gebruikt een spraak-naar-tekst tool gevolgd door ChatGPT om zijn sessienotities te structureren. Hij dicteert na elke sessie: "Vandaag sprak ik met [naam], 34 jaar, over zijn angsten rond zijn huwelijk, zijn seksuele problemen, en zijn gedachten over zelfbeschadiging..."

**Wat er juridisch gebeurt:**
1. De naam, leeftijd, en de meest intieme details van de cliënt — Art. 9 GDPR bijzondere categorie data — worden overgedragen aan OpenAI.
2. Er is geen geldige verwerkingsgrondslag voor deze overdracht.
3. Het beroepsgeheim is geschonden — strafbaar onder Art. 458 Strafwetboek [2] (België).
4. De cliënt heeft nooit toestemming gegeven.
5. Als de cliënt ooit ontdekt dat zijn sessienotities op Amerikaanse servers staan, is het vertrouwen — en de therapeutische relatie — onherstelbaar beschadigd.

**Wat er ook kan gebeuren:**
- Een datalek bij OpenAI waarbij sessiedata van cliënten uitlekt
- Een klacht bij de VVKP of het NIP die kan leiden tot schorsing
- Een strafrechtelijke vervolging wegens schending van beroepsgeheim
- Een GDPR-klacht bij de GBA met boetes

---

## Wat lokale AI oplost

**De architecturale oplossing:**
Een lokale server of krachtige laptop. Ollama met een open-weight model. Een eenvoudige interface voor notitie-input. Alle verwerking intern.

**Optioneel: whisper.cpp voor spraak-naar-tekst:**
whisper.cpp is een open-source spraak-naar-tekst model dat lokaal draait. De therapeut dicteert — de tekst wordt lokaal gegenereerd. Geen audio naar externe servers.

**Wat er juridisch verandert:**
- Geen overdracht van Art. 9-data aan een derde partij
- Beroepsgeheim intact
- GDPR compliant by architecture
- Geen verwerkersovereenkomst nodig voor de AI-component

**Wat er praktisch verandert:**
- Notities structureren in seconden in plaats van minuten
- Behandelplannen als concept in minuten
- Meer tijd voor cliënten, minder tijd voor administratie
- Geen angst dat sessiedata ergens op een server staat

---

## De kernboodschap voor het eerste gesprek

Beginnen met de therapeutische relatie — niet met technologie.

> "Uw cliënten vertellen u dingen die ze niemand anders vertellen. Dat vertrouwen is de basis van uw werk. Als u vandaag AI gebruikt voor uw notities of behandelplannen, weet u dan zeker dat die data niet buiten uw praktijk terechtkomt?"

Vervolg:

> "Lokale AI verwerkt alles op uw eigen apparaat. De sessienotities van uw cliënten verlaten uw praktijk niet. U heeft dezelfde functionaliteit — notities structureren, behandelplannen opstellen, rapporten schrijven — maar zonder het juridische en ethische risico."

---

## Vragen die ze stellen en hoe je antwoordt

**"Ik gebruik toch geanonimiseerde notities?"**

Anonimisering is moeilijker dan het lijkt. Een combinatie van leeftijd, beroep, en klacht kan een persoon identificeerbaar maken. Echte anonimisering vereist systematische verwijdering van alle identificeerbare elementen — dat doet niemand handmatig voor elke notitie. En als u later de anonieme notitie koppelt aan het dossier, is het sowieso niet meer anoniem.

**"Mijn cliënten geven toch toestemming als ik het vraag?"**

Toestemming in een therapeutische relatie is juridisch problematisch — er is een machtsongelijkheid. En ethisch: wilt u uw cliënten vragen of hun meest intieme gedachten op Amerikaanse servers mogen staan? Lokale AI elimineert die vraag volledig.

**"Is het niet omslachtig om lokaal te installeren?"**

Eenmalige installatie, daarna werkt het als elke andere tool. De interface lijkt op ChatGPT. Het enige verschil is dat alles intern blijft.

**"Wat als ik maar één laptop heb?"**

Een moderne laptop met een NPU-chip kan kleinere modellen (7B-13B) lokaal draaien — voldoende voor notities structureren en behandelplannen opstellen. Voor zwaardere taken is een mini-server op kantoor de oplossing.

**"Mijn beroepsorganisatie zegt niets over AI?"**

Klopt — de VVKP [5] en het NIP hebben nog geen specifieke AI-richtlijnen. Maar het beroepsgeheim en de GDPR-regels voor bijzondere categorieën gelden al. U bent zelf verantwoordelijk voor de keuzes die u maakt. Lokale AI is de meest conservatieve en verdedigbare keuze.

**"Wat kost het?"**

Hardware: €2.300-€3.500 voor een mini-PC met voldoende capaciteit. Setup en configuratie eenmalig. Daarna geen maandelijkse kosten voor de AI-component zelf. Vergelijk dat met €20-50 per maand voor een cloud AI-abonnement — plus het juridische risico dat u niet kunt kwantificeren.

---

## Bijzondere aandacht: crisis en suïcidaliteit

Dit is het meest gevoelige onderwerp in de therapeutische praktijk.

Sessienotities over suïcidale gedachten, zelfbeschadiging, of psychoses zijn de meest beschermde data denkbaar. Als deze informatie uitlekt, kan het levens vernietigen — carrière, relaties, zelfs verzekeringsrechtelijke gevolgen.

Een therapeut die dit soort notities door een cloud AI verwerkt, neemt een risico dat geen cliënt zou accepteren als hij het wist.

Met lokale AI: ook crisisnotities worden intern verwerkt. De meest kwetsbare informatie van de meest kwetsbare mensen blijft waar het hoort — in de praktijk, onder beroepsgeheim.

---

## Belgische en Nederlandse context

### België

**VVKP** — Vlaamse Vereniging van Klinisch Psychologen. Beroepsorganisatie en ethische code.

**BFP-FBP** — Beroepsfederatie voor Psychologen. Overkoepelende federatie.

**Erkenning:** klinisch psycholoog is een beschermd beroep in België (wet van 4 april 2014). Schending van beroepsregels kan leiden tot schorsing of schrapping.

**GGZ-financiering:** erkende psychologen werken binnen de conventie met de ziekteverzekering (RIZIV). Dossiers moeten voldoen aan RIZIV-eisen.

### Nederland

**NIP** — Nederlands Instituut van Psychologen. Beroepsorganisatie.

**BIG-register** [3] — Beroepen in de Individuele Gezondheidszorg. Psychologen en psychotherapeuten zijn BIG-geregistreerd. Tuchtrecht via het Regionaal Tuchtcollege voor de Gezondheidszorg.

**WGBO** [4] — Wet op de Geneeskundige Behandelingsovereenkomst. Regelt dossierplicht, bewaartermijnen (20 jaar), en rechten van patiënten.

**zorgdomein en EPD:** veel therapeuten werken met een Elektronisch Patiënten Dossier (EPD). De koppeling tussen lokale AI en bestaande EPD-software is een technisch aandachtspunt.

---

## Sectorcijfers (referentie)

- Aantal erkende klinisch psychologen in België: circa 10.000
- Aantal BIG-geregistreerde psychologen in Nederland: circa 28.000
- Aantal psychotherapeuten in België (erkend): circa 3.500
- Wachttijden in de GGZ: gemiddeld 3-6 maanden in Nederland, vergelijkbaar in België
- Administratieve last: therapeuten besteden gemiddeld 20-30% van hun werktijd aan administratie

De hoge administratieve last gecombineerd met lange wachttijden creëert een perfecte context voor AI-adoptie. De vraag is niet óf therapeuten AI gaan gebruiken — de vraag is welke AI.

---

## Bronnen

1. **GDPR — Verordening (EU) 2016/679, Art. 9(1) — Bijzondere categorieën**  
   EUR-Lex, Publicatieblad van de Europese Unie  
   https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng

2. **Art. 458 Strafwetboek België — Beroepsgeheim**  
   Belgisch Staatsblad / Ejustice  
   https://www.ejustice.just.fgov.be/eli/wet/1867/06/08/1867060850/justel

3. **Wet BIG — Wet op de beroepen in de individuele gezondheidszorg**  
   wetten.overheid.nl  
   https://wetten.overheid.nl/BWBR0006251/

4. **WGBO — Wet op de Geneeskundige Behandelingsovereenkomst, Art. 7:457 BW**  
   wetten.overheid.nl  
   https://wetten.overheid.nl/BWBR0005290/

5. **VVKP — Beroepsethische code klinisch psychologen**  
   Vlaamse Vereniging van Klinisch Psychologen  
   https://vvkp.be/klinisch-psychologen

---

_Onderdeel van: LocAI Bibliotheek · Sectordossiers_
_Vorige: S01 — Accountants & Boekhouders_
_Volgende: S03 — Juristen & Advocaten_
_Laatste update: 25 maart 2026_
