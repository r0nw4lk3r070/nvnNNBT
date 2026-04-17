# T03 — Smart Home
### LocAI Library · Home Front
_Version 0.1 · March 2026_

---

## The house that watches

You live in it. You trust it. You've filled it with devices that make life easier, more comfortable, more connected.

And every one of those devices sees you.

Not in the way a camera sees you. More subtle. More persistent. A pattern of behaviours that builds up over years, transferred to servers you've never seen, processed by algorithms you've never chosen, sold to parties you've never met.

This is the third dossier in the Home Front series. T01 covered family and data — what we share about those we love. T02 covered children online — what platforms do with the next generation. This dossier is about the home itself as an infrastructure for data collection.

---

## The devices and what they really do

### Your router

The router is the front door of your home network. Every device in your home communicates through it.

**The Odido/Lifemote case (2024):** Odido — a Dutch telecoms provider — sent customer device data to Lifemote, a Turkish AI startup, for three years without disclosure to customers. Which devices were in the home, how often they were used, when they were active. The data was used to "optimise the network." After publication the issue was patched silently, five days later, without a press release. No apology was issued.

This was not a hack. This was business as usual. Your router's manufacturer or provider may have similar arrangements.

---

### Your smart TV

The smart TV in your living room is one of the most aggressive data collection devices in the average household.

**Samsung ACR:** Automatic Content Recognition. Every 500 milliseconds Samsung's smart TV takes a screenshot of everything on screen — not only streaming content, but also whatever else is playing. The screenshot is matched against a database and used to build a viewing profile. That profile is sold to Google, advertisers, and data networks.

**The Vizio case:** Vizio once made twice as much revenue from selling viewing data as from selling the TVs themselves. The hardware was subsidised by the behaviour it could capture. You didn't buy a television. You became the product.

**How to stop it:** Settings → Support → Terms & Privacy → Viewing Experience Services → disable. But the next firmware update may turn it back on. The only radical solution: use a "dumb" HDMI streaming stick and ignore the smart TV's built-in functions entirely.

---

### Your smart speaker

"Alexa, turn off the lights." "Hey Google, what's the weather?"

These devices are continuously listening. Not everything is processed — there is a threshold sensor for the wake word. But the wake word threshold sometimes triggers incorrectly. And when it triggers, everything that follows is sent to a server.

**The human reviewers:** Amazon, Google and Apple all employ teams that listen to recordings to improve speech recognition. This was confirmed in multiple investigations. You agreed to this in the terms of service you didn't read.

**The location:** the microphone is always on. The server is in Virginia, or Frankfurt, or Tokyo. What you say in the kitchen goes to a data centre on another continent.

A living room without a smart speaker is quieter in the most literal sense.

---

### Your smartphone

Your smartphone is the most comprehensive tracking device ever placed in consumer hands.

It knows where you slept last night — and every night for the past three years. It knows when you left home, how long you were away, and where you went. It knows who you called, for how long, and at what time. It knows which apps you opened, how long you used them, and what you tapped.

Google Maps Timeline until 2023 stored this location history centrally — accessible to Google. After public pressure it moved "on-device" storage — but it still exists, still searchable, and still exported and sold to data brokers in market-wide agreements.

**Location data and law enforcement:** in the United States, location data is routinely sold to law enforcement without a court order. In Europe this practice is theoretically limited by GDPR — but the data brokers selling this data are not always based in Europe.

---

### Meta Ray-Ban smart glasses

In 2025, approximately 7 million pairs were sold. Marketing: "Designed for privacy, controlled by you."

**What happened:** the camera footage went to Meta servers. Filtered to Nairobi. Reviewed by workers at Sama — a content moderation firm. Some of those workers saw women undressing. People having sex. Intimate moments in private spaces, recorded because the glasses were present.

Meta confirmed this. Faces were "blurred," but the workers said inconsistently. The "designed for privacy" promise was a marketing message, not a technical guarantee.

**The broader point:** when a device is designed to capture the world around you — always connected, always uploading — "privacy" is not a feature. It is an absence of specific harm, until it isn't.

---

### Your smart doorbell

Ring and Nest doorbells built a video archive of everyone approaching your front door. Amazon (Ring) shared this footage with police departments in the United States without requiring a warrant — on request, using an informal network. Thousands of police departments, millions of homes.

