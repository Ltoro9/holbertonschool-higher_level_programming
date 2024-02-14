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
            list_objs = []

        filename = f"{cls.__name__}.json"
        json_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(json_list)
        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        a_list = []
        if json_string is None:
            return a_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """comment"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """comment"""
        filename = f"{cls.__name__}.json"
        with open(filename, "r") as file:
            data = file.read()
            if not data:
                return []
            return [cls.from_json_string(obj) for obj in json.loads(data)]
