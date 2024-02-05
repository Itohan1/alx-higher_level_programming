#!/usr/bin/python3
"""a class BaseGeometry (based on 6-base_geometry.py)"""

class BaseGeometry:
    """ a class BaseGeometry (based on 6-base_geometry.py)"""

    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Another public instance method"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
