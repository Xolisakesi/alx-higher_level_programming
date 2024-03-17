#!/usr/bin/python3
""" prints the State object with the name passed
as argument from the database """
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

    # Querying the State object with the specified name
    instance = session.query(State).filter(State.name == (sys.argv[4],))

    try:
        # Printing the ID of the State object if found
        print(instance[0].id)
    except IndexError:
        # Handling the case when no State object is found
        print("Not found")
