#!/usr/bin/python3
"""Start link class to table in database"""
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

    # Querying and printing all instances of the State class ordered by ID
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
