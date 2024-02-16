#!/usr/bin/python3
"""comment"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_base_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_base_custom_id(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_rectangle_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Rectangle.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"x": 2, "y": 8, "id": 1, "width": 10, "height": 7}]')

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
        self.assertEqual(r1, r2)

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
