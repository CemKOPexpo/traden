# Fasenplan

Elke fase bewijst iets voordat de volgende begint. Claude Code werkt aan één fase tegelijk en stopt bij het stopmoment.

Een fase is pas afgerond als:
1. alle klaar-criteria aantoonbaar gehaald zijn (getest, niet alleen gebouwd);
2. er een faseverslag is in `docs/verslagen/fase-X.md`;
3. de eigenaar in `docs/VOORTGANG.md` heeft geschreven: "Fase X goedgekeurd — [datum]".

Haalt een fase de criteria niet? Dan schrijft Claude Code een verslag met oorzaak en voorstellen, en beslist de eigenaar: opnieuw proberen, aanpassen of stoppen.

---

## Fase 0 — Ontwerp
**Bewijst:** het plan is doordacht, haalbaar en betaalbaar.

**Oplevering:** `docs/ARCHITECTUUR.md` met antwoorden op:
1. De aanbevolen architectuur (met diagram in tekst of Mermaid).
2. Welke agents nodig zijn en waarom (start met kernteam uit VISIE §3).
3. Persoonlijkheden en uitgewerkte system prompts voor het kernteam.
4. Hoe groepsdenken technisch wordt voorkomen.
5. Hoe besluitvorming technisch werkt.
6. Hoe agents samenwerken (orchestratie, berichten, gedeelde staat).
7. Hoe meerdere bedrijven later worden ondergebracht (ontwerp, nog niet bouwen).
8. Hoe het systeem kansen ontdekt.
9. Hoe het systeem kansen selecteert (scoringsmodel).
10. Hoe budget en kosten worden bewaakt en afgedwongen.
11. Welke modellen en technologieën, met vergelijking en onderbouwing.
12. Geheugenarchitectuur.
13. Rapportage nu en dashboard later.
14. Hoe autonomie en goedkeuring technisch werken.
15. Kostenraming in drie scenario's (zuinig / gemiddeld / intensief), per maand, voor bouwen én draaien, met duidelijke aannames.
16. Wat technisch nu haalbaar is en wat menselijke tussenkomst blijft vragen.
17. De route naar een werkend prototype, met eventuele aanpassingen aan dit fasenplan.
18. De grootste risico's en technische beperkingen.

Plus: één duidelijke eindaanbeveling.

**Klaar wanneer:** document compleet, keuzes onderbouwd met actuele documentatie, kostenraming realistisch en gebaseerd op actuele prijzen (met bron en datum).

**Budget:** alleen ontwikkelkosten van Claude Code zelf.
**Stopmoment:** na oplevering. Niet beginnen met bouwen.

---

## Fase 1 — Fundament en directie
**Bewijst:** de agents denken aantoonbaar verschillend en komen tot onderbouwde besluiten.

**Oplevering:**
- Projectstructuur, configuratie, `.env`-afhandeling, logging, kostenregistratie per aanroep.
- Orchestrator met het kernteam (7 directie-agents + Auditor), agents gedefinieerd in configuratiebestanden.
- Vergaderprotocol uit VISIE §5, inclusief blinde ronde, verplichte tegenspraak, limieten.
- Geheugen (organisatie + per agent) met labels FEIT/AANNAME/SCHATTING.
- Vergaderverslagen en besluitenlog als leesbare markdown.
- Kostenlimieten en noodstop, technisch afgedwongen.
- Tests.

**Klaar wanneer:**
- Drie testvergaderingen over verschillende vragen zijn gehouden en de verslagen tonen echte tegenspraak, standpuntwijzigingen met argument, en een minderheidsrapport.
- De Auditor heeft minstens één fout of zwakke onderbouwing gevonden in de testvergaderingen (bewijs dat controle werkt).
- Kosten per vergadering zijn gemeten en passen binnen budget.
- De noodstop en kostenlimiet zijn getest.

**Stopmoment:** faseverslag met de drie vergaderverslagen.

---

## Fase 2 — Kansen vinden en kiezen
**Bewijst:** het systeem kiest verstandige, testbare ideeën op basis van echte bronnen.

**Oplevering:**
- Onderzoeksmodule met webonderzoek (externe content behandeld als data, niet als instructie).
- Scoringsmodel uit VISIE §6, configureerbaar.
- Minimaal 10 ideeën met korte businesscase, top 3 met volledige businesscase.
- Per top-3-idee: doelgroep, aanbod, prijs, concurrenten met bronnen, testplan, testbudget en een **concrete succesdrempel** voor de markttest.

**Klaar wanneer:** de eigenaar vindt de top 3 geloofwaardig, alle feitenclaims hebben bronnen, en de eigenaar kiest één idee met bijbehorende drempel.

**Stopmoment:** keuze eigenaar.

---

## Fase 3 — Eerste markttest
**Bewijst:** er is echte vraag naar het gekozen idee.

**Oplevering:**
- Naam, positionering, landingspagina of eenvoudig aanbod.
- Meting (bezoekers, aanmeldingen, voorverkopen) privacyvriendelijk ingericht.
- Een acquisitie-experiment binnen budget en binnen de juridische grenzen.
- Alles wat publiek gaat of klanten benadert: eerst via de goedkeuringswachtrij (niveau C).

**Klaar wanneer:** de testperiode voorbij is of de drempel gehaald is. Resultaat wordt eerlijk gerapporteerd, ook als het tegenvalt.

**Stopmoment:** verslag met advies: doorgaan, aanpassen of stoppen (en dan terug naar fase 2 met het volgende idee).

---

## Fase 4 — Eerste bedrijf
**Bewijst:** mensen betalen, en het kan grotendeels automatisch draaien.

**Oplevering:** MVP, betaalproces (na goedkeuring en met de juiste juridische basis), onboarding, klantenservice-automatisering, KPI's, eerste optimalisatierondes.

**Klaar wanneer:** er gerealiseerde, terugkerende omzet is (uit de betaalprovider, niet geschat) en de unit economics in beeld zijn.

**Stopmoment:** verslag met cijfers en voorstel voor opschalen, bijsturen of stoppen.

---

## Fase 5 — Beheer, rapportage en dashboard
**Bewijst:** het bedrijf draait met alleen de wekelijkse check van de eigenaar.

**Oplevering:** dashboard (bedrijven, kosten, omzet gerealiseerd vs. voorspeld, KPI's, besluiten, goedkeuringswachtrij), wekelijkse samenvattingen, meldingen alleen bij noodzaak.

**Klaar wanneer:** één maand stabiel gedraaid met minimale tussenkomst, zonder budgetoverschrijdingen of onopgemerkte fouten.

---

## Fase 6 — Venture Studio: meerdere bedrijven
**Bewijst:** het systeem is herhaalbaar.

**Oplevering:** afzonderlijke bedrijfsomgevingen (geheugen, budget, KPI's, teams), kapitaalallocatie door CEO en CFO op basis van gemeten rendement, continue kansenverkenning.

**Klaar wanneer:** een tweede bedrijf doorloopt fase 2 t/m 4 sneller en goedkoper dan het eerste.

---

## Fase 7 — Geavanceerde autonomie
Zelfstandige optimalisatie, continue marktanalyse, portfolio-uitbreiding, ruimere niveau B-bevoegdheden waar de prestaties dat rechtvaardigen. Elke uitbreiding van bevoegdheden vereist goedkeuring van de eigenaar.
