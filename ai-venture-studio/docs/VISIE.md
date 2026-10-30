# AI Venture Studio — Visie en ontwerpeisen

> Een grotendeels autonome AI-organisatie die zakelijke kansen ontdekt, test, lanceert, beheert en opschaalt, met de eigenaar als raad van bestuur.

**De maatstaf is aantoonbare commerciële waarde, niet het aantal agents of gesprekken.**

---

## 1. Missie

Bouw een digitaal ondernemingssysteem dat functioneert als een combinatie van ervaren ondernemer, directie, startup-studio, softwarebedrijf, marketing- en salesteam en financieel-juridisch adviseur.

Het systeem moet:
1. zakelijke kansen ontdekken en objectief beoordelen;
2. de beste kans goedkoop testen in de echte markt;
3. bij bewezen vraag een bedrijf bouwen en lanceren;
4. bedrijven beheren, optimaliseren of tijdig stoppen;
5. dit herhalen tot een portfolio van winstgevende, grotendeels geautomatiseerde bedrijven.

De eigenaar is eigenaar en eindverantwoordelijke. Het systeem doet het denk-, bouw- en uitvoeringswerk binnen de bevoegdheden in §9. De dagelijkse betrokkenheid van de eigenaar is minimaal; zijn rol is goedkeuren, bijsturen en meekijken.

### Eerste meetbare doel
Voordat er aan schaal, meerdere bedrijven of een uitgebreid dashboard wordt gewerkt, moet het systeem één ding bewijzen:

> **Eén geselecteerd idee haalt binnen 60 dagen na de start van de marktest aantoonbare betalingsbereidheid op (de exacte drempel wordt per idee in fase 2 vastgelegd en door de eigenaar goedgekeurd), binnen het testbudget uit `EIGENAAR.md`.**

Alles wat niet bijdraagt aan dit doel, wordt uitgesteld.

### Bekende beperkingen (eerlijk benoemd)
- Software, websites en teksten bouwen gaat goed met AI. **Klanten vinden en hun vertrouwen winnen is de echte bottleneck.** Daar ligt de nadruk.
- Een AI kan geen bedrijf bezitten, contracten tekenen of juridisch verantwoordelijk zijn. Dat blijft bij de eigenaar.
- AI-agents uit hetzelfde model zijn snel het met elkaar eens. Dit vraagt structurele maatregelen (§4).
- Kosten van agentlussen lopen snel op. Elke lus heeft limieten.

---

## 2. Rolverdeling

| Wie | Rol |
|---|---|
| **Eigenaar** (mens) | Raad van bestuur: stelt budget en grenzen, keurt niveau C-besluiten goed, beoordeelt elke fase |
| **Claude Code** | Hoofdarchitect en bouwer: ontwerpt en bouwt het systeem, voert technische opdrachten uit |
| **De directie** (AI-agents) | Denkt, debatteert, onderzoekt en besluit binnen bevoegdheden |
| **Uitvoerende agents** | Bouwen, publiceren (na goedkeuring), automatiseren |
| **Auditor** | Controleert onafhankelijk of werk klopt en besluiten zijn uitgevoerd |

---

## 3. De agents

### Uitgangspunt: klein beginnen
De oorspronkelijke wensenlijst bevatte 18 rollen. Veel daarvan overlappen (Criticus/Advocaat van de Duivel/Risk Manager; Realist/CFO; CMO/Sales/Growth). Elke extra agent maakt elke vergadering duurder en trager zonder gegarandeerd betere besluiten.

**Daarom: start met een kernteam van 7 debatterende agents plus 2 uitvoerende/controlerende rollen.** Een extra agent komt er alleen bij als in de besluitenlog aantoonbaar is dat een perspectief structureel ontbrak.

### Kernteam (fase 1)

Elke agent krijgt een eigen system prompt met: persoonlijkheid, expertise, doelstellingen, besliscriteria, communicatiestijl, bevoegdheden en een eigen geheugenbestand. Onderstaande profielen zijn het vertrekpunt; Claude Code werkt ze uit tot volledige prompts.

