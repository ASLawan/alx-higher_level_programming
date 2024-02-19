#!/usr/bin/python3
"""
    Module that implements sql select
    state

"""
import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: <filenam> <username> <password> <database>")
        sys.exit(1)
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        port = 3306

        db_conn = MySQLdb.connect(
                user=username,
                passwd=password,
                db=db_name,
                port=port
                )
        cursor = db_conn.cursor()
        query = "SELECT * FROM states WHERE name LIKE binary\
                'N%' ORDER BY id ASC;"
        cursor.execute(query)
        states = cursor.fetchall()

        for state in states:
            print(state)
