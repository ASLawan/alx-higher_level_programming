#!/usr/bin/python3
"""
    Module to list all State objects and corresponding city objects
    in the given database

"""
import sys
from sqlalchemy import create_engine
from sqlachemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <filename> <username> <password> <database>")
        sys.exit(1)
    else:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]

        eng = create_engine(f'mysql: //{user}: {passwd}@localhost: 3306/{db}')
        Base.metadata.create_all(eng)
        Session = sessionmaker(bind=eng)
        session = Session()

        cities = session.query(City).order_by(City.id).all()
        for city in cities:
            if city.state:
                state_name = city.state.name
            print(f"{city.id}: {city.name} -> {state_name}")

        session.close()
