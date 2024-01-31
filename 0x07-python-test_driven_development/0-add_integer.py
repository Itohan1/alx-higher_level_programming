#!/usr/bin/python3
"""Write a function that adds 2 integers"""


def add_integer(a, b=98):
    """a and b must be integers or floats"""

    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    if a == float('NaN'):
        raise TypeError("a must be an integer")
    if b == float('NaN'):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
