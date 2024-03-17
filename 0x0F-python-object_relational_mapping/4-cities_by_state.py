#!/usr/bin/python3
"""Lists all states and their cities from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Establishing a database connection
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    # Executing SQL query to select cities and their corresponding states
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")

    # Fetching results
    rows = cur.fetchall()

    # Printing results
    for row in rows:
        print(row)

    # Closing cursor and database connection
    cur.close()
    db.close()
