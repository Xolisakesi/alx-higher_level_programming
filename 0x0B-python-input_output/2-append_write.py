#!/usr/bin/python3
"""
Contains the append_write function.
"""


def append_write(filename="", text=""):
    """
Appends a string to the end of a text file (UTF8).

    Args:
        filename (str): The name of the file.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters added.
    """

    with open(filename, 'a', encoding='utf-8') as file:
        nb_chars_added = file.write(text)

    return nb_chars_added
