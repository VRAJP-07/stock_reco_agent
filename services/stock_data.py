import yfinance as yf
import pandas as pd
import requests
from config import LOOKBACK_DAYS

# Disable SSL verification (⚠ only for dev)
from yfinance import utils
utils.requests = requests.Session()
utils.requests.verify = False  # 🔴 not safe for production

def get_price_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=f"{LOOKBACK_DAYS}d", interval="1h")
        df = df.dropna()
        return df
    except Exception as e:
        print(f"[ERROR] Couldn't fetch data for {ticker}: {e}")
        return pd.DataFrame()
