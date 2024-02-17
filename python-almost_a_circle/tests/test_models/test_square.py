#!/usr/bin/python3
"""comment"""


import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle

class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_Square_creation(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 3)

    def test_square_string(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_negative_numbers(self):
        with self.assertRaises(ValueError):
            s1 = Square(-1)
        with self.assertRaises(ValueError):
            s2 = Square(1, -2)
        with self.assertRaises(ValueError):
            s3 = Square(1, 2, -3)

    def test_square_zero_value(self):
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def test_square_area_method_exists(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_str_method_exist(self):
        s1 = Square(1, 2, 3)
        self.assertEqual(s1.__str__(), '[Square] (1) 2/3 - 1')

    def test_display_method_square(self):
        size = 2
        square_print = None
        self.assertEqual(Square(size).display(), square_print)

if __name__ == '__main__':
    unittest.main()
