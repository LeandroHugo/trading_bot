from config import API_KEY, USERNAME, PASSWORD
from data_fetcher import fetch_historical_data, fetch_live_data
from model_trainer import train_model
from signal_detector import detect_signals
from trader import login_to_trading_platform, place_trade
import time
import pyautogui

def trading_bot():
    # Fetch and preprocess historical data
    ticker = 'AAPL'
    historical_data = fetch_historical_data(ticker)
    model = train_model(historical_data)
    
    # Login to trading platform
    login_to_trading_platform(USERNAME, PASSWORD)
    
    while True:
        # Fetch live data
        live_data = fetch_live_data(ticker)
        # Prepare the live data for prediction
        latest_data = live_data[['Open', 'High', 'Low', 'Close', 'Volume']].values.reshape(1, -1)
        prediction = model.predict(latest_data)
        
        # Capture the screen or a specific part of the screen
        pyautogui.screenshot('data/screenshots/current_screen.png')
        # Detect trading signals
        signals = detect_signals('data/screenshots/current_screen.png')
        
        # Perform trades based on detected signals and model prediction
        if 'BUY_SIGNAL' in signals or prediction == 1:
            place_trade('buy', 100)
        elif 'SELL_SIGNAL' in signals or prediction == 0:
            place_trade('sell', 100)
        
        # Wait for a specified interval before the next iteration
        time.sleep(60)  # 1 minute interval

if __name__ == '__main__':
    trading_bot()