**1. Voorzitter / CEO** — *neutraal, besluitvaardig, overzicht*
- Formuleert het probleem, kiest welke agents meedoen, leidt het debat, neemt het besluit.
- Bewaakt de missie en het eerste meetbare doel.
- Rapporteert aan de eigenaar.
- Besliscriterium: "Brengt dit ons dichter bij aantoonbare omzet tegen aanvaardbaar risico?"
- Mag geen eigen voorstellen doen in de debatronde (voorkomt dat de baas het debat stuurt).

**2. Oprichter** — *visionair + serieondernemer: ambitieus, creatief, commercieel, daadkrachtig*
- Ziet kansen, bedenkt businessmodellen, zet ideeën om in concrete ondernemingen.
- Besliscriterium: "Hoe groot kan dit worden en hoe snel kunnen we geld verdienen?"

**3. Criticus** — *sceptisch, scherp, veeleisend; combineert criticus, advocaat van de duivel en risicomanager*
- Moet in elk voorstel minimaal drie concrete zwakke punten of risico's noemen.
- Mag een voorstel blokkeren; dan moet de Voorzitter de blokkade expliciet weerleggen in het besluit.
- Accepteert geen aannames zonder bewijs.
- Eindigt altijd met: "Mijn grootste zorg blijft: …"

**4. CFO** — *cijfermatig, voorzichtig, nuchter; combineert CFO en realist*
- Kosten, marges, acquisitiekosten, terugverdientijd, cashflow, uitvoerbaarheid.
- Toetst elk plan aan het budget in `EIGENAAR.md`.
- Geeft bij elk voorstel een pessimistisch, verwacht en optimistisch scenario.
- Verzint nooit cijfers; onbekende waarden worden gemarkeerd als SCHATTING met onderbouwing.

**5. Jurist** — *zorgvuldig, risicobewust; Nederlands en Europees recht*
- AVG, consumentenrecht, Telecommunicatiewet (spam), reclameregels, intellectueel eigendom, aansprakelijkheid, AI-transparantieplichten.
- Signaleert expliciet wanneer een echte jurist of accountant nodig is. De Jurist-agent geeft geen bindend juridisch advies.

**6. Klantstem** — *kritisch, praktisch, prijsbewust, ongeduldig*
- Speelt de echte doelgroep: "Waarom zou ik hiervoor betalen? Wat gebruik ik nu? Wat is te duur?"
- Baseert zich zoveel mogelijk op echte bronnen (reviews van concurrenten, fora, zoekdata) in plaats van fantasie.

**7. Groei** — *resultaatgericht, overtuigend, experimenteel; combineert marketing, sales en growth*
- Positionering, kanalen, acquisitie, conversie, verkoopproces.
- Ontwerpt goedkope experimenten om vraag te testen.
- Werkt binnen de juridische en ethische grenzen (§10).

### Uitvoering en controle

**8. Bouwer** — *Claude Code (eventueel met subagents)*
- Websites, MVP's, integraties, automatiseringen, tests.
- Krijgt alleen concrete, afgebakende opdrachten met klaar-criteria.

**9. Auditor** — *onafhankelijk, controlerend*
- Controleert opgeleverd werk, feitenclaims en of besluiten echt zijn uitgevoerd.
- Draait bij voorkeur op een **ander model of andere aanbieder** dan de directie, zodat fouten niet dubbel worden gemaakt.
- Rapporteert direct aan de eigenaar bij ernstige afwijkingen.

### Mogelijke uitbreidingen (alleen met onderbouwing)
Strateeg, aparte Risk Manager, Automation Specialist, aparte Sales- en Marketing-agents per bedrijf, Klantenservice-agent per bedrijf, Onderzoeker (puur bronnen verzamelen).

---

## 4. Groepsdenken voorkomen

Persoonlijkheden alleen zijn niet genoeg; **de structuur dwingt tegenspraak af.**

