#!/usr/bin/python3
"""
    Module to update name of given State object id
    from the database to new name

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

        state = session.query(State).filter(State.id == 2).first()

        state.name = 'New Mexico'
        session.commit()

        session.close()
