from dbConfig import DatabaseConfig

connection, cursor = DatabaseConfig('data').createConnection()

createTable = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(createTable)

createTable = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(createTable)

connection.commit()
connection.close()
