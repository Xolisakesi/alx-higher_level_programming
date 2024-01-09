#!/usr/bin/python3
"""Module for from_json_string function."""


def from_json_string(my_str):
    """
    Return the object represented by a JSON string.

    Args:
        my_str (str): JSON string to be converted to an object.

    Returns:
        object: Python data structure represented by the JSON string.
    """
    import json
    return json.loads(my_str)
