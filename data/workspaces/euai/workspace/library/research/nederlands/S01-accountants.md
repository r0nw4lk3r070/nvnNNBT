# S01 — Accountants & Boekhouders
### LocAI Bibliotheek · Sectordossier
_Versie 0.1 · 25 maart 2026_

---

## Wie zijn ze

Accountants en boekhouders zijn de financiële gewetens van het MKB. Ze werken voor kleine en middelgrote ondernemingen, zelfstandigen, vzw's en particulieren. Ze kennen hun klanten vaak al jaren — soms decennialang. Ze weten wat een bedrijf waard is, hoe gezond het is, en wat de eigenaar 's nachts wakker houdt.

**Typisch profiel:**
- Zelfstandige boekhouder of klein kantoor van 2-10 personen
- 30-100 actieve klantdossiers
- Werkzaam in een sterk gereguleerd beroep met wettelijke beroepsgeheim
- Lid van het ITAA (Instituut van de Accountants en de Belastingconsulenten) in België of de NBA (Nederlandse Beroepsorganisatie van Accountants) in Nederland
- Gewend aan compliance — maar niet altijd aan digitale compliance

**Werkritme:**
- Piekperiodes rond kwartaalaangiftes, jaarafsluiting en belastingaangifte
- Veel repetitief werk: categoriseren van transacties, controleren van facturen, opstellen van rapporten
- Steeds meer tijd kwijt aan communicatie met klanten over complexe fiscale vragen

---

## Welke data verwerken ze

Dit is de kern van het risico. Een accountant verwerkt de meest gevoelige financiële data van zijn klanten.

**Per klantdossier:**
- Bankafschriften — volledig inzicht in alle inkomsten en uitgaven
- Facturen en bonnen — leveranciers, klanten, bedragen
- Loonfiches en personeelsdata — salarissen, sociale zekerheid, premies
- Belastingaangiftes — BTW, vennootschapsbelasting, personenbelasting
- Jaarrekeningen — volledig financieel beeld van het bedrijf
- Contracten en overeenkomsten
- Correspondentie met belastingdienst en sociale zekerheid

**Voor particuliere klanten:**
- Persoonlijke bankafschriften
- Vastgoedinformatie
- Beleggingsportefeuilles
- Erfenissen en schenkingen

**Waarom dit zo gevoelig is:**
Een bankafschrift van een klant bevat niet alleen financiële informatie. Het vertelt het volledige verhaal van iemands leven — medische uitgaven, politieke donaties, religieuze giften, relatieproblemen, verslavingen. Een accountant die toegang heeft tot bankafschriften heeft meer inzicht in het privéleven van zijn klanten dan ze zelf beseffen.

---

## Welke wetten zijn van toepassing

### GDPR — Primaire wet

Bankafschriften, loonfiches, belastinggegevens — allemaal persoonsgegevens. Voor particuliere klanten geldt het volledige GDPR-regime.

**Verwerkingsgrondslag:** Art. 6(b) GDPR (uitvoering van een overeenkomst) [2] — de boekhouder verwerkt data omdat het noodzakelijk is om de boekhoudkundige dienst te verlenen.

**Bewaarplicht vs. opslagbeperking:** boekhoudkundige documenten moeten wettelijk 7 jaar bewaard worden (Belgisch en Nederlands boekhoudrecht). Dit staat in spanning met het GDPR-principe van opslagbeperking — maar de wettelijke bewaarplicht is een geldige grondslag voor langere bewaring.

**Verwerkersovereenkomst:** elke software die de boekhouder gebruikt om klantdata te verwerken — boekhoudpakket, cloud-opslag, AI-tool — vereist een DPA.

### DORA — Indirect van toepassing

Accountants zijn geen financiële instelling in de zin van DORA [3]. Maar:

1. Veel van hun klanten zijn dat wel — banken, verzekeraars, beleggingsfondsen.
2. Die klanten vallen onder DORA en moeten de ICT-leveranciers in hun toeleveringsketen beoordelen.
3. De accountant van een bank is een toeleverancier van die bank.
4. Als de accountant cloud AI gebruikt voor de verwerking van bankdata, triggert dat DORA-vragen bij zijn klant.

**Praktische consequentie:** een accountant die werkt voor financiële instellingen zal steeds vaker gevraagd worden om zijn ICT-praktijken te documenteren en te bewijzen.

### ITAA-beroepsregels — Beroepsgeheim

Het ITAA-reglement legt een uitgebreid beroepsgeheim op. Artikel 58 van de ITAA-wet [1]:

> "De leden van het Instituut zijn gehouden tot geheimhouding van alles wat hun in de uitoefening van hun beroep wordt toevertrouwd of ter kennis komt."

Dit beroepsgeheim is niet alleen een ethische verplichting — het is wettelijk afdwingbaar. Een accountant die klantdata deelt met een derde partij zonder toestemming van de klant, schendt zijn beroepsgeheim.

**De vraag:** is het gebruik van een cloud AI-tool een "delen met een derde partij"?

Juridisch is het antwoord genuanceerd maar de richting is duidelijk: als de cloud AI-provider data verwerkt op zijn servers, is dat technisch gezien een overdracht naar een derde partij. De verwerkersovereenkomst regelt de juridische relatie — maar het beroepsgeheim vergt meer dan een contractuele clausule.

### AI Act — Wanneer van toepassing

De meeste boekhoudkundige AI-toepassingen vallen onder minimaal risico of beperkt risico. Maar let op:

**Hoog-risico trigger:** als een AI-systeem bijdraagt aan beslissingen over de kredietwaardigheid van een klant (Bijlage III, punt 5b), of als het gebruikt wordt voor belastingaangiftes die essentiële financiële gevolgen hebben — dan kan het hoog-risico zijn.

**AI-geletterdheid (Art. 4, al van kracht):** elke accountant die AI gebruikt voor zijn werk moet voldoende AI-geletterd zijn. Dat is geen optie — het is een wettelijke verplichting.

---

## Concrete use cases voor AI

Dit zijn de taken waarvoor een accountant AI zou willen gebruiken.

### 1. Transactieclassificatie

**Wat het is:** bankafschriften importeren en elke transactie automatisch categoriseren in de juiste boekhoudkundige post.

**Tijdsbesparing:** een accountant die 50 klanten heeft met elk 200 transacties per maand — dat is 10.000 transacties per maand classificeren. Met AI: significante tijdsbesparing.

**Het risico bij cloud AI:** het volledige bankafschrift van de klant — met alle transacties, alle tegenpartijen, alle bedragen — gaat naar een externe server. De klant heeft daar geen toestemming voor gegeven. Het beroepsgeheim is in het geding.

**Met lokale AI:** het bankafschrift wordt verwerkt op de lokale server van het kantoor. Geen data verlaat het gebouw. De klant hoeft niet eens te weten dat er AI gebruikt wordt.

---

### 2. Factuurverwerking en OCR

**Wat het is:** foto's of scans van bonnen en facturen automatisch uitlezen en verwerken.

**Tijdsbesparing:** manuele invoer van facturen is tijdrovend en foutgevoelig. AI-OCR is sneller en nauwkeuriger.

**Het risico bij cloud AI:** facturen bevatten leveranciersnamen, BTW-nummers, bedragen, en soms persoonlijke informatie. Al die data gaat naar een externe server.

**Met lokale AI:** factuurverwerking op eigen hardware. Geen externe server, geen risico.

---

### 3. Rapportgeneratie

**Wat het is:** automatisch maandelijkse of kwartaalrapporten opstellen op basis van de boekhoudkundige data.

**Tijdsbesparing:** een rapport opstellen kost uren. Een AI die het eerste concept genereert bespaart significant tijd.

**Het risico bij cloud AI:** het volledige financiële beeld van de klant — omzet, kosten, marges, kasstromen — gaat als input naar een cloud model.

**Met lokale AI:** rapportgeneratie op eigen hardware. De financiële data van de klant blijft in het kantoor.

---

### 4. Fiscale vraagbeantwoording

**Wat het is:** een lokaal AI-model dat getraind is op Belgische/Nederlandse belastingwetgeving en kan antwoorden op fiscale vragen van klanten of medewerkers.

**Tijdsbesparing:** veel klantenvragen zijn repetitief. "Mag ik mijn auto aftrekken?" "Wat is de deadline voor mijn BTW-aangifte?" Een lokale fiscale assistent bespaart tijd.

**Het risico bij cloud AI:** de vraag bevat vaak context over de specifieke situatie van de klant — en die context is vertrouwelijk.

**Met lokale AI:** fiscale vragen worden beantwoord op eigen hardware. De context blijft intern.

---

### 5. Anomaliedetectie

**Wat het is:** AI die afwijkingen signaleert in financiële data — ongebruikelijke transacties, inconsistenties, potentiële fraude-indicatoren.

