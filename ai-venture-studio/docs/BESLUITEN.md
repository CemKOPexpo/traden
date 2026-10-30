# Besluitenlog

Elk belangrijk besluit (technisch of zakelijk) volgens dit sjabloon:

---
### [Datum] — [Korte titel]
- **Besluit:**
- **Waarom:**
- **Gebruikte informatie (met bronnen):**
- **Aannames:**
- **Bezwaren en minderheidsstandpunt:**
- **Verantwoordelijke:**
- **Evaluatie op:**
- **Uitkomst bij evaluatie:** (later invullen: klopte de voorspelling?)
---

<!-- Fase 0 — Ontwerpbesluiten (2026-10-30). Status "voorstel" = wacht op akkoord eigenaar. -->

---
### 2026-10-30 — Eigen lichte orchestrator in Python op de Anthropic SDK
- **Besluit:** De directie draait op een eigen Python-orchestrator die de Messages API aanroept via de officiële `anthropic`-SDK. Geen LangGraph, Agent SDK of Managed Agents voor de directie. *Status: voorstel.*
- **Waarom:** Het vergaderprotocol is een vaste pijplijn. Eigen code geeft per aanroep controle over kosten, schema's, caching en Batch, met de minste afhankelijkheden.
- **Gebruikte informatie (met bronnen):** ARCHITECTUUR §6; B1, B2, B3 (geraadpleegd 2026-10-30).
- **Aannames:** ±500–800 regels kerncode volstaan (SCHATTING). De voordelen van LangGraph zijn niet geverifieerd (de documentatie was niet bereikbaar).
- **Bezwaren en minderheidsstandpunt:** Met een framework is er minder eigen code om te onderhouden. Ook kan de Agent SDK hooks en budgetten "gratis" leveren. Niet overgenomen, omdat dat voor een lineair debat meer complexiteit oplevert dan het bespaart.
- **Verantwoordelijke:** Claude Code (hoofdarchitect)
- **Evaluatie op:** einde fase 1
- **Uitkomst bij evaluatie:**
---
### 2026-10-30 — Agents draaien via de API-sleutel, niet via de abonnementslogin
- **Besluit:** Agents gebruiken een API-sleutel uit een Console-organisatie, nooit de claude.ai-login. *Status: voorstel.*
- **Waarom:** Via de login gebruiken ze dezelfde limieten als het bouwen (B6). De 5-uurslimieten maken autonome runs onbetrouwbaar. Anthropic staat claude.ai-login in producten niet toe (B2). En de API geeft exacte kostenregistratie.
- **Gebruikte informatie (met bronnen):** B2, B3, B6.
- **Aannames:** geen.
- **Bezwaren en minderheidsstandpunt:** Via de login zou het "gratis" zijn binnen het abonnement. Niet overgenomen vanwege de betrouwbaarheid, de regels van Anthropic en de kosteninzichtelijkheid.
- **Verantwoordelijke:** Claude Code
- **Evaluatie op:** einde fase 1
- **Uitkomst bij evaluatie:**
---
### 2026-10-30 — Modelrouting: Sonnet 5.5 standaard, Opus 5.5 voor besluit, kritiek en audit, Haiku 5.5 voor samenvatten
- **Besluit:** Zoals in ARCHITECTUUR §11. Fable 5.1 wordt niet gebruikt. *Status: voorstel.*
- **Waarom:** Kosten. Een gemiddelde vergadering kost ~€1,30, en met Opus voor alle agents ~€4,70. Bovendien geeft het enige modeldiversiteit binnen één aanbieder.
- **Gebruikte informatie (met bronnen):** B1-prijzen, rekenmodel §15b.
- **Aannames:** Sonnet 5.5 is goed genoeg voor de debatrollen (te meten in fase 1).
- **Bezwaren en minderheidsstandpunt:** Echte diversiteit vraagt een tweede aanbieder (VISIE §4.5). De eigenaar wil dat nu niet. Dit restrisico is vastgelegd in §4 en §18.
- **Verantwoordelijke:** Claude Code
- **Evaluatie op:** einde fase 1 (gemeten kosten en kwaliteit)
- **Uitkomst bij evaluatie:**
---
### 2026-10-30 — Opslag: SQLite + markdown, geen vectordatabase
- **Besluit:** Eén SQLite-bestand voor de staat, kosten en het geheugen, met `bedrijf_id` in elke tabel. Leesbare verslagen in markdown. *Status: voorstel.*
- **Waarom:** Geen server nodig, eenvoudig, en het volstaat tot fase 6.
- **Gebruikte informatie (met bronnen):** VISIE §8; ARCHITECTUUR §11–12.
- **Aannames:** Er is één schrijver tegelijk.
- **Bezwaren en minderheidsstandpunt:** Een binair bestand in git geeft een rommelige historie. Daarom volgt een periodieke JSONL-dump.
- **Verantwoordelijke:** Claude Code
- **Evaluatie op:** einde fase 2
- **Uitkomst bij evaluatie:**
---
### 2026-10-30 — Draaien: fase 1 in een Claude Code-sessie, vanaf fase 2 via GitHub Actions; goedkeuringen en meldingen via GitHub Issues
- **Besluit:** Geen eigen computer en geen VPS. *Status: voorstel.*
- **Waarom:** De eigenaar heeft geen technische kennis en wil er weinig tijd in steken. GitHub stuurt automatisch e-mail en heeft een mobiele app voor goedkeuringen. De verwachte hostingkosten zijn €0.
- **Gebruikte informatie (met bronnen):** ARCHITECTUUR §11, §13, §14.
- **Aannames:** Het gratis Actions-tegoed volstaat. Niet geverifieerd, want docs.github.com was niet bereikbaar. Dit wordt gecontroleerd vóór fase 2.
- **Bezwaren en minderheidsstandpunt:** Afhankelijkheid van GitHub. Daarom blijft alles ook handmatig te draaien.
- **Verantwoordelijke:** Claude Code
- **Evaluatie op:** start fase 2
- **Uitkomst bij evaluatie:**
---
### 2026-10-30 — Budgetafdwinging in vier lagen; elke nieuwe uitgave is niveau C
- **Besluit:** (1) Console-credits zonder automatisch bijladen. (2) Een workspace spend limit van $55. (3) Een budgetbewaker in code die vóór elke aanroep het maximum controleert, staat 10% onder de Console-grens, waarschuwt bij 80% en stopt bij 100%. (4) Een noodstop. Op instructie van de eigenaar is elke nieuwe uitgave niveau C. *Status: voorstel.*
- **Waarom:** De eigenaar wil "nooit overschrijden, altijd vragen".
- **Gebruikte informatie (met bronnen):** B4, B5; EIGENAAR.md.
- **Aannames:** geen.
- **Bezwaren en minderheidsstandpunt:** Strenge goedkeuring vertraagt experimenten in fase 3. Daarom wordt er per idee een vooraf goedgekeurd testbudget gebruikt.
- **Verantwoordelijke:** Claude Code
- **Evaluatie op:** einde fase 1 (limiettests)
- **Uitkomst bij evaluatie:**
---
### 2026-10-30 — `temperature` vervangen door effort- en promptverschillen
- **Besluit:** VISIE §4.6 wordt technisch uitgevoerd met `effort`-niveaus en rolinstructies. *Status: voorstel (wijziging van VISIE).*
- **Waarom:** Vanaf API-versie 2026-10-21 geeft `temperature` een 400-fout op alle modellen (B8).
- **Gebruikte informatie (met bronnen):** B8.
- **Aannames:** geen.
- **Bezwaren en minderheidsstandpunt:** geen.
- **Verantwoordelijke:** Claude Code
- **Evaluatie op:** einde fase 1
- **Uitkomst bij evaluatie:**
---
