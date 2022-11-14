"""Tests for module 'utils' """
import unittest
import json
from utils import read_json_file, create_packages, create_offers, create_vehicles, round_down_2_digits
from models.package import Package
from models.offer import Offer
from models.vehicle import Vehicle
from copy import deepcopy


class TestUtils(unittest.TestCase):
    """Test cases for class 'Package'"""

    @classmethod
    def setUpClass(cls) -> None:
        with open('tests/data/offers/offers.json', 'r') as file:
            cls.test_offers = json.load(file)
        with open('tests/data/shipments/shipment1_packages.json', 'r') as file:
            cls.test_packages = json.load(file)
        cls.test_vehicles = [
            {
                "id": "V001",
                "max_speed": 5,
                "max_carriable_weight": 5,
            },
            {
                "id": "V002",
                "max_speed": 15,
                "max_carriable_weight": 5,
            },
            {
                "id": "V003",
                "max_speed": 10,
                "max_carriable_weight": 100,
            }
        ]

    def test_read_json_data_correctly(self):
        """Tests that we are able to set offers correctly"""
        file_path = 'tests/data/offers/offers.json'
        actual_data = read_json_file(file_path)
        self.assertIsNotNone(actual_data)
        self.assertIsInstance(actual_data, list)
        self.assertEqual(len(actual_data), 3)

    def test_read_json_data_file_absent(self):
        """Tests that we are able to set offers correctly"""
        file_path = 'tests/data/offers/offers_absent.json'
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

    def test_create_vehicles_with_valid_data(self):
        """Tests that we are able to create offers correctly"""
        vehicles = create_vehicles(self.test_vehicles)
        self.assertIsNotNone(vehicles)
        self.assertIsInstance(vehicles, list)
        for vehicle in vehicles:
            self.assertIsInstance(vehicle, Vehicle)

    def test_create_vehicles_with_invalid_data(self):
        """Tests that offers should not be set in case of invalid data"""
        self.test_vehicles_invalid = deepcopy(self.test_vehicles)
        del self.test_vehicles_invalid[0]["max_speed"]
        with self.assertRaises(TypeError) as err:
            create_vehicles(self.test_vehicles_invalid)

    def test_round_down_2_digits(self):
        """Tests that offers should not be set in case of invalid data"""
        self.assertEqual(round_down_2_digits(4.196667), 4.19)
        self.assertEqual(round_down_2_digits(4.2), 4.2)
        self.assertEqual(round_down_2_digits(4), 4)
        self.assertEqual(round_down_2_digits(4.192), 4.19)


if __name__ == "__main__":
    unittest.main()
