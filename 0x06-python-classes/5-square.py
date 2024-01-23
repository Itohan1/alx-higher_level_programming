#!/usr/bin/python3

"""defines a square by: (based on 3-square.py)"""

class Square:
    """defines a square by: (based on 3-square.py)"""

    def __init__(self, size=0):

        """defines a square by: (based on 3-square.py)"""

        self.__size = size

    @property
    def size(self):
        """defines a square by: (based on 3-square.py)"""

        self.__size = size

    @size.setter
    def size(self, value):
        """defines a square by: (based on 3-square.py)"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """defines a square by: (based on 3-square.py)"""

        return(self.__size * self.__size)

    def my_print(self):
        """defines a square by: (based on 3-square.py)"""

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
