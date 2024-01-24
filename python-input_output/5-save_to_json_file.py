#!/usr/bin/python3

"""Module for function that writes an object to a text file,
using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file,
    using a JSON representation"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
