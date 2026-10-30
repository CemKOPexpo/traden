"""Opening Range Breakout.

1. Bepaal de hoogste en laagste koers van de eerste `range_minutes` na de opening.
2. Sluit een candle daarna boven de range (met extra volume): long. Eronder: short.
3. Stop aan de andere kant van de range (of het midden, als die te ver weg ligt).
4. Doel = `reward_risk` x het risico.
Maximaal een trade per symbool per dag.
"""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from .base import Signal, Strategy


@dataclass
class ORBConfig:
    range_minutes: int = 15
    reward_risk: float = 2.0
    volume_factor: float = 1.2       # breakout-candle volume vs gemiddelde in de range
    max_range_pct: float = 0.03      # range > 3% van de koers: te wild, overslaan
    min_range_pct: float = 0.002     # range < 0,2%: te klein, ruis
    last_entry: str = "11:30"        # na dit tijdstip geen nieuwe ORB-trades
    allow_short: bool = True


class OpeningRangeBreakout(Strategy):
    name = "orb"

    def __init__(self, cfg: ORBConfig | None = None):
        self.cfg = cfg or ORBConfig()
        self.done: set[str] = set()

    def new_day(self, symbol: str) -> None:
        self.done.discard(symbol)

    def on_bar(self, symbol: str, today: pd.DataFrame) -> Signal | None:
        if symbol in self.done:
            return None
        start = today.index[0].normalize() + pd.Timedelta(hours=9, minutes=30)
        range_end = start + pd.Timedelta(minutes=self.cfg.range_minutes)
        now = today.index[-1]
        if now < range_end or now.time() > pd.Timestamp(self.cfg.last_entry).time():
            return None

        rng = today[today.index < range_end]
        if rng.empty:
            return None
        hi, lo = rng.high.max(), rng.low.min()
        mid = (hi + lo) / 2
        width = (hi - lo) / mid
        if not self.cfg.min_range_pct <= width <= self.cfg.max_range_pct:
            self.done.add(symbol)
            return None

        bar = today.iloc[-1]
        if bar.volume < self.cfg.volume_factor * rng.volume.mean():
            return None

        if bar.close > hi:
            stop = lo if (bar.close - lo) / bar.close < self.cfg.max_range_pct else mid
            side = 1
        elif bar.close < lo and self.cfg.allow_short:
            stop = hi if (hi - bar.close) / bar.close < self.cfg.max_range_pct else mid
            side = -1
        else:
            return None

        risk = abs(bar.close - stop)
        self.done.add(symbol)
        return Signal(
            side=side,
            stop=stop,
            target=bar.close + side * self.cfg.reward_risk * risk,
            reason=(f"ORB{self.cfg.range_minutes} {'long' if side > 0 else 'short'}: "
                    f"slot {bar.close:.2f} {'boven' if side > 0 else 'onder'} range "
                    f"{lo:.2f}-{hi:.2f} ({width:.2%}), volume x{bar.volume / rng.volume.mean():.1f}"),
        )
