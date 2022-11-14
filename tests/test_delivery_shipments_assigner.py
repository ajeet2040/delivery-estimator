"""Tests for module 'delivery_shipments_assigner' """
import json
import unittest
from delivery_shipments_assigner import DeliveryShipmentsAssigner
from models.vehicle import Vehicle
from models.package import Package
from copy import deepcopy


def assign_test_packages_vehicles(delivery_shipments_assigner: DeliveryShipmentsAssigner, packages: list, vehicles: list):
    """
    Helper method to add packages and vehicles to class directly for testing purpose
    :param delivery_shipments_assigner: DeliveryTimeCalculator instance
    :param packages: packages to be added
    :param vehicles: vehicles to be added
    :return:None
    """
    for vehicle in vehicles:
        delivery_shipments_assigner.vehicles.append(Vehicle(**vehicle))
    for package in packages:
        delivery_shipments_assigner.packages.append(Package(**package))


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

    def test_create_shipment_per_criteria_1(self):
        """Test case for selecting shipment based on criteria - test1"""
        # Input packages and vehicle
        with open('tests/data/shipments/shipment1_packages.json', 'r') as file:
            self.test_packages = json.load(file)
        delivery_shipments_assigner = DeliveryShipmentsAssigner(no_of_vehicles=2)
        assign_test_packages_vehicles(delivery_shipments_assigner, self.test_packages, self.test_vehicles)
        delivery_shipments_assigner.pending_packages = delivery_shipments_assigner.packages

        # Expected output
        packages_copy = deepcopy(delivery_shipments_assigner.packages)
        packages_copy[1].delivery_time = 1.78  # PKG2
        packages_copy[3].delivery_time = 0.85  # PKG
        expected_shipment_packages = [packages_copy[1], packages_copy[3]]
        expected_vehicle = delivery_shipments_assigner.vehicles[0]

        delivery_shipments_assigner.create_shipment_per_criteria(delivery_shipments_assigner.vehicles[0])
        selected_shipment = delivery_shipments_assigner.current_shipment

        # Tests
        self.assertIsNotNone(selected_shipment)
        self.assertEqual(len(selected_shipment["packages"]), 2)
        self.assertEqual(selected_shipment["packages"], expected_shipment_packages)
        self.assertEqual(selected_shipment["total_weight"], 185)
        self.assertEqual(selected_shipment["total_round_time"], 3.56)
        self.assertEqual(selected_shipment["vehicle"], expected_vehicle)

    def test_create_shipment_per_criteria_2(self):
        """Test case for selecting shipment based on criteria - test2"""
        # Input packages and vehicle
        with open('tests/data/shipments/shipment2_packages.json', 'r') as file:
            self.test_packages = json.load(file)
        delivery_shipments_assigner = DeliveryShipmentsAssigner(no_of_vehicles=2)
        assign_test_packages_vehicles(delivery_shipments_assigner, self.test_packages, self.test_vehicles)
        delivery_shipments_assigner.pending_packages = delivery_shipments_assigner.packages

        # Expected output
        packages_copy = deepcopy(delivery_shipments_assigner.packages)
        packages_copy[1].delivery_time = 1.42   # PKG2
        expected_shipment_packages = [packages_copy[1]]
        expected_vehicle = delivery_shipments_assigner.vehicles[0]

        delivery_shipments_assigner.create_shipment_per_criteria(delivery_shipments_assigner.vehicles[0])
        selected_shipment = delivery_shipments_assigner.current_shipment

        # Tests
        self.assertIsNotNone(selected_shipment)
        self.assertEqual(len(selected_shipment["packages"]), 1)
        self.assertEqual(selected_shipment["packages"], expected_shipment_packages)
        self.assertEqual(selected_shipment["total_weight"], 175)
        self.assertEqual(selected_shipment["total_round_time"], 2.84)
        self.assertEqual(selected_shipment["vehicle"], expected_vehicle)

    def test_create_shipment_per_criteria_3(self):
        """Test case for selecting shipment based on criteria - test3"""
        # Input packages and vehicle
        with open('tests/data/shipments/shipment3_packages.json', 'r') as file:
            self.test_packages = json.load(file)        # Input packages and vehicle
        delivery_shipments_assigner = DeliveryShipmentsAssigner(no_of_vehicles=2)
        assign_test_packages_vehicles(delivery_shipments_assigner, self.test_packages, self.test_vehicles)
        delivery_shipments_assigner.pending_packages = delivery_shipments_assigner.packages

        # Expected output
        packages_copy = deepcopy(delivery_shipments_assigner.packages)
        packages_copy[1].delivery_time = 1.35  # PKG5
        expected_shipment_packages = [packages_copy[1]]
        expected_vehicle = delivery_shipments_assigner.vehicles[0]

        delivery_shipments_assigner.create_shipment_per_criteria(delivery_shipments_assigner.vehicles[0])
        selected_shipment = delivery_shipments_assigner.current_shipment

        # Tests
        self.assertIsNotNone(selected_shipment)
        self.assertEqual(len(selected_shipment["packages"]), 1)
        self.assertEqual(selected_shipment["packages"], expected_shipment_packages)
        self.assertEqual(selected_shipment["total_weight"], 155)
        self.assertEqual(selected_shipment["total_round_time"], 2.70)
        self.assertEqual(selected_shipment["vehicle"], expected_vehicle)

    def test_create_shipment_per_criteria_4(self):
        """Test case for selecting shipment based on criteria - test3"""
        # Input packages and vehicle
        with open('tests/data/shipments/shipment4_packages.json', 'r') as file:
            self.test_packages = json.load(file)
        delivery_shipments_assigner = DeliveryShipmentsAssigner(no_of_vehicles=2)
        assign_test_packages_vehicles(delivery_shipments_assigner, self.test_packages, self.test_vehicles)
        delivery_shipments_assigner.pending_packages = delivery_shipments_assigner.packages

        # Expected output
        packages_copy = deepcopy(delivery_shipments_assigner.packages)
        packages_copy[0].delivery_time = 0.42  # PKG1
        expected_shipment_packages = [packages_copy[0]]
        expected_vehicle = delivery_shipments_assigner.vehicles[0]

        delivery_shipments_assigner.create_shipment_per_criteria(delivery_shipments_assigner.vehicles[0])
        selected_shipment = delivery_shipments_assigner.current_shipment

        # Tests
        self.assertIsNotNone(selected_shipment)
        self.assertEqual(len(selected_shipment["packages"]), 1)
        self.assertEqual(selected_shipment["packages"], expected_shipment_packages)
        self.assertEqual(selected_shipment["total_weight"], 50)
        self.assertEqual(selected_shipment["total_round_time"], 0.84)
        self.assertEqual(selected_shipment["vehicle"], expected_vehicle)

    def test_create_shipments_delivery(self):
        """Tests that we are correctly calculate delivery time for packages"""
        # Input packages and vehicle
        with open('tests/data/shipments/shipment1_packages.json', 'r') as file:
            self.test_packages = json.load(file)
        delivery_shipments_assigner = DeliveryShipmentsAssigner(no_of_vehicles=2)
        # Set offers and packages manually to avoid dependency on other methods
        assign_test_packages_vehicles(delivery_shipments_assigner, self.test_packages, self.test_vehicles)
        delivery_shipments_assigner.pending_packages = delivery_shipments_assigner.packages

        delivery_shipments_assigner.create_shipments_for_delivery()

        # Tests
        self.assertTrue(delivery_shipments_assigner.all_shipments_assigned)
        self.assertIsNotNone(delivery_shipments_assigner.shipments)
        self.assertEqual(len(delivery_shipments_assigner.pending_packages), 0)
        # Package PKG1
        self.assertEqual(3.98, delivery_shipments_assigner.packages[0].delivery_time)
        # Package PKG2
        self.assertEqual(1.78, delivery_shipments_assigner.packages[1].delivery_time)
        # Package PKG3
        self.assertEqual(1.42, delivery_shipments_assigner.packages[2].delivery_time)
        # Package PKG4
        self.assertEqual(0.85, delivery_shipments_assigner.packages[3].delivery_time)
        # Package PKG5
        self.assertEqual(4.18, delivery_shipments_assigner.packages[4].delivery_time)


if __name__ == "__main__":
    unittest.main()
