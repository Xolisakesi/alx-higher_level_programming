#!/usr/bin/python3
"""
Prints the State object with the name passed as
an argument from the database
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

    # Querying the State object with the specified ID
    new_instance = session.query(State).filter_by(id=2).first()

    # Updating the name of the retrieved State object
    new_instance.name = 'New Mexico'

    # Committing the transaction
    session.commit()
