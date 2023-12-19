#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """
    Defines a basic class for a square.

    Attributes:
    - size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square. Default is 0.
        """
        self.__size = size
