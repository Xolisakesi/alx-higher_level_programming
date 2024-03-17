#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Check if username, password, and database name are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)

        # Create a cursor object to execute queries
        cur = db.cursor()

        # Execute the query to select states with names starting with 'N'
        cur.execute("""SELECT * FROM states WHERE name
                    LIKE BINARY 'N%' ORDER BY states.id""")

        # Fetch all the rows
        rows = cur.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(str(e)))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'db' in locals() and db is not None:
            cur.close()
            db.close()
