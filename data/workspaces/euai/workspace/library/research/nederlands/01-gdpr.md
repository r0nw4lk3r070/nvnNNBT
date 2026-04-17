# 01 — GDPR / AVG
### LocAI Bibliotheek · Diepgang
_Verordening (EU) 2016/679 · Van kracht 25 mei 2018_
_Versie 0.1 · maart 2026_

---

## Wat dit document is

De GDPR is 99 artikelen lang en beslaat honderden overwegingen. Dit document is geen volledige juridische analyse — het is een werkdocument. We pakken de artikelen die voor ons relevant zijn, citeren de letterlijke tekst, vertalen die naar gewone taal, en trekken de implicatie voor lokale AI versus cloud AI.

Alles wat hier staat is gebaseerd op de officiële tekst van de verordening zoals gepubliceerd in het Publicatieblad van de Europese Unie.

---

## De kern in één zin

De GDPR geeft Europese burgers controle over hun persoonsgegevens en legt organisaties die die gegevens verwerken uitgebreide verplichtingen op — met echte boetes als ze zich er niet aan houden.

---

## Deel 1 — De basisprincipes (Art. 5)

### De letterlijke tekst

Artikel 5 lid 1 stelt dat persoonsgegevens:

> a) "worden verwerkt op een wijze die ten aanzien van de betrokkene rechtmatig, behoorlijk en transparant is ('rechtmatigheid, behoorlijkheid en transparantie')"

> b) "voor welbepaalde, uitdrukkelijk omschreven en gerechtvaardigde doeleinden worden verzameld en niet verder op een met die doeleinden onverenigbare wijze worden verwerkt ('doelbinding')"

> c) "toereikend zijn, ter zake dienend en beperkt tot wat noodzakelijk is voor de doeleinden waarvoor zij worden verwerkt ('minimale gegevensverwerking')"

> d) "juist zijn en zo nodig worden geactualiseerd ('juistheid')"

> e) "worden bewaard in een vorm die het mogelijk maakt de betrokkenen niet langer te identificeren dan noodzakelijk is voor de doeleinden waarvoor de persoonsgegevens worden verwerkt ('opslagbeperking')"

> f) "door het nemen van passende technische of organisatorische maatregelen op een dusdanige manier worden verwerkt dat een passende beveiliging ervan gewaarborgd is ('integriteit en vertrouwelijkheid')"

Artikel 5 lid 2:

> "De verwerkingsverantwoordelijke is verantwoordelijk voor de naleving van lid 1 en kan deze aantonen ('verantwoordingsplicht')."

### De vertaling

Zes principes die elke organisatie moet naleven als ze persoonsgegevens verwerkt.

**Rechtmatigheid, behoorlijkheid en transparantie:** je mag persoonsgegevens alleen verwerken als je daar een wettelijke grondslag voor hebt, je doet het op een fatsoenlijke manier, en je bent er open over.

**Doelbinding:** je verzamelt data voor een specifiek doel. Je mag die data niet zomaar voor iets anders gebruiken. Als je een e-mailadres verzamelt om een factuur te sturen, mag je het niet gebruiken voor een nieuwsbrief — tenzij de persoon daar apart toestemming voor heeft gegeven.

**Minimale gegevensverwerking:** verzamel alleen wat je echt nodig hebt. Niet alvast extra velden invullen "voor het geval dat." Als je naam en e-mailadres genoeg is, vraag dan geen geboortedatum.

**Juistheid:** houd data actueel. Verouderde informatie kan schade berokkenen.

**Opslagbeperking:** bewaar data niet langer dan nodig. Als een klant al drie jaar niets heeft gekocht, heeft het geen zin zijn persoonsgegevens voor altijd te bewaren.

**Integriteit en vertrouwelijkheid:** beveilig de data die je bewaart. Zowel technisch (encryptie, toegangscontrole) als organisatorisch (wie heeft toegang, hoe worden medewerkers getraind).

**Verantwoordingsplicht:** je kunt niet alleen zeggen dat je compliant bent — je moet het ook kunnen aantonen. Documentatie, verwerkingsregisters, beleid.

### De implicatie voor lokale AI versus cloud AI

