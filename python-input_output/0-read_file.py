#!/usr/bin/python3
"""comment"""


def read_file(filename=""):
    """comment"""

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
