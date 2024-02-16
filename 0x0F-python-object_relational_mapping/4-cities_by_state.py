#!/usr/bin/python3
"""
    Module to implemente script that displays cities
    by state from given database

"""
import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: < filename > < username > < password > < database >")
        sys.exit(1)
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]

        db = MySQLdb.connect(
                user=username,
                passwd=password,
                db=db_name,
                port=3306
                )
        cursor = db.cursor()
        query = "SELECT cities.id, cities.name, state.name\
                FROM cities\
                JOIN states ON cities.state_id = states.id"
        cursor.execute(query)

        cities = cursor.fetchall()

        for city in cities:
            print(city)
