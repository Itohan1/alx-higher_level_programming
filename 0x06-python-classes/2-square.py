#!/usr/bin/python3
"""defines a square by: (based on 1-square.py)"""


class Square:
    """defines a square by: (based on 1-square.py)"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
