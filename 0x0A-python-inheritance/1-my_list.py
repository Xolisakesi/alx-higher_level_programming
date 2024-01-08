#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """A custom class inheriting from the built-in list class."""

    def print_sorted(self):
        """Prints the sorted list without modifying the original list."""
        sorted_list = sorted(self)
        print(sorted_list)

