from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'radhika'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

#class Student(Resource):
#    def get(self, name):
#       return {'student': name}



class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': 'item'}, 200 if item else 404


    def post(self, name):
        data = request.get_json()
        if next(filter(lambda x: x['name'] == data['name'], items), None):
            return {'message': "An item with name {} already exists.".format(data['name'])}, 400
        else:
            item = {'name': data ['name'], 'price': data['price']}
            items.append(item)
            return items, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}




#api.add_resource(Student, '/student/<string:name>')    #http://127.0.0.1:5000/student/Radhika
#app.run(port=5000)

api.add_resource(Item, '/item/<string:name>')    #http://127.0.0.1:5000/student/Radhika
api.add_resource(ItemList, '/items')

app.run(port=5000, debug = True)
