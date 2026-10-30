"""Replay-engine: speelt historische candles af alsof het live is."""
from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from src.strategies.base import Strategy

from .broker import Order, PaperBroker, Trade
from .risk import RiskConfig, RiskManager


@dataclass
class SimConfig:
    start_cash: float = 25_000.0
    flat_time: str = "15:50"          # alles sluiten voor het slot, geen overnight risico
    risk: RiskConfig = field(default_factory=RiskConfig)


@dataclass
class SimResult:
    trades: list[Trade]
    equity: pd.Series                 # equity aan het eind van elke dag
    rejections: dict[str, int]
    start_cash: float


def run(data: dict[str, pd.DataFrame], strategy: Strategy, cfg: SimConfig | None = None) -> SimResult:
    cfg = cfg or SimConfig()
    broker = PaperBroker(cash=cfg.start_cash)
    risk = RiskManager(cfg.risk)
    flat = pd.Timestamp(cfg.flat_time).time()
    trades: list[Trade] = []
    equity = {}

    days = sorted({d for df in data.values() for d in df.index.normalize().unique()})
    for day in days:
        today = {s: df[df.index.normalize() == day] for s, df in data.items()}
        today = {s: df for s, df in today.items() if not df.empty}
        risk.new_day(broker.cash)
        for s in today:
            strategy.new_day(s)

        timeline = sorted({ts for df in today.values() for ts in df.index})
        for ts in timeline:
            for sym, df in today.items():
                if ts not in df.index:
                    continue
                bar = df.loc[ts]
                closed = broker.on_bar(sym, ts, bar)
                if ts.time() >= flat:
                    closed += broker.close(sym, bar.close, ts, "einde dag")
                for t in closed:
                    risk.register_pnl(t.pnl)
                trades += closed
                if ts.time() >= flat:
                    continue

                sig = strategy.on_bar(sym, df.loc[:ts])
                if sig is None or sym in broker.positions:
                    continue
                qty = risk.size(broker.cash, bar.close, sig.stop,
                                len(broker.positions) + len(broker.pending))
                if qty:
                    broker.submit(Order(sym, sig.side, qty, sig.stop, sig.target, sig.reason, ts))

        # Vangnet: alles wat nog open staat sluiten op de laatste candle van de dag.
        broker.cancel_all()
        for sym in list(broker.positions):
            last = today[sym].iloc[-1]
            for t in broker.close(sym, last.close, today[sym].index[-1], "einde dag"):
                risk.register_pnl(t.pnl)
                trades.append(t)
        equity[day] = broker.cash

    return SimResult(trades, pd.Series(equity, dtype=float), risk.rejections, cfg.start_cash)
