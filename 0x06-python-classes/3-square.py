#!/usr/bin/python3
class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initializes the square with an optional size.
        Raises a TypeError or ValueError for invalid input.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