Bij cloud AI stuur je data naar een externe server. Je hebt geen controle over wat er daarna mee gebeurt. Wordt het gebruikt voor modeltraining? Wordt het opgeslagen? Hoe lang? Kan een Amerikaanse rechtbank er toegang toe eisen?

Bij lokale AI blijft de data op je eigen apparaat of server. Jij bepaalt wat er mee gebeurt. Jij kunt de verantwoordingsplicht invullen — want jij bent de enige verwerkingsverantwoordelijke.

Het principe van minimale gegevensverwerking krijgt een nieuwe dimensie met AI: als je een taalmodel een patiëntdossier laat samenvatten, stuur je potentieel het volledige dossier naar de verwerker. Bij lokale AI is die "verwerker" jijzelf. Bij cloud AI is het een derde partij.

---

## Deel 2 — Verwerkingsgrondslag (Art. 6)

### De letterlijke tekst

> "De verwerking is alleen rechtmatig indien en voor zover aan ten minste een van de onderstaande voorwaarden is voldaan:
> a) de betrokkene heeft toestemming gegeven voor de verwerking van zijn persoonsgegevens voor een of meer specifieke doeleinden;
> b) de verwerking is noodzakelijk voor de uitvoering van een overeenkomst waarbij de betrokkene partij is;
> c) de verwerking is noodzakelijk om te voldoen aan een wettelijke verplichting die op de verwerkingsverantwoordelijke rust;
> d) de verwerking is noodzakelijk om de vitale belangen van de betrokkene of van een andere natuurlijke persoon te beschermen;
> e) de verwerking is noodzakelijk voor de vervulling van een taak van algemeen belang;
> f) de verwerking is noodzakelijk voor de behartiging van de gerechtvaardigde belangen van de verwerkingsverantwoordelijke of van een derde."

### De vertaling

Je mag persoonsgegevens alleen verwerken als je een van deze zes grondslagen hebt. Geen grondslag = geen verwerking. Punt.

De meest gebruikte grondslagen in de praktijk:

**Toestemming (a):** de persoon heeft expliciet ja gezegd. Let op: toestemming moet vrij, specifiek, geïnformeerd en ondubbelzinnig zijn. Een vooraf aangevinkt vakje is geen toestemming. "Door gebruik te maken van onze dienst gaat u akkoord" is geen toestemming.

**Overeenkomst (b):** je verwerkt data omdat het noodzakelijk is om een contract uit te voeren. Een accountant verwerkt financiële gegevens van een klant omdat dat noodzakelijk is voor de boekhouding. Dat is grondslag b.

**Gerechtvaardigd belang (f):** de meest flexibele grondslag, en daardoor de meest misbruikte. Je hebt een legitiem belang, en dat weegt zwaarder dan de privacybelangen van de betrokkene. Vereist een afweging — en die afweging moet je kunnen documenteren.

### De implicatie voor lokale AI versus cloud AI

Als je persoonsgegevens verwerkt via een cloud AI-dienst, heb je technisch gezien een verwerkersovereenkomst nodig met die dienst (zie Art. 28). Maar de grondslag voor de verwerking moet je zelf hebben.

Probleem: veel cloud AI-diensten verwerken data op manieren die buiten de oorspronkelijke grondslag vallen. Ze gebruiken conversaties voor modelverbetering, voor analytische doeleinden, of bewaren ze langer dan nodig. Dat is een schending van doelbinding (Art. 5b) — ook al heb je zelf een geldige grondslag voor de initiële verwerking.

Bij lokale AI is er geen derde partij die buiten jouw grondslag om iets doet met de data.

---

## Deel 3 — Bijzondere categorieën (Art. 9)

### De letterlijke tekst

> "Verwerking van persoonsgegevens waaruit ras of etnische afkomst, politieke opvattingen, religieuze of levensbeschouwelijke overtuigingen, of het lidmaatschap van een vakbond blijken, en verwerking van genetische gegevens, biometrische gegevens met het oog op de unieke identificatie van een persoon, gegevens over gezondheid, of gegevens met betrekking tot iemands seksueel gedrag of seksuele gerichtheid zijn verboden."

Gevolgd door uitzonderingen — maar die zijn beperkt en specifiek.

### De vertaling

