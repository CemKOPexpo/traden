"""Draai een fictieve trading-simulatie op historische data.

    python run_sim.py --data data --start 2026-08-01 --end 2026-09-30
"""
import argparse

from src.sim.data import load_dir
from src.sim.engine import SimConfig, run
from src.sim.report import metrics, write_report
from src.strategies.orb import ORBConfig, OpeningRangeBreakout

p = argparse.ArgumentParser()
p.add_argument("--data", default="data")
p.add_argument("--symbols", nargs="*")
p.add_argument("--start")
p.add_argument("--end")
p.add_argument("--cash", type=float, default=25_000)
p.add_argument("--range-minutes", type=int, default=15)
p.add_argument("--rr", type=float, default=2.0, help="reward/risk verhouding")
p.add_argument("--no-short", action="store_true")
p.add_argument("--out", default="reports/latest")
a = p.parse_args()

data = load_dir(a.data, [s.upper() for s in a.symbols] if a.symbols else None)
if not data:
    raise SystemExit(f"Geen CSV-bestanden in {a.data}/ -- draai eerst scripts/fetch_data.py")
data = {s: df.loc[a.start:a.end] for s, df in data.items()}

strategy = OpeningRangeBreakout(ORBConfig(range_minutes=a.range_minutes, reward_risk=a.rr,
                                          allow_short=not a.no_short))
res = run(data, strategy, SimConfig(start_cash=a.cash))
path = write_report(res, a.out, f"Simulatie ORB{a.range_minutes} ({', '.join(data)})")
for k, v in metrics(res).items():
    print(f"{k:>15}: {v:,.4f}" if isinstance(v, float) else f"{k:>15}: {v}")
print(f"\nRapport: {path}")
