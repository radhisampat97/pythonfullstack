import sqlite3
from flask_restful import Resource, reqparse
from dbConfig import DatabaseConfig

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def findUsername(cls, username):
        print("This is Username from findUsername: ", username)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        print("This is the row variable: ", row)
        if row:
            user = cls(*row)
            print("This is the user from database: ", user)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def findId(cls, _id):
        print(_id)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        print("This is from findId: ", row)
        print("This is from findId, row type: ", type(row))
        if row:
            user = cls(*row)
            print("This is the user from database: ", user)
        else:
            user = None

        connection.close()
        return user

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type = str,
        required = True,
        help = 'This field is required!'
    )
    parser.add_argument(
        'password',
        type = str,
        required = True,
        help = 'This field is required!'
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        print("This is from UserRegister class post method: ", data)
        
        if User.findUsername(data['username']):
            return {"message": 'A user with the current username already exist!'}, 400
        databaseName = 'data'
        connection, cursor = DatabaseConfig(databaseName).createConnection()

        query = "INSERT INTO users VALUES (NULL, ?, ?)" 
        cursor.execute(query, (data['username'], data['password']))

        # DatabaseConfig.commitClose()
        connection.commit()
        connection.close()
        return {"message" : "User created successfully!"}, 201