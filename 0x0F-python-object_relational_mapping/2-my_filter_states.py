#!/usr/bin/python3
"""
    Module that implements SQL select statement

"""
import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: < filename > < username > < password >\
            < database > < state name searched >")
        sys.exit(1)
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        port = 3306
        db_conn = MySQLdb.connect(
                user=username,
                passwd=password,
                db=db_name,
                port=port
                )
        cursor = db_conn.cursor()
        cursor.execute("SELECT * FROM states\
                WHERE name = '{}'\
                ORDER BY id ASC;".format(state_name))
        # cursor.execute(query.format(state_name))

        rows = cursor.fetchall()

        for row in rows:
            print(row)
