#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.agv[2]
    db_name = sys.agv[3]

    db = MySQLdb.connect(
            user=username,
            passwd=password,
            db=db_name,
            port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    states = cur.fetchall()

    for state in states:
        print(state)
