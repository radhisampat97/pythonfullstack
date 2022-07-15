'''
    This file will help in creating tables in the database.
    We have imported dbConfig.py file to connect with the database

'''
from dbConfig import DatabaseConfig

connection, cursor = DatabaseConfig('data').createConnection()

createTable = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(createTable)             # This will execute the cursor and will create a table in database

createTable = "CREATE TABLE IF NOT EXISTS employees (emp_id integer PRIMARY KEY, first_name text, last_name text,  email text, mobile integer, location text, job_role text, hire_date text, salary real )"
cursor.execute(createTable)             # This will execute the cursor and will create a table in database


connection.commit()     # To commit the changes 
connection.close()      # To save the changes and close the connection