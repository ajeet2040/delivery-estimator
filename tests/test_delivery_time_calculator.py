"""Tests for module 'delivery_time_estimator' """
import unittest
from delivery_time_calculator import DeliveryTimeCalculator
from models.vehicle import Vehicle
from models.package import Package


class TestDeliveryTimeCalculator(unittest.TestCase):
    """Test cases for class 'TestDeliveryTimeCalculator'"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_packages = [
            {
                "id": "PKG1",
                "weight": 50,
                "distance": 30,
                "offer_code": 'OFR001'
            },
            {
                "id": "PKG2",
                "weight": 75,
                "distance": 125,
                "offer_code": 'OFR008'
            },
            {
                "id": "PKG3",
                "weight": 175,
                "distance": 100,
                "offer_code": 'OFR003'
            },
            {
                "id": "PKG4",
                "weight": 110,
                "distance": 60,
                "offer_code": 'OFR002'
            },
            {
                "id": "PKG5",
                "weight": 155,
                "distance": 95,
                "offer_code": 'NA'
            }
        ]
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

    def test_calculate_delivery_time_packages(self):
        """Tests that we are correctly calculate delivery time for packages"""
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
        self.assertEqual(delivery_time_calculator.packages[1].delivery_time, 0.85)
        # Package PKG5
        self.assertEqual(delivery_time_calculator.packages[2].delivery_time, 4.19)


if __name__ == "__main__":
    unittest.main()
