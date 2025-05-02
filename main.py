"""Command‑line entry point for running back‑tests across tickers."""
import argparse
import datetime as dt
import pandas as pd

from fetch_data import get_intraday_data
from alpha import mean_reversion_signal
from backtester import backtest
from risk import sharpe, max_drawdown

def run(tickers, start, end):
    rows = []
    for ticker in tickers:
        df = get_intraday_data(ticker, start, end)
        sig = mean_reversion_signal(df)
        bt = backtest(df['Close'], sig)
        rows.append({
            'ticker': ticker,
            'sharpe': sharpe(bt['strategy_returns']),
            'max_drawdown': max_drawdown(bt['equity']),
            'cumulative_return': bt['equity'].iloc[-1] - 1.0,
        })
    return pd.DataFrame(rows)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tickers', nargs='+', required=True, help='Space‑separated tickers')
    parser.add_argument('--start', default=(dt.date.today() - dt.timedelta(days=5)).isoformat())
    parser.add_argument('--end', default=dt.date.today().isoformat())
    args = parser.parse_args()

    summary = run(args.tickers, args.start, args.end)
    print(summary.to_markdown(index=False))
