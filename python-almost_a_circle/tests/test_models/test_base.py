#!/usr/bin/python3

"""Module for unit testing and PEP8 validation"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
import os
import json
from io import StringIO


class TestBase(unittest.TestCase):
    """Base class tests"""
    def baseid(self):
        self.assertEqual(Base._Base__nb_objects, 0)
        test_obj = Base()
        self.assertEqual(test_obj.id, 1)

    def test_custom_id(self):
        id_obj = Base(89)
        self.assertEqual(id_obj.id, 89)
