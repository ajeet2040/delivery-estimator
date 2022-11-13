"""Tests for module 'delivery_time_calculator' """
import json
import unittest
from delivery_time_calculator import DeliveryTimeCalculator
from models.vehicle import Vehicle
from models.package import Package
from copy import deepcopy


class TestDeliveryTimeCalculator(unittest.TestCase):
    """Test cases for class 'TestDeliveryTimeCalculator'"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_vehicles = [
            {
                "id": "V001",
                "max_speed": 70,
                "max_carriable_weight": 200
            },
            {
                "id": "V002",
                "max_speed": 70,
                "max_carriable_weight": 200
            }
        ]

    def test_select_shipment_per_criteria_1(self):
        """Test case for selecting shipment based on criteria - test1"""
        # Input packages and vehicle
        self.test_packages = json.load(open('tests/data/shipments/shipment1_packages.json', 'r'))
        delivery_time_calculator = DeliveryTimeCalculator(no_of_vehicles=2)
        for vehicle in self.test_vehicles:
            delivery_time_calculator.vehicles.append(Vehicle(**vehicle))
        for package in self.test_packages:
            delivery_time_calculator.packages.append(Package(**package))

        # Expected output
        packages_copy = deepcopy(delivery_time_calculator.packages)
        packages_copy[1].delivery_time = 1.78  # PKG2
        packages_copy[3].delivery_time = 0.85  # PKG
        expected_shipment_packages = (packages_copy[1], packages_copy[3])
        expected_vehicle = delivery_time_calculator.vehicles[0]
        print("expected_shipment_packages", expected_shipment_packages)

        selected_shipment = delivery_time_calculator.select_shipment_per_criteria(delivery_time_calculator.packages,
                                                                                  delivery_time_calculator.vehicles[0])
        print("selected_shipment", selected_shipment)

        # Tests
        self.assertIsNotNone(selected_shipment)
        self.assertEqual(len(selected_shipment["packages"]), 2)
        self.assertEqual(selected_shipment["packages"], expected_shipment_packages)
        self.assertEqual(selected_shipment["total_weight"], 185)
        self.assertEqual(selected_shipment["total_round_time"], 3.56)
        self.assertEqual(selected_shipment["vehicle"], expected_vehicle)

    def test_select_shipment_per_criteria_2(self):
        """Test case for selecting shipment based on criteria - test2"""
        # Input packages and vehicle
        self.test_packages = json.load(open('tests/data/shipments/shipment2_packages.json', 'r'))
        delivery_time_calculator = DeliveryTimeCalculator(no_of_vehicles=2)
        for vehicle in self.test_vehicles:
            delivery_time_calculator.vehicles.append(Vehicle(**vehicle))
        for package in self.test_packages:
            delivery_time_calculator.packages.append(Package(**package))

        # Expected output
        packages_copy = deepcopy(delivery_time_calculator.packages)
        packages_copy[1].delivery_time = 1.42   # PKG2
        expected_shipment_packages = (packages_copy[1])
        expected_vehicle = delivery_time_calculator.vehicles[0]
        print("expected_shipment_packages", expected_shipment_packages)

        selected_shipment = delivery_time_calculator.select_shipment_per_criteria(delivery_time_calculator.packages,
                                                                                  delivery_time_calculator.vehicles[0])
        print("selected_shipment", selected_shipment)
        # Tests
        self.assertIsNotNone(selected_shipment)
        self.assertEqual(len(selected_shipment["packages"]), 1)
        self.assertEqual(selected_shipment["packages"], expected_shipment_packages)
        self.assertEqual(selected_shipment["total_weight"], 175)
        self.assertEqual(selected_shipment["total_round_time"], 2.84)
        self.assertEqual(selected_shipment["vehicle"], expected_vehicle)

    def test_select_shipment_per_criteria_3(self):
        """Test case for selecting shipment based on criteria - test3"""
        self.test_packages = json.load(open('tests/data/shipments/shipment3_packages.json', 'r'))
        # Input packages and vehicle
        delivery_time_calculator = DeliveryTimeCalculator(no_of_vehicles=2)
        for vehicle in self.test_vehicles:
            delivery_time_calculator.vehicles.append(Vehicle(**vehicle))
        for package in self.test_packages:
            delivery_time_calculator.packages.append(Package(**package))

        # Expected output
        packages_copy = deepcopy(delivery_time_calculator.packages)
        packages_copy[0].delivery_time = 1.35  # PKG5
        expected_shipment_packages = (packages_copy[0])
        expected_vehicle = delivery_time_calculator.vehicles[0]
        print("expected_shipment_packages", expected_shipment_packages)

        selected_shipment = delivery_time_calculator.select_shipment_per_criteria(delivery_time_calculator.packages,
                                                                                  delivery_time_calculator.vehicles[0])
        print("selected_shipment", selected_shipment)

        # Tests
        self.assertIsNotNone(selected_shipment)
        self.assertEqual(len(selected_shipment["packages"]), 1)
        self.assertEqual(selected_shipment["packages"], expected_shipment_packages)
        self.assertEqual(selected_shipment["total_weight"], 155)
        self.assertEqual(selected_shipment["total_round_time"], 2.70)
        self.assertEqual(selected_shipment["vehicle"], expected_vehicle)

    def test_calculate_delivery_time_packages(self):
        """Tests that we are correctly calculate delivery time for packages"""
        self.test_packages = json.load(open('tests/data/shipments/shipment1_packages.json', 'r'))
        delivery_time_calculator = DeliveryTimeCalculator(no_of_vehicles=2)
        # Set offers and packages manually to avoid dependency on other methods
        for vehicle in self.test_vehicles:
            delivery_time_calculator.vehicles.append(Vehicle(**vehicle))
        for package in self.test_packages:
            delivery_time_calculator.packages.append(Package(**package))

        delivery_time_calculator.calculate_time_for_packages()
        # Package PKG1
        self.assertEqual(delivery_time_calculator.packages[0].delivery_time, 3.98)
        # Package PKG2
        self.assertEqual(delivery_time_calculator.packages[1].delivery_time, 1.78)
        # Package PKG3
        self.assertEqual(delivery_time_calculator.packages[2].delivery_time, 1.42)
        # Package PKG4
        self.assertEqual(delivery_time_calculator.packages[3].delivery_time, 0.85)
        # Package PKG5
        self.assertEqual(delivery_time_calculator.packages[4].delivery_time, 4.19)


if __name__ == "__main__":
    unittest.main()
