#!/usr/bin/python3
"""
This module defines a Square class. The Square class
has private instance attributes size and position.
It also includes type and value checks for the size
and position attributes during instantiation.
The class also includes methods for calculating the
area of the Square and for printing the Square.
"""

class Square:
    """
    This class defines a square with private instance
    attributes size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new Square. Defaults to 0.
            position (tuple): The position of the new Square.
            Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position
            is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Get the position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position.

        Args:
            value (tuple): The position of the Square.

        Raises:
            TypeError: If position is not a tuple of
            2 positive integers.
        """
        if not (isinstance(value, tuple) or len(value) != 2 or 
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a \
                            tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Return the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the "#" character.
        If the size is 0, prints an empty line.
        Uses the position attribute to determine the square's position.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + "#" * self.__size
                            for _ in range(self.__size)))
