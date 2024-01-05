#!/usr/bin/python3

"""Defines a locked class."""

class LockedClass:
    """
    This class restricts the dynamic creation of new instance attributes
    except for 'first_name'.
    """

    __slots__ = ['first_name']
