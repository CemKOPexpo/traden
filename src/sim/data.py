"""Laden van historische OHLCV-data (CSV) voor de simulator."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

MARKET_TZ = "America/New_York"
REQUIRED = ["open", "high", "low", "close", "volume"]


def load_csv(path: str | Path, tz: str = MARKET_TZ) -> pd.DataFrame:
    """Lees een CSV met kolommen timestamp,open,high,low,close,volume.

    Tijden worden omgezet naar beurstijd, zodat 09:30 ook echt de opening is.
    """
    df = pd.read_csv(path)
    df.columns = [c.lower() for c in df.columns]
    ts_col = next(c for c in ("timestamp", "datetime", "date", "time") if c in df.columns)
    ts = pd.to_datetime(df[ts_col], utc=True).dt.tz_convert(tz)
    df = df.set_index(ts)[REQUIRED].astype(float).sort_index()
    df = df[~df.index.duplicated(keep="first")]
    return regular_session(df)


def regular_session(df: pd.DataFrame) -> pd.DataFrame:
    """Alleen de reguliere handelssessie (09:30-16:00 beurstijd)."""
    t = df.index.time
    open_t, close_t = pd.Timestamp("09:30").time(), pd.Timestamp("16:00").time()
    return df[(t >= open_t) & (t < close_t)]


def load_dir(directory: str | Path, symbols: list[str] | None = None) -> dict[str, pd.DataFrame]:
    """Laad alle <SYMBOL>.csv bestanden uit een map."""
    out = {}
    for f in sorted(Path(directory).glob("*.csv")):
        sym = f.stem.upper()
        if symbols is None or sym in symbols:
            out[sym] = load_csv(f)
    return out
