from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'shriya'
api = Api(app)

jwt = JWT(app, authenticate, identity)

employees = []


class Employee(Resource):
    #@jwt_required()
    def get(self):
        data = request.get_json()
        employee = next(filter(lambda x: x['emp_id'] == data['emp_id'], employees), None)
        return {'employee': employee}, 200 if employee else 404
        

    def post(self):
        data = request.get_json()
        if next(filter(lambda x : x['emp_id'] == data['emp_id'], employees), None):
            return {'message' : "An employee with empid '{}' already exists.".format(data['emp_id'])}, 400
        else:
            employee = {'emp_id': data['emp_id'], 'fname': data['fname'], 'lname': data['lname'], 'email': data['email'], 'mobile': data['mobile'], 'location': data['location'], 'job_role': data['job_role'], 'hire_date': data['hire_date'], 'salary': data['salary']}
            employees.append(employee)
            return employees, 201

    def delete(self):
        global employees
        data = request.get_json()
        employees = list(filter(lambda x: x['emp_id'] != data['emp_id'], employees))
        return {'message' : 'Employee info deleted!'}

    def put(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('price',
        #                     type = float,
        #                     required = True,
        #                     help = "This is required!"
        #                     )
        # parser.add_argument('name',
        #                     type = str,
        #                     required = True,
        #                     help = "This is required!"
        #                     )
        
        # data = parser.parse_args()
        # print(data)
        # print(dict(data))
        # print(type(data))

        data = request.get_json()
        employee = next(filter(lambda x: x['emp_id'] == data['emp_id'], employees))
        if employee is None:
            employee = {'emp_id': data['emp_id'], 'fname': data['fname'], 'lname': data['lname'], 'email': data['email'], 'mobile': data['mobile'], 'location': data['location'], 'job_role': data['job_role'], 'hire_date': data['hire_date'], 'salary': data['salary']}
            employees.append(employee)
        else:
            employee.update(data)
        return employee

        
class EmployeeList(Resource):
    def get(self):
        return {'employees' : employees}


api.add_resource(Employee, '/employee')     #http://127.0.0.1:5000/employee
api.add_resource(EmployeeList, '/employees')


app.run(port=5000, debug=True)