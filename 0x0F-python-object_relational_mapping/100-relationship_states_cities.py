#!/usr/bin/python3
"""
    Module that implements the creation of state and cities
    objects for the state

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: < filename > < username > < password > < database >")
        sys.exit(1)
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]

        engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                               .format(username, password, db_name))

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)

        session = Session()

        new_state = State(name='California')
        new_state_city = City(name='San Francisco')
        new_state.cities.append(new_state_city)

        session.add(new_state)
        session.add(new_state_city)
        session.commit()
        session.close()
