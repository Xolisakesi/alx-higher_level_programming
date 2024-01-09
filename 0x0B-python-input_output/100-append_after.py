#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_term="", insert_text=""):
    """
    Insert text after each line containing a given term in a file.

    Args:
        filename (str): The name of the file.
        search_term (str): The term to search for within the file.
        insert_text (str): The text to insert.
    """
    content = ""
    with open(filename) as file:
        for line in file:
            content += line
            if search_term in line:
                content += insert_text
    with open(filename, "w") as file:
        file.write(content)
