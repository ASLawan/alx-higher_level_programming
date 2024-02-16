#!/usr/bin/python3
"""
    Module that implements sql select
    state

"""
import sys
import MySQLdb


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <filenam> <username> <password> <database>")
        sys.exit(1)
    else:
        username = argv[1]
        password = argv[2]
        db_name = argv[3]
        port = 3306

        db = MySQLdb.connect(
                user=username,
                passwd=password,
                db=dba_name,
                port=port
                )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
        cursor.execute(query)
        states = cursor.fetchall()

        for state in states:
            print(state)
