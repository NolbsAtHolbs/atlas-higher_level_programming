#!/usr/bin/python3

"""Module for script that adds all arguments to a Python list,
and then save them to a file"""

import sys
import json

arguments = sys.argv[1:]

with open('add_item.json', 'w') as file:
    json.dump(arguments, file)
