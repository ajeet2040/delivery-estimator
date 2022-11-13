"""Tests for module 'utils' """
import unittest
from utils import read_json_file, create_packages, create_offers
from models.package import Package
from models.offer import Offer
from models.vehicle import Vehicle
from copy import deepcopy


class TestUtils(unittest.TestCase):
    """Test cases for class 'Package'"""

    @classmethod
    def setUpClass(cls) -> None:
        test_offers_path = 'tests/data/offers.json'
        cls.test_offers = read_json_file(test_offers_path)
        cls.test_packages = [
            {
                "id": "PKG1",
                "weight": 5,
                "distance": 5,
                "offer_code": 'OFR001'
            },
            {
                "id": "PKG2",
                "weight": 15,
                "distance": 5,
                "offer_code": 'OFR002'
            },
            {
                "id": "PKG3",
                "weight": 10,
                "distance": 100,
                "offer_code": 'OFR003'
            }
        ]

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

    def test_create_packages_with_valid_data(self):
        """Tests that we are able to add packages correctly"""
        packages = create_packages(self.test_packages)
        self.assertIsNotNone(packages)
        self.assertIsInstance(packages, list)
        for package in packages:
            self.assertIsInstance(package, Package)

    def test_create_packages_with_invalid_data(self):
        """Tests that packages should not be set in case of invalid data"""
        self.test_packages_invalid = deepcopy(self.test_packages)
        del self.test_packages_invalid[0]["distance"]
        with self.assertRaises(TypeError) as err:
            create_packages(self.test_packages_invalid)

    def test_create_packages_with_valid_data(self):
        """Tests that we are able to create offers correctly"""
        offers = create_offers(self.test_offers)
        self.assertIsNotNone(offers)
        self.assertIsInstance(offers, list)
        for offer in offers:
            self.assertIsInstance(offer, Offer)

    def test_create_offers_with_invalid_data(self):
        """Tests that offers should not be set in case of invalid data"""
        self.test_offers_invalid = deepcopy(self.test_offers)
        del self.test_offers_invalid[0]["code"]
        with self.assertRaises(TypeError) as err:
            create_offers(self.test_offers_invalid)
