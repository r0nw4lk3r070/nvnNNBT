# S08 — Vastgoedmakelaars
### LocAI Bibliotheek · Sectordossier
_Versie 0.1 · 25 maart 2026_

---

## Wie zijn ze

Vastgoedmakelaars werken dagelijks met de meest persoonlijke en financieel gevoelige informatie die er bestaat: wie iemand is, hoeveel hij heeft, en wat hij wil kopen of verkopen. Toch wordt de sector zelden in één adem genoemd met "dataintensief" of "zwaar gereguleerd" — terwijl makelaars in werkelijkheid onderworpen zijn aan een combinatie van GDPR, antiwitwaswetgeving en beroepsdeontologie die weinig andere kmo-sectoren evenaren.

Een vastgoedkantoor kan klein zijn — één makelaar met een handje medewerkers — maar de transacties die erdoor lopen zijn dat zeker niet. Een residentiële verkoop van drie ton gaat gepaard met identiteitsdocumenten, hypotheekinformatie, biedingshistorie, notariële correspondentie en AML-verificatiedossiers. Dat alles in één dossier, per cliënt, per transactie.

**Typisch profiel:**
- Solo makelaar tot middelgroot kantoor van 5–20 medewerkers
- Residentieel of commercieel vastgoed, soms beide
- Transactiegedreven model — inkomsten per verkoop of verhuur, niet per uur
- Sterk afhankelijk van lokale marktkennis en cliëntenvertrouwen

**Specifieke beroepsgroepen:**
- Residentiële makelaars — aan- en verkoop van woningen en appartementen
- Commercieel vastgoed — kantoren, handelspanden, bedrijfsgebouwen
- Verhuurmakelaars — verhuur van woningen en commercieel vastgoed
- Syndici — beheer van mede-eigendom (VME in België, VvE in Nederland)
- Vastgoedpromotoren — projectontwikkeling en nieuwe bouw

---

## Welke data verwerken ze

**Klantdata:**
- Identiteitsdocumenten — paspoort, identiteitskaart, rijksregisternummer (BE) of BSN (NL)
- Financiële gegevens — budget, beschikbaar eigen vermogen, hypotheekgegevens en lening­capaciteit
- Contactdata — naam, adres, telefoon, e-mail
- Zoekprofiel — locatievoorkeuren, type woning, minimale en maximale criteria
- Bezichtigingshistorie — welke panden bezocht, reacties, beslissingsproces

**Vastgoeddata:**
- Adres, kadastraal nummer, perceeloppervlakte
- Eigendomsdocumenten en eigendomstitels
- Foto's en videomateriaal van het pand
- Prijshistorie en eerdere transactieprijzen
- Taxatierapporten en schattingsverslagen
- Energieattesten (EPC) en technische keuringsrapporten

**Transactiedata:**
- Verkoopprijs en biedingshistorie — inclusief afgewezen biedingen
- Notariële akten en compromissen
- Hypotheekgegevens van de koper
- Sluitingsdatum en opschortende voorwaarden

**AML-data:**
- UBO-gegevens (uiteindelijk begunstigden) bij juridische eigenaars
- Origine van fondsen bij de aankoop
- Cliëntidentificatie en due diligence-dossiers conform AMLD5

**Wat dit specifiek maakt:**
De combinatie van identiteitsgegevens, financiële draagkracht, eigendomsinformatie en AML-documentatie is een van de gevoeligste dataverzamelingen die een kmo-professional kan beheren. Waar een boekhouder enkel financiële data ziet en een huisarts enkel medische data, ziet een vastgoedmakelaar tegelijk wie iemand is, wat hij bezit en hoeveel hij kan besteden. Dat maakt de verwerkingsverantwoordelijkheid van een makelaar zwaarder dan die van veel andere vrije beroepen — en de risico's bij een datalek navenant groter.

---

## Welke wetten zijn van toepassing

### GDPR — Cliëntprofielen, transactiedata en identiteitsverificatie

Makelaars verwerken identiteitsbewijzen, financiële data en transactiegegevens — bijzondere zorgvuldigheid is vereist bij elke stap in dat proces [1]. De GDPR legt meerdere verplichtingen op die in de dagelijkse praktijk van een vastgoedkantoor concreet voelbaar zijn.