Sommige data is zo gevoelig dat de GDPR er een extra beschermingslaag op legt. Deze "bijzondere categorieën" zijn in principe verboden te verwerken, tenzij je een expliciete uitzondering kunt aantonen.

De categorieën die in de praktijk het meest voorkomen:

**Gezondheidsdata:** alles wat iets zegt over de fysieke of mentale gezondheid van een persoon. Medische dossiers, diagnoses, medicatie, maar ook verzuimregistraties en sessienotities van een therapeut.

**Biometrische data:** vingerafdrukken, gezichtsherkenning, stemherkenning — als het gebruikt wordt om iemand uniek te identificeren.

**Genetische data:** DNA-informatie.

**Ras of etnische afkomst, politieke opvattingen, religieuze overtuigingen, seksuele gerichtheid:** categorieën die extra bescherming verdienen vanwege het discriminatierisico.

De uitzonderingen die in de praktijk relevant zijn:
- Expliciete toestemming van de betrokkene
- Verwerking noodzakelijk voor gezondheidszorg door een zorgprofessional met beroepsgeheim
- Verwerking noodzakelijk om vitale belangen te beschermen
- Verwerking voor archivering in het algemeen belang of wetenschappelijk onderzoek

### De implicatie voor lokale AI versus cloud AI

Dit is het artikel dat het verschil maakt voor sectoren als gezondheidszorg, maatschappelijk werk en jeugdzorg.

Een therapeut die sessienotities door een cloud AI laat verwerken, verwerkt bijzondere categorie data (gezondheid, mogelijk ook seksuele gerichtheid of religieuze overtuigingen) via een derde partij. De uitzondering voor gezondheidszorg geldt voor de therapeut zelf — niet automatisch voor de cloud-provider die de AI draait.

Een jeugdzorgorganisatie die cliëntdata verwerkt, werkt met data van minderjarigen (extra bescherming via Overweging 38) die ook gezondheids- en gedragsinformatie bevat. Art. 9-data op een Amerikaanse cloudserver is een compliance-nachtmerrie.

Bij lokale AI: de data verlaat de organisatie niet. De uitzondering voor zorgprofessionals met beroepsgeheim is van toepassing op de organisatie zelf. Er is geen derde partij die een eigen verwerkingsgrondslag nodig heeft.

---

## Deel 4 — Rechten van betrokkenen (Art. 12-22)

### De letterlijke tekst (samenvatting per artikel)

**Art. 13-14 — Informatieplicht:** betrokkenen moeten geïnformeerd worden over wie hun data verwerkt, waarom, hoe lang, en wat hun rechten zijn.

**Art. 15 — Recht op inzage:** betrokkenen hebben het recht te weten welke persoonsgegevens over hen verwerkt worden.

**Art. 16 — Recht op rectificatie:** onjuiste gegevens moeten gecorrigeerd kunnen worden.

**Art. 17 — Recht op gegevenswissing ("recht op vergetelheid"):**
> "De betrokkene heeft het recht van de verwerkingsverantwoordelijke zonder onredelijke vertraging wissing van hem betreffende persoonsgegevens te verkrijgen."

**Art. 18 — Recht op beperking van de verwerking:** in bepaalde situaties kan een betrokkene vragen de verwerking tijdelijk te stoppen.

**Art. 20 — Recht op dataportabiliteit:** betrokkenen hebben het recht hun data in een machineleesbaar formaat te ontvangen en over te dragen naar een andere dienst.

**Art. 21 — Recht van bezwaar:** betrokkenen kunnen bezwaar maken tegen verwerking op basis van gerechtvaardigd belang.

**Art. 22 — Geautomatiseerde besluitvorming:**
> "De betrokkene heeft het recht niet te worden onderworpen aan een uitsluitend op geautomatiseerde verwerking, waaronder profilering, gebaseerd besluit waaraan voor hem rechtsgevolgen zijn verbonden of dat hem op vergelijkbare wijze aanmerkelijk treft."

### De vertaling

**Recht op vergetelheid:** als iemand vraagt zijn data te verwijderen, moet je dat kunnen doen. En aantonen dat je het gedaan hebt.

