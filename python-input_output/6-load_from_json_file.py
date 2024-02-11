#!/usr/bin/python3
"""comment"""


import json


def load_from_json_file(filename):
    """comment"""

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