**Doelbinding:** data verzameld voor een specifieke transactie mag niet zomaar worden hergebruikt voor andere doeleinden, zoals marketingcampagnes of het opbouwen van een uitgebreid cliëntenprofiel voor toekomstige zaken. Voor elk nieuw verwerkingsdoel is ofwel een nieuwe rechtsgrond ofwel een nieuwe toestemming vereist.

**Bewaartermijnen:** identiteitsdocumenten die verzameld zijn voor een transactie mogen niet onbeperkt worden bewaard. De boekhoudkundige bewaarplicht (7 jaar) geldt voor financiële documenten, maar marketingprofielen kennen een kortere termijn. Het bijzondere geval bij makelaars is de spanning met AML-verplichtingen: antiwitwaswetgeving vereist dat identiteitsverificatiedossiers vijf jaar na het einde van de zakelijke relatie worden bewaard — een termijn die kan botsen met de GDPR-principes van dataminimalisatie als ze niet goed gedocumenteerd is.

**Verwerkersovereenkomsten:** elke cloud-CRM, elk digitaal dossiersysteem of elk AI-platform dat cliëntdata verwerkt namens het kantoor, is een verwerker in de zin van de GDPR. Een geldig verwerkersovereenkomst is verplicht — en de makelaar blijft als verwerkingsverantwoordelijke aansprakelijk voor wat die verwerker doet met de data.

### AMLD5 — Antiwitwasverplichting voor makelaars

Makelaars zijn meldingsplichtige entiteiten onder de vijfde anti-witwasrichtlijn (Richtlijn (EU) 2018/843) [2]. Dat is geen administratieve formaliteit — het is een wettelijke verplichting met strafrechtelijke gevolgen bij niet-naleving.

Concreet moeten makelaars: cliëntidentificatie uitvoeren (CDD — Customer Due Diligence) voor elke nieuwe zakelijke relatie, cliënten screenen tegen sanctielijsten en lijsten van politiek prominente personen (PEP's), de uiteindelijk begunstigden (UBO's) identificeren wanneer de koper of verkoper een rechtspersoon is, en verdachte transacties melden aan de bevoegde autoriteit — de CFI (Cel voor Financiële Informatieverwerking) in België [6] en de FIU-Nederland [7].

Dit creëert een bijzondere uitdaging voor gegevensbeheer: de AML-wetgeving verplicht actieve retentie van identiteitsverificatiedossiers, terwijl de GDPR vraagt om terughoudendheid met persoonsdata. Die spanning is beheersbaar — maar alleen als het kantoor een gedocumenteerd retentiebeleid heeft dat beide wettelijke regimes in evenwicht brengt. Die verplichting kan niet worden uitbesteed zonder een correcte verwerkersovereenkomst: als de AML-dossiers bij een externe cloud-dienst liggen, draagt het kantoor nog steeds de volledige verantwoordelijkheid.

### AI Act — Geautomatiseerde waarderingsmodellen (AVM)

Geautomatiseerde waarderingsmodellen — AI-systemen die vastgoedprijzen berekenen op basis van kenmerken, locatie en vergelijkbare transacties — kunnen als hoog-risico worden beschouwd onder Bijlage III van de AI Act [3] wanneer ze worden ingezet in de context van kredietbeslissingen, zoals hypotheekevaluaties door banken of kredietinstellingen.

Voor makelaars die AVM's intern gebruiken als adviesinstrument voor prijsbepaling is het risiconiveau lager. Toch gelden ook voor hen transparantieverplichtingen: wanneer een AI-systeem een invloed heeft op de prijs die aan een cliënt wordt gecommuniceerd, moet die invloed kenbaar zijn en moet er een menselijke beoordeling bovenop liggen.

Daarnaast gelden de professionele normen van het BIV [4] in België en de NVM [5] in Nederland, waarvan de deontologische codes rechtstreeks raken aan transparantie over waarderingsmethoden en informatieplicht tegenover cliënten. Een makelaar die een AI-gestuurd waarderapport aflevert zonder dat te vermelden, riskeert zowel tuchtrechtelijke als GDPR-gerelateerde problemen.

---

## Concrete use cases voor AI

### 1. Geautomatiseerde vastgoedwaardering (AVM)

**Wat het is:** AI schat de marktwaarde van een pand op basis van het adres, de kenmerken (oppervlakte, type, bouwjaar, staat), vergelijkbare transacties in de buurt en marktevolutie over tijd.

