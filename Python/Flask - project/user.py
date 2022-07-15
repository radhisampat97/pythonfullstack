import sqlite3
from flask_restful import Resource, reqparse
from dbConfig import DatabaseConfig
# print('This is from user.py:', __name__)

class User:
    '''
        This class will verify the incoming (through request)user detailscredentials, username, password
    '''
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def findUsername(cls, username):
        '''
            This function will identify the user whether the user is there based on his username
        '''
        print("This is Username from findUsername: ", username)
        connection = sqlite3.connect('data.db')         # This will create a connection to the database
        cursor = connection.cursor()                    # This will create a cursor object of the existing connection

        query = "SELECT * FROM users WHERE username = ?"      # This is the query to select the record based on the username
        result = cursor.execute(query, (username,))           # This will execute the query along with the given username.
        row = result.fetchone()                               # This will fetch one record from the database. This is an iterable 
        print("This is the row variable: ", row)
        if row:                                           # This will iterate over the object of the row
            user = cls(*row)
            print("This is the user from database: ", user)
        else:
            user = None                                 # This will return None value over no object in the database

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
    '''
        This class will register the incoming (through request) user details credentials, username, password
    '''

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
<<<<<<< HEAD
        return {"message" : "User created successfully!"}, 201
        
=======
        return {"message" : "User created successfully!"}, 201
>>>>>>> anurag
