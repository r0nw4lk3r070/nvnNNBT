# 04 — Data Act
### LocAI Bibliotheek · Diepgang
_Verordening (EU) 2023/2854 · Van kracht 12 september 2025_
_Versie 0.1 · maart 2026_

---

## Wat dit document is

De Data Act is de meest recente grote Europese datawet. Ze is minder bekend dan GDPR of de AI Act, maar ze heeft directe consequenties voor organisaties die willen migreren van cloud naar lokale oplossingen. Dit document volgt dezelfde structuur: letterlijke tekst, vertaling, implicatie.

---

## De kern in één zin

De Data Act geeft gebruikers het recht hun data te controleren, op te vragen en over te dragen — en verbiedt cloudproviders om dat te verhinderen of te bemoeilijken.

---

## Deel 1 — Waarom de Data Act bestaat

Drie problemen die de Data Act wil oplossen.

**Probleem 1 — Data gegenereerd door apparaten blijft bij de fabrikant.**
Je koopt een slimme thermostaat. Die genereert waardevolle data over jouw energieverbruik. Maar die data gaat automatisch naar de fabrikant — niet naar jou. De Data Act geeft jou als gebruiker het recht op die data.

**Probleem 2 — Overstappen van cloud is kunstmatig moeilijk.**
Een bedrijf dat wil migreren van AWS naar Azure, of van een cloud naar lokale infrastructuur, stuit op technische belemmeringen en financiële drempels. Providers hebben er belang bij dat je blijft. De Data Act verbiedt overstapbelemmeringen.

**Probleem 3 — Overheidsinstanties kunnen in noodgevallen geen data opvragen.**
Bij rampen of publieke noodsituaties hebben overheidsinstanties soms data nodig die privébedrijven bezitten. De Data Act creëert een rechtskader voor dergelijke uitzonderlijke toegang.

---

## Deel 2 — Voor wie geldt de Data Act?

De Data Act heeft een brede scope maar kent verschillende verplichtingen voor verschillende partijen.

**Fabrikanten van verbonden producten en aanbieders van gerelateerde diensten:**
Alles wat data genereert en verbonden is met het internet. Slimme apparaten, IoT-sensoren, industriële machines, medische apparatuur, voertuigen.

**Aanbieders van dataverwerkingsdiensten:**
Cloudproviders, datacenters, SaaS-aanbieders. Dit is de categorie die het meest relevant is voor de migratie naar lokale AI.

**Zakelijke gebruikers van verbonden producten:**
Bedrijven die verbonden producten gebruiken en data willen opvragen die door die producten gegenereerd wordt.

**Overheidsinstanties:**
In uitzonderlijke omstandigheden kunnen zij data opvragen bij bedrijven.

---

## Deel 3 — Recht op toegang tot data (Art. 4-6)

### De letterlijke tekst (Art. 4 lid 1)

> "Fabrikanten van verbonden producten zorgen ervoor dat gebruikers gemakkelijk, veilig en, indien van toepassing, rechtstreeks toegang kunnen krijgen tot de gegevens die door het verbonden product worden gegenereerd."

En (Art. 5 lid 1):

> "Op verzoek van een gebruiker stelt de houder van gegevens de gegevens onverwijld, gratis, in het gevraagde formaat en, indien dat technisch haalbaar is, continu en in real time ter beschikking aan een derde."

### De vertaling

Als gebruiker van een verbonden product of dienst heb je het recht op de data die jouw gebruik genereert. Gratis. In een bruikbaar formaat. Zonder onnodige vertraging.

Dit geldt ook voor bedrijven die SaaS-diensten gebruiken: de data die jij genereert binnen een cloudapplicatie is van jou. Je kunt die opvragen en overdragen aan een andere dienst.

### De implicatie voor lokale AI versus cloud AI

Dit artikel is de juridische basis voor data-export uit cloud AI-diensten. Als je jarenlang conversaties, documenten en analyses hebt opgeslagen in een cloud AI-platform, heb je het recht die data op te vragen en mee te nemen.

In de praktijk: voordat je migreert naar lokale AI, kun je een beroep doen op de Data Act om je historische data te exporteren.

---

## Deel 4 — Verbod op overstapbelemmeringen (Art. 23-31)

Dit is het meest directe artikel voor organisaties die willen migreren naar lokale AI.

### De letterlijke tekst (Art. 25 lid 1)

