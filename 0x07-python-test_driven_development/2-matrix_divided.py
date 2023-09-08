#!/usr/bin/python3
"""
This module defines a matrix division function
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix by a given number

    Args:
        matrix: A list of lists of integers or floats
        div: Number to be used for the division
    Raises:
        TypeError: If the matrix contains none numbers
        TypeError: If the matrix contains lists of different length
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix which represents the result of the division operations
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
                         of integers/floats")
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) \
                            of integers/floats")

    # Check if all rows in the matrix have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division
    return [[round(num / div, 2) for num in row] for row in matrix]
