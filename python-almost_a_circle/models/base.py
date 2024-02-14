#!/usr/bin/python3
"""comment"""


import json


class Base:
    """comment"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """comment"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def __repr__(self):
        return str(self.to_json_string())

    @classmethod
    def save_to_file(cls, list_objs):
        """comment"""
        if list_objs is None:
            file.write = "[]"
        filename = str(cls.__name__) + ".json"
        json_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(json_list)
        with open(filename, "w") as file:
            file.write(json_str)