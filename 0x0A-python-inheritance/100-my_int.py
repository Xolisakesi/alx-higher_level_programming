#!/usr/bin/python3
"""Module that defines a Square."""


class Square(Rectangle):
    """Class that represents a square."""


    def __init__(self, size):
        """Instantiation method with size."""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
