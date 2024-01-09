#!/usr/bin/python3

"""
Defines a JSON file-writing function.

"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Args:
        my_obj (object): The Python object.
        filename (str): The name of the file.
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
