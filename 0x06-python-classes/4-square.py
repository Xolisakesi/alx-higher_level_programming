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

        size:
            Property with getter and setter methods for accessing and modifying the size.

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
        self.__size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size with type and value validation.
        Raises a TypeError or ValueError for invalid input.

        Args:
            value (int): The new size value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
