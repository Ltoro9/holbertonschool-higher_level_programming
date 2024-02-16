#!/usr/bin/python3
"""comment"""


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_rectangle_creation(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_string_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
            Rectangle(1, "2")

if __name__ == '__main__':
    unittest.main()
