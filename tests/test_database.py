# tests/test_database.py
import unittest
from src.database import fetch_data

class TestDatabase(unittest.TestCase):
    def test_fetch_data(self):
        data = fetch_data('sales_data')
        self.assertIsInstance(data, list)
        if data:
            self.assertGreater(len(data), 0)