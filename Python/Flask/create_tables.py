from dbConfig import DatabaseConfig

connection, cursor = DatabaseConfig('data').createConnection()

createTable = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(createTable)

createTable = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(createTable)

cursor.execute("INSERT INTO items VALUES ('Jam', 50.00)")

connection.commit()     # To commit the changes 
connection.close()      # To save the changes and close the connection