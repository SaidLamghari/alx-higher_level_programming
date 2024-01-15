#!/usr/bin/python3
"""
Module for Rectangle for some tests.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_rectangle_area(self):
        """
        Test the calculation of the area of a Rectangle.
        """
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_rectangle_str(self):
        """
        Test the string representation of a Rectangle.
        """
        rectangle = Rectangle(4, 8, 2, 2, 1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 2/2 - 4/8")

    def test_rectangle_update(self):
        """
        Test updating the attributes of a Rectangle using the update() method.
        """
        rectangle = Rectangle(5, 5, 1, 1, 1)
        rectangle.update(2, 2, 2, 2, 2)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 2)
        self.assertEqual(rectangle.id, 2)

    def test_rectangle_update_kwargs(self):
        """
        Test updating the attributes of a Rectangle using
        keyword arguments in the update() method.
        """
        rectangle = Rectangle(3, 3, 1, 1, 1)
        rectangle.update(width=5, height=5, x=2, y=2)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 2)

    def test_rectangle_to_dictionary(self):
        """
        Test converting a Rectangle instance to a dictionary representation.
        """
        rectangle = Rectangle(4, 4, 2, 2, 1)
        rectangle_dict = rectangle.to_dictionary()
        expected_dict = {'id': 1, 'width': 4, 'height': 4, 'x': 2, 'y': 2}
        self.assertEqual(rectangle_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
