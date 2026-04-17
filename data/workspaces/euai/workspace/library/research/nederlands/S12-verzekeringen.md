# S12 — Verzekeringsmakelaars
### LocAI Bibliotheek · Sectordossier
_Versie 0.1 · 25 maart 2026_

---

## Wie zijn ze

Verzekeringsmakelaars zijn onafhankelijke tussenpersonen die in opdracht van hun cliënten de beste verzekeringsoplossingen zoeken bij diverse maatschappijen. Ze zijn geen agenten van één verzekeraar — ze werken voor de cliënt. Dat maakt hun positie bijzonder: ze verwerken uitgebreide persoonlijke en financiële informatie in een relatie van vertrouwen, en ze dragen een zorgplicht die in wetgeving is verankerd.

De sector loopt qua databescherming ver voor op het gemiddelde kmo. Verzekeraars en makelaars zijn al jaren gewend aan strenge regulering via FSMA (BE) en AFM/DNB (NL), sectorale gedragsregels, en bijzondere gegevens in de zin van de GDPR. Maar de echte uitdaging is AI: premieberekening, claimsbeoordeling en cliëntadvies worden steeds vaker ondersteund door systemen die al dan niet hoog-risico zijn onder de AI Act.

**Typisch profiel:**
- Onafhankelijke verzekeringskantoren — gezin, voertuig, brand, aansprakelijkheid
- Gespecialiseerde makelaars — leven, pensioen, inkomensverzekering
- Vergelijkingskantoren en -platformen — multi-verzekeraar, online of hybride
- Corporate brokers — beroepsaansprakelijkheid, krediet, export, grote risico’s

**Wat hen onderscheidt:** makelaars beschikken over een combinatie van financiële profielen, schadehistorie én gezondheidsinformatie. Die combinatie maakt hun dataverwerkingsrisico fundamenteel anders dan bij de meeste andere sectoren. Gezondheidsvragen op levensverzekeringen vallen onder artikel 9 van de GDPR — de zwaarste categorie bijzondere persoonsgegevens.

---

## Welke data verwerken ze

**Cliëntdata:**
- Persoonsgegevens — naam, adres, geboortedatum, rijksregisternummer (BE) / BSN (NL)
- Financiël profiel — inkomen, vermogen, schulden, gezinssituatie
- Polis- en productgegevens — lopende verzekeringen, premiegeschiedenis, dekkingen
- Schadehistorie — eerdere claims, afwijzingen, frauderegistraties

**Bijzondere persoonsgegevens (Art. 9 GDPR):**
- Gezondheidsinformatie op levensverzekeringen en hospitalisatieverzekeringen — medische voorgeschiedenis, aandoeningen, medicatiegebruik
- Invaliditeits- en arbeidsongeschiktheidsstatus
- In sommige niches: genetische data voor specifieke risicobeoordeling

**Bedrijfsdata (zakelijke portefeuille):**
- Jaarrekeningen en financiële rapportages van zakelijke cliënten
- Risicoadressen en verzekerbare objecten
- Bedrijfsspecifieke blootstellingen — productaansprakelijkheid, beroepsrisico’s, cyberrisico

**Compliance- en AML-data:**
- KYC-documenten (know your customer) — identiteitsbewijzen, herkomst middelen
- FATF-screenings en PEP-checks (politiek prominente personen)
- Transactieregistraties voor witwaspreventie

**Wat dit specifiek maakt:** het is de combinatie die het risico vergroot. Een financiël profiel is gevoelig. Schadehistorie is gevoelig. Gezondheidsinformatie is artikel 9 — de zwaarste categorie. Wanneer alle drie op één cliëntdossier staan en worden geanalyseerd door een — al dan niet lokale — AI, is een grondig privacydossier geen optionele extra.

---

## Welke wetten zijn van toepassing

### GDPR — Artikel 9 en de gezondheidsvraag

Gezondheidsinformatie is bijzondere persoonsgegevens onder artikel 9 van de GDPR [1]. De verwerking ervan is in principe verboden, tenzij een uitdrukkelijke uitzondering van toepassing is. Voor verzekeringsmakelaars is de belangrijkste uitzondering artikel 9, lid 2, sub b: verwerking noodzakelijk voor uitvoering van verplichtingen en de uitoefening van rechten op het gebied van arbeids-, sociale zekerheids- en socialebeschermingsrecht — of, voor levens- en inkomensverzekeringen: artikel 9, lid 2, sub a (uitdrukkelijke toestemming van de betrokkene).

