#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    Represents a rebellious integer.
    """

    def __eq__(self, other):
        """
        Inverts the equality operator.

        Parameters:
            - other: The other operand in the equality comparison.

        Returns:
            bool: The result of the inverted equality check.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator.

        Parameters:
            - other: The other operand in the inequality comparison.

        Returns:
            bool: The result of the inverted inequality check.
        """
        return super().__eq__(other)
