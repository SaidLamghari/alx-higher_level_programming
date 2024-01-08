#!/usr/bin/python3
""" the function def max_integer(list=[]):"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([4, -3, 2, -1]), 4)

    def test_single_number(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-3]), -3)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-3, -3, -3, -3]), -3)


if __name__ == '__main__':
    unittest.main()
