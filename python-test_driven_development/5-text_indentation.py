#!/usr/bin/python3

"""Module for function that prints text with 2 new lines after ., ?, and :"""


def text_indentation(text):

    """Function that prints text with 2 lines after ., ?, and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in '.:?':
        text = text.replace(char, char + '\n\n')

    print(*(ln.strip() for ln in (text + '\n').splitlines()), sep='\n', end='')
