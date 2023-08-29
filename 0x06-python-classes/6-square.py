#!/usr/bin/python3
"""
This module defines a Square class. The Square class
has a private instance attribute size.
It also includes type and value checks for the size
attribute during instantiation.
The class also includes methods for calculating the
area of the Square and for printing the Square.
"""


class Square:
    """
    This class defines a square with a private instance
    attribute size.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new Square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size.

        Args:
            value (int): The size of the Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the "#" character.
        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
