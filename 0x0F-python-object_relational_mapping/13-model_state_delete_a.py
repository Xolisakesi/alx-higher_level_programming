#!/usr/bin/python3
""" Prints the State object with the name passed
as an argument from the database. """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

def main():
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        return

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        state_name = sys.argv[4]

        instance = session.query(State).filter(State.name == state_name).first()
        if instance:
            print(instance.id)
        else:
            print("State with name '{}' not found.".format(state_name))

    except SQLAlchemyError as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