In Belgium and the Netherlands, GDPR provides more protection — but the data still sits on Amazon's servers. The archive exists. What happens to it falls under the terms of Amazon's privacy policy, not under your expectations as a homeowner.

---

### Your Nest thermostat

Google's Nest thermostat knows:
- When you are home
- When you leave
- When you sleep
- How warm you keep your house
- How long your heating takes to reach temperature

This is a detailed daily pattern of life in your home. Combined with your other Google data — location, search, Gmail — it adds another layer to a profile that already knows you intimately.

---

### Your baby monitor

The baby monitor connected to the manufacturer's servers is one of the few devices where security failures have caused direct harm. Poorly secured cameras have been accessed by strangers. Some manufacturers store footage indefinitely. The market pressure is on features, not on security.

---

## The home as a data factory

What leaves a typical European home on a normal day:

| Device | What it sends |
|---|---|
| Smart TV | Viewing behaviour → ad profile |
| Smart speaker | Voice data → model improvement |
| Router | Device inventory → household profile |
| Smartphones | Location data → physical targeting |
| Nest thermostat | Presence patterns → insurance profile |
| Smart doorbell | Visitor footage → law enforcement access |
| Baby monitor | Interior footage → manufacturer servers |
| Laptop/browser | Browsing behaviour → ad network |

All of this value is created in your home. The labour is yours: your behaviour, your conversations, your patterns of life. The value flows to external servers. You receive convenience in exchange.

That exchange was never explicitly offered. You didn't sign it. It emerged gradually, device by device, update by update.

---

## The scale of the fine is not the measure of the harm

Since GDPR came into force in 2018, approximately €5.88 billion in fines have been issued across Europe.

Meta received the largest single fine: €1.2 billion (2023, Irish DPA, for GDPR violations involving US data transfers). 

Meta's revenue in 2023: approximately €134 billion. The €1.2 billion fine equals roughly four days of revenue.

As one analyst wrote:

> "The fine is not a punishment. It is a tax on data theft. Built into the spreadsheet. Cheaper than compliance."

GDPR fines are a cost of business for the largest platforms, not a deterrent. The protection comes not from the regulator but from the architecture: data that does not leave your home cannot be fined for how it is used.

---

## The postman analogy

From *The Great Return* (Ron Spoelstra, 2025):

Imagine a smart speaker in your living room as a postman who moves into your house. He doesn't deliver post — he listens. All day, every day. Everything said in the kitchen, the living room, the bedroom. Every evening he writes a report and sends it to his employer.

You agreed to this. It was in paragraph 47 of the terms of service.

A local AI assistant is a different kind of postman. He brings what you need — answers, reminders, help — and then leaves. He doesn't inventory your house. He doesn't send nightly reports. He works for you, not for the platform that deployed him.

The question is not whether you want a postman. The question is what kind.

---

## Local alternatives

You do not have to replace everything at once. But for each cloud service there is a local alternative — free, stable, and yours.

| Cloud service | Local alternative |
|---|---|
| Google Calendar | Nextcloud Calendar |
| Google Drive / iCloud | Nextcloud / Syncthing |
| Google Photos | Immich (local, with AI photo search) |
| Spotify | Navidrome + own collection |
| Google Keep / Notion | Obsidian (local) / Joplin |
| ChatGPT / Alexa | Ollama + open-weight model |
| Gmail | ProtonMail / own mail server |
| LastPass / 1Password cloud | Vaultwarden (local Bitwarden) |

Each of these alternatives requires a one-time setup. After that they run independently, without subscription, without the data leaving your home.

---

## AETHER — a reference implementation

AETHER is a home infrastructure built on repurposed desktop hardware. Three months of stable operation, tested for daily household use.

What it replaced:
- Google Calendar → Nextcloud Calendar
- Google Drive → Nextcloud + Syncthing
- Google Photos → Immich with local AI-powered search
- ChatGPT → Ollama with locally running open-weight model
- Various cloud subscriptions → local services on one machine

Hardware: old desktop PC, refurbished, no new investment required.

What it proved: you don't need a technical background. You need one afternoon of setup and the willingness to let go of the familiar interface. After that, the local infrastructure is quieter, faster for local tasks, and completely yours.

AETHER is not a product. It is a demonstration of what is possible — on ordinary hardware, for an ordinary household, today.

---

## Where to start: four steps

### Today — free — 30 minutes

