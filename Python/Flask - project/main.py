"""
    This main.py file is the main file for this project.
    The server starts from here. All the endpoints are registered in this file.
    This file helps in routing the incoming api request to the appropriate resource.
    This file has all the main imports required to create the server
"""
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from user import UserRegister
from security import authenticate, identity
from employees import Employee, EmployeeList

app = Flask(__name__) 
app.secret_key = 'radhika'
api = Api(app)

jwt = JWT(app, authenticate, identity)          # This will generate a token 

# Employee and EmployeeList is shifted to employees.py file and the required imports are added  on line 12

api.add_resource(Employee, '/employee')     #http://127.0.0.1:5000/employees
api.add_resource(EmployeeList, '/employees')
api.add_resource(UserRegister, '/register')
# print('This is from main.py:', __name__)

if __name__ == '__main__':        # If the main.py file is executed then only the server will start
    app.run(port=5000, debug=True)