> "Aanbieders van dataverwerkingsdiensten nemen alle redelijke maatregelen om de overstap door klanten naar een andere aanbieder van dataverwerkingsdiensten te vergemakkelijken."

En (Art. 25 lid 2):

> "Aanbieders van dataverwerkingsdiensten leggen klanten geen commerciële, technische, contractuele of organisatorische belemmeringen op die het overstappen verhinderen of ontmoedigen."

### De letterlijke tekst (Art. 29 — afschaffing overstapkosten)

> "Aanbieders van dataverwerkingsdiensten brengen klanten geen kosten in rekening voor het overstapproces."

Met een overgangsperiode: dit verbod geldt volledig vanaf **12 januari 2027**.

### De vertaling

Cloudproviders mogen het je niet moeilijk maken om te vertrekken. Geen contractuele lock-in die migratie verbiedt. Geen technische belemmeringen die export onmogelijk maken. En vanaf januari 2027: geen kosten voor het overstapproces.

In de praktijk vandaag: sommige providers rekenen aanzienlijke "egress fees" voor het downloaden van je eigen data. Dat mag straks niet meer.

### De implicatie voor lokale AI versus cloud AI

Dit is de wettelijke rugdekking voor de migratie naar lokale AI.

Als een organisatie besluit te migreren van cloud AI naar lokale deployment, heeft ze het juridische recht om:
- Alle data te exporteren in een bruikbaar formaat
- Dat gratis te doen (vanaf januari 2027)
- Te verwachten dat de provider technisch meewerkt aan de migratie

De Data Act maakt de exit uit de cloud niet alleen mogelijk maar juridisch afdwingbaar.

---

## Deel 5 — Functionele gelijkwaardigheid (Art. 26)

### De letterlijke tekst

> "Aanbieders van dataverwerkingsdiensten zetten zich in voor functionele gelijkwaardigheid na overstap, door ervoor te zorgen dat de doeldienst ten minste het functionele niveau biedt dat de brondienst bood."

### De vertaling

Een cloudprovider moet actief meewerken om ervoor te zorgen dat je na de overstap dezelfde functionaliteit hebt. Ze mogen de migratie niet saboteren door bepaalde functies niet te ondersteunen of data in een onbruikbaar formaat aan te leveren.

### De implicatie voor lokale AI versus cloud AI

Dit artikel beschermt organisaties die migreren van cloud AI naar lokale AI tegen "vendor-lock-in door opzet." Als een cloudprovider zijn data exporteert in een formaat dat je nieuwe lokale systeem niet kan lezen, is dat een schending van de Data Act.

---

## Deel 6 — Overheidstoegang in noodsituaties (Art. 14-22)

### De letterlijke tekst (Art. 14 lid 1)

> "Een overheidsinstantie of een instelling, orgaan of bureau van de Unie kan van een gegevenshouder verlangen dat deze uitzonderlijke noodzaak en de gegevens die nodig zijn om te reageren op een openbare noodsituatie of om een andere openbare noodzaak te vervullen, ter beschikking worden gesteld."

### De vertaling

In uitzonderlijke omstandigheden — een pandemie, een natuurramp, een terroristische aanslag — kunnen overheidsinstanties data opvragen bij bedrijven die die data bezitten.

Dit is geen permanente surveillancebevoegdheid. De vereisten zijn streng: er moet een echte noodsituatie zijn, de gevraagde data moet noodzakelijk zijn, en het verzoek moet proportioneel zijn.

### De implicatie voor lokale AI versus cloud AI

Dit artikel raakt cloud en lokale deployments beiden. Het verschil: bij cloud AI heeft de overheid een derde partij als tussenpersoon. Bij lokale AI communiceert de overheid rechtstreeks met de organisatie.

Voor de meeste MKB-organisaties is dit artikel minder relevant — noodsituaties waarbij de overheid hun data nodig heeft zijn zeldzaam. Maar voor grotere organisaties in kritieke sectoren is het een bekende bepaling.

---

## Deel 7 — Verbod op onrechtmatige internationale datatransfers (Art. 32)

### De letterlijke tekst

> "Aanbieders van dataverwerkingsdiensten nemen alle redelijke technische, juridische en organisatorische maatregelen, met inbegrip van het sluiten van contractuele regelingen, om te voorkomen dat niet-persoonsgebonden gegevens die worden bewaard in de Unie, worden overgedragen aan of toegankelijk gemaakt voor overheidsinstanties van derde landen."

