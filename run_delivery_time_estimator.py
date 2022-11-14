from copy import deepcopy
from delivery_cost_estimator import DeliveryCostEstimator
from delivery_shipments_assigner import DeliveryShipmentsAssigner
from utils import read_json_file, get_user_input, create_objects
from config import OFFERS_JSON_PATH, MAX_VEHICLES_LIMIT, MAX_PACKAGES_LIMIT
from models.package import Package
from models.offer import Offer
from models.vehicle import Vehicle


def run() -> None:
    """Run Script for Delivery Assignment, Cost and Time Calculation"""
    try:
        # Load offers data
        offers = read_json_file(OFFERS_JSON_PATH)

        # base_delivery_cost and no_of_packages
        input1_expected = [("Base Delivery Cost", 'float', "Number", False, False),
                           ("No of Packages", 'int', "Integer", 0, MAX_PACKAGES_LIMIT)]
        input1_data = get_user_input(input1_expected)
        base_delivery_cost, no_of_packages = input1_data

        # packages details
        input2_expected = [("Package Id", 'str', "Text", False, False),
                           ("Package Weight", 'float', "Number", 0, False),
                           ("Distance", 'float', "Number", 0, False),
                           ("offer Code", 'str', "Text", False, False)
                           ]
        packages = []
        sample_package = {
            "id": "",
            "weight": "",
            "distance": "",
            "offer_code": ""
        }
        for x in range(0, no_of_packages):
            input2_data = get_user_input(input2_expected)
            pkg_data = deepcopy(sample_package)
            pkg_data["id"], pkg_data["weight"], pkg_data["distance"], pkg_data["offer_code"] = input2_data
            packages.append(pkg_data)

        # no_of_vehicles and max_speed and max_carriable_weight
        input3_expected = [("No of Vehicles", 'int', "Integer", 0, MAX_VEHICLES_LIMIT),
                           ("Max speed", 'float', "Number", 0, False),
                           ("Max Carriable Weight", 'float', "Number", 0, False)]
        input3_data = get_user_input(input3_expected)
        no_of_vehicles, max_speed, max_carriable_weight = input3_data

        # Calculate Cost of packages
        delivery_cost_estimator = DeliveryCostEstimator(base_delivery_cost=base_delivery_cost,
                                                        no_of_packages=no_of_packages)
        delivery_cost_estimator.set_offers(create_objects(offers, Offer))
        delivery_cost_estimator.set_packages(create_objects(packages, Package))
        delivery_cost_estimator.assign_offer_package()
        delivery_cost_estimator.calculate_delivery_cost()

        # Calculated Delivery Time
        vehicles_data = [{"id": f"V{i}", "max_speed": max_speed, "max_carriable_weight": max_carriable_weight}
                         for i in range(0, no_of_vehicles)]
        delivery_shipments_assigner = DeliveryShipmentsAssigner(no_of_vehicles=no_of_vehicles)
        delivery_shipments_assigner.set_packages(delivery_cost_estimator.packages)
        delivery_shipments_assigner.set_vehicles(create_objects(vehicles_data, Vehicle))
        delivery_shipments_assigner.create_shipments_for_delivery()

        if delivery_shipments_assigner.all_shipments_assigned is True:
            # Print out package info as requested
            for package in delivery_cost_estimator.packages:
                print(f"{package.id} {package.discount_amt} {package.total_delivery_cost}"
                      f" {package.delivery_time}")
    except FileNotFoundError:
        print("File not found. Exiting!")
    except Exception as err:
        print(f"Internal error occurred: {err}")


if __name__ == "__main__":
    run()
