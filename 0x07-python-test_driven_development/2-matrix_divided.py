#!/usr/bin/python3
"""
Divides all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists of int/float): The original matrix.
        div (int/float): The number by which to divide all elements
        of the matrix.

    Raises:
        TypeError: If the matrix is not a list of lists of
        integers/floats.
        TypeError: If any row of the matrix has a different size.
        TypeError: If div is not a number (int/float).
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists of int/float: A new matrix with each value
        divided by div, rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or \
        not all(isinstance(row, list) for row in matrix) or not \
            all(isinstance(item, (int, float))
                for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
