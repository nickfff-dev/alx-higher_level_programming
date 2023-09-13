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

    nested_arr = [[1 for x in range(i+1)] if i < 2 else [1, 1]
                  for i in range(n)]
    for i in range(2, n):
        for j in range(1, len(nested_arr[i])-1):
            nested_arr[i][j] = nested_arr[i-1][j-1] + nested_arr[i-1][j]
    return nested_arr
