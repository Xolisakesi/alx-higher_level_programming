#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Connects to MySQL server and lists all states from the database

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name

    Returns:
        None
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database, charset="utf8")

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows and print them
        for row in cursor.fetchall():
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
