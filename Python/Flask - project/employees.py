'''
    This file contains all the reuired imports for executing different functions
    Like Insert, Update, Delete records
'''

from dbConfig import DatabaseConfig
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required



class Employee(Resource):
    parser = reqparse.RequestParser()   
    parser.add_argument(                # This is through the request we want a name
        'emp_id',
        type=int,
        required=True,
        help='This is required field'
    )
    parser.add_argument(               
        'first_name',
        type=str,
        required=False,
        help='This is required field'
    )
    parser.add_argument(               
        'last_name',
        type=str,
        required=False,
        help='This is required field'
    )

    parser.add_argument(               
        'email',
        type=str,
        required=False,
        help='This is required field'
    )

    parser.add_argument(               
        'mobile',
        type=int,
        required=False,
        help='This is required field'
    )

    parser.add_argument(               
        'location',
        type=str,
        required=False,
        help='This is required field'
    )

    parser.add_argument(               
        'job_role',
        type=str,
        required=False,
        help='This is required field'
    )

    parser.add_argument(               
        'hire_date',
        type=str,
        required=False,
        help='This is required field'
    )

    parser.add_argument(               
        'salary',
        type=float,
        required=False,
        help='This is required field'
    )


    @jwt_required()
    def get(self):
        data = Employee.parser.parse_args()
        employee = self.findEmployee(data['emp_id'])
        if employee:
            return employee
        return {'message': 'Employee not found!'}, 404
       
        

    @classmethod
    def findEmployee(cls, emp_id):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
        query = "SELECT * FROM employees WHERE emp_id=?"
        result = cursor.execute(query, (emp_id,))
        row = result.fetchone()
        connection.close()
   
        if row:
            return {'employee': {
                'emp_id': row[0],
                'first_name': row[1],
                'last_name': row[2],
                'email': row[3],
                'mobile': row[4],
                'location': row[5],
                'job_role': row[6],
                'hire_date': row[7],
                'salary': row[8]
            }}

    @classmethod
    def insert(cls, employee):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
        query = "INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        result = cursor.execute(query, (employee['emp_id'], employee['first_name'], employee['last_name'], employee['email'], employee['mobile'], employee['location'], employee['job_role'], employee['hire_date'], employee['salary']))
        
        connection.commit()
        connection.close()  

    @classmethod
    def update(cls, employee):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
  
        query = "UPDATE employees SET salary=? WHERE emp_id=?"
        result = cursor.execute(query, (employee['salary'], employee['emp_id']))
        
        connection.commit()
        connection.close()


    @jwt_required()
    def post(self):
        data = Employee.parser.parse_args()
        print(data['emp_id'])
        if self.findEmployee(data['emp_id']):
            return {'message' : "An employee with emp_id '{}' already exists.".format(data['emp_id'])}, 400
        employee = {'emp_id' : data['emp_id'], 'first_name' : data['first_name'], 'last_name' : data['last_name'], 'email' : data['email'], 'mobile' : data['mobile'], 'location' : data['location'], 'job_role' : data['job_role'], 'hire_date' : data['hire_date'], 'salary' : data['salary']}
        print("These are the employee details: ", employee)

        try:
            self.insert(employee)
        except:
            return {'message': 'An error occured while inserting employee'}, 500
        return employee, 201

    
    @jwt_required()
    def delete(self):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
        data = Employee.parser.parse_args()
        if self.findEmployee(data['emp_id']):
            query = "DELETE FROM employees WHERE emp_id=?"
            result = cursor.execute(query, (data['emp_id'],))
            connection.commit()
            connection.close() 
            return {'message' : 'Employee deleted!'}
        return {'message': 'Employee does not exists!'}


    @jwt_required()
    def put(self):
        data = Employee.parser.parse_args()
        employee = self.findEmployee(data['emp_id'])
        updatedEmployee = {'emp_id' : data['emp_id'], 'first_name' : data['first_name'], 'last_name' : data['last_name'], 'email' : data['email'], 'mobile' : data['mobile'], 'location' : data['location'], 'job_role' : data['job_role'], 'hire_date' : data['hire_date'], 'salary' : data['salary']}

        if employee is None:
            try:
                self.insert(updatedEmployee)
            except:
                return {"message": "An error occured while inserting employee"}, 500
        
        else:
            try:
                self.update(updatedEmployee)
            except:
                return{"message": "An error occured while updating employee"}, 500
        return updatedEmployee

        

class EmployeeList(Resource):
    def get(self):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
  
        query = "SELECT * FROM employees"
        result = cursor.execute(query)

        employees = []
        for row in result:
            employees.append({'first_name': row[1], 'last_name': row[2]})

        connection.close()
        return {'employees' : employees}