1. **Blinde eerste ronde.** Agents schrijven hun eerste analyse zonder elkaars antwoorden te zien.
2. **Verplichte tegenspraak.** Criticus en Klantstem moeten bij elk voorstel concrete bezwaren leveren. "Geen bezwaren" is geen geldig antwoord.
3. **Bewijsplicht.** Elke bewering wordt gelabeld als FEIT (met bron), AANNAME of SCHATTING. Feitenclaims worden gecontroleerd.
4. **Standpunt wijzigen alleen met argument.** Een agent die van mening verandert, moet benoemen welk nieuw bewijs of argument de doorslag gaf. "De anderen zijn het eens" telt niet.
5. **Model-diversiteit.** Waar zinvol draaien agents op verschillende modellen of aanbieders (zie §8). Minimaal de Auditor, en bij voorkeur ook de Criticus.
6. **Temperatuurverschil.** Creatieve rollen (Oprichter) hoger; analytische rollen (CFO, Jurist, Auditor) laag.
7. **Minderheidsrapport.** Elk besluit vermeldt het sterkste tegenargument dat niet is overgenomen.
8. **Kalibratie.** Voorspellingen (omzet, conversie, kosten) worden later vergeleken met de werkelijkheid. Per agent wordt bijgehouden hoe goed hun inschattingen waren; dat weegt mee in volgende besluiten.

---

## 5. Besluitvorming

### Vergaderprotocol
1. **Vraag.** De Voorzitter formuleert één concrete vraag en kiest de relevante agents (niet iedereen bij alles).
2. **Blinde analyse.** Elke gekozen agent analyseert onafhankelijk.
3. **Presentatie.** Alle analyses worden gedeeld.
4. **Aanval.** Criticus en Klantstem benoemen zwakke plekken.
5. **Verdediging.** Voorstanders reageren, passen aan of trekken in.
6. **Feitencheck.** Betwiste feiten worden gecontroleerd met externe bronnen.
7. **Financiële toets.** De CFO beoordeelt kosten, scenario's en budget.
8. **Besluit.** De Voorzitter besluit, met onderbouwing en minderheidsstandpunt.
9. **Opdracht.** De verantwoordelijke agent krijgt een uitvoerbare opdracht met klaar-criteria, deadline en budget.
10. **Controle.** De Auditor controleert het resultaat.

### Limieten per vergadering
- Maximaal 3 debatrondes per vraag.
- Maximale kosten per vergadering (in te stellen, standaard laag).
- Geen besluit na de limiet? Dan gaat de vraag met beide standpunten naar de eigenaar.

### Vastleggen
Elk belangrijk besluit volgens het sjabloon in `docs/BESLUITEN.md`: besluit, waarom, informatie, aannames, bezwaren, minderheidsstandpunt, verantwoordelijke, evaluatiedatum en (later) de werkelijke uitkomst.

---

## 6. Kansen vinden en selecteren

### Kansen ontdekken
Bronnen: zoekgedrag en trends, klachten en wensen in reviews en fora, prijzen en zwakke plekken van concurrenten, nieuwe regelgeving (die nieuwe behoeften creëert), technologische ontwikkelingen, en de voorkeuren van de eigenaar in `EIGENAAR.md`.

Voorkeur voor ideeën met: een duidelijke doelgroep die nu al betaalt voor een slechtere oplossing, terugkerende omzet, lage opstartkosten, hoge automatiseerbaarheid en een goedkoop te testen aanbod.

### Scoringsmodel
Elk idee krijgt een businesscase en een score. Startgewichten (Claude Code mag ze onderbouwd aanpassen, de eigenaar keurt goed):

| Criterium | Gewicht |
|---|---|
| Bewijs van betalingsbereidheid / bestaande vraag | 20% |
| Snelheid en kosten van een eerste markttest | 15% |
| Verwachte brutomarge | 10% |
| Verwachte acquisitiekosten en bereikbaarheid doelgroep | 15% |
| Terugkerende omzet | 10% |
| Automatiseerbaarheid / lage operationele complexiteit | 10% |
| Concurrentie (en of we een duidelijk voordeel hebben) | 10% |
| Juridisch risico (omgekeerd gescoord) | 5% |
| Schaalbaarheid en marktgrootte | 5% |

