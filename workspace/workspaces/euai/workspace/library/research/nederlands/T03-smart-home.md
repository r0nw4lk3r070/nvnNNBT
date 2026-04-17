# T03 — De Smart Home
### LocAI Bibliotheek · Thuisfront
_Versie 0.1 · maart 2026_

---

## Wat er in een gemiddeld Europees huis staat

Niet hypothetisch. Niet toekomstig. Vandaag.

**De router** — cartografeert elk apparaat op het netwerk. Naam, MAC-adres, verbindingstijden. Odido stuurde die data drie jaar lang naar Lifemote, een AI-startup in Turkije, zonder dat klanten het wisten. De patch kwam vijf dagen na publicatie. Stil. Geen perscommuniqué. Geen excuses.

**De smart TV** — maakt twee keer per seconde een screenshot van wat er op het scherm staat. Niet alleen van streamingdiensten — van alles. Een DVD, een laptop gespiegeld, een camera. Samsung's ACR-systeem matcht die screenshots tegen een database en verkoopt het profiel aan Google, advertentienetwerken, en datamakelaars. Vizio genereerde ooit twee keer zoveel omzet uit het verkopen van kijkdata als uit het verkopen van TV's. De hardware is gesubsidieerd door jouw gedrag.

**De slimme speaker** — luistert continu. Amazon, Google, Apple — ze bewaren opnames. Menselijke medewerkers luisteren mee om de spraakherkenning te verbeteren. Je hebt daarvoor toestemming gegeven. In de gebruiksvoorwaarden. Die je niet gelezen hebt.

**De smartphone** — weet waar je geslapen hebt, hoe laat je vertrok, hoe lang je weg was. Locatiedata wordt gebruikt voor advertenties, verkocht aan datamakelaars, en in de VS zelfs verkocht aan wetshandhaving zonder gerechtelijk bevel.

**De slimme bril** — Meta's Ray-Ban smart glasses. Zeven miljoen paar verkocht in 2025. Marketingslogan: "Designed for privacy, controlled by you." Werkelijkheid: camerabeelden gingen naar Meta's servers, werden gefilterd naar Nairobi, en werden beoordeeld door medewerkers van Sama. Medewerkers die vrouwen zagen uitkleden. Mensen die seks hadden. Privéruimtes die nooit voor een camera bedoeld waren. Meta bevestigde de praktijk. De gezichten waren "wazig" — zeiden ze. De medewerkers zeiden dat de vervaging inconsistent was.

**De slimme deurbel** — geeft Amazon een videoarchief van iedereen die je voordeur nadert.

**De thermostaat** — vertelt Google wanneer je thuis bent, wanneer je slaapt, hoe warm je je huis houdt.

**De babyfoon** — verbonden met externe servers van de fabrikant. Beelden en audio van de meest beschermde ruimte in huis.

Elk apparaat apart gekocht. Elke privacyschending begraven in een ander document. Elke onderneming die naar een beleidspage wijst als het fout gaat.

---

## De boete die niet pijn doet

Sinds de GDPR in 2018 in werking trad, heeft Europa circa €5,88 miljard aan boetes uitgedeeld.

Meta betaalde €1,2 miljard. Dat was vier dagen omzet. LinkedIn betaalde €310 miljoen. TikTok €530 miljoen. Uber €290 miljoen.

Elk van die bedrijven bleef de dag na de boete gewoon draaien.

De boete is geen straf. Het is een belasting op datadiefstal. Ingecalculeerd in de spreadsheet. Goedkoper dan compliance.

In Kroatië werd een telecomoperator beboet €4,5 miljoen in november 2025 voor het doorsturen van klantdata naar Servië zonder adequate waarborgen — en voor het voortzetten daarvan nadat ze gesommeerd waren te stoppen. In Spanje ontving Vodafone meer dan 30 GDPR-boetes in vier jaar en bleef illegale marketinggesprekken voeren.

Dit is geen systeem van verantwoording. Het is een systeem van taxatie.

---

## Hoe het thuisnetwerk in werkelijkheid werkt

Laten we het concreet maken.

