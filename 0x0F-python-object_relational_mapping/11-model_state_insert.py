#!/usr/bin/python3
"""
    Module to add the State object 'Louisina' to
    the given database

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

        engine = create_engine(f'mysql://{username}\
                :{password}@localhost:3306/{db_name}')

        Base.metadata.create.all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()

        print(new_state.id)

        session.close()
