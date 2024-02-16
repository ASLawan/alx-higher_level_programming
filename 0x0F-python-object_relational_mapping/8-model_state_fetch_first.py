#!/usr/bin/python3
"""
    Module to list all State objects from the given
    database

"""
import sys
from sqlalchemy import create_engine
from sqlachemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: < filename > < username > < database >")
        sys.exit(1)
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        engine = create_engine(f'mysql://{username}\
                :{password}@localhost:3306/{db_name}')
        Base.metadata.create.all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).order_by(State.id).first()
        if (state):
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")
        session.close()
