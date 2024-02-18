#!/usr/bin/python3
"""
    Module to list all State objects from the given
    database that contain the letter 'a'

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
        engine = create_engine(f'mysql://{username}\
                :{password}@localhost:3306/{db_name}')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).\
            filter(State.name.like('%a%')).\
            order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")

        session.close()
