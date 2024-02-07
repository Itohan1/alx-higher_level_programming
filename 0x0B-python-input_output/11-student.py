#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return ({a: getattr(self, a) for k in attrs if hasattr(self, a)})
        return (self.__dict__)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
