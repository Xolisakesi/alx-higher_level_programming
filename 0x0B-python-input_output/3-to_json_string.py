#!/usr/bin/python3
"""Module for to_json_string function."""


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: Object to be converted to JSON.

    Returns:
        str: JSON representation of the input object.
    """
    import json
    return json.dumps(my_obj)
