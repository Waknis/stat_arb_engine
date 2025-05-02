"""Alpha‑factor generation utilities."""
import numpy as np
import pandas as pd

def vwap(df: pd.DataFrame) -> pd.Series:
    """Volume‑weighted average price (cumulative)."""
    cum_dollar = (df['Close'] * df['Volume']).cumsum()
    cum_vol = df['Volume'].cumsum().replace({0: np.nan})
    return cum_dollar / cum_vol

def zscore(series: pd.Series, window: int = 30) -> pd.Series:
    """Rolling z‑score."""
    rolling_mean = series.rolling(window).mean()
    rolling_std = series.rolling(window).std()
    return (series - rolling_mean) / rolling_std

def mean_reversion_signal(df: pd.DataFrame, window: int = 30, threshold: float = 1.0) -> pd.Series:
    """Return +1 long, ‑1 short, 0 flat based on z‑score of price deviation from VWAP."""
    deviation = df['Close'] - vwap(df)
    z = zscore(deviation, window)
    signal = np.where(z < -threshold, 1, np.where(z > threshold, -1, 0))
    return pd.Series(signal, index=df.index)
