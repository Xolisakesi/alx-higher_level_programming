#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Establishing a database connection
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    # Extracting the pattern to be matched
    match = sys.argv[4]

    # Executing SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))

    # Fetching results
    rows = cur.fetchall()

    # Printing results
    for row in rows:
        print(row)

    # Closing cursor and database connection
    cur.close()
    db.close()
