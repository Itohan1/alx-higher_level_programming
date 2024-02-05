#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """return: [Rectangle] <width>/<height>"""

        dstring = "[" + str(self.__class__.__name__) + "] "
        dstring += str(self.__width) + "/" + str(self.__height)
        return (dstring)
