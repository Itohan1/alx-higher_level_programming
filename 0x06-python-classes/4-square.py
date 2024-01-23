#!/usr/bin/python3
"""defines a square by: (based on 3-square.py)"""


class Square:
    """defines a square by: (based on 3-square.py)"""

    def __init__(self, size=0):
        """defines a square by: (based on 3-square.py)"""

        self.__size = size

    @property
    def size(self):
        """finds the current size of the square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """defines a square by: (based on 3-square.py)"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""

        return (self.__size * self.__size)
