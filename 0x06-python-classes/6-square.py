#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

    @property
    def size(self):

        self.__size = size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):

        self.position = position

    @position.setter
    def position(self, value):



