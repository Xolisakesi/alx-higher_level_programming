#!/usr/bin/python3
"""
Defines a function matrix_divided that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Parameters:
        - matrix (list of lists): The matrix to be divided.
        - div (number): The divisor.

    Raises:
        - TypeError: If the matrix is not a list .
        - TypeError: If each row of the matrix doesn't have the same size.
        - TypeError: If the divisor is not a number.
        - ZeroDivisionError: If the divisor is equal to zero.

    Returns:
        list of lists: The new matrix with elements divided by the divisor.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
