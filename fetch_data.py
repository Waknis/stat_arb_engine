"""Intraday data downloader using Polygon.io."""

import os
import requests
import pandas as pd

def get_intraday_data(ticker: str, start_date: str, end_date: str, interval: str = "1m"):
    """
    Fetch intraday data via Polygon.io Aggregates endpoint.
    Requires environment variable POLYGON_API_KEY.
    
    Parameters
    ----------
    ticker : str
        Stock symbol
    start_date : str
        Start date in ISO format (YYYY-MM-DD)
    end_date : str
        End date in ISO format (YYYY-MM-DD)
    interval : str
        Time interval, default "1m" for 1-minute bars
        
    Returns
    -------
    pandas.DataFrame
        DataFrame with OHLCV data
    """
    api_key = os.getenv("POLYGON_API_KEY")
    if api_key is None:
        raise RuntimeError("Set POLYGON_API_KEY environment variable to use Polygon.io API.")
    
    # Convert interval from "1m" format to "1" format for Polygon API
    multiplier = interval.rstrip("m")
    
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/minute/{start_date}/{end_date}"
    params = {"adjusted": "true", "limit": 50000, "apiKey": api_key}
    
    resp = requests.get(url, params=params, timeout=30).json()
    if resp.get("resultsCount", 0) == 0:
        raise ValueError(f"No data returned for {ticker}")

    df = pd.DataFrame(resp["results"])
    df["timestamp"] = pd.to_datetime(df["t"], unit="ms")
    df = df.set_index("timestamp").rename(
        columns={"o": "Open", "h": "High", "l": "Low", "c": "Close", "v": "Volume"}
    )
    return df[["Open", "High", "Low", "Close", "Volume"]]