**Recht op dataportabiliteit:** een patiënt mag zijn dossier opvragen in een formaat dat een andere zorgverlener kan inlezen. Een klant mag zijn transactiegeschiedenis exporteren.

**Geautomatiseerde besluitvorming:** een AI mag geen beslissingen nemen die iemands leven beïnvloeden zonder menselijke tussenkomst. Een AI-systeem dat kredietaanvragen beoordeelt, sollicitaties screent, of uitkeringsbesluiten neemt — dat vereist altijd een menselijke toets.

### De implicatie voor lokale AI versus cloud AI

Het recht op vergetelheid is bij lokale AI technisch uitvoerbaar: je weet precies welke database de data bevat, je kunt het verwijderen, en je kunt het aantonen.

Bij cloud AI is dit structureel complexer: de data kan gecached zijn, gebruikt zijn voor modelverbetering, opgeslagen zijn in back-ups die je niet beheert. Zelfs als de provider belooft te verwijderen, kun je het niet verifiëren.

Art. 22 over geautomatiseerde besluitvorming is cruciaal voor de AI Act — het is het GDPR-artikel dat het meest direct aansluit op de AI Act's vereiste van menselijk toezicht (Art. 14 AI Act). De twee wetten versterken elkaar hier: GDPR verbiedt volledig geautomatiseerde besluitvorming met rechtsgevolgen, de AI Act verplicht menselijk toezicht bij hoog-risico AI.

---

## Deel 5 — Verwerkersovereenkomst (Art. 28)

### De letterlijke tekst

> "Wanneer de verwerking namens een verwerkingsverantwoordelijke wordt uitgevoerd, maakt de verwerkingsverantwoordelijke uitsluitend gebruik van verwerkers die afdoende garanties met betrekking tot het toepassen van passende technische en organisatorische maatregelen bieden, zodat de verwerking aan de vereisten van deze verordening voldoet en de bescherming van de rechten van de betrokkene gewaarborgd is."

En:

> "De verwerker verwerkt de persoonsgegevens uitsluitend op basis van gedocumenteerde instructies van de verwerkingsverantwoordelijke."

### De vertaling

Als je een derde partij inschakelt om persoonsgegevens te verwerken — een boekhoudsoftware, een HR-systeem, een cloud AI-dienst — dan moet je een verwerkersovereenkomst (DPA, Data Processing Agreement) afsluiten.

Die overeenkomst moet vastleggen:
- Wat de verwerker mag doen met de data
- Dat de verwerker alleen verwerkt op basis van jouw instructies
- Welke beveiligingsmaatregelen de verwerker neemt
- Dat de verwerker je informeert bij een datalek
- Dat de verwerker de data verwijdert of teruggeeft als de samenwerking eindigt

### De implicatie voor lokale AI versus cloud AI

Elke cloud AI-dienst is een verwerker. Je hebt een verwerkersovereenkomst nodig. Die moet voldoen aan Art. 28. En je moet kunnen aantonen dat de verwerker de afspraken nakomt.

In de praktijk: Microsoft, Google en OpenAI bieden standaard DPA's aan. Die zijn geschreven door hun juristen, in hun voordeel, met beperkte onderhandelmogelijkheden voor een kleine organisatie.

Twee problemen:
1. De DPA beschermt je juridisch maar garandeert niets technisch. Je kunt niet controleren of de verwerker zich aan de afspraken houdt.
2. Als de verwerker subverwerkers inschakelt — en dat doen ze allemaal — heb je een keten van verwerkersrelaties die je niet kunt overzien.

Bij lokale AI: geen verwerker. Geen DPA nodig. De data verwerkt de organisatie zelf, op eigen hardware, onder eigen controle.

---

## Deel 6 — Datalekken (Art. 33-34)

### De letterlijke tekst

Art. 33 lid 1:
> "In geval van een inbreuk in verband met persoonsgegevens meldt de verwerkingsverantwoordelijke dit zonder onredelijke vertraging en, indien mogelijk, uiterlijk 72 uur nadat hij er kennis van heeft genomen, aan de bevoegde toezichthoudende autoriteit."

Art. 34 lid 1:
> "Wanneer de inbreuk in verband met persoonsgegevens waarschijnlijk een hoog risico inhoudt voor de rechten en vrijheden van natuurlijke personen, deelt de verwerkingsverantwoordelijke de betrokkene de inbreuk in verband met persoonsgegevens onverwijld mede."

