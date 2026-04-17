# S04 — Medische & Tandartspraktijken
### LocAI Bibliotheek · Sectordossier
_Versie 0.1 · 25 maart 2026_

---

## Wie zijn ze

Artsen en tandartsen staan dagelijks aan het begin van het meest persoonlijke wat er bestaat: de gezondheid van hun patiënten. Ze kennen lichamen en levens zoals niemand anders. Ze horen klachten die mensen thuis niet durven uitspreken. Ze zien kwetsbaarheden die verborgen blijven voor familie en vrienden.

Het vertrouwen dat patiënten hen schenken is de basis van de geneeskunde zelf — en dat vertrouwen vereist absolute discretie.

**Typisch profiel:**
- Huisartsenpraktijk van 1-5 artsen
- Tandartspraktijk van 1-4 tandartsen
- 1.500-2.500 actieve patiënten per huisarts
- Hoge administratieve last: consultatieverslag, attesten, doorverwijzingen, correspondentie met specialisten
- Werken met een Elektronisch Medisch Dossier (EMD) — verplicht in België en Nederland

**Specifieke beroepsgroepen:**
- Huisartsen — breed patiëntenbestand, poortwachtersfunctie
- Tandartsen — combinatie medisch en technisch werk
- Specialisten — diepere expertise, vaak ziekenhuisgebonden maar ook zelfstandig
- Kinesitherapeuten — behandelplannen, voortgangsverslagen
- Verpleegkundigen in zelfstandige praktijk

---

## Welke data verwerken ze

**Per patiëntdossier:**
- Medische voorgeschiedenis — alle aandoeningen, operaties, ziekenhuisopnames
- Medicatielijst — alle huidige en vroegere medicatie
- Consultatieverslag — wat besproken is bij elk consult
- Laboratoriumresultaten — bloedwaarden, urine, biopsies
- Beeldvorming — röntgenfoto's, echo's, scans
- Doorverwijzingen — naar welke specialist en waarom
- Attesten en verslagen — voor werkgever, verzekeraar, school, rechtbank
- Psychosociale context — gezinssituatie, werk, stress, verslaving
- Seksuele gezondheid — anticonceptie, SOA, seksueel overdraagbare aandoeningen
- Psychiatrische informatie — depressie, angststoornissen, psychoses
- Genetische informatie — familiale aandoeningen, erfelijke risico's

**Wat dit data specifiek maakt:**
Medische data is de meest gevoelige categorie persoonsgegevens die bestaat. Een gelekt medisch dossier kan iemands verzekering beïnvloeden, zijn carrière schaden, zijn relaties beschadigen, en zijn waardigheid aantasten. Kanker, HIV, psychiatrische diagnoses, verslavingen — informatie die iemand zorgvuldig afschermt van zijn omgeving.

---

## Welke wetten zijn van toepassing

### GDPR Art. 9 — Gezondheidsdata als bijzondere categorie

Alle medische data is bijzondere categorie data onder GDPR Art. 9. De verwerking is in principe verboden, tenzij de uitzondering voor gezondheidszorg van toepassing is (Art. 9 lid 2h).

Die uitzondering geldt voor de arts zelf en voor zorgverleners onder zijn supervisie — niet automatisch voor externe tools en diensten die hij gebruikt.

**Cruciaal punt:** een cloud AI-tool die patiëntdata verwerkt is een externe verwerker. De overdracht van medische data aan die verwerker vereist een geldige GDPR-grondslag. De uitzondering voor gezondheidszorg dekt de arts — maar dekt hij ook zijn cloud AI-tool?

Juridisch antwoord: neen. De uitzondering geldt voor de zorgprofessional, niet voor zijn leveranciers. Voor externe verwerkers is een expliciete verwerkersovereenkomst én een geldige grondslag vereist.

### Medisch beroepsgeheim

**België:** Art. 458 Strafwetboek [1]. Het medisch beroepsgeheim is absoluut — behalve wettelijke uitzonderingen. Schending is strafbaar.

**Nederland:** Art. 7:457 BW (WGBO) [2] en Art. 88 Wet BIG [3]. Het beroepsgeheim geldt voor alle BIG-geregistreerde zorgverleners.

**De vraag voor cloud AI:** als een arts patiëntdata invoert in een cloud AI-tool — ook voor administratief gebruik — is dat een schending van het medisch beroepsgeheim?

Juridisch: het is een ernstig risico. De data verlaat de directe controlesfeer van de arts en wordt verwerkt door een derde partij die geen zorgverlener is en niet gebonden is aan medisch beroepsgeheim.