1. **Smart TV:** go into settings and disable ACR (Automatic Content Recognition). On Samsung: Settings → Support → Terms & Privacy → Viewing Experience Services. Note: a firmware update may re-enable this. Check after every major update.
2. **Google Maps:** disable Timeline. Go to myaccount.google.com → Data & Privacy → Location History.
3. **Ad personalisation:** myaccount.google.com → Data & Privacy → Ad personalisation → disable.
4. **Smart speakers:** move them out of bedrooms. The bedroom is the one space where continuous listening is most uncomfortable.

---

### This weekend — €50-100

1. **Pi-hole on Raspberry Pi:** a network-level ad and tracker blocker. All devices on your network are protected without anything being installed on each one. Blocks known tracker domains before the data can leave.
2. **Signal** instead of WhatsApp: end-to-end encrypted by default, no meta-data sold, open source.
3. **DuckDuckGo** as default search engine: no profile building, no filter bubble, comparable results.

---

### This quarter — €150-300

1. **Nextcloud** on an old laptop or mini-PC: your own cloud for files, calendar, contacts. Accessible from all your devices.
2. **Immich** for photos: local Google Photos with automatic backup from smartphone, face recognition, searchable by content.
3. **Jellyfin** for media: your own Netflix for films and series you own. **Navidrome** for music.

---

### This year — €800-1,500

A modern mini-PC with AMD Ryzen AI Max+ or equivalent, sufficient to run a 70B open-weight model locally. This is the AETHER architecture: full local AI for the whole household.

What this enables:
- A local AI assistant that knows nothing about you except what you tell it in that session
- Document analysis without anything leaving your home
- Voice commands processed locally, without microphones connected to external servers
- Local photo search ("show me photos of the children at the seaside") without uploading to Google

This is not a future technology. It runs today, on available hardware, with free open-source software.

---

## The awareness is not enough on its own

After the Odido/Lifemote story was published, Odido silently patched the data transfer within five days. No press release. No apology. No compensation for three years of data transferred without consent.

The awareness is not enough on its own. Knowing that your television watches you does not stop it watching you.

The knowledge creates the demand for an alternative. The hardware to build that alternative exists. The software to run it is free and open. The only thing missing is the moment when you decide that enough is enough.

---

## Glossary

**ACR (Automatic Content Recognition)** — technology in smart TVs that takes screenshots at regular intervals and matches them against a database of known content. Used to build viewing profiles. On by default on most Samsung, LG and other major smart TV brands.

**Data broker** — company whose core business is buying, processing and reselling personal data. Data brokers aggregate data from many sources — loyalty cards, app permissions, location data, public records — into detailed profiles. Most consumers have never heard of data brokers that hold detailed profiles about them.

**CLOUD Act (Clarifying Lawful Overseas Use of Data Act, US, 2018)** — US legislation that allows American authorities to demand access to data held by US companies, even if that data is stored on servers outside the United States. The existence of the CLOUD Act is one legal reason why EU data on US cloud platforms is legally complex under GDPR.

**Ollama** — open-source tool for running large language models locally on your own hardware. Supports dozens of open-weight models. Free and available for Windows, Mac and Linux.

**Whisper.cpp** — local implementation of OpenAI's Whisper speech recognition model. Runs entirely on your own hardware without internet. Audio never leaves the device.

**Pi-hole** — open-source network-level ad and tracker blocker. Runs on a Raspberry Pi or other small device on your network. Blocks known tracker and advertiser domains before the request reaches external servers.

**Nextcloud** — open-source platform for self-hosted file storage, calendar, contacts, and collaboration tools. Often described as a self-hosted alternative to Google Drive and Google Workspace.

**Immich** — open-source, self-hosted photo and video management platform. Alternative to Google Photos, with automatic smartphone backup and AI-powered search.

**Syncthing** — open-source file synchronisation tool. Synchronises folders between devices without any central server. Data travels directly from one device to another, encrypted.

**Vaultwarden** — open-source, self-hosted password manager compatible with the Bitwarden app. Alternative to cloud-based password managers. Password database stays on your own system.

**Navidrome** — open-source, self-hosted music server. Streams your own music collection to any device. Alternative to Spotify for music you own.

**Jellyfin** — open-source, self-hosted media server. Streams video files from your own collection to any device. Alternative to Netflix for films and series you own.

---

_Part of: LocAI Library · Home Front_
_Previous: T02 — Children Online_
_Sector dossiers: S01-S05_
_Last updated: March 2026_
