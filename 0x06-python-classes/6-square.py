#!/usr/bin/python3

"""defines a square by: (based on 5-square.py)"""

class Square:
    """defines a square by: (based on 5-square.py)"""

    def __init__(self, size=0, position=(0, 0)):
        """defines a square by: (based on 5-square.py)"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """defines a square by: (based on 5-square.py)"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """defines a square by: (based on 5-square.py)"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """defines a square by: (based on 5-square.py)"""

        return (self.__position)

    @position.setter
    def position(self, value):
        """defines a square by: (based on 5-square.py)"""

        if (not isinstance(value, tuple)) or len(value) != 2 or not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """defines a square by: (based on 5-square.py)"""

        return(self.__size * self.__size)

    def my_print(self):
        """defines a square by: (based on 5-square.py)"""

        if self.__size == 0:
            print("")
            return

        [print("") for a in range(self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for b in range(self.__position[0])]
            [print("#", end="") for c in range(self.__size)]
            print("")
