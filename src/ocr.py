# src/ocr.py
import cv2
import pytesseract

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    test_image_path = 'data/screenshots/sample_image.png'
    text = extract_text_from_image(test_image_path)
    print(text)