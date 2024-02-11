#!/usr/bin/python3
"""comment"""


import json


def save_to_json_file(my_obj, filename):
    """comment"""

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
