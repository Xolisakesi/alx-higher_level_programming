#!/usr/bin/python3

"""Defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        return {k: getattr(self, k) for k in (attrs if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs) else self.__dict__) if hasattr(self, k)}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
