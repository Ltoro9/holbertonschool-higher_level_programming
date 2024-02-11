#!/usr/bin/python3
"""comment"""


def write_file(filename="", text=""):
    """comment"""

    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
