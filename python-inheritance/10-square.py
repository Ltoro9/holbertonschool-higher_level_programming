#!/usr/bin/python3
"""comment"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """comment"""
    def __init__(self, size):
        BaseGeometry().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
