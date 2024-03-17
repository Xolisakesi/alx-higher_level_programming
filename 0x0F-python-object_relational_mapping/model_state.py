#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

# Creating a custom metadata
mymetadata = MetaData()

# Creating an instance of declarative_base with the custom metadata
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class representing a state with id and name attributes
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
