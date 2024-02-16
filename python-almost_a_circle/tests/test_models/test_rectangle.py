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

    def test_rectangle_string_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_string_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_string_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_five_arguments(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

if __name__ == '__main__':
    unittest.main()
