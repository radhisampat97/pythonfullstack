'''
    This file helps in creating the database.
    This file will help us for creating the connection with the database
'''
import sqlite3


class DatabaseConfig:
    def __init__(self, databaseName):
        self.databaseName = databaseName

    def createConnection(self):
        databaseName = '.'.join((str(self.databaseName), 'db'))
        print(databaseName)
        connection = sqlite3.connect(databaseName)
        cursor = connection.cursor()
        return connection, cursor

    def commitClose(self):
        connection, cursor = self.createConnection()   # This is to create connection with database.db txt file and to execute it
        connection.commit()
        connection.close()