**Waarde:** snellere waarderingsadviezen, objectieve prijsinput voor verkoopgesprekken, minder afhankelijkheid van subjectieve "buikgevoel"-prijsbepaling.

**Met lokale AI:** jouw database van vergelijkbare transacties, jouw lokale marktkennis en jouw historische verkoopprijzen blijven op jouw eigen server. Een cloud AVM-platform voedt zijn model met data van alle aangesloten kantoren — inclusief jouw concurrenten. Jouw prijskennis is jouw concurrentievoordeel; dat hoort niet in een gedeeld model thuis.

---

### 2. Cliëntmatching

**Wat het is:** AI koppelt zoekprofielen van kopers aan het beschikbare aanbod op basis van locatievoorkeuren, budget, woningtype, specifieke criteria en gedragspatronen uit eerdere bezichtigingen.

**Waarde:** snellere matches, hogere conversie, minder tijdverlies op bezichtigingen die bij voorbaat geen match zijn.

**Met lokale AI:** jouw kopersdatabase bevat financiële informatie, hypotheekcapaciteit en persoonlijke zoekvoorkeuren — bijzonder gevoelige data. Die verwerking hoort in een gecontroleerde omgeving, niet op servers van een extern platform.

---

### 3. Marktanalyse en rapportage

**Wat het is:** AI genereert marktanalyses, prijsevolutierapporten en buurtanalyses op basis van historische transactiedata en actuele marktinformatie.

**Waarde:** professionele cliëntenrapporten en marktpresentaties in minuten in plaats van uren. Sterkere positie in verkoopgesprekken met eigenaars die willen weten wat hun pand waard is.

**Met lokale AI:** jouw lokale marktintelligentie — wat er verkocht is, aan welke prijs, hoe snel, in welke staat — is de kern van jouw concurrentiepositie als lokale expert. Dat is precies het soort informatie dat je niet wilt delen met een platform dat ook je concurrent bedient.

---

### 4. Contractassistentie

**Wat het is:** AI helpt bij het opstellen of nalezen van verkoopovereenkomsten, huurcontracten, verhuuropdrachten en mandaten — structuurcontrole, ontbrekende clausules signaleren, standaardformulering voorstellen.

**Waarde:** tijdsbesparing bij routinedocumenten, minder kans op vergeten clausules, snellere doorlooptijd van dossiers.

**Met lokale AI:** transactiedata en cliënt­identiteitsgegevens worden verwerkt tijdens het opstellen van contracten — dat gebeurt op jouw eigen server, zonder dat een extern AI-model die informatie verwerkt of opslaat. Juridische review door een notaris of advocaat blijft altijd vereist.

---

### 5. AML-screening

**Wat het is:** AI screent cliënten systematisch tegen sanctielijsten, PEP-registers (Politically Exposed Persons) en andere risico-indicatoren als onderdeel van de AMLD5-verplichting tot cliëntidentificatie.

**Waarde:** snellere en volledigere due diligence, gedocumenteerde compliance, minder risico op het inadvertent onboarden van gesanctioneerde personen of entiteiten.

**Opgelet AI Act:** als de screening automatisch cliënten weigert of markeert zonder menselijk toezicht, is dat problematisch. AML-beslissingen — het al dan niet aangaan van een zakelijke relatie of het doen van een melding — vereisen altijd een menselijke beoordeling. AI is hier een hulpmiddel voor screening, niet een besluitvormend systeem. Bovendien is AML-screeningdata buitengewoon gevoelig: deze verwerking dient in een strikt gecontroleerde omgeving te gebeuren, met volledige audittrail.

---

## Het concrete risico met cloud-AI

**Het CRM-scenario:**

Een vastgoedkantoor centraliseert alle cliëntdossiers in een cloud-CRM met geïntegreerde AI-functies voor matching en rapportage. Comfortabel, overzichtelijk — en juridisch een mijnenveld.

1. Elk cliëntdossier — scan van identiteitskaart of paspoort, financiële situatie, hypotheekcapaciteit, persoonlijke zoekvoorkeuren — staat op servers in de Verenigde Staten of een andere derde jurisdictie buiten de EU.
2. De AI van het platform gebruikt die data om zijn aanbevelings- en matchingmodellen te verfijnen — op basis van de gecombineerde data van alle aangesloten kantoren.
3. Onder AMLD5 moeten identiteitsverificatiedossiers vijf jaar bewaard en auditeerbaar zijn — maar het kantoor heeft geen controle over hoe de data bij de cloudprovider wordt opgeslagen, geback-upt of verwijderd.
4. Een datalek bij de cloudprovider stelt niet alleen contactgegevens bloot, maar volledige identiteits- en financiële profielen van kopers en verkopers — inclusief de AML-dossiers.
5. De makelaar is de verwerkingsverantwoordelijke. De aansprakelijkheid, de meldingsplicht bij de toezichthouder, de eventuele boetes — die liggen volledig bij het kantoor, niet bij de cloudprovider.

