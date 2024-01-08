#!/usr/bin/python3
"""Module that defines the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class; otherwise False.

    :param obj: The object to check.
    :param a_class: The specified class to check against.
    :return: True if the object is an instance of the specified class or
             any of its subclasses; otherwise False.
    """
    return isinstance(obj, a_class)

