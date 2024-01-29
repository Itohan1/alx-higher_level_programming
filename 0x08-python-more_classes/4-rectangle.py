#!/usr/bin/python3
"""Area and Perimeter"""


class Rectangle:
    """Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)"""

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""

        return(self.__width * self.__height)

    def parameter(self):
        """returns the rectangle perimeter"""

        if self.__width == 0 or self.__height == 0:
            return (0)

        return (2 * (self.__width * self.__height))

    def __str__(self):
        """print the rectangle with the character #"""

        if self.__width == 0 or self.__height == 0:
            return ("")
        rec = []

        for i in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if i != self.__height:
                rec.append('\n')
        return("".join(rec))

    def __repr__(self):
        """ return a string representation of the rectangle to be able to recreate a new instance by using eval()"""
        return f"Rectangle({self.__width}, {self.__height})"