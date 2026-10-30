# Plan: Daytrade-bot met Claude Code

> **Eerst eerlijk:** geen enkele trader, mens of AI, maakt geen fouten. Ik kan de koers van morgen
> niet voorspellen, en het grootste deel van de particuliere daytraders verliest geld. Daarom gaan we
> er in dit plan niet van uit dat de bot "altijd gelijk heeft". We bouwen hem zo dat hij **verliezen
> beperkt als hij ongelijk heeft**. Risicobeheer is het belangrijkste onderdeel van dit plan, niet
> een bijzaak. Dit plan is geen financieel advies.

---

## 1. Rolverdeling: wat doet Claude, wat doet de bot?

Een veelgemaakte fout is een taalmodel elke paar seconden laten beslissen over kopen of verkopen.
Een LLM is daar te traag en te onvoorspelbaar voor, en het is niet goed te backtesten. Daarom verdelen
we het werk zo:

| Onderdeel | Wie | Waarom |
|---|---|---|
| Orders plaatsen, stops bewaken, signalen berekenen | **Deterministische Python-bot** | Snel, herhaalbaar, te backtesten |
| Strategie ontwerpen, code schrijven, backtests analyseren | **Claude Code (samen met jou)** | Daar ben ik sterk in |
| Pre-market briefing: nieuws, earnings, macro-agenda | **Claude (geplande taak)** | Veel tekst samenvatten en beoordelen |
| Nieuws-sentiment per aandeel (filter: wel/niet traden) | **Claude API** als classificatie-stap | Score komt als input in de regels |
| Dagevaluatie, tradejournaal, verbeterpunten | **Claude (na sluiting)** | Leren van fouten |
| Eindverantwoordelijkheid, kill switch | **Jij** | Het is jouw geld |

---

## 2. Benodigde onderdelen

### 2.1 Broker-koppeling (met API)
Belangrijk: **DEGIRO heeft geen officiële API**, dus die valt af. Opties voor iemand in Nederland
(beschikbaarheid en voorwaarden vooraf zelf nagaan):

| Broker | Markten | API | Opmerking |
|---|---|---|---|
| **Interactive Brokers** | Aandelen VS/EU, opties, futures, forex | TWS / IB Gateway (Python: `ib_async`) | Beschikbaar in NL, lage kosten, gratis paper account. **Aanbevolen start.** |
| **Saxo Bank** | Aandelen, CFD's, forex | OpenAPI (REST) | Nederlandse aanwezigheid, gratis simulatie-omgeving |
| **Alpaca** | Aandelen VS, crypto | REST + websocket, er bestaat ook een MCP-server | Paper trading erg makkelijk; check of je als NL-ingezetene een live account kunt openen |
| **Bitvavo / Kraken** | Crypto | REST + websocket | 24/7 markt, hoge volatiliteit |

Aandachtspunten:
- **PDT-regel (VS):** bij Amerikaanse brokers gold voor margin-accounts een minimum van $25.000 om
  vaak te daytraden. Aan deze regel wordt gesleuteld; check de actuele status bij je broker.
- API-sleutels **zonder opnamerechten**, opgeslagen in een `.env`-bestand dat nooit in git komt.
- Stop-losses altijd **bij de broker** plaatsen (bracket/OCO-orders), niet alleen in onze code.
  Valt de bot uit, dan blijft de stop staan.

### 2.2 Marktdata
- Realtime koersen en candles (1m/5m): eerst via de broker, later eventueel Polygon, Databento of
  Alpaca Data.
- Historische data voor backtests: minstens 2 tot 3 jaar aan minuutdata.
- Level 2 / orderboek is pas nodig voor geavanceerdere strategieën.

### 2.3 Nieuws en actualiteit
- **Nieuwsfeeds:** Benzinga (via Alpaca), Finnhub, Marketaux, RSS van Reuters en andere persbureaus.
- **Economische kalender:** rentebesluiten (Fed/ECB), CPI, banencijfers (NFP). Standaardregel:
  **geen nieuwe posities van 5 min vóór tot 15 min ná** grote macro-cijfers.
- **Earnings-kalender:** geen positie aanhouden in een aandeel met cijfers op dezelfde dag, tenzij de
  strategie daar juist op gebouwd is.
- **Claude-sentimentlaag:** koppen per ticker worden beoordeeld als positief, negatief of neutraal,
  samen met de relevantie. Dat werkt als **filter**, niet als koop-signaal op zichzelf.
- **Halts / LULD:** handelsstops herkennen en niet blind doorhandelen.

### 2.4 Scanner (welke aandelen vandaag?)
Elke ochtend een watchlist samenstellen op basis van:
- Gap-up/gap-down groter dan 3% ten opzichte van het vorige slot
- Relatief volume groter dan 2x het gemiddelde
- Liquiditeit: koers boven $5, gemiddeld dagvolume boven 1 miljoen, kleine spread
- Een duidelijke "catalyst": nieuws, cijfers, upgrade of downgrade

### 2.5 Patroonherkenning en strategieën
We beginnen met **1 of 2 eenvoudige, bewezen en goed testbare** strategieën en breiden pas uit als
die werken:

1. **Opening Range Breakout (ORB):** de range van de eerste 5 tot 15 minuten bepalen en handelen op
   een uitbraak met volume.
2. **VWAP-pullback/reclaim:** in een trend instappen bij een terugval naar de VWAP.
3. **Momentum op nieuws:** gapper met catalyst, instap op de eerste pullback ("bull flag").

