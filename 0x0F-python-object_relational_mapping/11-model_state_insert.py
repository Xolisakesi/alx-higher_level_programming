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

    # Creating a new State object with the name passed as an argument
    new_state = State(name='Louisiana')

    # Adding the new State object to the session
    session.add(new_state)

    # Querying the database to retrieve the newly added State object
    new_instance = session.query(State).filter_by(name='Louisiana').first()

    # Printing the ID of the newly added State object
    print(new_instance.id)

    # Committing the transaction
    session.commit()