**Praktisch:** cliënten die een antwoord invullen op een medische vragenlijst voor een levensverzekering, verlenen toestemming voor die specifieke verwerkingsactiviteit. Die toestemming is niet automatisch overdraagbaar aan een AI-systeem dat datzelfde antwoord gebruikt om premies te berekenen of risico’s te modelleren bij een derde partij.

### AI Act — Risicoclassificatie voor verzekeringsAI

Al dan niet hoog-risico, afhankelijk van de toepassing:

- **Hoog-risico (Bijlage III):** AI-systemen die worden gebruikt voor krediet- of verzekeringsbeoordeling van personen, in het bijzonder systemen die bepalen of iemand verzekerd wordt of tegen welke premie [2]. Dit valt onder de categorie “AI-systemen voor het beoordelen van kredietwaardigheid of het beoordelen van en genereren van creditscores” — een categorie die in de praktijk ook op verzekeringsrisicobeoordeling van toepassing is.
- **Beperkt risico:** AI die adviesgesprekken simuleert of documenten genereert maar geen beslissingen neemt over acceptatie of premie.
- **Minimaal risico:** interne administratieve automatisering zonder beslissingsgewicht.

### FSMA — Belgische Autoriteit voor Financiële Diensten en Markten

Verzekeringsmakelaars in België moeten geregistreerd zijn bij de FSMA [3] en voldoen aan de ge dragsregels uit de wet van 4 april 2014 betreffende de verzekeringen en de MiFID-like bepalingen voor financiële producten. De FSMA heeft recent verklaringen gepubliceerd over AI-gebruik in financiële dienstverlening.

### Wft — Wet op het financieel toezicht (Nederland)

In Nederland zijn verzekeringsmakelaars onderworpen aan de Wet op het financieel toezicht (Wft) [4]. Toezicht wordt gehouden door de AFM (gedrag) en DNB (prudentieel). De Wft stelt eisen aan zorgplicht, adviesproces en klantdossierbeheer — die direct raken aan hoe AI-tools in het adviesproces mogen worden ingezet.

### AMLD5 — Antiwitwasrichtlijn

Verzekeringsmakelaars vallen als verplichte entiteiten onder de vijfde antiwitwasrichtlijn [5]. Dat impliceert KYC-verplichtingen, transactiemonitoring bij bijzondere betaalstromen, en documentatieplicht. AI die klantprofielen screent op AML-risico valt potentieel onder de hoog-risico categorie van de AI Act.

### IDD — Insurance Distribution Directive (2016/97)

De IDD [6] regelt de verdeling van verzekeringsproducten in de EU. Ze verplicht makelaars tot transparantie over hun remuneratie, tot een adviesproces dat in het belang van de cliënt is, en tot gepaste productkennis. AI-tools in het adviesproces moeten voldoen aan de IDD-zorgplicht: de tool mag geen advies geven dat niet in het belang van de cliënt is.

---

## Concrete use cases voor AI

### 1. Polisanalyse en gapdetectie

**Wat het is:** AI analyseert het bestaande verzekeringsportefeuille van een cliënt en identificeert dekkinsgaten, overlappingen en mogelijke optimaliseringen.

**Waarde:** makelaars kunnen sneller en grondiger adviseren, cliënten krijgen een genuanceerder beeld van hun risico’s, en de kwaliteit van het adviesproces stijgt.

**Met lokale AI:** het volledige cliëntprofiel — financiël, verzekeringstechnisch, soms inclusief gezondheidsinfo — blijft op het eigen systeem. Geen overdracht naar een cloud-analyseplatform.

---

### 2. Schadebegeleiding en correspondentie

**Wat het is:** AI ondersteunt het schadebegeleidingsproces door correspondentie met verzekeringsmaatschappijen voor te bereiden, statusupdates samen te vatten en cliënten te informeren.

**Waarde:** minder administratieve last voor makelaars, snellere doorlooptijden voor cliënten, betere dossiervorming.

**Met lokale AI:** schadedata bevat naast financiële informatie soms ook medische context (bij invaliditeitsschadevorderingen, gezondheidszorgverzekeringen). Die data verlaat het kantoor niet.

---

### 3. Cliëntadvies en gespreksvoorbereiding

**Wat het is:** AI helpt de makelaar bij de voorbereiding van een adviesgesprek: samenvatting van het dossier, relevante risicofactoren, vragen die gesteld moeten worden, mogelijke productopties.

**Waarde:** betere gespreksvoorbereiding, meer cliëntgerichtheid, consistentere advieskwaliteit over het volledige kantoor.

