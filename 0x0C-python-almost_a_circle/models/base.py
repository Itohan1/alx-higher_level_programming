#!/usr/bin/python3
"""Write the first class Base"""
import json
import csv
import turtle


class Base:
    """private class attribute
        Arg: id
        Return: str"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Update the class Base by adding the static method"""

        if list_dictionaries is None or list_dictionaries == []:
            return ([])
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Update the class Base by adding the class method"""

        Fname = cls.__name__ + ".json"
        with open(Fname, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                json.string = cls.to_json_string([
                    ob.to_dictionary() for ob in list_objs])
                file.write(json.string)

    @staticmethod
    def from_json_string(json_string):
        """Update the class Base by adding the static method"""

        if json_string is None or len(json_string) == "[]":
            return ([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Update the class Base by adding the class method"""

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            elif cls.__name__ == "Square":
                new = cls(1)
            else:
                raise ValueError("unsupported class")
            new.update(**dictionary)
            return (new)

    @classmethod
    def load_from_file(cls):
        """Update the class Base by adding the class method"""

        Fname = str(cls.__name__) + ".json"
        try:
            with open(Fname, "r") as json_File:
                list_dicts = Base.from_json_string(json_File.read())
                return ([cls.create(**a) for a in list_dicts])
        except IOError:
            return ([])
