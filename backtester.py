"""Event‑driven back‑tester for intraday bar data."""
import numpy as np
import pandas as pd

def backtest(price: pd.Series,
             signal: pd.Series,
             cost_per_share: float = 0.0005) -> pd.DataFrame:
    """Compute P&L with simple fill and fixed bid‑ask cost per share."""
    # Enter next bar (signal shift)
    positions = signal.shift().fillna(0)
    # Vectorized returns
    returns = price.pct_change().fillna(0)
    # Strategy returns after cost on position changes
    strat_ret = positions * returns - np.abs(positions.diff().fillna(0)) * cost_per_share
    equity = (1 + strat_ret).cumprod()
    return pd.DataFrame({'equity': equity, 'strategy_returns': strat_ret})