### De vertaling

Cloudproviders mogen jouw niet-persoonsgebonden bedrijfsdata niet zomaar overdragen aan buitenlandse overheden. Ze moeten juridisch verzet bieden als een buitenlandse overheid om toegang vraagt.

Dit is een directe reactie op de CLOUD Act-discussie: zelfs voor niet-persoonsgebonden data wil Europa dat Europese data niet zomaar door buitenlandse overheden opgevraagd kan worden.

### De implicatie voor lokale AI versus cloud AI

Bij lokale AI staat de data bij jou. Geen cloudprovider die voor jou moet beslissen of hij voldoet aan een Amerikaans gerechtelijk bevel. Jij beslist. En als een buitenlandse overheid toegang wil tot jouw data, loopt dat via de normale juridische kanalen van jouw land — niet via de interne procedures van een Amerikaans techbedrijf.

---

## Deel 8 — De Data Act in de context van de bibliotheek

De Data Act is het bruggetje tussen wat er al was (GDPR, NIS2, DORA) en wat er aan komt (AI Act).

**Richting het verleden:**
De Data Act versterkt GDPR door ook niet-persoonsgebonden data te beschermen en dataportabiliteit wettelijk af te dwingen.

**Richting de toekomst:**
De Data Act maakt de migratie van cloud naar lokale AI juridisch en praktisch uitvoerbaar. Ze neemt de exit-barrière weg die cloudproviders jarenlang als strategisch voordeel gebruikten.

**De combinatie met AI Act:**
De AI Act verplicht organisaties tot betere controle over hun data en systemen. De Data Act geeft hen de juridische instrumenten om die controle ook daadwerkelijk te nemen — door data terug te halen uit cloud-omgevingen en lokaal te beheren.

Samen vormen ze een beleidspakket dat de richting aangeeft: data en intelligentie horen thuis bij de organisaties en mensen die ze genereren.

---

## Tijdlijn Data Act

| Datum | Wat |
|---|---|
| 11 januari 2024 | Data Act gepubliceerd in het Publicatieblad |
| 12 september 2025 | Data Act van kracht |
| 12 januari 2027 | Verbod op overstapkosten volledig van toepassing |
| 12 september 2027 | Sommige bepalingen voor bestaande contracten van toepassing |

---

## Begrippenlijst

**Verbonden product** — een product dat data genereert en verbonden is met het internet of een ander netwerk. Slimme apparaten, industriële machines, voertuigen, medische apparatuur.

**Gegevenshouder** — de partij die feitelijk toegang heeft tot data en die kan delen. Vaak de fabrikant of de dienstverlener.

**Gegevensontvangende partij** — de partij aan wie data wordt overgedragen op verzoek van de gebruiker.

**Aanbieder van dataverwerkingsdiensten** — cloudproviders, datacenters, SaaS-aanbieders. Elke partij die data verwerkt namens een klant.

**Overstapproces** — het geheel van technische en organisatorische handelingen dat nodig is om van de ene dataverwerkingsdienst naar de andere over te stappen, inclusief data-export en -import.

**Egress fees** — kosten die cloudproviders rekenen voor het downloaden of exporteren van data. Verboden vanaf 12 januari 2027.

**Functionele gelijkwaardigheid** — het principe dat een doeldienst na migratie minstens hetzelfde functionele niveau biedt als de brondienst. Cloudproviders moeten hier actief aan bijdragen.

**Niet-persoonsgebonden data** — data die niet direct of indirect herleidbaar is tot een identificeerbare persoon. Machinedata, productiedata, sensordata. Valt onder de Data Act maar niet onder GDPR.

---

## Checklist voor een klantgesprek

- [ ] Gebruikt u verbonden apparaten die data genereren? Weet u waar die data naartoe gaat?
- [ ] Heeft u geprobeerd uw eigen data te exporteren uit uw cloudplatformen?
- [ ] Bent u op de hoogte dat overstapkosten van cloudproviders vanaf januari 2027 verboden zijn?
- [ ] Heeft u in uw contracten met cloudleveranciers een exit-clausule?
- [ ] Weet u welke niet-persoonsgebonden bedrijfsdata u in de cloud heeft staan?
- [ ] Overweegt u migratie naar lokale systemen? De Data Act geeft u het juridische recht op uw data.

---

_Vorige document: 03-dora.md_
_Volgende document: 05-ai-act.md_
_Laatste update: maart 2026_
