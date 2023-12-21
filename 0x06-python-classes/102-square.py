#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Defines a square with size attribute."""

    def __init__(self, size=0):
        """
        Initializes the square with optional size.
        
        Args:
        size (float or int, optional): The size of the square (default is 0).
        
        Raises:
        TypeError: If size is not a number.
        ValueError: If size is negative.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size with type and value validation.
        
        Args:
        value (float or int): The size to be set.
        
        Raises:
        TypeError: If value is not a number.
        ValueError: If value is negative.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Defines the equality operator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the inequality operator."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines the less than operator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the less than or equal to operator."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines the greater than operator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the greater than or equal to operator."""
        return self.area() >= other.area()
