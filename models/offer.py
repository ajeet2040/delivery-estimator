"""Module for entity 'offer'."""
from dataclasses import dataclass


@dataclass
class Offer:
    """Class for keeping track of offer codes and their criteria"""
    code: str
    min_distance: float
    max_distance: float
    min_weight: float
    max_weight: float
    discount_per: float

    def is_offer_code_valid(self, distance: float, weight: float) -> bool:
        """
        Check if offer is valid for the package based in criteria
        :param distance: distance of package delivery
        :param weight: weight of package
        :return: offer_status: whether offer code is valid or not
        """
        pass
