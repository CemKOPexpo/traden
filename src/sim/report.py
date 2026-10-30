"""Journaal en rapportage: de basis om van de simulatie te leren."""
from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

import pandas as pd

from .engine import SimResult


def trades_frame(res: SimResult) -> pd.DataFrame:
    df = pd.DataFrame([asdict(t) for t in res.trades])
    if not df.empty:
        df["direction"] = df.side.map({1: "long", -1: "short"})
        df["hour"] = pd.to_datetime(df.entry_time).map(lambda t: t.hour)
    return df


def metrics(res: SimResult) -> dict:
    df = trades_frame(res)
    eq = pd.concat([pd.Series([res.start_cash]), res.equity.reset_index(drop=True)])
    dd = (eq / eq.cummax() - 1).min()
    if df.empty:
        return {"trades": 0, "net_pnl": 0.0, "max_drawdown": dd}
    wins, losses = df[df.pnl > 0], df[df.pnl <= 0]
    gross_loss = -losses.pnl.sum()
    return {
        "trades": len(df),
        "winrate": len(wins) / len(df),
        "avg_r": df.r_multiple.mean(),
        "expectancy_eur": df.pnl.mean(),
        "profit_factor": wins.pnl.sum() / gross_loss if gross_loss else float("inf"),
        "net_pnl": df.pnl.sum(),
        "return_pct": eq.iloc[-1] / res.start_cash - 1,
        "max_drawdown": dd,
        "best_trade": df.pnl.max(),
        "worst_trade": df.pnl.min(),
    }


def breakdown(df: pd.DataFrame, col: str) -> pd.DataFrame:
    g = df.groupby(col)
    return pd.DataFrame({
        "trades": g.size(),
        "winrate": g.pnl.apply(lambda s: (s > 0).mean()),
        "avg_r": g.r_multiple.mean(),
        "pnl": g.pnl.sum(),
    }).round(3)


def write_report(res: SimResult, out_dir: str | Path, title: str) -> Path:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    df = trades_frame(res)
    df.to_csv(out / "trades.csv", index=False)
    res.equity.to_csv(out / "equity.csv", header=["equity"])

    m = metrics(res)
    fmt = {k: (f"{v:.2%}" if k in ("winrate", "return_pct", "max_drawdown") else
               f"{v:,.2f}" if isinstance(v, float) else v) for k, v in m.items()}
    lines = [f"# {title}", "", "## Kerncijfers", "", "| metric | waarde |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in fmt.items()]
    if not df.empty:
        for col, label in [("symbol", "Per symbool"), ("direction", "Long vs short"),
                           ("hour", "Per uur van instap"), ("exit_reason", "Per exit-reden")]:
            lines += ["", f"## {label}", "", breakdown(df, col).to_markdown()]
        worst = df.nsmallest(5, "pnl")[["entry_time", "symbol", "direction", "pnl", "r_multiple", "reason"]]
        lines += ["", "## 5 slechtste trades (om van te leren)", "", worst.to_markdown(index=False)]
    if res.rejections:
        lines += ["", "## Door risk manager geweigerd", ""]
        lines += [f"- {k}: {v}x" for k, v in res.rejections.items()]
    path = out / "report.md"
    path.write_text("\n".join(lines) + "\n")
    return path
