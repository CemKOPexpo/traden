# traden: daytrade-simulator

Fictief traden op historische data. Er gaat geen echt geld en er is geen broker-koppeling.
Zie [PLAN.md](PLAN.md) voor het totaalplan en [LEARNING.md](LEARNING.md) voor de leercyclus.

## Snel starten
```bash
pip install -r requirements.txt
python scripts/fetch_data.py SPY QQQ AAPL NVDA TSLA AMD META --interval 5m --period 60d
python run_sim.py --data data --out reports/eerste-run
python -m pytest -q tests
```

## Hoe de simulatie werkt
- Candles worden een voor een afgespeeld; de strategie ziet alleen het verleden.
- Een signaal op de slotkoers wordt uitgevoerd op de open van de volgende candle, met slippage
  en commissie.
- Raakt een candle zowel de stop als het doel, dan telt de stop (conservatief).
- De risk manager bepaalt de positiegrootte (1% risico), stopt bij -2% op een dag en sluit
  alles om 15:50.
- Uitvoer: `report.md` (kerncijfers, uitsplitsingen, slechtste trades), `trades.csv`, `equity.csv`.

## Structuur
```
src/sim/        data, paper broker, risk manager, replay-engine, rapport
src/strategies/ strategieen (nu: Opening Range Breakout)
scripts/        data downloaden
tests/          controle van de simulator-mechaniek
```
