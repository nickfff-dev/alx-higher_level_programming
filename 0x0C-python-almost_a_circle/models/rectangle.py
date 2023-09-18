#!/usr/bin/python3
"""this module defines a class Rectangle
    that inherits from the class Base.
"""
from models.base import Base


class Rectangle(Base):
    """ defines class Rectangle inherited from base.

        Attributes:
            width(int): width of the rectangle.
            height(int): the height of the rectangle.
            x(int): the x coordinate of the rectangle.
            y(int): the y coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ rectangle instance constructor
            Args:
                width(int): width of the rectangle.
                height(int): the height of the rectangle.
                x(int): the x coordinate of the rectangle.
                y(int): the y coordinate of the rectangle.
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ the accessor/getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """ the setter/mutator for the width attribute"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ the accessor/getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """ the setter/mutator for the height attribute"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ the accessor/getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """ the setter/mutator for the x attribute"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ the accessor/getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """ the setter/mutator for the y attribute"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ method for calculating area"""
        return self.__width * self.__height

    def display(self):
        """ method that draws the rectangle"""
        # Print new lines for 'y'
        print('\n'*self.__y, end='')
        # Iterating through the height of the rectangle
        for row in range(self.__height):
            # Print spaces for 'x'
            print(' '*self.__x, end='')
            # Print the rectangle
            for col in range(self.__width):
                print('#', end='')

            # Start a new line after each row
            print()

    def __str__(self):
        """ str representation of class"""
        return "[Rectangle] " + "(" + str(self.id) + ") " + str(self.__x) + \
            "/" + str(self.__y) + " - " + \
            str(self.__width) + "/" + str(self.__height)

    def update(self, *args):
        """Update rectangle attributes"""
        attrs = ["id", "width", "height", "x", "y"]
        if len(args) > 0:
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)
