# tests/test_model_trainer.py
import unittest
from src.model_trainer import train_model
from src.data_fetcher import fetch_historical_data

class TestModelTrainer(unittest.TestCase):

    def test_train_model(self):
        data = fetch_historical_data('AAPL')
        model = train_model(data)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()