```
Jouw huis
├── Router (ISP)
│   ├── Stuurt metadata naar ISP
│   ├── Stuurt apparaatnamen naar fabrikant
│   └── Stuurde apparaatnamen naar Lifemote (Odido, 3 jaar lang)
│
├── Smart TV
│   ├── Screenshot elke 500ms → Samsung ACR → advertentienetwerk
│   └── Kijkprofiel verkocht aan Google, X, en anderen
│
├── Alexa / Google Home
│   ├── Luistert continu naar activeringwoord
│   ├── Stuurt audiodata naar externe servers
│   └── Menselijke medewerkers reviewen opnames
│
├── Smartphones (2-4)
│   ├── Locatietracking continu
│   ├── App-data naar tientallen externe servers
│   └── Locatiedata verkocht aan datamakelaars
│
├── Smart Home apparaten
│   ├── Thermostaat → Google (wanneer thuis, slaappatroon)
│   ├── Deurbel → Amazon (videoarchief bezoekers)
│   └── Babyfoon → fabrikant servers
│
└── Laptop / tablet
    ├── Browserdata → Google / advertentienetwerk
    └── App-data → tientallen externe services
```

Dit is wat er dagelijks uit een gemiddeld Europees huis vertrekt. Zonder dat iemand een bewuste beslissing heeft genomen. Zonder dat iemand het ziet.

---

## De smart home als datafabriek

"Your home is working" — dat was de openingszin van het Substack-artikel dat dit dossier voorafging.

Het is een accurate beschrijving. Een smart home is geen huis dat voor jou werkt. Het is een huis dat voor de platforms werkt die de apparaten verkochten.

De waarde die gegenereerd wordt:
- Kijkgedrag → advertentieprofiel → hogere advertentietarieven
- Locatiedata → bewegingspatronen → targeting voor fysieke winkels
- Stemdata → spraakherkenning verbetering → betere producten voor de fabrikant
- Apparaatnamen → huishoudprofiel → data voor datamakelaars
- Thermostaat data → aanwezigheidspatroon → verzekeringsprofiel

Al die waarde wordt gecreëerd in jouw huis. Door jou. En stroomt weg naar externe servers.

De inversie is eenvoudig te formuleren maar moeilijk te realiseren: wat als die intelligentie bij jou bleef?

---

## Hoe lokale AI de smart home herdefineert

### Van luisteren naar lokaal begrijpen

Een slimme speaker die lokaal draait — op eigen hardware, met een open-source spraakmodel — hoort jou, verwerkt de vraag lokaal, en antwoordt. Geen audiobestand naar Amazon. Geen menselijke medewerker in een call center die meeluistert.

De functionaliteit is identiek. De dataflow is fundamenteel anders.

**Wat werkt lokaal vandaag:**
- Spraakherkenning: whisper.cpp draait op een moderne CPU of NPU
- Taalmodel: Ollama met een 7B-13B model beantwoordt dagelijkse vragen
- Kalender en planning: Nextcloud of een lokale kalenderapp
- Muziek: een lokale muziekserver (Navidrome, Jellyfin)
- Nieuws en informatie: lokale RSS-aggregator

### Van slimme TV naar privé-scherm

ACR uitzetten is technisch mogelijk maar niet altijd eenvoudig. Op Samsung-TV's: Instellingen → Ondersteuning → Voorwaarden & Privacy → Diensten van Kijkervaring → uitzetten.

Maar uitschakelen is niet hetzelfde als verwijderen. Het datakanaal is er — je hebt het alleen dichtgedraaid. Bij de volgende firmware-update kan het opnieuw aanstaan.

De radicale oplossing: een "domme" HDMI-stick (Chromecast zonder Google-account, een lokale media-server via HDMI) als interface, en de smart-TV-functies volledig negeren.

### Van router-as-a-service naar eigen infrastructuur

Een Pi-hole op het thuisnetwerk blokkeert advertentieservers op DNS-niveau voor alle apparaten tegelijk. Geen installatie op elk apparaat afzonderlijk — één centrale blokkade.