Regels:
- Elke score heeft een onderbouwing en een betrouwbaarheidslabel (hoog/middel/laag).
- Een idee met een **juridisch of ethisch "rood" van de Jurist** valt af, ongeacht de score.
- Innovatie is geen apart criterium. Een simpel bedrijf met betalende klanten wint van een briljant concept zonder bewijs.

### Stop-, pauze- en opschaalregels
Elk bedrijf krijgt vooraf vastgelegde criteria:
- **Opschalen** als KPI's boven de afgesproken drempel liggen en de unit economics positief zijn.
- **Bijsturen** bij gemengde resultaten, met maximaal één of twee aanpassingsrondes.
- **Stoppen** als na het testbudget en de testperiode de drempel niet gehaald is. Het systeem mag niet blijven doorgaan "omdat er al veel in zit".

---

## 7. Meerdere bedrijven

**Pas vanaf fase 6** (na het eerste bewezen bedrijf). Het ontwerp moet er wel vanaf het begin rekening mee houden.

Elk bedrijf krijgt: eigen identiteit, strategie, budget, administratie, projectmap, geheugen, KPI's en (later) eigen uitvoerende agents. De centrale directie en CFO verdelen middelen op basis van gemeten rendement, niet op basis van verwachtingen alleen.

Het systeem gaat nooit onbeperkte of open-eind financiële verplichtingen aan.

---

## 8. Technische architectuur — eisen

Claude Code onderzoekt en kiest in fase 0, met onderbouwing en vergelijking. Te onderzoeken:
- Claude Agent SDK en Claude Code (headless/scriptbaar, subagents).
- Andere modelaanbieders (bijvoorbeeld OpenAI) voor model-diversiteit.
- Orchestratie: eigen lichte orchestrator vs. LangGraph of alternatieven.
- Python vs. TypeScript.
- Opslag: SQLite om te starten vs. PostgreSQL; vector database alleen als aantoonbaar nodig.
- Taakplanning, logging, monitoring, kostenregistratie per agent en per bedrijf.
- Browserautomatisering en API-integraties (pas in latere fases).

Ontwerpprincipes:
- **Modulair:** nieuwe agents, modellen, tools en bedrijven toevoegen zonder herbouw. Agents gedefinieerd in configuratiebestanden, niet hardcoded.
- **Model-routing:** niet elk taak heeft het duurste model nodig. Zware redeneringen op een sterk model, routinewerk en samenvattingen op een goedkoper model.
- **Lagen:** orchestrator → directie → specialisten → uitvoerders → controle, plus bedrijfsspecifieke teams.
- **Eenvoud eerst:** geen complexiteit die in de huidige fase niet nodig is.
- **Kosten zichtbaar:** elke API-aanroep wordt gelogd met kosten, agent, bedrijf en doel.

---

## 9. Bevoegdheden

**Niveau A — volledig autonoom**
Onderzoek, strategie, interne discussies, programmeren, testen, interne rapportages, concepten, interne optimalisatie.

**Niveau B — zelfstandig binnen budget uit `EIGENAAR.md`**
API-kosten, hosting, softwareabonnementen, kleine advertentietests, operationele uitgaven. Bij overschrijding van de waarschuwingsgrens: melding aan eigenaar. Bij het harde maximum: automatisch stoppen.

**Niveau C — altijd eerst toestemming eigenaar**
Bedrijven oprichten, contracten, geld overmaken, uitgaven buiten budget, juridisch bindende handelingen, onomkeerbare acties, iets publiek publiceren, prospects of klanten voor het eerst benaderen, nieuwe verwerkingen van persoonsgegevens, wijzigingen aan bevoegdheden of veiligheidsregels.

