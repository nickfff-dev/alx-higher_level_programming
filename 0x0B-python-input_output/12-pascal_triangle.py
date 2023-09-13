#!/usr/bin/python3
"""
module defines a function that returns the Pascal’s triangle of n

"""


def pascal_triangle(n):
    """
    a function that returns the Pascal’s triangle of n.

    Args:
        n(int): number of rows in rectangle

    Returns:
        list: a list of lists
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row += [sum(pair) for pair in zip(last_row, last_row[1:])]
        row.append(1)
        triangle.append(row)
    return triangle
