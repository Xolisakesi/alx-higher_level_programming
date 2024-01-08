#!/usr/bin/python3
"""Module that defines the Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initialize a square with a given size."""
        super().__init__(size, size)
