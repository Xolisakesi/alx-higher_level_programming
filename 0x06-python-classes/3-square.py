#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """
    Defines a square with a private size attribute.

    Attributes:
        __size (int): Private attribute representing the size of the square.

    Methods:
        __init__(self, size=0):
            Initializes the square with an optional size.
            Raises a TypeError or ValueError for invalid input.

        area(self):
            Returns the current square area.
    """

    def __init__(self, size=0):
        """
        Initializes the square with an optional size.
        Raises a TypeError or ValueError for invalid input.

        Args:
            size (int): The size of the square (default is 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