Een eigen router (op basis van OpenWrt of pfSense) geeft volledige controle over wat het netwerk doet. Geen fabrikant-firmware die onbekende datastromen opent.

### Van cloud-afhankelijk naar lokaal-first

Het model dat The Great Return beschrijft voor organisaties — lokaal-first, cloud-als-uitbreiding — geldt ook voor het huis.

| Dienst | Cloud versie | Lokale versie |
|---|---|---|
| Agenda | Google Calendar | Nextcloud Calendar |
| Bestanden | Google Drive / iCloud | Nextcloud / Syncthing |
| Foto's | Google Photos | Immich (lokaal) |
| Muziek | Spotify | Navidrome + eigen collectie |
| Notities | Google Keep / Notion | Obsidian (lokaal) / Joplin |
| AI-assistent | ChatGPT / Alexa | Ollama + open-weight model |
| E-mail | Gmail | ProtonMail / eigen server |
| Wachtwoorden | LastPass / 1Password cloud | Vaultwarden (lokaal Bitwarden) |

Niet alles hoeft tegelijk. Elke stap die je zet, is een stap waarbij minder data jouw huis verlaat.

---

## AETHER als referentie-implementatie

AETHER is het bewijs dat dit geen theorie is.

Gebouwd op oude desktop-hardware. Meer dan drie maanden stabiel gedraaid. Android-apps die werken. Lokale AI via Ollama. Google-diensten vervangen voor een volledig huishouden.

Wat AETHER doet:
- Agenda — volledig lokaal, geen Google Calendar
- Bestanden — lokale opslag, geen Google Drive
- AI-assistent — Ollama met open-weight model, geen ChatGPT
- Geen data die het huis verlaat

Wat AETHER bewijst:
- Het vereist geen technische achtergrond om te bouwen
- Het is stabiel genoeg voor dagelijks gebruik
- Het is goedkoper dan de som van alle cloud-abonnementen
- Het is de architectuur die in The Great Return beschreven wordt — maar dan thuis

De eerste klant was het eigen huishouden. Dat is de eerlijkste test.

---

## De postman aan de deur — thuis

The Great Return beschrijft het "postman at the door" paradigma voor organisaties: de lokale AI heeft volledige privé-context en communiceert met de buitenwereld alleen via bounded, specifieke verzoeken. De intelligentie woont bij de gebruiker.

Thuis is dat paradigma nog directer.

Een slimme speaker die in jouw huis staat en alles doorstuur naar een server in Virginia — dat is niet een postman die een pakket brengt. Dat is een postman die in jouw huis woont, alles noteert wat er gezegd wordt, en elke avond een rapport stuurt naar zijn werkgever.

Een lokale AI-assistent op eigen hardware — die weet wat je agenda is, welke muziek je leuk vindt, wat je kinderen vandaag op school hebben — en die niets deelt — dat is de postman aan de deur. Hij brengt wat je nodig hebt. Hij gaat daarna weg. Hij inventariseert de inhoud van je huis niet.

---

## De drie lagen van het thuisfront

Dit dossier sluit de thuisreeks af. De drie dossiers samen beschrijven drie lagen van hetzelfde probleem.

**T01 — Gezin & Data:** het grote plaatje. Wat er verzameld wordt, wie er van profiteert, wat de alternatieven zijn.

**T02 — Kinderen Online:** de meest kwetsbaren. Data die verzameld wordt op een leeftijd waarop er geen geïnformeerde keuze mogelijk is.

**T03 — De Smart Home:** de concrete infrastructuur. Elk apparaat, elke dataroom, elke stap naar een lokaal alternatief.

Samen vormen ze het argument voor het thuisfront: lokale AI is niet alleen voor bedrijven. Het is voor elk gezin dat zijn huis wil terugnemen.

---

## De vraag die alles samenvat

Het Odido-artikel eindigde met een zin die als slotakkoord van dit hele dossier dient:

> "The awareness is not enough on its own. Knowing that your television watches you does not stop it watching you. The knowledge creates the demand for an alternative. The hardware to build that alternative exists. The software to run it is free and open. The only thing missing is the moment when Jan and Marie decide that enough is enough."

