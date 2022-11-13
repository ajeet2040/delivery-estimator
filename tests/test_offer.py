"""Tests for module 'offer' """
import unittest
from models.offer import Offer


class TestOffer(unittest.TestCase):
    """Test cases for class 'Offer'"""

    def test_create_offer_without_code(self):
        """Tests that offer code is required for Offer"""
        with self.assertRaises(TypeError):
            Offer(min_weight=10, max_weight=100, min_distance=20, max_distance=200, discount_per=10)

    def test_create_offer_without_min_weight(self):
        """Tests that min_weight is required for Offer"""
        with self.assertRaises(TypeError):
            Offer(code='OFO001', max_weight=100, min_distance=20, max_distance=200, discount_per=10)

    def test_create_offer_without_max_weight(self):
        """Tests that max_weight is required for Offer"""
        with self.assertRaises(TypeError):
            Offer(code='OFO001', min_weight=10, min_distance=20, max_distance=200, discount_per=10)

    def test_create_offer_without_min_distance(self):
        """Tests that min_distance is required for Offer"""
        with self.assertRaises(TypeError):
            Offer(code='OFO001', min_weight=10, max_weight=100, max_distance=200, discount_per=10)

    def test_create_offer_without_max_distance(self):
        """Tests that max_distance is required for Offer"""
        with self.assertRaises(TypeError):
            Offer(code='OFO001', min_weight=10, max_weight=100, min_distance=20, discount_per=10)

    def test_create_offer_without_discount_per(self):
        """Tests that discount_per is required for Offer"""
        with self.assertRaises(TypeError):
            Offer(code='OFO001', min_weight=10, max_weight=100, min_distance=20, max_distance=200)

    def test_is_offer_code_valid(self):
        offer = Offer(code='OFO001', min_weight=10, max_weight=100, min_distance=20, max_distance=200, discount_per=10)
        self.assertFalse(offer.is_offer_code_valid(distance=10, weight=20))
        self.assertFalse(offer.is_offer_code_valid(distance=100, weight=200))
        self.assertTrue(offer.is_offer_code_valid(distance=100, weight=50))
