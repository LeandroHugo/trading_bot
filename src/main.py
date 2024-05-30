from config import API_KEY, USERNAME, PASSWORD
from data_fetcher import fetch_historical_data
from model_trainer import train_model
from signal_detector import detect_signals
from trader import login_to_trading_platform, place_trade
import time
import pyautogui

def trading_bot():
    # Fetch and preprocess data
    ticker = 'AAPL'
    data = fetch_historical_data(ticker)
    model = train_model(data)
    
    # Login to trading platform
    login_to_trading_platform(USERNAME, PASSWORD)
    
    while True:
        # Capture the screen or a specific part of the screen
        pyautogui.screenshot('data/screenshots/current_screen.png')
        # Detect trading signals
        signals = detect_signals('data/screenshots/current_screen.png')
        # Predict using the trained model
        latest_data = fetch_historical_data(ticker).iloc[-1]
        prediction = model.predict([latest_data[['Open', 'High', 'Low', 'Close', 'Volume']]])
        # Perform trades based on detected signals and model prediction
        if 'BUY_SIGNAL' in signals or prediction == 1:
            place_trade('buy', 100)
        elif 'SELL_SIGNAL' in signals or prediction == 0:
            place_trade('sell', 100)
        # Wait before the next iteration
        time.sleep(60)

if __name__ == '__main__':
    trading_bot()