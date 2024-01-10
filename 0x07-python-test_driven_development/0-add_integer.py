#!/usr/bin/python3
"""
Defines a function add_integer that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Parameters:
        - a: The first integer.
        - b: The second integer (default is 98).

    Raises:
        - TypeError: If a or b is not an integer or float.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))

    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)

    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