### De vertaling

Als er een datalek is — data gestolen, verloren, of onbedoeld openbaar gemaakt — moet je dat binnen 72 uur melden bij de toezichthouder (in België: de GBA, in Nederland: de AP).

Als het lek een hoog risico vormt voor de betrokkenen — denk aan medische data, financiële data, of data van minderjarigen — moet je de betrokkenen zelf ook informeren.

De 72-uur klok begint te lopen op het moment dat je weet dat er een lek is. Niet wanneer je het volledig hebt onderzocht. Niet wanneer je advocaat terug is van vakantie.

### De implicatie voor lokale AI versus cloud AI

Bij cloud AI: een datalek bij de provider is ook jouw datalek. Je bent de verwerkingsverantwoordelijke — de meldplicht ligt bij jou, niet bij de provider. Maar je bent afhankelijk van de provider om je tijdig te informeren. En "tijdig" in een cloud-omgeving met miljoenen klanten kan betekenen dat jij als kleine organisatie ver achteraan in de rij staat.

Bij lokale AI: je beheert de data zelf. Een lek is onmiddellijk zichtbaar in je eigen systemen. Je bent niet afhankelijk van de communicatiesnelheid van een externe provider.

---

## Deel 7 — Privacy by Design en Privacy by Default (Art. 25)

### De letterlijke tekst

> "Rekening houdend met de stand van de techniek, de uitvoeringskosten, en de aard, het toepassingsgebied, de context en de doeleinden van de verwerking, alsmede met de qua waarschijnlijkheid en ernst uiteenlopende risico's voor de rechten en vrijheden van natuurlijke personen die aan de verwerking verbonden zijn, treft de verwerkingsverantwoordelijke, zowel bij de bepaling van de middelen voor de verwerking als bij de verwerking zelf, passende technische en organisatorische maatregelen [...] teneinde de gegevensbeschermingsbeginselen [...] op een doeltreffende wijze uit te voeren."

En:

> "De verwerkingsverantwoordelijke treft passende technische en organisatorische maatregelen om ervoor te zorgen dat in beginsel alleen persoonsgegevens worden verwerkt die noodzakelijk zijn voor elk specifiek verwerkingsdoeleinde."

### De vertaling

**Privacy by design:** bouw privacy in vanaf het begin. Niet als laagje dat je er achteraf op plakt. Als je een systeem ontwerpt, stel jezelf de vraag: hoe verwerken we zo min mogelijk data, zo veilig mogelijk, op een manier die de rechten van betrokkenen respecteert?

**Privacy by default:** de standaardinstellingen van je systeem moeten altijd de meest privacy-vriendelijke optie zijn. Als een gebruiker niets instelt, deelt hij zo min mogelijk. Niet zo veel mogelijk.

### De implicatie voor lokale AI versus cloud AI

Privacy by design is het architectuurprincipe dat lokale AI belichaamt.

Een systeem dat data lokaal verwerkt, zonder externe API-calls, zonder datatransfers naar derde partijen, zonder logging op vreemde servers — dat is privacy by design in zijn meest directe vorm.

Een systeem dat standaard alle data naar een cloud stuurt, tenzij de gebruiker actief opt-out — dat is het tegenovergestelde van privacy by default.

SPOREN is gebouwd op dit principe: geen cloud, geen externe verwerking, data blijft op de eigen server van de organisatie. Dat is geen marketingkeuze — het is een architectuurkeuze die direct voortkomt uit Art. 25.

---

## Deel 8 — Boetes (Art. 83)

### De letterlijke tekst

Art. 83 lid 4:
> "Inbreuken op de volgende bepalingen worden overeenkomstig lid 2 bestraft met administratieve geldboeten van maximaal 10 000 000 EUR of, voor een onderneming, van maximaal 2 % van de totale wereldwijde jaarlijkse omzet."

Art. 83 lid 5:
> "Inbreuken op de volgende bepalingen worden overeenkomstig lid 2 bestraft met administratieve geldboeten van maximaal 20 000 000 EUR of, voor een onderneming, van maximaal 4 % van de totale wereldwijde jaarlijkse omzet."

