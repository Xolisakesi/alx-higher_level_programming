#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_0_usa for a specified state"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Establishing a database connection
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    # Executing SQL query to select cities for the specified state
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

    # Fetching results
    rows = cur.fetchall()

    # Extracting city names and printing them
    city_names = [row[0] for row in rows]
    print(*city_names, sep=", ")

    # Closing cursor and database connection
    cur.close()
    db.close()
