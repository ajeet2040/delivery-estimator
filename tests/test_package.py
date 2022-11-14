"""Tests for module 'package' """
import unittest
from models.package import Package
from models.offer import Offer


class TestPackage(unittest.TestCase):
    """Test cases for class 'Package'"""

    def test_create_package_without_weight(self):
        """Tests that offer code is required for package"""
        with self.assertRaises(TypeError):
            Package(id="PKG1", distance=5, offer_code="OFR1")

    def test_create_package_without_distance(self):
        """Tests that distance is required for package"""
        with self.assertRaises(TypeError):
            Package(id="PKG1", weight=5, offer_code="OFR1")

    def test_create_package_without_offer_code(self):
        """Tests that offer code is required for package"""
        with self.assertRaises(TypeError):
            Package(id="PKG1", weight=5, distance=10)

    def test_calculate_delivery_cost_package_1(self):
        """Test delivery cost for a package 1"""
        package = Package(id="PKG1", weight=5, distance=10, offer_code="OFR1")
        base_delivery_cost = 100
        expected_delivery_cost = 200
        package.calculate_delivery_cost(base_delivery_cost, weight_multiplier=10, distance_multiplier=5)
        self.assertIsNotNone(package.delivery_cost)
        self.assertEqual(package.delivery_cost, expected_delivery_cost)

    def test_calculate_delivery_cost_package_2(self):
        """Test delivery cost for a package 2"""
        package = Package(id="PKG2", weight=10, distance=0, offer_code="OFR1")
        base_delivery_cost = 100
        expected_delivery_cost = 200

        package.calculate_delivery_cost(base_delivery_cost, weight_multiplier=10, distance_multiplier=10)
        self.assertIsNotNone(package.delivery_cost)
        self.assertEqual(package.delivery_cost, expected_delivery_cost)

    def test_calculate_discount_package_1(self):
        """Test discount for package 1"""
        package = Package(id="PKG1", weight=5, distance=10, offer_code="OFR1")
        offer = Offer(code='OFR1', min_distance=5, max_distance=10, min_weight=1, max_weight=5, discount_per=10)
        package.delivery_cost = 200
        package.assigned_offer = offer
        expected_discount = 20

        package.calculate_discount()
        self.assertIsNotNone(package.discount_amt)
        self.assertEqual(package.discount_amt, expected_discount)

    def test_calculate_discount_package_2(self):
        """Test discount for package 2"""
        package = Package(id="PKG2", weight=5, distance=10, offer_code="OFR1")
        expected_discount = 0

        package.calculate_discount()
        self.assertIsNotNone(package.discount_amt)
        self.assertEqual(package.discount_amt, expected_discount)

    def test_calculate_total_delivery_cost_package_1(self):
        """Test total delivery cost for a package 1"""
        package = Package(id="PKG1", weight=5, distance=10, offer_code="OFR1")
        offer = Offer(code='OFR1', min_distance=5, max_distance=10, min_weight=1, max_weight=5, discount_per=10)
        package.delivery_cost = 200
        package.assigned_offer = offer
        package.discount_amt = 20
        expected_total_delivery_cost = 180

        package.calculate_total_delivery_cost()
        self.assertIsNotNone(package.total_delivery_cost)
        self.assertEqual(package.total_delivery_cost, expected_total_delivery_cost)

    def test_calculate_total_delivery_cost_package_2(self):
        """Test total delivery cost for a package 2"""
        package = Package(id="PKG2", weight=5, distance=10, offer_code="OFR1")
        package.delivery_cost = 200
        expected_total_delivery_cost = 200

        package.calculate_total_delivery_cost()
        self.assertIsNotNone(package.total_delivery_cost)
        self.assertEqual(package.total_delivery_cost, expected_total_delivery_cost)


if __name__ == "__main__":
    unittest.main()

