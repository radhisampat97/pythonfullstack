import sqlite3


class DatabaseConfig:
    def __init__(self, databaseName=None):
        self.databaseName = databaseName

    def createConnection(self):
        databaseName = '.'.join((str(self.databaseName), 'db'))
        print(databaseName)
        connection = sqlite3.connect(databaseName)
        cursor = connection.cursor()
        return connection, cursor

    def commitClose(self):
        connection, cursor = self.createConnection()
        connection.commit()
        connection.close()
