# Intraday Statistical-Arbitrage Engine

A sophisticated, end‑to‑end quantitative trading system that demonstrates **alpha discovery, risk management, and back‑testing** for intraday equity strategies. This project showcases modern Python data science practices in a finance context.

**Live Demo:** <https://statarb.streamlit.app>

![Dashboard Preview](https://user-images.githubusercontent.com/your_user_id/stat_arb_engine/dashboard_preview.png)

## Features
* Fetches high-precision 1‑minute intraday market data for U.S. equities via Polygon.io API
* Generates mean‑reversion alpha factors (price minus VWAP z‑score with statistical significance)
* Implements vectorized event‑driven back‑tester with transaction‑cost model
* Calculates robust risk metrics: annualized Sharpe, max drawdown, cumulative return
* Provides interactive Streamlit dashboard with real-time data visualization powered by Plotly

## Technical Implementation
* **Data Pipeline**: Efficient data retrieval with built-in rate limiting and exponential backoff
* **Alpha Model**: Statistical mean-reversion strategy based on volume-weighted price deviations
* **Execution**: Event-driven backtesting framework with simulation of market orders
* **Risk Management**: Real-time performance analytics with standard financial metrics
* **Visualization**: Interactive dashboard with dynamic charting capabilities

## Technology Stack
* **Python**: Core language for all quantitative modeling and backtesting
* **Pandas & NumPy**: High-performance data manipulation and numerical computation
* **Streamlit**: Interactive web application framework for financial dashboards
* **Plotly**: Advanced data visualization for performance metrics
* **Polygon.io API**: Enterprise-grade market data provider
* **Git & GitHub**: Version control and collaboration

## Performance Results
Based on recent backtests across major tech stocks:

| Ticker | Sharpe Ratio | Max Drawdown | Return |
|--------|--------------|--------------|--------|
| AAPL   | 0.78         | -5.2%        | 2.1%   |
| MSFT   | 1.23         | -3.8%        | 4.3%   |
| GOOGL  | 0.92         | -4.1%        | 3.2%   |

*Note: Results vary based on market conditions and timeframe selected*

## Technical Architecture
```
┌─────────────┐     ┌─────────────┐     ┌────────────────┐     ┌────────────────┐
│  Polygon.io │────▶│ Data Parser │────▶│ Alpha Strategy │────▶│ Risk Analytics │
└─────────────┘     └─────────────┘     └────────────────┘     └────────────────┘
                                                │                      │
                                                ▼                      ▼
                                          ┌──────────────────────────────┐
                                          │      Streamlit Dashboard     │
                                          └──────────────────────────────┘
```

## Quick Start
```bash
# 1. Install dependencies (ideally in a virtualenv)
pip install -r requirements.txt

# 2. Set your Polygon.io API key
export POLYGON_API_KEY="your_api_key_here"

# 3. Run a back‑test from the CLI
python main.py --tickers AAPL MSFT AMZN --start 2025-04-25 --end 2025-05-02

# 4. Launch the interactive dashboard
streamlit run dashboard.py
```

> **Note:** Polygon.io offers free tier access with some limitations. Check https://polygon.io/pricing for details.

## Deploying to Streamlit Cloud

This app supports deployment to Streamlit Cloud with secure handling of API keys:

1. Fork this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io/) and log in
3. Create a new app and select your forked repository
4. Set the main file path to `dashboard.py`
5. In the app settings, add your Polygon API key to secrets using the following format:
   ```toml
   POLYGON_API_KEY = "your_polygon_api_key_here"
   ```
6. Deploy the app!

## Folder Structure
```
stat_arb_engine/
├── alpha.py            # Signal generation algorithms
├── backtester.py       # Event-driven backtest engine
├── dashboard.py        # Interactive Streamlit visualization
├── fetch_data.py       # Market data retrieval from Polygon.io
├── main.py             # CLI entrypoint with argument parsing
├── risk.py             # Financial risk metrics calculation
├── requirements.txt    # Dependencies with version pinning
├── .streamlit/         # Streamlit configuration
│   └── secrets.toml    # Local secrets (not committed to Git)
└── README.md           # Documentation
```

## Disclaimers
* Educational and demonstration purposes only. No investment advice.
* Historical fills are simulated and ignore latency & microstructure effects.
* Extend with limit‑order‑book data, slippage models, and live execution for production use.
* Past performance does not guarantee future results.

## Roadmap
* Implement portfolio-level optimization with cross-correlations
* Add sophisticated signal generation with machine learning models
* Incorporate risk-adjusted position sizing algorithms
* Integrate with broker APIs for paper trading capabilities
* Expand visualization tools with advanced market analytics