### Wet op de Patiëntenrechten (België) / WGBO (Nederland)

**België:** Wet van 22 augustus 2002 betreffende de rechten van de patiënt. Patiënten hebben recht op inzage in hun dossier, recht op privacy, en recht op correctie van onjuiste gegevens.

**Nederland:** Wet op de Geneeskundige Behandelingsovereenkomst (WGBO). Vergelijkbare rechten. Bewaartermijn: 20 jaar na laatste behandeling.

### AI Act — Hoog risico

Medische AI is expliciet hoog-risico als het bijdraagt aan diagnose of behandelbeslissingen [4].

**Wat hoog-risico is:**
- AI die symptomen analyseert en diagnoses suggereert
- AI die behandelplannen opstelt of aanpast
- AI die medicatiedoseringen berekent
- AI die beeldvorming analyseert (radiologie-AI)

**Wat waarschijnlijk niet hoog-risico is:**
- AI die consultatieverslag dicteert en structureert
- AI die standaardbrieven en doorverwijzingen opstelt
- AI die agenda beheert en afspraken plant

**Maar:** zelfs administratieve AI die patiëntdata verwerkt, valt onder GDPR Art. 9 — ongeacht het AI Act-risiconiveau.

### eHealth-regelgeving

**België:** het eHealth-platform [5] reguleert de digitale uitwisseling van medische data. Toegang tot patiëntgegevens via het MyCareNet-netwerk vereist authenticatie en autorisatie.

**Nederland:** het Landelijk Schakelpunt (LSP) en het Nationaal Gezondheidsinformatiepunt (Nuts) regelen gegevensuitwisseling tussen zorgverleners.

**Implicatie:** medische data die via cloud AI verwerkt wordt, verlaat het gereguleerde eHealth-ecosysteem. Dat is een extra compliance-risico bovenop GDPR.

---

## Concrete use cases voor AI

### 1. Consultatieverslagen dicteren en structureren

**Wat het is:** de arts dicteert zijn bevindingen na een consultatie. AI zet de gesproken tekst om naar een gestructureerd consultatieverslag in het EMD.

**Tijdsbesparing:** een huisarts met 30 consultaties per dag besteedt gemiddeld 3-5 minuten per consultatie aan verslaglegging. Dat is 90-150 minuten per dag. AI kan dit halveren.

**Het risico bij cloud AI:** de gesproken consultatie — naam van de patiënt, klacht, bevindingen, diagnose, medicatie — gaat als audiobestand of tekst naar een externe server. Art. 9 GDPR. Medisch beroepsgeheim.

**Met lokale AI + whisper.cpp:** spraak-naar-tekst lokaal verwerkt. De audio verlaat het kabinet niet. Het consultatieverslag wordt lokaal gegenereerd.

---

### 2. Doorverwijzingsbrieven opstellen

**Wat het is:** AI genereert een conceptbrief voor doorverwijzing naar een specialist op basis van de consultatie-informatie.

**Tijdsbesparing:** doorverwijzingsbrieven zijn tijdrovend maar grotendeels gestandaardiseerd. AI bespaart 5-10 minuten per doorverwijzing.

**Het risico bij cloud AI:** medische geschiedenis, diagnose, reden van doorverwijzing — alles naar een externe server.

**Met lokale AI:** doorverwijzingen lokaal gegenereerd. Niets verlaat het kabinet.

---

### 3. Attest en verslag genereren

**Wat het is:** attesten voor werkgever, school, verzekeraar, of rechtbank. AI genereert het juiste formaat op basis van de beschikbare medische informatie.

**Tijdsbesparing:** attesten zijn repetitief. AI bespaart significant tijd bij veel voorkomende attesten.

**Het risico bij cloud AI:** medische informatie die in een attest staat is per definitie gevoelig — anders was het attest niet nodig.

**Met lokale AI:** attestgeneratie intern. Gevoelige medische informatie blijft intern.

---

### 4. Medicatiecontrole en interacties

**Wat het is:** AI controleert of een nieuw voor te schrijven medicament interacties heeft met de bestaande medicatie van de patiënt.

**Tijdsbesparing en veiligheid:** medicatie-interacties zijn een van de grootste risico's in de geneeskunde. Een lokale AI die dit systematisch controleert is een veiligheidstool.

**AI Act-aandacht:** dit is potentieel hoog-risico als de AI bijdraagt aan de medicatiebeslissing. Menselijk toezicht (Art. 14) is verplicht — de arts bevestigt altijd.

**Met lokale AI:** medicatiecontrole intern, op basis van een lokale farmacologische database.

