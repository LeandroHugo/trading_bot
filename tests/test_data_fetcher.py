# tests/test_data_fetcher.py
import unittest
from src.data_fetcher import fetch_historical_data, fetch_live_data

class TestDataFetcher(unittest.TestCase):

    def test_fetch_historical_data(self):
        data = fetch_historical_data('AAPL')
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_fetch_live_data(self):
        data = fetch_live_data('AAPL')
        self.assertIsNotNone(data)
        self.assertTrue('Close' in data)

if __name__ == '__main__':
    unittest.main()