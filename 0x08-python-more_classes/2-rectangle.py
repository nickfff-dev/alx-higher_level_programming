#!/usr/bin/python3
""" Represents a Rectangle. """


class Rectangle:
    """ Represents a Rectangle. """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle instance.

        Args:
            width (int, optional): Width of the rectangle.
            height (int, optional): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets the width of this Rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of this Rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ Gets the height of this Rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of this Rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of this Rectangle.

        Returns:
            The area of this Rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of this Rectangle.

        Returns:
            The perimeter of this Rectangle or 0 if width or height is 0.
        """
        # check if width or height is 0
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
