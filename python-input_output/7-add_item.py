#!/usr/bin/python3

"""Module for script that adds all arguments to a Python list,
and then save them to a file"""

import os
import json
import sys

if not os.path.isfile('add_item.json'):
    data = [sys.argv[1]]
else:
    with open('add_item.json', 'r') as file:
        data = json.load(file)
    data.append(sys.argv[1])

with open('add_item.json', 'w') as file:
    json.dump(data, file)
