# Class to abstract away connecting to the mysql database.
import sys
import mysql.connector

class ManageConnections:

    db = None

    # Opens a connection to the mysql database.
    def open_connection(self):
        
        try:
            self.db = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='random_projects',
                autocommit=True
            )
        except mysql.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        # We can use this cursor to process any of the tables in the database.
        cursor = self.db.cursor()
        return cursor

    # Closes the connection to the mariadb database.
    def close_connection(self, cursor):
        cursor.close()
        self.db.close()