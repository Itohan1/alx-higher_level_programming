#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """a class Student that defines a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return{b: getattr(self, b) for b in attrs if hasattr(self, b)}
        return self.__dict__
