"""This module is to define any utility methods needed by application"""
import json


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
