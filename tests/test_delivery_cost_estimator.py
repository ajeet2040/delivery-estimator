"""Tests for module 'delivery_cost_estimator' """
import unittest
from delivery_cost_estimator import DeliveryCostEstimator
from utils import read_json_file
from models.offer import Offer
from models.package import Package
from copy import deepcopy


class TestDeliveryCostEstimator(unittest.TestCase):
    """Test cases for class 'TestDeliveryCostEstimator'"""

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

    def test_assign_offer_to_package(self):
        """Tests that we are correctly set offer to package"""
        delivery_cost_estimator = DeliveryCostEstimator(base_delivery_cost=100, no_of_packages=10)
        # Set offers and packages manually to avoid dependency on other methods

        for offer in self.test_offers:
            delivery_cost_estimator.offers.append(Offer(**offer))
        for package in self.test_packages:
            delivery_cost_estimator.packages.append(Package(**package))

        delivery_cost_estimator.assign_offer_package()
        self.assertIsNone(delivery_cost_estimator.packages[0].assigned_offer)
        self.assertIsNone(delivery_cost_estimator.packages[1].assigned_offer)
        self.assertIsNotNone(delivery_cost_estimator.packages[2].assigned_offer)
        self.assertEquals(delivery_cost_estimator.packages[2].assigned_offer.code, 'OFR003')

    def test_total_delivery_cost_package(self):
        """Tests that we are correctly set offer to package"""
        delivery_cost_estimator = DeliveryCostEstimator(base_delivery_cost=100, no_of_packages=10)
        # Set offers and packages manually to avoid dependency on other methods
        for offer in self.test_offers:
            delivery_cost_estimator.offers.append(Offer(**offer))
        for package in self.test_packages:
            delivery_cost_estimator.packages.append(Package(**package))
        delivery_cost_estimator.packages[2].assigned_offer = delivery_cost_estimator.offers[2]

        delivery_cost_estimator.calculate_delivery_cost()
        # Package PKG1
        self.assertEqual(delivery_cost_estimator.packages[0].delivery_cost, 175)
        self.assertEqual(delivery_cost_estimator.packages[0].discount_amt, 0)
        self.assertEqual(delivery_cost_estimator.packages[0].total_delivery_cost, 175)
        # Package PKG2
        self.assertEqual(delivery_cost_estimator.packages[1].delivery_cost, 275)
        self.assertEqual(delivery_cost_estimator.packages[1].discount_amt, 0)
        self.assertEqual(delivery_cost_estimator.packages[1].total_delivery_cost, 275)
        # Package PKG3
        self.assertEqual(delivery_cost_estimator.packages[2].delivery_cost, 700)
        self.assertEqual(delivery_cost_estimator.packages[2].discount_amt, 35)
        self.assertEqual(delivery_cost_estimator.packages[2].total_delivery_cost,665)


if __name__ == "__main__":
    unittest.main()

