#!/usr/bin/python3

"""
Function to multiply two matrices using NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy

    Parameters:
    m_a: list of lists
    m_b: list of lists

    Returns:
    list of lists: The product of the matrix multiplication

    Raises:
    TypeError: If m_a or m_b is not a list, or if m_a or
    m_b is not a list of lists, or if one element of those list of
    lists is
    not an integer or a float, or if m_a or m_b is not a rectangle
    (all ‘rows’
    should be of the same size)
    ValueError: If m_a or m_b is empty (it means: = [] or = [[]]),
    or if m_a and
    m_b can’t be multiplied
    """
    for name, matrix in [("m_a", m_a), ("m_b", m_b)]:
        if not isinstance(matrix, list):
            raise TypeError(f"{name} must be a list")
        if not matrix or not all(isinstance(row, list)
                                 for row in matrix):
            raise TypeError(f"{name} must be a list of lists")
        if not all(matrix):
            raise ValueError(f"{name} can't be empty")
        if not all(isinstance(el, (int, float)) for row in matrix
                   for el in row):
            raise TypeError(f"{name} should contain only integers \
                            or floats")
        if not len(set(len(row) for row in matrix)) == 1:
            raise TypeError(f"each row of {name} must should be of \
                            the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b).tolist()
