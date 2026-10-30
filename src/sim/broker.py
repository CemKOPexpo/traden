"""Paper broker: voert orders uit op historische candles met realistische kosten.

Uitvoeringsregels (bewust conservatief):
- Een signaal op de slotkoers van candle i wordt uitgevoerd op de OPEN van candle i+1.
- Slippage en commissie worden altijd in ons nadeel gerekend.
- Raakt een candle zowel de stop als het koersdoel, dan nemen we aan dat de stop eerst
  geraakt werd (we weten niet wat er binnen de candle gebeurde).
- Opent de koers voorbij de stop (gap), dan vullen we op de open, niet op de stop.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd


@dataclass
class Order:
    symbol: str
    side: int            # +1 long, -1 short
    qty: int
    stop: float
    target: float
    reason: str
    signal_time: pd.Timestamp


@dataclass
class Position:
    symbol: str
    side: int
    qty: int
    entry: float
    stop: float
    target: float
    reason: str
    entry_time: pd.Timestamp
    risk_per_share: float


@dataclass
class Trade:
    symbol: str
    side: int
    qty: int
    entry: float
    exit: float
    entry_time: pd.Timestamp
    exit_time: pd.Timestamp
    reason: str
    exit_reason: str
    pnl: float
    r_multiple: float


@dataclass
class PaperBroker:
    cash: float
    commission_per_share: float = 0.005
    min_commission: float = 1.0
    slippage_bps: float = 2.0
    pending: list[Order] = field(default_factory=list)
    positions: dict[str, Position] = field(default_factory=dict)

    def _slip(self, price: float, side: int) -> float:
        # side = richting van de transactie (+1 kopen, -1 verkopen)
        return price * (1 + side * self.slippage_bps / 10_000)

    def _commission(self, qty: int) -> float:
        return max(self.min_commission, qty * self.commission_per_share)

    def submit(self, order: Order) -> None:
        if order.symbol not in self.positions:
            self.pending.append(order)

    def on_bar(self, symbol: str, ts: pd.Timestamp, bar: pd.Series) -> list[Trade]:
        """Verwerk een nieuwe candle: eerst openstaande orders vullen, dan stops/doelen."""
        for order in [o for o in self.pending if o.symbol == symbol]:
            self.pending.remove(order)
            fill = self._slip(bar.open, order.side)
            # Gap voorbij de stop: trade is al ongeldig, niet instappen.
            if (fill - order.stop) * order.side <= 0:
                continue
            self.cash -= self._commission(order.qty)
            self.positions[symbol] = Position(
                symbol, order.side, order.qty, fill, order.stop, order.target,
                order.reason, ts, abs(fill - order.stop),
            )

        pos = self.positions.get(symbol)
        if pos is None:
            return []
        if pos.side > 0:
            stop_hit, target_hit = bar.low <= pos.stop, bar.high >= pos.target
            gap_stop, gap_target = bar.open <= pos.stop, bar.open >= pos.target
        else:
            stop_hit, target_hit = bar.high >= pos.stop, bar.low <= pos.target
            gap_stop, gap_target = bar.open >= pos.stop, bar.open <= pos.target

        if stop_hit:
            return [self._close(pos, bar.open if gap_stop else pos.stop, ts, "stop")]
        if target_hit:
            return [self._close(pos, bar.open if gap_target else pos.target, ts, "target")]
        return []

    def close(self, symbol: str, price: float, ts: pd.Timestamp, why: str) -> list[Trade]:
        pos = self.positions.get(symbol)
        return [self._close(pos, price, ts, why)] if pos else []

    def _close(self, pos: Position, price: float, ts: pd.Timestamp, why: str) -> Trade:
        exit_px = self._slip(price, -pos.side)
        gross = (exit_px - pos.entry) * pos.side * pos.qty
        commission = self._commission(pos.qty)
        self.cash += gross - commission           # entry-commissie ging al van cash af
        del self.positions[pos.symbol]
        pnl = gross - 2 * commission
        r = pnl / (pos.risk_per_share * pos.qty)
        return Trade(pos.symbol, pos.side, pos.qty, pos.entry, exit_px, pos.entry_time, ts,
                     pos.reason, why, pnl, r)

    def cancel_all(self) -> None:
        self.pending.clear()
