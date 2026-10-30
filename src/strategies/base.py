"""Basisinterface voor strategieen."""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass
class Signal:
    side: int        # +1 long, -1 short
    stop: float
    target: float
    reason: str      # waarom deze trade? komt in het journaal


class Strategy:
    name = "base"

    def new_day(self, symbol: str) -> None:
        """Wordt aan het begin van elke handelsdag per symbool aangeroepen."""

    def on_bar(self, symbol: str, today: pd.DataFrame) -> Signal | None:
        """`today` bevat ALLEEN de candles van vandaag t/m de huidige (gesloten) candle.

        Zo kan een strategie nooit in de toekomst kijken.
        """
        raise NotImplementedError
