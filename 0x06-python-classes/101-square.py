#!/usr/bin/python3
class Square:
    """Defines a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with optional size and position.
        Raises TypeError or ValueError for invalid input.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size with type and value validation.
        Raises TypeError or ValueError for invalid input.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position with type and value validation.
        Raises TypeError or ValueError for invalid input.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # and position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square."""
        result = []
        if self.__size == 0:
            return ''
        for _ in range(self.__position[1]):
            result.append('')
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        return '\n'.join(result)
