import sqlite3
from dbConfig import DatabaseConfig


class ItemModule:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def findItem(cls, name):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
   
        if row:
            return {'item': {
                'name': row[0],
                'price': row[1]
            }}

    @classmethod
    def insert(cls, item):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
  
        query = "INSERT INTO items VALUES (?, ?)"
        result = cursor.execute(query, (item['name'], item['price']))
        
        connection.commit()
        connection.close()  

    @classmethod
    def update(cls, item):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
  
        query = "UPDATE items SET price=? WHERE name=?"
        result = cursor.execute(query, (item['price'], item['name']))
        
        connection.commit()
        connection.close()