---

### 5. Patiëntcommunicatie

**Wat het is:** AI helpt bij het opstellen van begrijpelijke uitleg voor patiënten — wat betekent deze diagnose, hoe werkt dit medicament, wat zijn de bijwerkingen.

**Waarde:** medische communicatie in begrijpelijke taal verbetert therapietrouw en patiënttevredenheid.

**Het risico bij cloud AI:** de diagnose en het medicament — gekoppeld aan de context van de patiënt — gaan naar een externe server.

**Met lokale AI:** patiëntcommunicatie intern gegenereerd.

---

## Het concrete risico bij cloud AI

**Scenario — De huisarts met spraak-naar-tekst:**
Een huisarts gebruikt een cloud spraak-naar-tekst tool gecombineerd met een AI-assistent om zijn consultaties te verwerken. Na elk consult dicteert hij: "Patiënt Jan Janssen, 52 jaar, rookt, heeft diabetes type 2, bloed recent 8,4, overweeg insuline..."

**Wat er juridisch gebeurt:**
1. Naam, leeftijd, diagnose, laboratoriumresultaten — Art. 9 GDPR bijzondere categorie — gaan naar een externe server.
2. Er is geen geldige verwerkingsgrondslag voor deze overdracht.
3. Het medisch beroepsgeheim is potentieel geschonden.
4. De patiënt heeft geen toestemming gegeven.
5. De data staat op servers in de VS, mogelijk onderworpen aan de CLOUD Act.

**Wat de patiënt zou vinden:**
De meeste patiënten gaan ervan uit dat hun medische informatie in het kabinet blijft. Als ze wisten dat hun HIV-status, psychiatrische diagnose, of verslaving op een Amerikaanse server staat — ze zouden van arts wisselen.

---

## Wat lokale AI oplost

**De architecturale oplossing:**
Een mini-PC of krachtige laptop in het kabinet. whisper.cpp voor lokale spraak-naar-tekst. Ollama met een medisch-geoptimaliseerd open-weight model. Integratie met het bestaande EMD via een lokale API.

**Wat er juridisch verandert:**
- Geen overdracht van Art. 9-data aan externe servers
- Medisch beroepsgeheim intact
- GDPR compliant by architecture
- eHealth-compliance: data blijft binnen de organisatie

**Wat er praktisch verandert:**
- Consultatieverslag in seconden gedicteerd en gestructureerd
- Doorverwijzingen en attesten in minuten
- Medicatiecontrole geautomatiseerd
- Meer tijd voor patiënten, minder voor administratie

---

## De kernboodschap voor het eerste gesprek

Beginnen met de patiënt — niet met technologie.

> "Uw patiënten vertrouwen u met de meest persoonlijke informatie die bestaat. Als u vandaag AI gebruikt voor uw verslaglegging — weet u dan zeker dat die informatie op uw eigen systemen blijft?"

Vervolg:

> "Lokale AI verwerkt alles in uw kabinet. De medische gegevens van uw patiënten verlaten uw praktijk niet. U bent compliant met GDPR, met het medisch beroepsgeheim, en met de eHealth-regelgeving. En u bespaart significant tijd op administratie."

---

## Vragen die ze stellen en hoe je antwoordt

**"Mijn EMD-software is ook in de cloud — is dat niet hetzelfde probleem?"**

Uw EMD heeft een specifieke verwerkersovereenkomst en is gecertificeerd voor medische data. Dat is anders dan een generieke cloud AI-tool gebruiken. Bovendien: steeds meer EMD-leveranciers bieden on-premise versies aan, precies om dit probleem te vermijden.

**"Ik gebruik toch alleen de voornaam of een patiëntnummer?"**

Medische data met leeftijd, diagnose, en medicatie is herleidbaar tot een individu — ook zonder naam. En in de praktijk gebruikt niemand consequent pseudoniemen in een gesprokken dictaat.

**"Het Riziv/de zorgverzekeraar vereist toch digitale dossiers?"**

Digitale dossiers en cloud AI zijn twee verschillende dingen. Uw EMD kan digitaal en compliant zijn terwijl uw AI-tools lokaal draaien. De eis voor digitale dossiers vereist geen cloud AI.

**"Is lokale AI niet te langzaam voor dagelijks gebruik?"**

Voor consultatieverslag en attesten — taken van seconden tot minuten — is moderne lokale AI ruim voldoende. De snelheid hoeft niet te concurreren met cloud AI. Ze moet alleen snel genoeg zijn voor de taak — en dat is ze.

**"Mijn patiënten zijn ouder — die begrijpen AI toch niet?"**

