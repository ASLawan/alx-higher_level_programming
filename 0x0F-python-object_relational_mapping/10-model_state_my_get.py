#!/usr/bin/python3
"""
    Module to print State object from the given
    database with name passed as argument

"""
import sys
from sqlalchemy import create_engine
from sqlachemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: < filename > < username >\
                < password > < database >")
        sys.exit(1)
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]

        engine = create_engine(f'mysql://{username}\
                :{password}@localhost:3306/{db_name}')

        Base.metadata.create.all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).\
            filter(State.name == state_name).first()

        if (state):
            print(f"{state.id}")
        else:
            print("Mot found")

        session.close()
