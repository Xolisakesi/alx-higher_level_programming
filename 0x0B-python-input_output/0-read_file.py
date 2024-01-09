#!/usr/bin/python3
"""
Contains the read_file function.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
