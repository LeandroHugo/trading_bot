# src/model_trainer.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(data):
    X = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    y = (data['Close'].shift(-1) > data['Close']).astype(int)  # Binary classification: 1 if price goes up, 0 if down
    X_train, X_test, y_train, y_test = train_test_split(X[:-1], y[:-1], test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    joblib.dump(model, 'data/models/trading_model.pkl')
    return model

if __name__ == "__main__":
    from data_fetcher import fetch_historical_data
    ticker = "AAPL"
    data = fetch_historical_data(ticker)
    model = train_model(data)
    print("Model trained and saved.")