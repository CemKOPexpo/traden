"""Download historische candles naar data/<SYMBOL>.csv via Yahoo Finance (yfinance).

Let op: Yahoo geeft 5-minuten candles alleen voor de laatste ~60 dagen en 1-uur candles
voor ~2 jaar. Voor langere minuutdata later overstappen op Alpaca, Polygon of Databento.

    python scripts/fetch_data.py SPY QQQ AAPL NVDA TSLA --interval 5m --period 60d
"""
import argparse
from pathlib import Path

import yfinance as yf

p = argparse.ArgumentParser()
p.add_argument("symbols", nargs="+")
p.add_argument("--interval", default="5m")
p.add_argument("--period", default="60d")
p.add_argument("--out", default="data")
a = p.parse_args()

Path(a.out).mkdir(exist_ok=True)
for sym in a.symbols:
    df = yf.download(sym, interval=a.interval, period=a.period, auto_adjust=False,
                     progress=False, multi_level_index=False)
    if df.empty:
        print(f"{sym}: geen data")
        continue
    df.index.name = "timestamp"
    df.columns = [c.lower() for c in df.columns]
    df[["open", "high", "low", "close", "volume"]].to_csv(Path(a.out) / f"{sym.upper()}.csv")
    print(f"{sym}: {len(df)} candles, {df.index[0]} t/m {df.index[-1]}")
