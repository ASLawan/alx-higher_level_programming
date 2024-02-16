#!/usr/bin/python3
"""
    Module to print all city objects from the
    database

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: < filename > < username > < password > < database >")
        sys.exit(1)
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]

        engine = create_engine(f'mysql://{username}:{password}\
                @localhost:3306/{db_name}')
        Base.metadata.create.all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        cities = session.query(City).order_by(City.id).all()

        for city in cities:
            print(f"{city.state.name}: ({city.id}) {city.name}")

        session.close()
