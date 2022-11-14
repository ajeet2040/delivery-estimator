"""This module will be responsible for organising packages into shipments on available vehicles
based on fixed delivery criteria.
"""
from copy import copy, deepcopy
from itertools import combinations
from utils import round_down_2_digits


class DeliveryShipmentsAssigner:
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
        self.pending_packages = []     # keeps track of packages pending to be delivered
        self.current_shipment = {}     # Selected shipment for next delivery

        self.all_shipments_assigned = False  #
        self.shipments = []

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

    def create_shipment_per_criteria(self, vehicle: object) -> dict:
        """
        Algorithm ot create shipments based on certain fixed delivery criteria
        :param packages:
        :param vehicle:
        :return: shipment dict with packages, total weight, round time, vehicle used
        """
        self.current_shipment = {}
        selected_shipment_info = {
            "packages": [],
            "total_weight": 0,
            "total_round_time": 0,
            "vehicle": vehicle
        }
        for group_length in range(len(self.pending_packages), 0, -1):
            selected_packages_group = []
            # Create packages group for maximum length
            packages_group = combinations(self.pending_packages, group_length)
            # Select packages on criteria: total shipment weight <= max_carriable_weight
            for group in packages_group:
                shipment_info = deepcopy(selected_shipment_info)
                shipment_info["packages"] = list(group)
                shipment_info["total_weight"] = sum(pkg.weight for pkg in group)
                if shipment_info["total_weight"] <= vehicle.max_carriable_weight:
                    selected_packages_group.append(shipment_info)
            # Select packages on criteria: package group with maximum valid weight
            if len(selected_packages_group) > 1:
                valid_packages_max_weight = (max(selected_packages_group,
                                                 key=lambda item: item["total_weight"]))["total_weight"]
                selected_packages_group = [x for x in selected_packages_group
                                           if x["total_weight"] == valid_packages_max_weight]
            # Calculate time for each package and shipment as well
            selected_packages_group_time = []
            for package_group in selected_packages_group:
                group_max_time = 0
                for package in package_group["packages"]:
                    package.delivery_time = round_down_2_digits(package.distance/vehicle.max_speed)
                    group_max_time = package.delivery_time if package.delivery_time > group_max_time else group_max_time
                package_group["total_round_time"] = round_down_2_digits(group_max_time * 2)
                selected_packages_group_time.append(package_group)
            # Select packages on criteria: package group with minimum time required to deliver
            # NOTE: In case of multiple groups with same time, the first one available will be selected
            if len(selected_packages_group_time) > 1:
                selected_packages_group = min(selected_packages_group_time, key=lambda item: item["total_round_time"])
            if selected_packages_group:
                self.current_shipment = selected_packages_group[0]
                break
        print("No valid shipment found as per delivery criteria")

    def create_shipments_for_delivery(self) -> None:
        """
        Main Algorithm for creating shipments based on number of vehicles available.
        :return: None
        """
        self.pending_packages = copy(self.packages)
        vehicles_available = [{"vehicle": v, "next_available_time": 0} for v in self.vehicles]
        while len(self.pending_packages) > 0:
            selected_vehicle = (min(vehicles_available, key=lambda item: item["next_available_time"]))
            self.create_shipment_per_criteria(selected_vehicle["vehicle"])
            if not self.current_shipment:
                print("Delivery failed as shipment could not be formed as per delivery criteria!")
                break
            # Update packages delivery time as per vehicle available time
            for package in self.current_shipment["packages"]:
                package.delivery_time += selected_vehicle["next_available_time"]
                package.delivery_time = round_down_2_digits(package.delivery_time)
            self.shipments.append(self.current_shipment)
            self.pending_packages = list(filter(lambda item: item not in self.current_shipment["packages"],
                                                 self.pending_packages))
            # update vehicle next available time based on total round time of shipment
            selected_vehicle["next_available_time"] += self.current_shipment["total_round_time"]
        self.all_shipments_assigned = True
