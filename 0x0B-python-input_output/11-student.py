#!/usr/bin/python3

class Student:
    """Represents a student."""
    
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student."""
        return {k: getattr(self, k) for k in (attrs if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs) else self.__dict__) if hasattr(self, k)}
    
    def reload_from_json(self, json):
        """Replaces all attributes of the Student."""
        for k, v in json.items():
            setattr(self, k, v)