**Let op IDD:** het adviesproces moet in het belang van de cliënt zijn en gedocumenteerd worden. AI die het advies ingeeft maar niet documenteerbaar is, voldoet niet aan IDD-vereisten.

---

### 4. Compliance- en AML-ondersteuning

**Wat het is:** AI screent nieuw inkomende cliënten op AML-risicoprofielen, trekt relevante informatie samen en genereert een KYC-samenvatting voor de dossierbeheerder.

**Waarde:** snellere onboarding, minder handmatig opzoekwerk, consistent documentatieniveau.

**Let op AI Act:** AML-screeningsystemen vallen potentieel in de hoog-risico categorie. Documentatie- en menselijk-toezicht-vereisten zijn van toepassing.

---

### 5. Documentverwerking en premieoverzichten

**Wat het is:** AI verwerkt inkomende verzekeringsoverzichten, polisdocumenten en premieberichten — haalt kerngegevens eruit en vult het cliëntdossier bij.

**Waarde:** tijdsbesparing op administratief niveau, minder invoerfouten, up-to-date dossiers.

**Met lokale AI:** polisdocumenten bevatten persoonsgegevens van de cliënt en soms financiële data van de verzekeraar. Verwerking via een cloud OCR-dienst is een verwerkersverhouding die contractueel moet worden vastgelegd.

---

## Het concrete risico met cloud-AI

**Het gezondheidsdata-scenario:**

Een levensverzekeringskantoor gebruikt een cloud AI-platform voor cliëntadvies en risicoanalyse.

1. Een cliënt vult een medische vragenlijst in voor een levensverzekeringsofferte. De antwoorden worden samen met het financiïl profiel en de schadehistorie in het AI-platform geladen.
2. De artikle 9-data — gezondheidsinformatie — verlaat zo de beveiligde omgeving van het kantoor en wordt verwerkt op servers van de cloud-aanbieder, potentieel buiten de EU.
3. Het platform traint zijn risicomodellen op geaggregeerde cliëntdata van alle aangesloten makelaars. De gezondheidsinformatie van jouw cliënten draagt bij aan het model van een concurrent.
4. Een cliënt vraagt inzage in hoe zijn gezondheidsinformatie is gebruikt. Jij hebt geen antwoord dat je kunt geven over de verwerkingsketen bij de cloudaanbieder.
5. De GBA of AP stelt een onderzoek in na een klacht. De verwerkersovereenkomst voor het AI-platform dekt de artikel 9-verwerking niet expliciet. Dat is een overtreding.

Lokale verwerking van polisanalyse en cliëntadviezen: artikel 9-data blijft binnen het kantoor, verwerkingsdoeleinden zijn controleerbaar en aantoonbaar, en het adviesproces voldoet aan IDD-documentatieverplichtingen.

---

## De kernboodschap voor het eerste gesprek

Begin bij het bijzondere karakter van de data.

> "Jij verwerkt gezondheidsinformatie. Dat is artikel 9 GDPR — de strengste categorie. Die informatie mag je niet naar een cloud AI-platform sturen zonder expliciete grondslag en een waterdichte verwerkersovereenkomst. En dat doet bijna niemand goed."

Vervolg:

> "Lokale AI verwerkt het cliëntdossier, bereidt adviesgesprekken voor en genereert documentatie — zonder dat gezondheidsdata, financiële profielen of schadehistorie de kantooromgeving verlaten. Dat is de enige architectuur die zowel GDPR artikel 9 als IDD naleving tegelijk ondersteunt."

---

## Vragen die ze stellen en hoe je antwoordt

**"Wij vragen alleen wat de verzekeraar ons vraagt — de verantwoordelijkheid ligt bij hen."**

Nee. Jij vraagt de gezondheidsvragen aan de cliënt. Jij bent daarmee de verwerkingsverantwoordelijke voor die data. De verzekeraar is een afzonderlijke verwerkingsverantwoordelijke voor wat zij ermee doen nadat jij het hen overdraagt. Die twee verwerkingsactiviteiten zijn juridisch gescheiden — jouw verantwoordelijkheid eindigt niet bij overdracht.

**"Onze cliënten geven toestemming op het aanvraagformulier."**

Die toestemming geldt voor de verwerkingsactiviteit die op het formulier beschreven staat — doorgaans het aanvragen van een offerte bij de verzekeraar. Ze dekt niet het laden van die gegevens in een extern AI-analyseplatform. Voor dat gebruik heb je een aparte grondslag en een aparte transparantieplicht.

**"Wij zijn een klein kantoor — die regels zijn toch voor grote spelers?"**

