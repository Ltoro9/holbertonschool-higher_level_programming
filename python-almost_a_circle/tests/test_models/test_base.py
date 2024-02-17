#!/usr/bin/python3
"""comment"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """comment"""
    def test_init(self):
        b  = Base(1)
        self.assertEqual(b.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(13)
        self.assertEqual(b2.id, 13)
        b3 = Base(-1)
        self.assertEqual(b3.id, -1)
        b4 = Base(0)
        self.assertEqual(b4.id, 0)
        b5 = Base()
        self.assertEqual(b5.id, 2)
        b6 = Base(None)
        self.assertEqual(b6.id, 3)
        b7 = Base(5)
        b7.id = 10
        self.assertEqual(b7.id, 10)
        b8 = Base("Hola")
        self.assertEqual(b8.id, 'Hola')

    def test_to_json_string(self):
        r = Rectangle(10, 7, 2, 8)
        r_dict = r.to_dictionary()
        json_dictionary = Rectangle.to_json_string([r_dict])
        self.assertEqual(json_dictionary, '[{"id": 14, "width": 10, "height": 7, "x": 2, "y": 8}]')
        s = Square(5, 1, 2)
        s_dict = s.to_dictionary()
        json_dictionary = Square.to_json_string([s_dict])
        self.assertEqual(json_dictionary, '[{"id": 15, "size": 5, "x": 1, "y": 2}]')

    def test_rectangle_from_json_string(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_rectangle_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(id(r1), id(r2))
        self.assertEqual({'id': 4, 'width': 3, 'height': 5, 'x': 1, 'y': 0}, {'id': 4, 'width': 3, 'height': 5, 'x': 1, 'y': 0})

    def test_rectangle_save_and_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertIsInstance(list_rectangles_output[0], Rectangle)
        self.assertIsInstance(list_rectangles_output[1], Rectangle)

    def test_square_save_and_load_from_file(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(len(list_squares_output), 2)
        self.assertIsInstance(list_squares_output[0], Square)
        self.assertIsInstance(list_squares_output[1], Square)

if __name__ == '__main__':
    unittest.main()
