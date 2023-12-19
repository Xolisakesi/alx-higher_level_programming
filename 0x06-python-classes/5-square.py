#!/usr/bin/python3
class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initializes the square with an optional size.
        Raises a TypeError or ValueError for invalid input.
        """
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size with type and value validation.
        Raises a TypeError or ValueError for invalid input.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
