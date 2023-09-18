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
        self.__width = width

    @property
    def height(self):
        """ the accessor/getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """ the setter/mutator for the height attribute"""
        self.__height = height

    @property
    def x(self):
        """ the accessor/getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """ the setter/mutator for the x attribute"""
        self.__x = x

    @property
    def y(self):
        """ the accessor/getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """ the setter/mutator for the y attribute"""
        self.__y = y
