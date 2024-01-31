#!/usr/bin/python3

"""Module for unit testing and PEP8 validation"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
from io import StringIO


class TestBase(unittest.TestCase):
    """Base class tests"""
    def baseid(self):
        self.assertEqual(Base._Base__nb_objects, 0)
        test_obj = Base()
        self.assertEqual(test_obj.id, 1)

    def testid(self):
        id_obj = Base(89)
        self.assertEqual(id_obj.id, 89)

class TestJSON(unittest.TestCase):
    def empty(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def notdict(self):
        self.assertEqual(Base.to_json_string([3, 4, 5]), "[3, 4, 5]")

    def notlist(self):
        self.assertEqual(Base.to_json_string(51), "51")

    def success(self):
        r1 = Rectangle(5, 7)
        dict1 = r1.to_dictionary()
        check = '[{"id": 2, "width": 5, "height": 7, "x": 0, "y": 0}]'
        self.assertEqual(Base.to_json_string([dict1]), check)

class TestFromJSONMethod(unittest.TestCase):
    def empty1(self):
        empty1 = Base.from_json_string(None)
        self.assertEqual(empty1, [])

    def empty2(self):
        empty2 = Base.from_json_string("[]")
        self.assertEqual(empty2, [])

    def dict(self):
        d = {'id': 50}
        dl = [d]
        jl = Base.to_json_string(dl)
        self.assertEqual(Base.from_json_string(jl), [{'id': 50}])
