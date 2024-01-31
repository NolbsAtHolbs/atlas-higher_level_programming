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


class TestSquareAttrs(unittest.TestCase):
    def tsize(self):
        s1 = Square(5)
        res = s1.__str__()
        self.assertEqual(res, "[Square] (20) 0/0 - 5")