Dat moment volgt historisch op een schandaal. Odido was dat schandaal. Stil gepatcht. Nauwelijks gedekt. Makkelijk te missen.

Maar voor wie het gelezen heeft: de vraag is niet meer of er een alternatief is. De vraag is wanneer.

---

## Praktische startgids voor het thuisfront

Voor de lezer die nu wil beginnen — in volgorde van eenvoudig naar uitgebreid.

### Stap 1 — Vandaag, gratis (30 minuten)

- ACR uitzetten op de smart TV (Instellingen → Privacy → Kijkservices)
- Locatiegeschiedenis uitzetten op smartphones (Google Maps → Timeline → uitzetten)
- Advertentiepersonalisatie uitzetten (myaccount.google.com → Data & Privacy)
- Slimme speakers uit slaapkamers verwijderen

### Stap 2 — Dit weekend (€50-100)

- Pi-hole installeren op een Raspberry Pi — blokkeert advertentieservers voor het hele netwerk
- Signal installeren als vervanging voor WhatsApp
- DuckDuckGo instellen als standaard zoekmachine op alle apparaten

### Stap 3 — Dit kwartaal (€150-300)

- Nextcloud installeren op een oude laptop of mini-PC — vervangt Google Drive, Google Calendar, Google Contacts
- Immich installeren voor lokale fotoopslag — vervangt Google Photos
- Jellyfin of Navidrome voor lokale mediabibliotheek

### Stap 4 — Dit jaar (€800-1.500)

- AMD Ryzen AI Max+ mini-PC of equivalent
- Ollama met een 70B open-weight model
- Volledig lokaal AI-systeem voor het hele gezin
- AETHER-architectuur: lokale agenda, bestanden, AI-assistent

Elke stap staat op zichzelf. Je hoeft niet meteen naar stap 4. Maar elke stap is een stap waarbij jouw huis iets minder voor de platforms werkt — en iets meer voor jou.

---

## Begrippenlijst

**ACR (Automatic Content Recognition)** — technologie in smart TV's die screenshots maakt van het scherm en die matcht met een database om kijkgewoonten te analyseren. Ingeschakeld by default op de meeste Samsung, LG, en andere smart TV's.

**MAC-adres** — een uniek identificatienummer van elk netwerkapparaat. Wordt gebruikt om apparaten te identificeren op een netwerk. Odido stuurde MAC-adressen en apparaatnamen naar Lifemote.

**Lifemote** — een AI-startup die netwerkinformatie van thuisrouters analyseert voor telecomproviders. Ontving drie jaar lang data van Odido-klanten zonder hun medeweten.

**Pi-hole** — open-source software die op een kleine computer (Raspberry Pi) draait en advertentieservers blokkeert voor alle apparaten op het thuisnetwerk via DNS-blokkering.

**OpenWrt** — open-source firmware voor routers. Vervangt fabrikant-firmware en geeft volledige controle over routergedrag en datastromen.

**Nextcloud** — open-source platform dat Google Drive, Google Calendar, en Google Contacts vervangt. Draait op eigen hardware.

**Immich** — open-source fotobeheersysteem. Vervangt Google Photos. Draait op eigen hardware, gezichtsherkenning lokaal.

**Jellyfin** — open-source mediaserver. Vervangt Netflix/Spotify voor eigen videoen muziekcollecties.

**Navidrome** — open-source muziekserver. Vervangt Spotify voor eigen muziekcollectie.

**Vaultwarden** — open-source wachtwoordmanager compatibel met de Bitwarden-client. Vervangt LastPass of 1Password cloud. Draait op eigen hardware.

**Syncthing** — open-source bestandssynchronisatietool. Synchroniseert bestanden tussen apparaten zonder externe server.

**Whisper.cpp** — open-source spraak-naar-tekst model van OpenAI, geïmplementeerd in C++ voor lokale uitvoering. Vervangt cloud spraakherkenning.

---

_Onderdeel van: LocAI Bibliotheek · Thuisfront_
_Vorige: T02 — Kinderen Online_
_Dit is het laatste dossier in de thuisreeks._
_Laatste update: maart 2026_
