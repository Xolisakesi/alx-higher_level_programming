#!/usr/bin/python3
"""Module that defines the lookup function."""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    :param obj: The object to inspect.
    :return: A list of attribute and method names of the object.
    """
    return dir(obj)

