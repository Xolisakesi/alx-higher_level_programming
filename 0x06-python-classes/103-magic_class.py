#!/usr/bin/python3
import math

class MagicClass:
    """Defines a class that replicates the given bytecode."""

    def __init__(self, radius=0):
        """Initializes the MagicClass with an optional radius."""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Calculates the area of the MagicClass instance."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the MagicClass instance."""
        return 2 * math.pi * self.__radius
