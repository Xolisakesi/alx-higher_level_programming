#!/usr/bin/python3
"""
Script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def filter_states(username, password, database):
    """
    Connects to MySQL server and lists states with names starting with 'N'.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)

        # Create a cursor object to execute queries
        cursor = db.cursor()

        # Execute the query to select states with name starting with 'N'
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(str(e)))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'db' in locals() and db is not None:
            db.close()


if __name__ == "__main__":
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call function to filter states
    filter_states(username, password, database)
