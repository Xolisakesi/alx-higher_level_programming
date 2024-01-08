#!/usr/bin/python3
"""Module that defines the is_same_class function."""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    :param obj: The object to check.
    :param a_class: The specified class to check against.
    :return: True if the object is an instance of the specified class;
             otherwise False.
    """
    return type(obj) is a_class

