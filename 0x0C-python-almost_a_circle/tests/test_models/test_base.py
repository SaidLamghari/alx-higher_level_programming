#!/usr/bin/python3
"""
Module for some Base unit tests.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """
    def setUp(self):
        """
        Instantiates class
        """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """
        Cleans test_method.
        """
        pass

    def test_base_negative_id(self):
        """
        Test the creation of Base instances with negative IDs.
        """
        base = Base(-10)
        self.assertEqual(base.id, -10)

    def test_base_string_id(self):
        """
        Test the creation of Base instances with string IDs.
        """
        base = Base("test")
        self.assertEqual(base.id, "test")


if __name__ == '__main__':
    unittest.main()