U hoeft uw patiënten niet uit te leggen hoe uw dictaatsoftware werkt. U hoeft alleen te weten dat hun data veilig is. Dat is uw verantwoordelijkheid, niet de hunne.

---

## Bijzondere aandacht: tandartspraktijk

Tandartsen verwerken naast medische data ook beeldvorming (röntgenfoto's, CBCT-scans) en financiële data (behandelkosten, verzekeringsclaims).

**AI-use cases specifiek voor tandartsen:**
- Analyse van röntgenfoto's voor cariësdetectie — dit is hoog-risico AI Act
- Behandelplannen genereren op basis van bevindingen
- Factuurverwerking en verzekeringsclaims
- Patiëntcommunicatie over behandelingen

**Hoog-risico aandacht:** AI die röntgenfoto's analyseert en diagnoses stelt is expliciet hoog-risico. Menselijk toezicht van de tandarts is altijd verplicht — de AI is een hulpmiddel, geen vervanging.

---

## Bijzondere aandacht: kinesitherapeuten

Kinesitherapeuten werken met behandelplannen, voortgangsverslagen en doorverwijzingen van artsen.

**AI-use cases:**
- Behandelplan opstellen op basis van diagnose en doelstellingen
- Voortgangsverslag genereren
- Oefenschema's voorstellen

**GDPR-aandacht:** behandelplannen bevatten medische diagnoses (doorverwezen door de arts) — bijzondere categorie data.

---

## Belgische en Nederlandse context

### België

**RIZIV** — Rijksinstituut voor Ziekte- en Invaliditeitsverzekering. Reguleert de terugbetaling van medische prestaties en stelt eisen aan elektronische dossiervoering.

**eHealth-platform** [5] — Belgisch platform voor digitale uitwisseling van medische data. Vereist voor samenwerking tussen zorgverleners.

**Domus Medica** — Beroepsorganisatie voor huisartsen in Vlaanderen.

**BVGG** — Belgische Vereniging voor Geestelijke Gezondheid. Relevant voor psychiaters en psychologen met medische achtergrond.

### Nederland

**KNMG** — Koninklijke Nederlandsche Maatschappij tot bevordering der Geneeskunst. Beroepsorganisatie voor artsen.

**NZa** — Nederlandse Zorgautoriteit. Toezicht op zorgmarkt en tarieven.

**IGJ** — Inspectie Gezondheidszorg en Jeugd. Toezicht op kwaliteit en veiligheid van zorg.

**LSP** — Landelijk Schakelpunt. Digitale uitwisseling van medische data tussen zorgverleners.

---

## Sectorcijfers (referentie)

- Aantal huisartsen in België: circa 12.000
- Aantal huisartsen in Nederland: circa 14.000
- Aantal tandartsen in België: circa 8.500
- Aantal tandartsen in Nederland: circa 9.000
- Gemiddelde administratieve last huisarts: 2-3 uur per dag
- Potentiële tijdsbesparing met AI voor verslaglegging: 40-60%
- Wachttijden voor nieuwe patiënten bij huisartsen: gemiddeld 2-4 weken (NL), vergelijkbaar (BE)

De combinatie van hoge administratieve last, patiëntentekort en toenemende vergrijzing maakt de medische sector bijzonder ontvankelijk voor AI-ondersteuning. De vraag is niet óf — de vraag is hoe, en met wiens data.

---

## Bronnen

1. **Art. 458 Strafwetboek België — Medisch beroepsgeheim**  
   Belgisch Staatsblad / ejustice.just.fgov.be  
   <https://www.ejustice.just.fgov.be/eli/wet/1867/06/08/1867060801/justel>

2. **WGBO — Art. 7:457 BW — Geheimhoudingsplicht**  
   wetten.overheid.nl  
   <https://wetten.overheid.nl/BWBR0005290/>

3. **Wet BIG — Art. 88 — Zwijgplicht**  
   wetten.overheid.nl  
   <https://wetten.overheid.nl/BWBR0006251/>

4. **AI Act — Verordening (EU) 2024/1689, Bijlage III — Hoog-risico medische AI**  
   EUR-Lex, Publicatieblad van de Europese Unie  
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

5. **eHealth-platform België — Digitale uitwisseling medische data**  
   Federale overheidsdienst / eHealth  
   <https://www.ehealth.fgov.be/>

---

_Onderdeel van: LocAI Bibliotheek · Sectordossiers_
_Vorige: S03 — Juristen & Advocaten_
_Volgende: S05 — Horeca_
_Laatste update: 25 maart 2026_
