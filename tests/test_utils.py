"""Tests for module 'utils' """
import unittest
from utils import read_json_file


class TestUtils(unittest.TestCase):
    """Test cases for class 'Package'"""

    def test_read_json_data_correctly(self):
        """Tests that we are able to set offers correctly"""
        file_path = 'tests/data/offers.json'
        actual_data = read_json_file(file_path)
        self.assertIsNotNone(actual_data)
        self.assertIsInstance(actual_data, list)
        self.assertEqual(len(actual_data), 3)

    def test_read_json_data_file_absent(self):
        """Tests that we are able to set offers correctly"""
        file_path = 'tests/data/offers_absent.json'
        with self.assertRaises(FileNotFoundError):
            read_json_file(file_path)

