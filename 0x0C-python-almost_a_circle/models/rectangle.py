#!/usr/bin/python3
import unittest
from models.base import Base
"""Write the class Rectangle that inherits from Base"""


class Rectangle(Base):
    """"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Private instance attributes with its own public getter and setter"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        if (value < 0):
            raise ValueError("value must be greater than 0")
        self.__width = value


    @property
    def height(self):
        """Private instance attributes with its own public getter and setter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        if (value < 0):
            raise ValueError("value must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """Private instance attributes with its own public getter and setter"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        if (value < 0):
            raise ValueError("value must be greater than 0 or equal to 0")
        self.__x = value

    @property
    def y(self):
        """Private instance attributes with its own public getter and setter"""
        return (self.__x)

    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        if (value < 0):
            raise ValueError("value must be greater than or equal to zero")
        self.__y = value
