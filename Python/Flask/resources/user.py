import sqlite3
from flask_restful import Resource, reqparse
from dbConfig import DatabaseConfig
from modules.user import UserModule
# print("This is from user: ", __name__)


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This field is required!'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field is required!'
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        print("This is from UserRegister class post method: ", data)

        if UserModule.findUsername(data['username']):
            return {"message": 'A user with the current username already exists!'}, 400

        databaseName = 'data'
        connection, cursor = DatabaseConfig(databaseName).createConnection()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        # DatabaseConfig.commitClose()
        connection.commit()
        connection.close()
        return {"message": "User created successfully!"}, 201