De lokale AI-aanpak: cliëntprofielen, transactiedata en AML-dossiers op een eigen server, met volledige controle over retentie, toegang en audittrails — en zonder dat die data bijdraagt aan een gedeeld model elders.

---

## De kernboodschap voor het eerste gesprek

Begin niet bij AMLD5 of GDPR. Begin bij het concurrentievoordeel.

> "Jouw lokale marktkennis — welke panden er verkopen, aan welke prijs, hoe snel, aan wat voor kopers — is het meest waardevolle wat jouw kantoor heeft. Als je die data verwerkt via een cloud AI-platform, voedt je daarmee een model dat ook alle andere kantoren op dat platform ten goede komt. Jouw inzicht wordt gedeeld inzicht."

Vervolg:

> "Lokale AI maakt van diezelfde marktkennis een exclusief voordeel. Waarderingen, matchings, marktanalyses — allemaal op basis van jouw transacties, jouw cliënten, op jouw server. Niet elders."

---

## Vragen die ze stellen en hoe je antwoordt

**"Ik gebruik al een cloud-CRM — Salesforce, HubSpot, of een vastgoedspecifiek platform. Moet ik dat weggooien?"**

Nee. De vraag is niet welke tool je gebruikt, maar welke data erin zit en wat er met die data gebeurt. Een cloud-CRM voor contactbeheer is iets anders dan AI-verwerking van identiteitsdocumenten en financiële profielen. Je kunt de twee combineren: lichte contactdata in je bestaande platform, gevoelige dossierdata en AI-verwerking in een lokale omgeving. De architectuur bepaalt het risico, niet het merk van de tool.

**"Mijn AML-softwareleverancier zorgt voor compliance — dat is hun probleem, niet het mijne."**

Dat is een misverstand dat makelaars duur kan komen te staan. Jij bent als meldingsplichtige entiteit de verwerkingsverantwoordelijke. Je leverancier is een verwerker. Als die leverancier een datalek heeft, als zijn retentiebeleid niet klopt, of als zijn servers buiten de EU staan zonder adequaatheidsbesluit — de aansprakelijkheid ligt bij jou. Een verwerkersovereenkomst is verplicht, en die overeenkomst vermindert de aansprakelijkheid niet, ze documenteert de verantwoordelijkheidsverdeling.

**"Is lokale AI niet veel te duur voor een kantoor van mijn omvang?"**

De instapkosten voor lokale AI zijn de afgelopen twee jaar sterk gedaald. Voor een klein tot middelgroot kantoor is een adequate lokale omgeving realistisch haalbaar voor een investering die vergelijkbaar is met de jaarlijkse abonnementskosten van een cloud-CRM — zonder de doorlopende datarisico's. Stel die kosten af tegen de gemiddelde kostprijs van een datalek voor een kmo: €15.000 tot €50.000, exclusief reputatieschade [sectorcijfers].

**"Mijn cliënten vertrouwen mij — ze zullen echt geen klacht indienen over data."**

Vertrouwen beschermt niet tegen een datalek bij een derde partij. Als jouw cloudprovider gehackt wordt, bepaalt niet jouw relatie met de cliënt de gevolgen — dan bepalen de GBA of de AP, en de AMLD5-toezichthouders, wat er moet gebeuren. Meldplicht bij een datalek is wettelijk verplicht en onafhankelijk van de cliëntrelatie.

**"Wat is het verschil tussen een cloud AI-assistent gebruiken voor een e-mail en het verwerken van cliëntdata?"**

Dat is precies de juiste vraag. Een generieke AI gebruiken om een prospectiemail te herschrijven is fundamenteel anders dan een cliëntdossier met identiteitsgegevens en financiële informatie invoeren in een cloud-AI-tool. In het eerste geval verwerk je geen persoonsdata. In het tweede geval ben je een verwerker die data overdraagt aan een derde partij — met alle GDPR-verplichtingen van dien. Die grens is in de dagelijkse praktijk gemakkelijk te overschrijden; bewustzijn ervan is de eerste stap.

