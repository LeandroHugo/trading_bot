# src/signal_detector.py
import openai
import cv2
import pytesseract

openai.api_key = 'YOUR_OPENAI_API_KEY'

def detect_signals(image_path):
    image = cv2.imread(image_path)
    text = pytesseract.image_to_string(image)
    # Process the text to identify trading signals
    return text

if __name__ == "__main__":
    test_image_path = 'data/screenshots/sample_image.png'
    signals = detect_signals(test_image_path)
    print(signals)