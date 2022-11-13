"""Module for entity 'Package'."""
from dataclasses import dataclass
from typing import Optional

from offer import Offer

@dataclass
class Package:
    """Class for keeping track of package"""
    id: str
    weight: float
    distance: float
    offer_code: str
    assigned_offer: Optional[Offer] = None
    delivery_cost: Optional[float] = 0
    discount_amt: Optional[float] = 0
    total_delivery_cost: Optional[float] = 0

    def calculate_delivery_cost(self, base_delivery_cost: float) -> None:
        """
        Calculates delivery cost for the package.
        :param base_delivery_cost: base delivery cost to be applied
        :return: None
        """
        pass

    def calculate_discount(self):
        """
        Calculate Discount amount for the package.
        :return: None
        """
        pass

    def calculate_total_delivery_cost(self):
        """
        Calculate total delivery cost for the package
        :return: None
        """
        pass

