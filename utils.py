"""This module is to define any utility methods needed by application"""
import json
from models.vehicle import Vehicle
from models.offer import Offer
from models.package import Package


def read_json_file(file_path: str) -> list:
    """
    Reads and return JSOM data from file system.
    :param file_path: path of json file
    :return: json data
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError as err:
        print(f"File `{file_path}`not found. Error is: {err}")
        raise err


def create_packages(packages_data: list) -> list:
    """
    Create packages based on data provided.
    :param packages_data: list of package along with details
    :return: package objects
    :raises TypeError in case Package object properties are invalid
    """
    packages = []
    for idx, package in enumerate(packages_data):
        try:
            packages.append(Package(**package))
        except TypeError as err:
            print(f"Make sure all properties of package are provided correctly.")
            raise err
    return packages


def create_offers(offers_data: list) -> list:
    """
    Sets Available offers.
    :param offers_data: list of offer along with criteria for discount
    :return: offer objects
    :raises TypeError in case offer object properties are invalid
    """
    offers = []
    for idx, offer in enumerate(offers_data):
        try:
            offers.append(Offer(**offer))
        except TypeError as err:
            print(f"Make sure all properties of offer are setup in json file.")
            raise err
    return offers


def create_vehicles(vehicles_data: list) -> list:
    """
    Creates Available vehicles.
    :param vehicles_data: list of vehicles along with their properties
    :return: offer objects
    :raises TypeError in case offer object properties are invalid
    """
    vehicles = []
    for idx, vehicle in enumerate(vehicles_data):
        try:
            vehicles.append(Vehicle(**vehicle))
        except TypeError as err:
            print(f"Make sure all properties of offer are setup in json file.")
            raise err
    return vehicles
