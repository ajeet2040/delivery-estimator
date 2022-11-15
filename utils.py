"""This module is to define any utility methods needed by application"""
import json
import math
import builtins
from typing import Any
import sys


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


def create_objects(objects_data: list, object_class: object) -> list:
    """
    Create packages based on data provided.
    :param object_class: Class for which object is to created
    :param objects_data: list of dict objects along with details
    :return: objects created
    :raises TypeError in case Package object properties are invalid
    """
    objects = []
    for idx, data in enumerate(objects_data):
        try:
            objects.append(object_class(**data))
        except TypeError as err:
            print(f"Make sure all properties of {object_class.__name__}  are provided correctly.")
            raise err
    return objects


def round_down_2_digits(num: float) -> float:
    """
    Rounds down to 2 decimal digits if more are present.
    :param num: number to be rounded
    :return: rounded number
    """
    return math.floor((num * 100))/100.0


def input_check_and_conversion(input_data: list, expected_inputs: list) -> Any:
    """
    Validates input and converts to the relevant type.
    :param input_data: data entered by user
    :param expected_inputs: list of tuples with 'Name', 'type to be converted', 'Label of type',
    'greater than value', 'max limit'
    :return: Converted data if validation success else false
    """
    if not len(input_data) == len(expected_inputs):
        print("Please enter correct number of data as requested!")
        return False
    for idx, expected_data in enumerate(expected_inputs):
        # Check for data type
        try:
            conversion = getattr(builtins, expected_data[1])
            input_data[idx] = conversion(input_data[idx])
        except ValueError:
            print(f"{expected_data[0]} should be {expected_data[2]}")
            return False
        # Check for min value
        if expected_data[3] is not False:
            if not input_data[idx] > expected_data[3]:
                print(f"{expected_data[0]} should be more than {expected_data[3]}")
                return False
        # Check for max value
        if expected_data[4] is not False:
            if input_data[idx] > expected_data[4]:
                print(f"{expected_data[0]} should not be more than {expected_data[4]}")
                return False
    return input_data


def get_user_input(expected_inputs: list) -> list:
    """
    Prompts, fetches user input and validates and converts them.
    :param expected_inputs: list of tuples with 'Name', 'type to be converted', 'Label of type',
    :return: Converted data
    """
    message = f"Enter {', '.join(x[0] for x in expected_inputs)} separated by spaces. (type 'EXIT' to close app.)"
    print(message)
    while True:
        input_data = list(map(lambda x: x.strip(), input().split()))
        if input_data == ['EXIT']:
            sys.exit(0)
        input_data = input_check_and_conversion(input_data, expected_inputs)
        if input_data:
            break
    return input_data
