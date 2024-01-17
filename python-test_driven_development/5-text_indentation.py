#!/usr/bin/python3

"""Module for function that prints text with 2 new lines after ., ?, and :"""


def text_indentation(text):

    """Function that prints text with 2 lines after ., ?, and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars_to_split = [".", "?", ":"]
    start = 0
    for i, char in enumerate(text):
        if char in chars_to_split:
            if text[i + 1] == " ":
                print(text[start:i + 1].strip())
            else:
                print(text[start:i + 1])
            print("")
            start = i + 2

    if start < len(text):
        print(text[start:].strip())