De GDPR kent geen omvangsdrempel voor artikel 9. Zelfs een eenmanskantoor met tien levensverzekeringspolissen verwerkt bijzondere persoonsgegevens en is verplicht tot een expliciete grondslag en adequate beveiliging. De FSMA verwacht dat geregistreerde makelaars hun data governance op orde hebben, ongeacht kantooromvang.

**"Onze AI-tool is toch GDPR-gecertificeerd?"**

GDPR-certificering van een tool zegt iets over de beveiligingsmaatregelen voor data-opslag. Het zegt niets over of jij een geldige verwerkingsgrondslag hebt voor het insturen van artikel 9-data naar die tool. Dat moet jij aantonen — de tool kan dat niet voor jou doen.

**"Kunnen we dan nog wel AI gebruiken?"**

Absoluut. Het gaat erom wáár de AI draait. Een lokaal ingezette AI die op jouw eigen server artikel 9-data verwerkt, met jou als enige verwerkingsverantwoordelijke, is technisch en juridisch solide. De architectuur bepaalt de compliance — niet de technologie.

---

## Belgische en Nederlandse context

### België

**FSMA — Autoriteit voor Financiële Diensten en Markten** [3] is de gedragstoezichthouder voor verzekeraars en makelaars in België. FSMA heeft aandacht voor AI-gebruik in financiële dienstverlening en publiceert circulaires over technologische risico’s.

**Assuralia** [7] is de beroepsvereniging van de Belgische verzekeringsondernemingen. Assuralia publiceert sectorstandaarden, omzetcijfers en beleidsposities — relevant als referentie voor de context waarin makelaars opereren.

**De GBA — Gegevensbeschermingsautoriteit** [8] handhaaft de GDPR in België. De GBA heeft boetes opgelegd in de financiële sector voor inadequate verwerking van bijzondere persoonsgegevens.

### Nederland

**AFM — Autoriteit Financiële Markten** [4] houdt gedragstoezicht op verzekeringsmakelaars. De AFM verwacht dat makelaars de zorgplicht kunnen aantonen, ook wanneer AI-tools worden ingezet in het adviesproces.

**DNB — De Nederlandsche Bank** houdt prudentieel toezicht en publiceert richtlijnen over het gebruik van AI-modellen in de financiële sector.

**Verbond van Verzekeraars** [9] is de brancheorganisatie van Nederlandse verzekeringsmaatschappijen. Hun gedragsregels raken indirect aan de makelaarsmarkt.

---

## Sectorcijfers (referentie)

- Aantal FSMA-geregistreerde verzekeringstussenpersonen in België: ca. 10.500 (FSMA, 2024)
- Aantal bij AFM geregistreerde verzekeringstussenpersonen in Nederland: ca. 5.000 (AFM, 2024)
- Aandeel kantoren met een actieve levensverzekeringsportefeuille: ca. 65%
- Gemiddelde kosten datalek bij financiële dienstverleners: €3,8 miljoen (IBM Cost of Data Breach Report 2024, sector gemiddelde)
- Aandeel datalekken in financiële diensten veroorzaakt door externe cloudproviders: 24% (IBM, 2024)

---

## Bronnen

1. **GDPR — Verordening (EU) 2016/679 (incl. Art. 9 — bijzondere persoonsgegevens)**
   EUR-Lex, volledig geconsolideerde tekst
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj>

2. **AI Act — Verordening (EU) 2024/1689 — Bijlage III (hoog-risico AI-systemen)**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

3. **FSMA — Autoriteit voor Financiële Diensten en Markten**
   <https://www.fsma.be>

4. **Wft / AFM — Wet op het Financieel Toezicht / Autoriteit Financiële Markten**
   <https://www.afm.nl>

5. **AMLD5 — Richtlijn (EU) 2018/843 antiwitwassen**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/dir/2018/843/oj>

6. **IDD — Insurance Distribution Directive (EU) 2016/97**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/dir/2016/97/oj>

7. **Assuralia — Beroepsvereniging van Belgische Verzekeraars**
   <https://www.assuralia.be>

8. **GBA — Gegevensbeschermingsautoriteit**
   <https://www.gegevensbeschermingsautoriteit.be>

9. **Verbond van Verzekeraars (Nederland)**
   <https://www.verzekeraars.nl>

---

_Onderdeel van: LocAI Bibliotheek · Sectordossiers_
_Vorige: S11 — HR & Rekrutering_
_Volgende: S13 — Bouw & Aannemers_
_Laatste update: 25 maart 2026_