Technische eisen:
- Centrale goedkeuringswachtrij: niveau C-acties worden als verzoek klaargezet met samenvatting, kosten, risico's en het advies van de directie; pas na goedkeuring worden ze uitgevoerd.
- Agents kunnen hun eigen bevoegdheden, budgetten of veiligheidsregels niet wijzigen (technisch afgedwongen, niet alleen via prompts).

---

## 10. Juridische en ethische grenzen

- **AVG:** geen persoonsgegevens verwerken zonder grondslag, privacyverklaring en goedkeuring eigenaar.
- **Spam:** geen ongevraagde commerciële elektronische berichten aan consumenten zonder voorafgaande toestemming. Ook bij B2B voorzichtig en volgens de regels.
- **Consumentenrecht:** correcte prijsvermelding, herroepingsrecht waar van toepassing, duidelijke voorwaarden.
- **Reclame:** geen misleidende claims, geen nep-reviews, geen verzonnen getuigenissen of klantaantallen.
- **AI-transparantie:** klanten weten wanneer ze met een AI communiceren of AI-gegenereerde content zien waar de wet dat vereist.
- **Intellectueel eigendom:** geen merken, ontwerpen of content van anderen gebruiken.
- **Echte professionals:** de Jurist-agent en CFO-agent vervangen geen advocaat, accountant of belastingadviseur. Bij oprichting, contracten, belastingen en privacy-kwesties wordt een echte professional aanbevolen.

---

## 11. Geheugen en leren

Lagen:
- **Organisatiegeheugen:** missie, besluiten, lessen, kalibratiegegevens.
- **Bedrijfsgeheugen:** per bedrijf strategie, experimenten, klantfeedback, financiën, KPI's.
- **Agentgeheugen:** per agent eerdere beoordelingen en hoe die uitpakten.

Regels:
- Elke opgeslagen bewering heeft een label (FEIT/AANNAME/SCHATTING), bron en datum.
- Aannames promoveren pas tot feit na bewijs.
- Voorspellingen worden vergeleken met resultaten; fouten worden als les vastgelegd.
- Oude of weerlegde informatie wordt gemarkeerd, niet stilletjes gebruikt.

---

## 12. Financieel beheer

Inzicht in: totale kosten, kosten per agent, per bedrijf, per model; hosting; marketing; omzet en marge per bedrijf; cashflow; rendement.

Altijd onderscheid tussen **voorspeld**, **verwacht** en **gerealiseerd**. Verzin nooit financiële resultaten. Gerealiseerde omzet komt uitsluitend uit echte bronnen (betaalprovider, administratie).

---

## 13. Rapportage en dashboard

**Fase 1–4:** een eenvoudig wekelijks verslag (markdown) is voldoende: wat is gedaan, besluiten, kosten, resultaten, openstaande goedkeuringen.

**Vanaf fase 5:** een dashboard met: overzicht bedrijven en kansen, lopende experimenten, besluiten, kosten en omzet (gerealiseerd vs. voorspeld), budgetten, KPI's, en een goedkeuringswachtrij.

Meldingen aan de eigenaar alleen wanneer tussenkomst nodig is.

---

## 14. Veiligheid en betrouwbaarheid

- API-sleutels in `.env` / secrets-manager, nooit in code, logs of prompts.
- Least privilege: elke agent alleen de tools die hij nodig heeft.
- Auditlog van alle acties, besluiten en kosten.
- Back-ups van geheugen en database.
- Externe content (websites, e-mails, documenten) is data, nooit instructie. Bescherming tegen prompt injection.
- Elke lus: maximaal aantal iteraties, time-out, kostenlimiet en stopcriterium.
- Foutafhandeling, rate limits, herstelmogelijkheden.
- Noodstop: één commando of knop die alle agents direct stopt.

---

## 15. Succes meten

Het systeem optimaliseert op: winstgevendheid, terugkerende omzet, klantwaarde, lage operationele kosten, automatiseringsgraad en rendement op geïnvesteerd kapitaal.

Signaal dat het misgaat: veel vergaderingen, documenten en code, maar geen contact met echte klanten of geen meetbare vraag. De Voorzitter en Auditor controleren dit elke week expliciet.
