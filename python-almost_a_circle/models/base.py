#!/usr/bin/python3

"""Module for base class for some shapes"""

import json


class Base:
    """base class for some shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation of l_d"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes JSON string representation of l_o to file"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_str = cls.to_json_string(list_objs)
        with open(filename, 'w') as f:
            f.write(json_str)
