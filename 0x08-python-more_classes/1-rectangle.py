#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Private instance attribute: width"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Private instance attribute: height"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TYpeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
