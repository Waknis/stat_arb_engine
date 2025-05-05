"""Risk & performance metrics."""
import numpy as np
import pandas as pd

def sharpe(returns: pd.Series, risk_free_rate: float = 0.0, freq: int = 252) -> float:
    """
    Annualized Sharpe ratio with proper risk-free rate adjustment.
    
    Parameters
    ----------
    returns : pd.Series
        Series of returns (typically daily)
    risk_free_rate : float
        Annualized risk-free rate (default 0)
    freq : int
        Annualization factor (252 for daily trading days, 12 for monthly, etc.)
        
    Returns
    -------
    float
        Annualized Sharpe ratio
    """
    # Validate returns
    if returns.empty or returns.isna().all():
        return 0.0
        
    # Calculate mean and standard deviation
    mean_return = returns.mean()
    vol = returns.std()
    
    # Handle edge cases
    if vol == 0 or np.isnan(vol) or np.isnan(mean_return):
        return 0.0
    
    # Convert risk-free rate to same frequency as returns
    period_risk_free = risk_free_rate / freq
    
    # Calculate Sharpe ratio - CORRECTED FORMULA
    # We only annualize the final result, not the mean return itself
    excess_return = mean_return - period_risk_free
    sharpe_ratio = excess_return / vol * np.sqrt(freq)
    
    # Limit extreme values for display purposes
    return np.clip(sharpe_ratio, -10, 10)

def max_drawdown(equity_curve: pd.Series) -> float:
    """Maximum drawdown of equity curve (<= 0)."""
    rolling_max = equity_curve.cummax()
    drawdown = equity_curve / rolling_max - 1.0
    return drawdown.min()
