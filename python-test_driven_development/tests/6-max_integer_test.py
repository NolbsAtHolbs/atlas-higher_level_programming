#!/usr/bin/python3

"""Module for a Unittest for max_integer function"""


import unittest
max_integer = __import__("6-max_integer").max_integer

class UTMaxInteger(unittest.TestCase):
    """class unit tester"""
    def test_one_negative(self):
        self.assertEqual(max_integer([-8, 3, 6, 4]), 6)

    def test_one_element(self):
        self.assertEqual(max_integer([55]), 55)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