De zwaarste boetes (4%) gelden voor schendingen van: de basisprincipes (Art. 5), verwerkingsgrondslagen (Art. 6), bijzondere categorieën (Art. 9), en rechten van betrokkenen (Art. 12-22).

### De vertaling

Er zijn twee boetecategorieën. De lichtste: tot €10 miljoen of 2% omzet. De zwaarste: tot €20 miljoen of 4% omzet.

Voor een MKB-bedrijf van 10 personen met €500.000 omzet betekent 4% = €20.000. Dat klinkt minder dramatisch dan de krantenkoppen over miljoenenboetes bij grote techbedrijven. Maar het is nog steeds een existentieel bedrag voor een kleine praktijk.

En de financiële boete is niet het enige risico. Reputatieschade is bij veel kleine organisaties groter: een therapeut die zijn patiënten moet informeren over een datalek verliest vertrouwen dat hij niet meer terugkrijgt.

### Gedocumenteerde boetes in Europa (selectie)

- **Meta (Ierland, 2023):** €1,2 miljard voor het overdragen van persoonsgegevens naar de VS zonder adequate bescherming. Grootste GDPR-boete ooit op dat moment.
- **Google (Frankrijk, 2022):** €150 miljoen voor cookie-toestemmingsschending.
- **H&M (Duitsland, 2020):** €35 miljoen voor onrechtmatige surveillance van medewerkers.
- **Clearview AI (meerdere landen, 2022):** boetes in Italië, Griekenland, Frankrijk voor illegale verwerking van biometrische data.

Patroon: grote techbedrijven krijgen de grote boetes. MKB krijgt kleinere boetes — maar die zijn er wel degelijk, ook in België en Nederland.

---

## Deel 9 — De toezichthouders

### België — Gegevensbeschermingsautoriteit (GBA)

Website: gegevensbeschermingsautoriteit.be
Meldingen van datalekken: via het online meldportaal op de website
Klachten indienen: ook via de website

De GBA is relatief actief in vergelijking met sommige andere Europese toezichthouders. Ze publiceert aanbevelingen, behandelt klachten, en voert eigen onderzoeken uit.

### Nederland — Autoriteit Persoonsgegevens (AP)

Website: autoriteitpersoonsgegevens.nl
Vergelijkbare structuur als de GBA. Bekend om proactieve communicatie over nieuwe ontwikkelingen, waaronder AI.

### Het one-stop-shop principe

Als een bedrijf in meerdere EU-lidstaten actief is, hoeft het maar met één toezichthouder te communiceren — de toezichthouder in het land van de hoofdvestiging. Voor grote techbedrijven is dat vaak Ierland (waar veel Amerikaanse bedrijven hun Europese hoofdkantoor hebben).

---

## Deel 10 — GDPR en AI: de verbinding

Dit is de schakel naar de AI Act.

De GDPR regelt hoe persoonsgegevens verwerkt mogen worden. De AI Act regelt hoe intelligente systemen die persoonsgegevens verwerken ontworpen en ingezet moeten worden.

Ze overlappen op meerdere punten:

| GDPR | AI Act | Gemeenschappelijk principe |
|---|---|---|
| Art. 5 — Dataminimalisatie | Art. 10 — Databeheer | Gebruik alleen de data die nodig is |
| Art. 22 — Geen volledig geautomatiseerde besluitvorming | Art. 14 — Menselijk toezicht | Mensen blijven in de lus |
| Art. 25 — Privacy by design | Art. 9 — Risicomanagement | Bouw het goed van het begin |
| Art. 17 — Recht op vergetelheid | Art. 12 — Logging en traceerbaarheid | Beheer van data lifecycle |
| Art. 83 — Boetes | Art. 99 — Boetes | Echte consequenties |

De AI Act verwijst expliciet naar GDPR. Een AI-systeem dat de AI Act naleeft maar de GDPR schendt is niet compliant. Beide wetten moeten samen nageleefd worden.

**De praktische consequentie:**
Vanaf december 2027 (verwachte nieuwe deadline) hebben organisaties die hoog-risico AI inzetten een dubbele compliance-last: AI Act voor het systeem, GDPR voor de data. De makkelijkste manier om beide te combineren: lokale verwerking, waarbij de organisatie zelf de volledige controle heeft over zowel het systeem als de data.

