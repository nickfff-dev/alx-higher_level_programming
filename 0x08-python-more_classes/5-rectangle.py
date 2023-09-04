#!/usr/bin/python3
"""
A class representing a rectangle.
"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def __del__(self):
        """
        Destructor for the Rectangle class.
        """
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return ("#" * self.width + "\n" *
                    (self.height - 1) + "#" * self.width)

    def __repr__(self):
        """
        Return a string representation of the rectangle for debugging.

        Returns:
            str: The string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.width, self.height)
