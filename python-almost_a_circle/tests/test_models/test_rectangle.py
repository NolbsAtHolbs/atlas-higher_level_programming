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


class TestRectangle(unittest.TestCase):
    def stringwidth(self):
        with self.assertRaises(TypeError):
            bad_rect = Rectangle("two", 2)
