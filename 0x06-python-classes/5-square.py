#!/usr/bin/python3
"""
This module defines a Square class for representing squares.
"""


class Square:
    """
    A class that defines a square.

    Args:
        size (int): the size of the square

    Attributes:
        area(): Returns the area of the square.
        my_print(): Prints the square using the "#" character.
    """

    def __init__(self, size=0):
        """
        Constructs a new Square instance.

        Args:
            size (int): optional The size of the square (default is 0)
            """
        self.size = size

    @property
    def size(self):
        """
        The size property getter.

        Returns:
                int The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The size property setter.

        Args:
            value (int): The new size of the square

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the current square area.

        Returns:
            int The area of the square
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
