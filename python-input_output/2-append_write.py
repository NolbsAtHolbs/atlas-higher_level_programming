#!/usr/bin/python3

"""Module for function that appends a string at the end of a UTF8 text file
and returns the num of chars added"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a UTF8 text file
    and returns the num of chars added"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
