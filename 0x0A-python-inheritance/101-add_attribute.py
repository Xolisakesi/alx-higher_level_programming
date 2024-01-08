#!usr/bin/python3
"""
This module provides functionality for adding attributes to objects.
"""

def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    :param obj: The object to which the attribute will be added.
    :param attribute: The name of the attribute.
    :param value: The value of the attribute.
    :raise TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[attribute] = value
