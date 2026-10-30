"""Tests van de simulator met kunstmatige candles (alleen om de mechaniek te controleren)."""
import pandas as pd
import pytest

from src.sim.broker import Order, PaperBroker
from src.sim.engine import SimConfig, run
from src.sim.risk import RiskConfig, RiskManager
from src.strategies.orb import OpeningRangeBreakout

DAY = "2026-03-02"


def bars(rows, day=DAY):
    """rows: lijst van (open, high, low, close, volume) per 5 minuten vanaf 09:30."""
    idx = pd.date_range(f"{day} 09:30", periods=len(rows), freq="5min", tz="America/New_York")
    return pd.DataFrame(rows, index=idx, columns=["open", "high", "low", "close", "volume"])


def flat_day(price=100.0, n=78):
    return [(price, price + 0.1, price - 0.1, price, 1000)] * n


def bar(o, h, l, c):
    return pd.Series({"open": o, "high": h, "low": l, "close": c, "volume": 1})


def no_costs_broker():
    return PaperBroker(cash=10_000, commission_per_share=0, min_commission=0, slippage_bps=0)


def test_order_fills_on_next_open_not_signal_close():
    b = no_costs_broker()
    ts = pd.Timestamp(f"{DAY} 10:00", tz="America/New_York")
    b.submit(Order("X", 1, 10, stop=99, target=104, reason="t", signal_time=ts))
    b.on_bar("X", ts, bar(101, 101.5, 100.5, 101))
    assert b.positions["X"].entry == 101


def test_stop_wins_when_bar_hits_both():
    b = no_costs_broker()
    ts = pd.Timestamp(f"{DAY} 10:00", tz="America/New_York")
    b.submit(Order("X", 1, 10, stop=99, target=102, reason="t", signal_time=ts))
    b.on_bar("X", ts, bar(100, 100.5, 99.5, 100))
    [t] = b.on_bar("X", ts + pd.Timedelta("5min"), bar(100, 103, 98, 100))
    assert t.exit_reason == "stop" and t.exit == 99 and t.r_multiple == pytest.approx(-1)


def test_gap_through_stop_fills_at_open():
    b = no_costs_broker()
    ts = pd.Timestamp(f"{DAY} 10:00", tz="America/New_York")
    b.submit(Order("X", 1, 10, stop=99, target=104, reason="t", signal_time=ts))
    b.on_bar("X", ts, bar(100, 100.5, 99.5, 100))
    [t] = b.on_bar("X", ts + pd.Timedelta("5min"), bar(97, 97.5, 96, 97))
    assert t.exit == 97 and t.r_multiple == pytest.approx(-3)


def test_position_sizing_risks_one_percent():
    rm = RiskManager(RiskConfig(risk_per_trade=0.01, max_position_value=1.0))
    rm.new_day(10_000)
    assert rm.size(10_000, entry=100, stop=98, open_positions=0) == 50  # 50 x 2 = 100 = 1%


def test_daily_loss_limit_halts_trading():
    rm = RiskManager(RiskConfig(daily_loss_limit=0.02))
    rm.new_day(10_000)
    rm.register_pnl(-250)
    assert rm.size(10_000, 100, 98, 0) == 0 and rm.halted


def test_orb_long_breakout_hits_target():
    rows = [(100, 100.5, 99.5, 100, 1000)] * 3            # range 99.5 - 100.5
    rows += [(100.4, 101.0, 100.3, 100.9, 3000)]           # breakout, signaal
    rows += [(101, 104.0, 100.9, 103.9, 2000)]             # doel 2R (103.7) wordt geraakt
    rows += flat_day(103.9, 73)
    res = run({"X": bars(rows)}, OpeningRangeBreakout(), SimConfig(start_cash=25_000))
    [t] = res.trades
    assert t.side == 1 and t.exit_reason == "target" and t.pnl > 0


def test_positions_closed_before_end_of_day():
    rows = [(100, 100.5, 99.5, 100, 1000)] * 3
    rows += [(100.4, 101.0, 100.3, 100.9, 3000)]
    rows += flat_day(101.0, 74)                            # geen stop, geen doel
    res = run({"X": bars(rows)}, OpeningRangeBreakout(), SimConfig(start_cash=25_000))
    [t] = res.trades
    assert t.exit_reason == "einde dag" and t.exit_time.time() <= pd.Timestamp("15:50").time()


def test_strategy_cannot_see_future():
    seen = []

    class Spy(OpeningRangeBreakout):
        def on_bar(self, symbol, today):
            seen.append((today.index[-1], len(today)))
            return None

    df = bars(flat_day())
    run({"X": df}, Spy())
    assert all(df.index[n - 1] == ts for ts, n in seen)
