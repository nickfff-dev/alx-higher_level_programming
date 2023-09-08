#!/usr/bin/python3
"""

This module contain a function that prints a square

"""


def print_square(size):
    """
    Print a square with the character '#'.

    Args:
        size (int): The length of the square.

    Raises:
        TypeError: If size is not an integer or a float.
        ValueError: If size is less than 0.
        TypeError: If size is a float and less than 0.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
