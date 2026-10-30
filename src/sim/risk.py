"""Risk manager: heeft altijd het laatste woord over elke trade."""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class RiskConfig:
    risk_per_trade: float = 0.01      # 1% van het account per trade
    daily_loss_limit: float = 0.02    # bij -2% stopt de bot voor de dag
    max_trades_per_day: int = 10
    max_positions: int = 3
    max_position_value: float = 0.25  # max 25% van het account in een positie


class RiskManager:
    def __init__(self, cfg: RiskConfig):
        self.cfg = cfg
        self.day_start_equity = 0.0
        self.day_pnl = 0.0
        self.trades_today = 0
        self.halted = False
        self.rejections: dict[str, int] = {}

    def new_day(self, equity: float) -> None:
        self.day_start_equity = equity
        self.day_pnl = 0.0
        self.trades_today = 0
        self.halted = False

    def register_pnl(self, pnl: float) -> None:
        self.day_pnl += pnl
        if self.day_pnl <= -self.cfg.daily_loss_limit * self.day_start_equity:
            self.halted = True

    def _reject(self, why: str) -> int:
        self.rejections[why] = self.rejections.get(why, 0) + 1
        return 0

    def size(self, equity: float, entry: float, stop: float, open_positions: int) -> int:
        """Aantal aandelen, of 0 als de trade wordt afgewezen."""
        if self.halted:
            return self._reject("dagelijkse verlieslimiet")
        if self.trades_today >= self.cfg.max_trades_per_day:
            return self._reject("max trades per dag")
        if open_positions >= self.cfg.max_positions:
            return self._reject("max posities")
        per_share = abs(entry - stop)
        if per_share <= 0:
            return self._reject("ongeldige stop")
        qty = math.floor(equity * self.cfg.risk_per_trade / per_share)
        qty = min(qty, math.floor(equity * self.cfg.max_position_value / entry))
        if qty < 1:
            return self._reject("positie te klein")
        self.trades_today += 1
        return qty
