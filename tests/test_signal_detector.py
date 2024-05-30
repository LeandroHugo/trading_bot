import unittest
from src.signal_detector import detect_signals

class TestSignalDetector(unittest.TestCase):

    def test_detect_signals(self):
        test_image_path = 'data/screenshots/sample_image.png'
        signals = detect_signals(test_image_path)
        self.assertIsNotNone(signals)
        self.assertIsInstance(signals, str)

if __name__ == '__main__':
    unittest.main()