**Waarde:** accountants zijn wettelijk verplicht fraude te detecteren en te melden. AI kan dit systematischer en sneller doen dan manuele controle.

**Hoog-risico trigger:** als anomaliedetectie leidt tot beslissingen over klanten (creditwaardigheid, belastingaangifte), is het mogelijk hoog-risico onder de AI Act.

**Met lokale AI:** anomaliedetectie op eigen data, zonder dat gevoelige financiële patronen van klanten naar een externe server gaan.

---

## Het concrete risico bij cloud AI

Laten we het scenario schetsen dat een accountant zou moeten vrezen.

**Het scenario:**
Een accountant van 6 personen gebruikt ChatGPT Team om bankafschriften te categoriseren. Hij kopieert de transacties in de chat en vraagt: "categoriseer deze transacties voor mijn boekhoudsoftware."

**Wat er juridisch gebeurt:**
1. De bankafschriften van zijn klant — persoonsgegevens — worden overgedragen aan OpenAI als verwerker.
2. Er is geen DPA getekend met OpenAI specifiek voor deze verwerking (de standaard ChatGPT Team DPA dekt dit mogelijk niet expliciet).
3. De data staat op servers in de VS, onderworpen aan de CLOUD Act.
4. Het ITAA-beroepsgeheim is mogelijk geschonden.
5. Als de klant ooit vraagt "heeft u mijn bankdata gedeeld met derden?" — het antwoord is ja.

**Wat er kan gebeuren:**
- Een klant klaagt bij het ITAA over schending van beroepsgeheim
- De GBA ontvangt een melding over GDPR-schending
- In het slechtste geval: een datalek bij OpenAI waarbij de financiële data van de klant uitlekt

**De kans dat dit morgen gebeurt:** klein. De kans dat het juridische landschap de komende twee jaar strenger wordt en dit soort gebruik steeds risicovoller maakt: groot.

---

## Wat lokale AI oplost

**De architecturale oplossing:**
Een mini-PC op het kantoor. Ollama draait lokaal. Een open-weight model — Llama 3.3, Mistral, of een fine-tuned fiscaal model — verwerkt de data.

**Wat er juridisch verandert:**
- Geen overdracht aan een derde partij: de data verlaat het kantoor niet
- Geen DPA nodig voor de AI-component: geen externe verwerker
- Beroepsgeheim intact: de data wordt verwerkt door de accountant zelf, op zijn eigen hardware
- GDPR compliant by architecture: geen cross-border datatransfer, geen externe logging

**Wat er praktisch verandert:**
- Zelfde functionaliteit als cloud AI voor de meeste taken
- Geen per-token kosten: na de hardware-investering zijn de marginale kosten nul
- Werkt offline: geen internetafhankelijkheid voor vertrouwelijke verwerking
- Volledige controle over welke modelversie draait

---

## De kernboodschap voor het eerste gesprek

Niet beginnen met technologie. Beginnen met het beroepsgeheim.

> "U heeft beroepsgeheim. Dat is niet alleen een ethische verplichting — het is wettelijk afdwingbaar. Als u vandaag bankafschriften van uw klanten verwerkt via een cloud AI-tool, verlaat die data uw kantoor. Dat is een spanning met uw beroepsgeheim die u moet kennen en waarover u een bewuste keuze moet maken."

Vervolg als ze doorvragen:

> "Lokale AI lost dit architectureel op. De data verlaat het kantoor niet. Uw beroepsgeheim is niet in het geding. En de functionaliteit — transactieclassificatie, rapportgeneratie, fiscale vragen — is vergelijkbaar met wat cloud AI biedt."

---

## Vragen die ze stellen en hoe je antwoordt

**"Maar ik heb toch een DPA met mijn cloudprovider?"**

Een DPA regelt de juridische relatie maar garandeert niets technisch. U kunt niet controleren of de provider de afspraken nakomt. Bij lokale AI is er geen externe provider — u bent de enige verwerkingsverantwoordelijke.

**"Is het niet veel duurder?"**

Hardware is een eenmalige investering van €2.300-€3.500. Geen maandelijkse abonnementen, geen per-token kosten. Over een 3-5 jaar periode is lokale AI typisch goedkoper dan een equivalent cloud-abonnement — zeker als u de compliance-overhead meeneeemt.

**"Zijn lokale modellen niet minder goed dan ChatGPT?"**

