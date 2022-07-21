from dbConfig import DatabaseConfig
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from modules.items import ItemModule


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help='This is required field'
    )
    parser.add_argument(
        'price',
        type=float,
        required=False,
        help='This is required field'
    )

    @jwt_required()
    def get(self):
        data = Item.parser.parse_args()
        item = ItemModule.findItem(data['name'])
        if item:
            return item.json()
        return {'message': 'Item not found!'}, 404
       
        # data = request.get_json()
        # item = next(filter(lambda x: x['name'] == data['name'], items), None)
        # return {'item': item}, 200 if item else 404


    @jwt_required()
    def post(self):
        data = Item.parser.parse_args()
        if ItemModule.findItem(data['name']):
            return {'message': "An item with name '{}' already exists.".format(data['name'])}, 400
        item = ItemModule(name= data['name'], price= data['price'])

        try:
            item.insert()
        except:
            return {"message": "An error occurred while inserting item"}, 500
        return item.json(), 201

        # data = request.get_json()
        # if next(filter(lambda x : x['name'] == data['name'], items), None):
        #     return {'message' : "An item with name '{}' already exists.".format(data['name'])}, 400
        # else:
        #     item = {'name' : data['name'], 'price' : data['price']}
        #     items.append(item)
        #     return items, 201


    
    @jwt_required()
    def delete(self):
        connection, cursor = DatabaseConfig('data').createConnection()
        data = Item.parser.parse_args()
        if ItemModule.findItem(data['name']):
            query = "DELETE FROM items WHERE name=?"
            cursor.execute(query, (data['name'],))
            connection.commit()
            connection.close()
            return {'message': "Item deleted!"}
        return {'message': 'Item does not exists!'}

        # global items
        # data = request.get_json()
        # items = list(filter(lambda x: x['name'] != data['name'], items))
        # return {'message' : 'Item deleted!'}

    @jwt_required()
    def put(self):
        data = Item.parser.parse_args()
        item = ItemModule.findItem(data['name'])
        updatedItem = ItemModule(name=data['name'], price=data['price'])

        if item is None:
            try:
                updatedItem.insert()
            except:
                return {"message": "An error occurred while inserting item"}, 500
        else:
            try:
                updatedItem.update()
            except:
                return {"message": "An error occurred while inserting item"}, 500
        return updatedItem.json()


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
        # data = request.get_json()
        # item = next(filter(lambda x: x['name'] == data['name'], items))
        # if item is None:
        #     item = {'name' : data['name'], 'price' : data['price']}
        #     items.append(item)
        # else:
        #     items.update(data)
        # return item

        # [{'name': 'sugar', 'price':'10}]



class ItemList(Resource):

    def get(self):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
  
        query = "SELECT * FROM items"
        result = cursor.execute(query)

        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()
        return {'items' : items}

