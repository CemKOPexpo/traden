# Leerproces: hoe de bot (en Claude) beter wordt

## Eerlijk over "Claude leert"
Claude onthoudt niets tussen sessies en wordt niet slimmer door te traden: het model zelf
verandert niet. Het **systeem** leert wel, via drie dingen die in deze repo bewaard worden:

1. **Het journaal** (`reports/*/trades.csv`): elke trade met reden van instap en uitstap.
2. **Dit bestand**: lessen die we samen trekken. Claude leest dit aan het begin van elke sessie.
3. **De code/parameters**: verbeteringen worden regels in de strategie of de risk manager.

## De leercyclus
1. **Simuleren**: `python run_sim.py --start ... --end ...` op een TRAININGSperiode.
2. **Analyseren**: Claude leest `report.md` en de slechtste trades. Wanneer gaat het mis?
   Welk uur, welke richting, welk soort aandeel?
3. **Hypothese**: "ORB-shorts in de eerste 30 minuten verliezen". Schrijf die hieronder op.
4. **Aanpassen**: een regel of parameter wijzigen.
5. **Valideren op een TESTperiode** die we nog niet gezien hebben. Alleen als het daar ook
   beter is, houden we de wijziging. Anders gaat ze terug: dat is overfitting.
6. **Les vastleggen** in de tabel hieronder, ook als het niet werkte.

## Spelregels tegen zelfbedrog
- Periodes splitsen: bv. 70% training, 30% test. De testperiode alleen gebruiken om te controleren,
  nooit om te tunen.
- Minimaal ~100 trades voordat we conclusies trekken uit een winrate.
- Kosten en slippage altijd aan laten staan.
- Een verbetering moet logisch te verklaren zijn, niet alleen "het getal werd beter".
- Wijzigingen een voor een testen.

## Lessen
| Datum | Hypothese | Training | Test | Besluit |
|---|---|---|---|---|
| 2026-10-30 | Controle: zonder patroon in de koers (toevalsdata) moet ORB verliezen door de kosten | n.v.t. | n.v.t. | Klopt (-4,3%). De simulator verzint geen winst. |