---

## Belgische en Nederlandse context

### België

**BIV — Beroepsinstituut van Vastgoedmakelaars** [4]. Erkend zijn bij het BIV is wettelijk verplicht om als makelaar te mogen optreden in België. Het BIV hanteert een deontologische code die onder meer verplichtingen oplegt rond cliëntenvertrouwelijkheid, informatieverstrekking en professionele zorgvuldigheid — verplichtingen die rechtstreeks raken aan hoe cliëntdata mag worden verwerkt en bewaard.

**CFI — Cel voor Financiële Informatieverwerking** [6] is de Belgische AML-meldingsautoriteit voor vastgoedmakelaars. Makelaars zijn verplicht verdachte transacties te melden aan de CFI. De CFI heeft richtlijnen gepubliceerd over de toepassing van AMLD5 in de vastgoedsector, inclusief specificaties over welke transacties bijzondere aandacht verdienen.

**Notaris:** in België speelt de notaris een centrale rol bij vastgoedtransacties — hij staat in voor de eigendomsoverdracht en de authenticatie van de akte. De makelaar en de notaris zijn gezamenlijk verantwoordelijk voor een correcte identificatie van partijen, maar elk vanuit hun eigen wettelijk kader.

### Nederland

**NVM — Nederlandse Vereniging van Makelaars** [5] is de grootste beroepsvereniging voor makelaars in Nederland, met circa 4.500 aangesloten kantoren. Naast de NVM zijn VastgoedPRO en VBO Makelaar actieve beroepsverenigingen. Aansluiting bij een beroepsvereniging is in Nederland niet wettelijk verplicht, maar in de praktijk een marktstandaard voor erkende makelaars.

**FIU-Nederland — Financial Intelligence Unit** [7] ontvangt AML-meldingen van Nederlandse makelaars. Het aantal meldingen vanuit de vastgoedsector stijgt jaar op jaar, wat de sector onder toenemend toezicht plaatst.

**Notaris:** in Nederland is de rol van de notaris bij vastgoedtransacties wettelijk verankerd — de eigendomsoverdracht verloopt via de notariële akte en inschrijving in het Kadaster. De makelaar faciliteert de transactie; de notaris formaliseert ze. Beide partijen verwerken gevoelige cliëntdata in hetzelfde dossier, wat afstemming over verwerkersverantwoordelijkheden vereist.

---

## Sectorcijfers (referentie)

- Aantal erkende makelaars BIV (België): ca. 12.000 (2024) [4]
- Aantal NVM-leden (Nederland): ca. 4.500 kantoren [5]
- Gemiddelde transactiewaarde residentieel vastgoed BE (2024): ca. €300.000
- Gemiddelde transactiewaarde residentieel vastgoed NL (2024): ca. €435.000
- AML-meldingen vastgoedsector aan FIU-Nederland 2023: in stijgende lijn [7]
- Gemiddelde kosten datalek kmo: €15.000–50.000 (IBM Cost of Data Breach Report 2024, gecorrigeerd voor kmo-schaal)

---

## Bronnen

1. **GDPR — Verordening (EU) 2016/679**
   EUR-Lex, volledig geconsolideerde tekst
   <https://eur-lex.europa.eu/eli/reg/2016/679/oj/nld>

2. **AMLD5 — Richtlijn (EU) 2018/843 — Antiwitwas (vijfde richtlijn)**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/dir/2018/843/oj>

3. **AI Act — Verordening (EU) 2024/1689 — Risicoklassificatie en bijlage III**
   EUR-Lex
   <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

4. **BIV — Beroepsinstituut van Vastgoedmakelaars**
   <https://www.biv.be>

5. **NVM — Nederlandse Vereniging van Makelaars**
   <https://www.nvm.nl>

6. **CFI — Cel voor Financiële Informatieverwerking (AML meldpunt België)**
   <https://www.ctif-cfi.be>

7. **FIU-Nederland — Financial Intelligence Unit**
   <https://www.fiu-nederland.nl>

---

_Onderdeel van: LocAI Bibliotheek · Sectordossiers_
_Vorige: S07 — Kappers & Beauty_
_Volgende: S09 — Non-profit & Vzw_
_Laatste update: 25 maart 2026_
