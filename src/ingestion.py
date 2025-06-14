# src/ingestion.py
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def fetch_index_data(ticker='^GSPC', period='1y', interval='1d'):
    """
    Fetch historical index data from Yahoo Finance.
    Example ticker: '^GSPC' (S&P 500), '^NSEI' (Nifty 50)
    """
    df = yf.download(ticker, period=period, interval=interval)
    df.reset_index(inplace=True)
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    df.dropna(inplace=True)
    return df

def save_to_csv(df, filepath='data/sample_index_data.csv'):
    df.to_csv(filepath, index=False)

if __name__ == '__main__':
    df = fetch_index_data(ticker='^GSPC')
    save_to_csv(df)
    print("Data saved to data/sample_index_data.csv")