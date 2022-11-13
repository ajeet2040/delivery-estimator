"""This module will be responsible for organising packages into shipments on available vehicles
based on fixed delivery criteria.
"""
class DeliveryTimeCalculator:
    """
    Responsible for organising packages into shipments on available vehicles
    based on fixed delivery criteria.
    """

    def __init__(self, no_of_vehicles: int) -> None:
        """
        Initialises Estimator instance
        :param no_of_vehicles: no of vehicles available
        """
        self.no_of_vehicles = no_of_vehicles
        self.vehicles = []
        self.packages = []

    def set_vehicles(self, vehicles: list) -> None:
        """
        Adds vehicles to be used for delivery
        :param vehicles: list of vehicles objects
        :return: None
        """
        self.vehicles = vehicles

    def set_packages(self, packages: list) -> None:
        """
        Adds packages.
        :param packages: list of packages objects
        :return: None
        """
        self.packages = packages

    def select_shipment_per_criteria(self, packages, vehicle):
        pass

    def calculate_time_for_packages(self) -> None:
        pass
