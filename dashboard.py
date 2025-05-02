"""Streamlit dashboard for interactive exploration."""
import streamlit as st
import pandas as pd
import datetime as dt
import plotly.express as px
from main import run

st.set_page_config(page_title='Stat‑Arb Engine', layout='wide')
st.title('Intraday Statistical Arbitrage Engine')
st.write("Using Polygon.io for reliable market data")

with st.sidebar:
    st.header("Configuration")
    tickers_input = st.text_input('Tickers (space‑separated)', 'AAPL MSFT AMZN GOOGL')
    
    col1, col2 = st.columns(2)
    with col1:
        days_back = st.slider('Days Back', min_value=1, max_value=30, value=7)
    
    with col2:
        end_date = st.date_input("End Date", dt.date.today())
    
    start_date = end_date - dt.timedelta(days=days_back)
    st.write(f"Date Range: {start_date.isoformat()} to {end_date.isoformat()}")
    
    run_button = st.button('Run Back‑test', type="primary")

# Check if API key is present
api_key_info = st.empty()
if not run_button and "summary" not in st.session_state:
    api_key_info.info("Make sure your Polygon API key is set as an environment variable.")

if run_button:
    with st.spinner('Running back-test...'):
        try:
            tickers = tickers_input.strip().upper().split()
            summary = run(tickers, start_date.isoformat(), end_date.isoformat())
            st.session_state["summary"] = summary
            st.session_state["tickers"] = tickers
            api_key_info.empty()
        except Exception as e:
            st.error(f"Error: {str(e)}")

if "summary" in st.session_state:
    summary = st.session_state["summary"]
    
    # Format the summary table
    formatted_summary = summary.copy()
    formatted_summary["sharpe"] = formatted_summary["sharpe"].map("{:.2f}".format)
    formatted_summary["max_drawdown"] = formatted_summary["max_drawdown"].map("{:.2%}".format)
    formatted_summary["cumulative_return"] = formatted_summary["cumulative_return"].map("{:.2%}".format)
    
    # Performance metrics
    st.header('Performance Metrics')
    st.dataframe(formatted_summary, use_container_width=True)
    
    # Create tabs for different visualizations
    tab1, tab2 = st.tabs(["Sharpe Ratio", "Returns & Drawdown"])
    
    with tab1:
        # Sharpe ratio visualization
        fig = px.bar(
            summary, 
            x='ticker', 
            y='sharpe',
            title="Sharpe Ratio by Ticker",
            color='sharpe',
            color_continuous_scale=px.colors.sequential.Blues
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        # Returns and drawdown visualization
        fig = px.scatter(
            summary,
            x='max_drawdown',
            y='cumulative_return',
            title="Return vs Maximum Drawdown",
            text='ticker',
            size=summary['cumulative_return'].abs() * 100,
            color='sharpe',
            color_continuous_scale=px.colors.diverging.RdBu,
            range_color=[-50, 50]
        )
        fig.update_traces(textposition='top center')
        st.plotly_chart(fig, use_container_width=True)

# Add explanation
with st.expander("About this dashboard"):
    st.write("""
    This dashboard uses Polygon.io's API to fetch reliable intraday market data for backtesting. 
    
    **Metrics explained**:
    - **Sharpe Ratio**: Measures risk-adjusted returns. Higher values indicate better risk-adjusted performance.
    - **Max Drawdown**: The largest percentage drop from peak to trough. Lower values are better.
    - **Cumulative Return**: Total percentage return over the period.
    
    The statistical arbitrage engine implements a mean-reversion strategy on intraday price data.
    """)
