"""Tests for module 'offer' """
import unittest
from models.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    """Test cases for class 'Vehicle'"""

    def test_create_vehicle_without_code(self):
        """Tests that id is required for Vehicle"""
        with self.assertRaises(TypeError):
            Vehicle(max_speed=100, max_carriable_weight=20)

    def test_create_vehicle_without_max_speed(self):
        """Tests that max_speed is required for Vehicle"""
        with self.assertRaises(TypeError):
            Vehicle(id='V001', max_carriable_weight=20)

    def test_create_vehicle_without_max_carriable_weight(self):
        """Tests that max_carriable_weight is required for Vehicle"""
        with self.assertRaises(TypeError):
            Vehicle(id='V001', max_speed=100)
