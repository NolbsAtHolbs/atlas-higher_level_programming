#!/usr/bin/python3

"""Module for function that returns the JSON representation of a string object"""


import json

def to_json_string(my_obj):
    """Function that returns the JSON representation of a string object"""
    return json.dumps(my_obj)