Technische bouwstenen: VWAP, EMA 9/20, ATR (voor de stopafstand), RSI, volumeprofiel,
support/resistance-niveaus, candlestickpatronen (via `pandas-ta` of `TA-Lib`).

Machine learning (bijvoorbeeld een classifier op features) komt **pas later**, en alleen met strenge
out-of-sample tests. Het grootste gevaar is **overfitting**: een strategie die perfect werkt op het
verleden en faalt in de praktijk.

### 2.6 Risicobeheer (niet onderhandelbaar)
| Regel | Startwaarde |
|---|---|
| Risico per trade | max **0,5 tot 1%** van het account |
| Positiegrootte | `risico € / (instap − stop)` |
| Dagelijks verlieslimiet | **−2%**, daarna stopt de bot voor de rest van de dag |
| Wekelijkse verlieslimiet | **−5%**, daarna pauze en evaluatie |
| Max gelijktijdige posities | 3 |
| Max trades per dag | 10 (tegen overtrading) |
| Alles sluiten | 10 min vóór het slot (geen overnight risico) |
| Kill switch | 1 commando of 1 Telegram-bericht sluit alles en stopt de bot |
| Sanity checks | geen order als de spread te groot is, de data ouder is dan X sec of de positie te groot is |

### 2.7 Infrastructuur
- **Taal:** Python 3.12
- **Hosting:** een kleine VPS (stabiel, dicht bij de beurs), niet je laptop
- **Opslag:** SQLite/PostgreSQL voor trades, signalen, logs
- **Monitoring:** Telegram-bot voor meldingen (trade, fout, verlieslimiet geraakt)
- **Backtesting:** `vectorbt` of `backtrader`, met realistische kosten en slippage
- **Claude-integratie:** geplande Claude Code-taken (pre-market, post-market) plus een MCP-server
  voor de broker, zodat je mij in gewone taal kunt vragen hoe de posities ervoor staan

---

## 3. Architectuur

```
traden/
├── config/            # instellingen, risicolimieten (yaml)
├── src/
│   ├── data/          # marktdata + nieuws ophalen
│   ├── scanner/       # dagelijkse watchlist
│   ├── strategies/    # ORB, VWAP, ... (elk een losse module)
│   ├── risk/          # positiegrootte, limieten, kill switch
│   ├── execution/     # broker-adapter (IBKR / Alpaca / paper)
│   ├── ai/            # Claude: sentiment, briefing, evaluatie
│   └── monitor/       # Telegram, logging, dashboard
├── backtest/          # backtests en rapporten
├── tests/             # unit tests (vooral risk + execution!)
└── .env.example       # API-sleutels (echte .env nooit committen)
```

Datastroom: `Data → Scanner → Strategie (signaal) → Nieuwsfilter → Risk Manager (goedkeuren/afwijzen) → Execution → Log/Telegram`

De **Risk Manager heeft altijd het laatste woord**: ook een "perfect" signaal wordt afgewezen als een
limiet geraakt is.

---

## 4. Fasering

| Fase | Inhoud | Duur | Klaar als... |
|---|---|---|---|
| **0. Keuzes** | Markt, broker, kapitaal, tijdsinvestering vastleggen | 1 week | Beslissingen in dit document |
| **1. Fundament** | Projectstructuur, broker-koppeling (paper), data ophalen, logging | 1–2 weken | Bot leest live koersen en plaatst een paper-order |
| **2. Strategie + backtest** | ORB implementeren, backtest op 2–3 jaar met kosten/slippage | 2–3 weken | Positieve verwachtingswaarde out-of-sample, max drawdown acceptabel |
| **3. Risk + nieuws** | Risk manager, kill switch, nieuwsfilter, macro-kalender | 1–2 weken | Alle risicoregels hebben tests |
| **4. Paper trading** | Volledig automatisch op een paper account | **min. 4–8 weken** | Resultaten lijken op de backtest |
| **5. Klein live** | Echt geld, maar een klein bedrag dat je kunt missen | 1–3 maanden | Stabiel, geen technische incidenten |
| **6. Opschalen** | Kapitaal of strategieën geleidelijk uitbreiden | doorlopend | Op basis van data, niet van gevoel |

Mijn advies is om het begin van fase 5 **semi-automatisch** te doen: de bot stelt een trade voor,
jij keurt die goed met één tik in Telegram. Volledig automatisch pas als het vertrouwen er is.

---

## 5. Wat het je kost (indicatie)
- Broker: €0 vast (IBKR/Alpaca), per trade een kleine commissie
- Marktdata: €0 tot €100+ per maand, afhankelijk van de bron
- VPS: €5 tot €20 per maand
- Claude API voor sentiment en briefings: beperkt, enkele euro's tot tientjes per maand
- **Belasting (NL):** intensief daytraden kan door de Belastingdienst gezien worden als box 1
  (resultaat uit overige werkzaamheden) in plaats van box 3. Overleg dit met een belastingadviseur.

---

## 6. Beslissingen die jij moet nemen
1. **Welke markt?** Amerikaanse aandelen (meeste liquiditeit en data), Europese aandelen, crypto
   (24/7) of forex/futures?
2. **Welke broker?** Mijn voorkeur: Interactive Brokers (of Alpaca als je alleen in de VS handelt en
   snel wilt beginnen).
3. **Startkapitaal** voor de live fase, en hoeveel je maximaal wilt kunnen verliezen.
4. **Automatisering:** volledig automatisch, of eerst met jouw goedkeuring per trade?
5. **Tijd:** hoeveel uur per dag kun je meekijken? (De Amerikaanse beurs is 15:30 tot 22:00 NL-tijd.)
