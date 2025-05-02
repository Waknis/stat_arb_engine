"""Risk & performance metrics."""
import numpy as np
import pandas as pd

def sharpe(returns: pd.Series, freq: int = 252 * 390) -> float:
    """Annualized Sharpe ratio given intraday frequency (252 trading days × 390 minutes)."""
    vol = returns.std()
    if vol == 0 or np.isnan(vol):
        return 0.0
    return (returns.mean() * freq) / (vol * np.sqrt(freq))

def max_drawdown(equity_curve: pd.Series) -> float:
    """Maximum drawdown of equity curve (<= 0)."""
    rolling_max = equity_curve.cummax()
    drawdown = equity_curve / rolling_max - 1.0
    return drawdown.min()
