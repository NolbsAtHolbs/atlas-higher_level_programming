#!/usr/bin/python3

"""Module for unit testing and PEP8 validation"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
import os
import json
import io


class TestBase(unittest.TestCase):
    """Base class tests"""
    def baseid(self):
        """test do it test done"""
        b1 = Base()
        b2 = Base()
        b3 = Base(8)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 8)