---

## Begrippenlijst

**Verwerkingsverantwoordelijke** — de organisatie of persoon die het doel en de middelen van de gegevensverwerking bepaalt. Jij als ondernemer die klantdata verwerkt. Jij bent verantwoordelijk — ook als je een verwerker inschakelt.

**Verwerker** — een partij die persoonsgegevens verwerkt namens de verwerkingsverantwoordelijke. Een cloud AI-dienst is een verwerker. Een boekhoudpakket is een verwerker. Je hebt altijd een verwerkersovereenkomst nodig.

**Betrokkene** — de natuurlijke persoon wiens persoonsgegevens verwerkt worden. Je klant, je patiënt, je medewerker.

**Persoonsgegevens** — alle informatie die direct of indirect herleidbaar is tot een identificeerbare persoon. Naam, e-mailadres, IP-adres, locatiedata, cookie-ID's — allemaal persoonsgegevens.

**Bijzondere categorieën** — extra gevoelige persoonsgegevens die extra bescherming vereisen (zie Art. 9): gezondheid, genetisch, biometrisch, ras, politiek, religie, vakbond, seksualiteit.

**Verwerkersovereenkomst (DPA)** — een contract tussen verwerkingsverantwoordelijke en verwerker dat vastlegt hoe de verwerker de data mag gebruiken. Verplicht onder Art. 28.

**Gerechtvaardigde belangen** — een verwerkingsgrondslag waarbij je argumenteert dat jouw legitieme belang zwaarder weegt dan de privacybelangen van de betrokkene. Vereist een gedocumenteerde afweging.

**Toestemming** — een verwerkingsgrondslag waarbij de betrokkene vrij, specifiek, geïnformeerd en ondubbelzinnig ja heeft gezegd. Moet even makkelijk in te trekken zijn als te geven.

**Datalek** — een inbreuk op de beveiliging die leidt tot vernietiging, verlies, wijziging, ongeoorloofde verstrekking of toegang van persoonsgegevens. Meldplicht binnen 72 uur bij de toezichthouder.

**Privacy by design** — het principe dat privacybescherming van meet af aan in het ontwerp van een systeem wordt ingebouwd, niet achteraf toegevoegd.

**Privacy by default** — het principe dat de standaardinstellingen altijd de meest privacy-vriendelijke optie zijn.

**Profilering** — elke geautomatiseerde verwerking van persoonsgegevens waarbij die gegevens worden gebruikt om bepaalde aspecten van een persoon te evalueren, zoals gedrag, voorkeuren of betrouwbaarheid.

**DPO (Data Protection Officer / Functionaris Gegevensbescherming)** — een verplichte rol voor bepaalde organisaties (overheid, grootschalige verwerking van bijzondere categorieën, grootschalige monitoring). De DPO adviseert over GDPR-naleving en is het aanspreekpunt voor de toezichthouder.

---

## Checklist voor MKB

Gebruik dit als snelle audit voor een klantgesprek.

- [ ] Heb je een register van verwerkingsactiviteiten? (Art. 30)
- [ ] Heb je voor elke verwerking een geldige grondslag? (Art. 6)
- [ ] Heb je verwerkersovereenkomsten met alle derde partijen? (Art. 28)
- [ ] Informeer je betrokkenen over hun rechten? (Art. 13-14)
- [ ] Kun je voldoen aan een inzageverzoek binnen 30 dagen? (Art. 15)
- [ ] Kun je data verwijderen als iemand dat vraagt? (Art. 17)
- [ ] Weet je wat je moet doen bij een datalek? (Art. 33-34)
- [ ] Is je systeem gebouwd met privacy by design? (Art. 25)
- [ ] Verwerk je bijzondere categorieën — en heb je daarvoor een expliciete grondslag? (Art. 9)
- [ ] Stuur je data buiten de EU — en heb je daarvoor adequate waarborgen? (Art. 44-49)

---

_Vorige document: 00-geschiedenis.md_
_Volgende document: 02-nis2.md_
_Laatste update: maart 2026_
