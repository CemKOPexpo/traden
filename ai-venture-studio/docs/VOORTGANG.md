# Voortgang

## Huidige status
- Huidige fase: **Fase 0 — Ontwerp**
- Status: **oplevering klaar, wacht op beoordeling door de eigenaar**
- Volgende stap: de eigenaar leest `docs/ARCHITECTUUR.md` (begin bij §0 en §15) en beslist over de beslispunten hieronder. Pas na de regel "Fase 0 goedgekeurd — [datum]" begint fase 1.

## Open beslispunten voor de eigenaar
1. **Abonnement vanaf fase 1:** route A (Pro + zelf API-credits kopen, ~€72 per maand) of route B (Max 5x met $100 API-credits, ~€110 per maand). Zie ARCHITECTUUR §15a.
2. **API-grens bij route B:** de workspace-limiet op $55 houden (≈ €50, het huidige budget) of het volledige inbegrepen tegoed van $100 gebruiken?
3. **Kostenregel:** klopt het dat API-kosten binnen het goedgekeurde API-budget mogen zonder dat elke keer te vragen (niveau B), terwijl elke *nieuwe* uitgave niveau C is?
4. **Tweede modelaanbieder voor de Auditor:** nu "nee". Accepteer je het restrisico (ARCHITECTUUR §4), of later heroverwegen (~€1–3 per maand)?
5. **Aanpassingen aan FASEN.md en VISIE.md** (ARCHITECTUUR §17): testvergaderingen met echte vragen, een Auditor-criterium met ingebouwde fouten, de voorbereiding van de eigenaar (KvK/betaalprovider) al tijdens fase 2, effort in plaats van temperature.
6. **Uitgesloten sectoren en taal:** het voorstel in EIGENAAR.md (geen gokken, financieel advies, medische claims of volwassenencontent; Nederlands) bevestigen of aanpassen.
7. **Dagelijkse samenvatting:** akkoord met e-mail via GitHub Issues, een korte melding op dagen zonder nieuws, en de chat op afroep?
8. **Locatie van het project:** nu staat het in de submap `ai-venture-studio/` van de repo `traden`. Wil je liever een eigen repo? Die moet je dan zelf aanmaken.

## Wat de eigenaar zelf moet regelen (pas na goedkeuring van fase 0, vóór de testvergaderingen in fase 1)
- Een Anthropic Console-account aanmaken (platform.claude.com) en een workspace `venture-studio` met een spend limit van $55.
- Route A: credits kopen (max. €50) en automatisch bijladen UIT. Route B: overstappen op Max 5x, na 7 dagen de credits koppelen via claude.ai → Settings → Billing, en geen extra credits kopen.
- Een API-sleutel aanmaken en die als geheim in de omgeving zetten (Claude Code legt uit hoe). De sleutel nooit in de chat plakken.
- Optioneel: in de netwerkinstellingen van de omgeving docs.github.com en docs.langchain.com toestaan, zodat de twee niet-geverifieerde aannames gecontroleerd kunnen worden.

## Goedkeuringen eigenaar
<!-- De eigenaar schrijft hier: "Fase X goedgekeurd — [datum]". Zonder deze regel start de volgende fase niet. -->

## Logboek
### 2026-10-30 — Fase 0 uitgevoerd
- **Gedaan:**
  - Projectbestanden uit de zip in `ai-venture-studio/` gezet.
  - De eigenaar gebundelde vragen gesteld en de antwoorden verwerkt in EIGENAAR.md.
  - De sectie "Kosten, abonnement en API" toegevoegd aan CLAUDE.md.
  - Actuele documentatie geraadpleegd: prijzen, Agent SDK, headless, rate- en spend limits, API-credits voor Max, abonnementen.
  - ARCHITECTUUR.md geschreven (18 punten + eindaanbeveling + prompts), en de ontwerpbesluiten vastgelegd in BESLUITEN.md.
- **Getest:** niets. Er is geen code geschreven, conform fase 0.
- **Werkt / werkt niet:** n.v.t. Niet geverifieerd: de LangGraph- en GitHub Actions-documentatie, omdat die domeinen geblokkeerd zijn door het netwerkbeleid van de sessie.
- **Kosten:** €0 aan API. Alleen gebruik van het Claude-abonnement voor het bouwen.
- **Volgende stap:** beoordeling door de eigenaar.
