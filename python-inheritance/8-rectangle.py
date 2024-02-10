#!/usr/bin/python3
"""comment"""


class BaseGeometry:
    """comment"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """comment"""
    def __init__(self, width, height):
        self.__height = height
        self.__width = width
        self.integer_validator("width", width)
        self.integer_validator("height",height)
