import sqlite3
from dbConfig import DatabaseConfig

class UserModule:
    """
        This class will verify the incoming (through request) user credentials, username and password.
    """
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def findUsername(cls, username):
        """
            This function will identify the user whether that user present in the database, based on his username.
        """
        connection, cursor = DatabaseConfig('data').createConnection()     # This will create a connection to the database

        query = "SELECT * FROM users WHERE username=?"      # This is the query to select the record based on the username.
        result = cursor.execute(query, (username,))         # This will execute the query along with the given username.
        row = result.fetchone()                             # This will fetch one record from the database. This is an iterable.
        print("THis is the type of the row: ", type(row))
        if row:                                             # This will iterate over the object of the row.
            user = cls(*row)
            print('This is the user from database: ', user)
        else:
            user = None                                     # This returns user as None if the username does not matches.

        connection.close()
        return user

    @classmethod
    def findId(cls, _id):
        # _id = str(_id,)
        connection, cursor = DatabaseConfig('data').createConnection()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        print("This is from findId: ", row)
        print("This is from findId, row type: ", type(row))
        if row:
            user = cls(*row)
            print('This is the user from database: ', user)
        else:
            user = None

        connection.close()
        return user
