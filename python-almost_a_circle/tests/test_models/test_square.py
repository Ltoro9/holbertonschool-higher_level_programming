#!/usr/bin/python3
"""comment"""


import unittest
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_Square_creation(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_square_string(self):
        with self.assertRaises(TypeError):
            Square("5")

    def test_square_negative_numbers(self):
        with self.assertRaises(ValueError):
            s1 = Square(-5)

    def test_square_area_method_exists(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_str_method_exist(self):
        s1 = Square(1, 2, 3)
        self.assertEqual(s1.__str__(), '[Square] (1) 2/3 - 1')

if __name__ == '__main__':
    unittest.main()
