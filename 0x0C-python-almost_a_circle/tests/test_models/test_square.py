#!/usr/bin/python3
"""
Module for Square unit tests.
"""
import unittest
from models.base import Base
from models.square import Square
import io


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_square_area(self):
        """
        Test the calculation of the area of a Square.
        """
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_square_str(self):
        """
        Test the string representation of a Square.
        """
        square = Square(4, 2, 2, 1)
        self.assertEqual(str(square), "[Square] (1) 2/2 - 4")

    def test_square_update(self):
        """
        Test updating the attributes of a Square using the update() method.
        """
        square = Square(5, 1, 1, 1)
        square.update(2, 2, 2, 2)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 2)

    def test_square_update_kwargs(self):
        """
        Test updating the attributes of a Square using
        keyword arguments in the update() method.
        """
        square = Square(3, 1, 1, 1)
        square.update(size=5, x=2, y=2)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)

    def test_square_to_dictionary(self):
        """
        Test converting a Square instance to a dictionary representation.
        """
        square = Square(4, 2, 2, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 4, 'x': 2, 'y': 2}
        self.assertEqual(square_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
