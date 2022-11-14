from copy import deepcopy
from delivery_cost_estimator import DeliveryCostEstimator
from utils import create_objects, read_json_file, get_user_input
from config import OFFERS_JSON_PATH, MAX_PACKAGES_LIMIT
from models.package import Package
from models.offer import Offer


def run() -> None:
    """Run Script for Delivery Cost Calculation"""

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
        print(packages, "packages")

        # Calculate Cost of packages
        delivery_cost_estimator = DeliveryCostEstimator(base_delivery_cost=base_delivery_cost,
                                                        no_of_packages=no_of_packages)
        delivery_cost_estimator.set_offers(create_objects(offers, Offer))
        delivery_cost_estimator.set_packages(create_objects(packages, Package))
        delivery_cost_estimator.assign_offer_package()
        delivery_cost_estimator.calculate_delivery_cost()

        # Print out package info as requested
        for package in delivery_cost_estimator.packages:
            print(f"{package.id} {package.discount_amt} {package.total_delivery_cost}")
    except FileNotFoundError:
        print("File not found. Exiting!")
    except Exception as err:
        print(f"Internal error occurred: {err}")


if __name__ == "__main__":
    run()
