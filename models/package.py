"""Module for entity 'Package'."""
from dataclasses import dataclass
from typing import Optional

from models.offer import Offer


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
    delivery_time: Optional[float] = 0

    def calculate_delivery_cost(self, base_delivery_cost: float, weight_multiplier: float,
                                distance_multiplier: float) -> None:
        """
        Calculates delivery cost for the package.
        :param weight_multiplier: multiplication factor for weight
        :param distance_multiplier: multiplication factor for distance
        :param base_delivery_cost: base delivery cost to be applied
        :return: None
        """
        self.delivery_cost = base_delivery_cost + (self.weight * weight_multiplier) + \
            (self.distance * distance_multiplier)

    def calculate_discount(self) -> None:
        """
        Calculate Discount amount for the package.
        :return: None
        """
        if self.assigned_offer:
            self.discount_amt = self.delivery_cost * (self.assigned_offer.discount_per/100)

    def calculate_total_delivery_cost(self) -> None:
        """
        Calculate total delivery cost for the package
        :return: None
        """
        self.total_delivery_cost = self.delivery_cost - self.discount_amt
