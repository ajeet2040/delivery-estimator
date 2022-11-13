"""This module will be responsible for working with different packages in a shipment and setting up
their delivery cost considering any discount if applicable"""
from models.offer import Offer
from models.package import Package


class DeliveryCostEstimator:
    """
    Responsible for working with different packages setting up
    their delivery cost considering any discount if applicable
    """

    def __init__(self, base_delivery_cost: float, no_of_packages: int, weight_multiplier: int = 10,
                 distance_multiplier: int = 5) -> None:
        """
        Initialises Estimator instance
        :param base_delivery_cost: base delivery cost that will be fixed
        :param no_of_packages: no of packages to be estimated for cost
        :param weight_multiplier: multiplication factor for weight to deduce cost
        :param distance_multiplier: multiplication factor for distance to deduce cost
        """
        self.base_delivery_cost = base_delivery_cost
        self.no_of_packages = no_of_packages
        self.weight_multiplier = weight_multiplier
        self.distance_multiplier = distance_multiplier
        # NOTE: The offers are stored here for simplicity purpose. For scalability, this can be queried from database.
        self.offers = []
        self.packages = []

    def set_offers(self, offers_list: list) -> None:
        """
        Sets Available offers.
        :param offers_list: list of offer along with criteria for discount
        :return: None
        :raises TypeError in case offer object properties are invalid
        """
        for idx, offer_data in enumerate(offers_list):
            try:
                self.offers.append(Offer(**offer_data))
            except TypeError as err:
                print(f"Make sure all properties of offer are setup in json file.")
                raise err

    def add_packages(self, packages: list) -> None:
        """
        Sets packages.
        :param packages: list of packages along with details
        :return: None
        :raises TypeError in case Package object properties are invalid
        """
        for idx, package in enumerate(packages):
            try:
                self.packages.append(Package(**package))
            except TypeError as err:
                print(f"Make sure all properties of package are provided correctly.")
                raise err

    def assign_offer_package(self) -> None:
        """
        Assigns applicable offer to the package
        :return: None
        """
        for package in self.packages:
            matched_offer = next((offer for offer in self.offers if offer.code == package.offer_code), False)
            if matched_offer and matched_offer.is_offer_code_valid(package.distance, package.weight):
                package.assigned_offer = matched_offer

    def calculate_delivery_cost(self) -> None:
        """
        Calculates Discount and Delivery Cost for every package
        :return: None
        """
        for package in self.packages:
            package.calculate_delivery_cost(self.base_delivery_cost, self.weight_multiplier, self.distance_multiplier)
            package.calculate_discount()
            package.calculate_total_delivery_cost()
