#!/usr/bin/python3
"""
    Module that implements the creation of state and cities
    objects for the state

"""
import sys
from sqlachemy import create_engine
from sqlalchemy.orm import sessionmaker
from relations_city import City
from relations_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: < filename > < username > < password > < database >")
        sys.exit(1)
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]

        engine = create_engine(f'mysql://{username} : {password}\
                                @localhost:3306/{db_name}')

        Base.metadata.create.all(engine)

        Session = sessionmaker(bind=engine)

        session = Session()

        state_and_cities = State(name="California",
                                 cities=[City(name="San Francisco")])
        session.add(state_and_cities)
        session.commit()
        session.close()