Voor de meeste boekhoudkundige taken — transactieclassificatie, rapportgeneratie, fiscale vraagbeantwoording — presteren moderne 70B-parameter modellen vergelijkbaar met GPT-4. Voor het lezen van de nieuwste belastingcirculaires heeft u altijd een menselijke specialist nodig. Dat verandert niet.

**"Wat als het stukgaat?"**

Lokale systemen zijn onderhoudbaar. De software is stabiel. Als er iets is, is er een service-contract. En: als uw cloudprovider morgen een storing heeft, staat u ook stil. Lokale AI werkt offline.

**"Moet ik mijn medewerkers dan opnieuw opleiden?"**

De interface lijkt op ChatGPT. De leercurve is minimaal. Wat verandert is het beleid: welke data mag door de AI, welke niet. Dat is een halve dag training.

**"Wat zegt het ITAA hierover?"**

Het ITAA heeft nog geen specifieke richtlijnen uitgebracht over AI-gebruik en beroepsgeheim. Dat betekent niet dat het geen risico is — het betekent dat de verantwoordelijkheid bij u ligt. Lokale AI is de meest conservatieve en verdedigbare keuze.

---

## Timing en urgentie

**December 2027** is de verwachte nieuwe deadline voor AI Act-naleving voor hoog-risico systemen (EP-commissiestemming 18 maart 2026, plenaire stemming 26 maart verwacht). De urgentie blijft — wie wacht tot 2027 verliest anderhalf jaar voorbereiding.

Het sterkste argument is het beroepsgeheim — en dat geldt nu al.

Elke dag dat een accountant cloud AI gebruikt voor vertrouwelijke klantdata is een dag waarop zijn beroepsgeheim potentieel in het geding is. Dat is geen toekomstig risico. Dat is het heden.

De AI Act voegt daar urgentie aan toe voor de accountants die AI gebruiken voor taken die hoog-risico kunnen zijn. Maar het beroepsgeheim-argument werkt ongeacht de AI Act.

---

## Belgische en Nederlandse context

### België

**ITAA** — Instituut van de Accountants en de Belastingconsulenten. Beroepsregulering voor erkende boekhouders en accountants. Beroepsgeheim verankerd in de ITAA-wet.

**GBA** — Gegevensbeschermingsautoriteit. Toezicht op GDPR in België. Actief in het behandelen van klachten en het uitvaardigen van aanbevelingen.

**Relevante btw-software:** Isabel, Winbooks, Wolters Kluwer, Exact, Silverfin. Veel van deze systemen zijn cloud-gebaseerd. De accountant moet voor elk systeem een DPA hebben.

### Nederland

**NBA** — Nederlandse Beroepsorganisatie van Accountants. Regulering voor RA's en AA's [4]. Vergelijkbaar beroepsgeheim als ITAA.

**AFM** — Autoriteit Financiële Markten. Toezicht op de accountancysector. Actief op het gebied van kwaliteit en onafhankelijkheid.

**Relevante software:** Exact, AFAS, Twinfield, SnelStart. Zelfde DPA-verplichting als in België.

---

## Sectorcijfers (referentie)

- Aantal erkende boekhouders en accountants in België (ITAA): circa 17.000
- Aantal accountantskantoren in Nederland (NBA): circa 5.000 kantoren
- Geschatte markt Benelux voor lokale AI in accountancy: nog niet gekwantificeerd maar substantieel
- Gemiddelde tijdsbesparing AI voor transactieclassificatie: 40-60% van manuele verwerkingstijd (industry estimate)

---

## Bronnen

1. **ITAA-wet 17 maart 2019, Art. 58 — Beroepsgeheim**  
   Wet betreffende de beroepen van accountant en belastingadviseur, Belgische staatsblad / FOD Economie  
   <https://economie.fgov.be/nl/legislation/wet-van-17-maart-2019>

2. **GDPR — Verordening (EU) 2016/679, Art. 6(b) — Verwerkingsgrondslag**  
   EUR-Lex, Publicatieblad van de Europese Unie  
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng>

3. **DORA — Verordening (EU) 2022/2554 — Digitale operationele weerbaarheid**  
   EUR-Lex, Publicatieblad van de Europese Unie  
   <https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng>

4. **NBA — Verordening gedrags- en beroepsregels accountants (VGBA)**  
   Koninklijke Nederlandse Beroepsorganisatie van Accountants  
   <https://www.nba.nl/regelgeving>

---

_Onderdeel van: LocAI Bibliotheek · Sectordossiers_
_Volgende: S02 — Therapeuten & Psychologen_
_Laatste update: 25 maart 2026_
