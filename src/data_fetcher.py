# src/data_fetcher.py
import yfinance as yf

def fetch_historical_data(ticker, period="1y", interval="1d"):
    data = yf.download(ticker, period=period, interval=interval)
    return data

def fetch_live_data(ticker):
    ticker_obj = yf.Ticker(ticker)
    data = ticker_obj.history(period="1m")
    return data.iloc[-1]  # Return the most recent data point

if __name__ == "__main__":
    ticker = "AAPL"
    historical_data = fetch_historical_data(ticker)
    print(historical_data)

    live_data = fetch_live_data(ticker)
    print(live_data)