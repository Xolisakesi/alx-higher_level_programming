#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Creating a database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Creating all tables associated with the Base
    Base.metadata.create_all(engine)

    # Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying the first State object
    instance = session.query(State).first()

    # Printing the result
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")
