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
            raise TypeError("width must be an integer")

        if (value < 0 or value == 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Private instance attributes with its own public getter and setter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height  must be an integer")

        if (value < 0 or value == 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Private instance attributes with its own public getter and setter"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Private instance attributes with its own public getter and setter"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Update the class Rectangle by adding the public method"""
        return (self.__width * self.__height)

    def display(self):
        """Update the class Rectangle by adding the public method"""
        for i in range(self.y):
            print('')
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Update the class Rectangle by overriding the __str__"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x, self.__y,
                                                        self.__width,
                                                        self.__height)
                )

    def update(self, *args, **kwargs):
        """Update the class Rectangle by updating the public method"""
        if args and len(args) != 0:
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Update the class Rectangle by adding the public method"""

        return ({
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
                })
