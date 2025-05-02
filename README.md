# Intraday Statistical-Arbitrage Engine

A lightweight, end‑to‑end project that demonstrates **alpha discovery, risk management, and back‑testing** for a quant‑trading résumé.

## Features
* Pulls 1‑minute intraday data for U.S. equities via Polygon.io API
* Generates mean‑reversion alpha factors (price minus VWAP z‑score)
* Vectorized event‑driven back‑tester with simple transaction‑cost model
* Risk metrics: annualized Sharpe, max drawdown, cumulative return
* Enhanced Streamlit dashboard with interactive visualizations using Plotly

## Quick Start
```bash
# 1. Install deps (ideally in a virtualenv)
pip install -r requirements.txt

# 2. Set your Polygon.io API key
export POLYGON_API_KEY="your_api_key_here"

# 3. Run a back‑test from the CLI
python main.py --tickers AAPL MSFT AMZN --start 2025-04-25 --end 2025-05-02

# 4. Launch the interactive dashboard
streamlit run dashboard.py
```

> **Note:** Polygon.io offers free tier access with some limitations. Check https://polygon.io/pricing for details.

## Folder Structure
```
stat_arb_engine/
├── alpha.py            # Signal generation
├── backtester.py       # Backtest engine
├── dashboard.py        # Streamlit visualization
├── fetch_data.py       # Data retrieval from Polygon.io
├── main.py             # CLI entrypoint
├── risk.py             # Risk metrics
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

## Disclaimers
* Educational use only. No investment advice.
* Historical fills are simulated and ignore latency / microstructure noise.
* Extend with limit‑order‑book data, slippage models, and live execution for production use.

## Roadmap
* Add portfolio level optimization with multiple tickers
* Implement more sophisticated strategies beyond mean-reversion
* Add option to export results to CSV/Excel
* Implement more advanced risk metrics and drawdown analysis
