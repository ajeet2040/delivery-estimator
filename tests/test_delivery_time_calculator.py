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
        with open('tests/data/shipments/shipment1_packages.json', 'r') as file:
            self.test_packages = json.load(file)
        delivery_time_calculator = DeliveryTimeCalculator(no_of_vehicles=2)
        for vehicle in self.test_vehicles:
            delivery_time_calculator.vehicles.append(Vehicle(**vehicle))
        for package in self.test_packages:
            delivery_time_calculator.packages.append(Package(**package))

        # Expected output
        packages_copy = deepcopy(delivery_time_calculator.packages)
        packages_copy[1].delivery_time = 1.78  # PKG2
        packages_copy[3].delivery_time = 0.85  # PKG
        expected_shipment_packages = [packages_copy[1], packages_copy[3]]
        expected_vehicle = delivery_time_calculator.vehicles[0]

        selected_shipment = delivery_time_calculator.select_shipment_per_criteria(delivery_time_calculator.packages,
                                                                                  delivery_time_calculator.vehicles[0])

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
        with open('tests/data/shipments/shipment2_packages.json', 'r') as file:
            self.test_packages = json.load(file)
        delivery_time_calculator = DeliveryTimeCalculator(no_of_vehicles=2)
        for vehicle in self.test_vehicles:
            delivery_time_calculator.vehicles.append(Vehicle(**vehicle))
        for package in self.test_packages:
            delivery_time_calculator.packages.append(Package(**package))

        # Expected output
        packages_copy = deepcopy(delivery_time_calculator.packages)
        packages_copy[1].delivery_time = 1.42   # PKG2
        expected_shipment_packages = [packages_copy[1]]
        expected_vehicle = delivery_time_calculator.vehicles[0]

        selected_shipment = delivery_time_calculator.select_shipment_per_criteria(delivery_time_calculator.packages,
                                                                                  delivery_time_calculator.vehicles[0])
        # Tests
        self.assertIsNotNone(selected_shipment)
        self.assertEqual(len(selected_shipment["packages"]), 1)
        self.assertEqual(selected_shipment["packages"], expected_shipment_packages)
        self.assertEqual(selected_shipment["total_weight"], 175)
        self.assertEqual(selected_shipment["total_round_time"], 2.84)
        self.assertEqual(selected_shipment["vehicle"], expected_vehicle)

    def test_select_shipment_per_criteria_3(self):
        """Test case for selecting shipment based on criteria - test3"""
        with open('tests/data/shipments/shipment3_packages.json', 'r') as file:
            self.test_packages = json.load(file)        # Input packages and vehicle
        delivery_time_calculator = DeliveryTimeCalculator(no_of_vehicles=2)
        for vehicle in self.test_vehicles:
            delivery_time_calculator.vehicles.append(Vehicle(**vehicle))
        for package in self.test_packages:
            delivery_time_calculator.packages.append(Package(**package))

        # Expected output
        packages_copy = deepcopy(delivery_time_calculator.packages)
        packages_copy[1].delivery_time = 1.35  # PKG5
        expected_shipment_packages = [packages_copy[1]]
        expected_vehicle = delivery_time_calculator.vehicles[0]

        selected_shipment = delivery_time_calculator.select_shipment_per_criteria(delivery_time_calculator.packages,
                                                                                  delivery_time_calculator.vehicles[0])

        # Tests
        self.assertIsNotNone(selected_shipment)
        self.assertEqual(len(selected_shipment["packages"]), 1)
        self.assertEqual(selected_shipment["packages"], expected_shipment_packages)
        self.assertEqual(selected_shipment["total_weight"], 155)
        self.assertEqual(selected_shipment["total_round_time"], 2.70)
        self.assertEqual(selected_shipment["vehicle"], expected_vehicle)

    def test_select_shipment_per_criteria_4(self):
        """Test case for selecting shipment based on criteria - test3"""
        with open('tests/data/shipments/shipment4_packages.json', 'r') as file:
            self.test_packages = json.load(file)
        # Input packages and vehicle
        delivery_time_calculator = DeliveryTimeCalculator(no_of_vehicles=2)
        for vehicle in self.test_vehicles:
            delivery_time_calculator.vehicles.append(Vehicle(**vehicle))
        for package in self.test_packages:
            delivery_time_calculator.packages.append(Package(**package))

        # Expected output
        packages_copy = deepcopy(delivery_time_calculator.packages)
        packages_copy[0].delivery_time = 0.42  # PKG1
        expected_shipment_packages = [packages_copy[0]]
        expected_vehicle = delivery_time_calculator.vehicles[0]

        selected_shipment = delivery_time_calculator.select_shipment_per_criteria(delivery_time_calculator.packages,
                                                                                  delivery_time_calculator.vehicles[0])

        # Tests
        self.assertIsNotNone(selected_shipment)
        self.assertEqual(len(selected_shipment["packages"]), 1)
        self.assertEqual(selected_shipment["packages"], expected_shipment_packages)
        self.assertEqual(selected_shipment["total_weight"], 50)
        self.assertEqual(selected_shipment["total_round_time"], 0.84)
        self.assertEqual(selected_shipment["vehicle"], expected_vehicle)

    def test_create_shipments_delivery(self):
        """Tests that we are correctly calculate delivery time for packages"""
        with open('tests/data/shipments/shipment1_packages.json', 'r') as file:
            self.test_packages = json.load(file)
        delivery_time_calculator = DeliveryTimeCalculator(no_of_vehicles=2)
        # Set offers and packages manually to avoid dependency on other methods
        for vehicle in self.test_vehicles:
            delivery_time_calculator.vehicles.append(Vehicle(**vehicle))
        for package in self.test_packages:
            delivery_time_calculator.packages.append(Package(**package))

        delivery_time_calculator.create_shipments_delivery()
        self.assertTrue(delivery_time_calculator.shipments_organising_status)
        # Package PKG1
        self.assertEqual(3.98, delivery_time_calculator.packages[0].delivery_time)
        # Package PKG2
        self.assertEqual(1.78, delivery_time_calculator.packages[1].delivery_time)
        # Package PKG3
        self.assertEqual(1.42, delivery_time_calculator.packages[2].delivery_time)
        # Package PKG4
        self.assertEqual(0.85, delivery_time_calculator.packages[3].delivery_time)
        # Package PKG5
        self.assertEqual(4.18, delivery_time_calculator.packages[4].delivery_time)


if __name__ == "__main__":
    unittest.main()
