#!/usr/bin/python3
"""Unittest for max_integer()"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing max_integer()"""
    def test_no_args(self):
        """testing for no args"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Testing for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_arg(self):
        """Testing for one arg"""
        self.assertEqual(max_integer([23]), 23)

    def test_multiple_args(self):
        """Testing for multiple args"""
        self.assertEqual(max_integer([3, 4, 7]), 7)

    def test_same_args(self):
        """Testing same args case"""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_negatives_positives(self):
        """Testing negative ints"""
        self.assertEqual(max_integer([-1, 3, -4]), 3)

    def test_negatives(self):
        """Testing negative ints"""
        self.assertEqual(max_integer([-1, -2, -4]), -1)

    def test_floats(self):
        """Testing floats"""
        self.assertEqual(max_integer([2.32, 2.33, 2.34]), 2.34)

    def test_numeric_string(self):
        """Testing numeric string case"""
        self.assertEqual(max_integer("192834754"), "9")

    def test_string(self):
        """Unittest for string"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_lists(self):
         """Unittest for lists"""
         self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_str_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
                max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),
                ["sic"])

    def test_inf(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]),
                         float('inf'))

    def test_nan(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('nan'), 100]), 100)

    def test_mixed_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_mixed_list_int_str(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([99, "foo"])

    def test_none(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_int(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_float(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(9.8)
