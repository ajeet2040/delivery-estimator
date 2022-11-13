"""Module for entity 'Vehicle'."""
from dataclasses import dataclass


@dataclass
class Vehicle:
    """Class for keeping track of Vehicle"""
    id: str
    max_speed: float
    max_carriable_weight: float
