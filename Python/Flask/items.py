from dbConfig import DatabaseConfig
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required



class Item(Resource):
    parser = reqparse.RequestParser()   # This is through the request we want a name
    parser.add_argument(                # This is through the request we want a name
        'name',
        type=str,
        required=True,
        help='This is required field'
    )
    parser.add_argument(               # This is through the request we want a name and price
        'price',
        type=float,
        required=False,
        help='This is required field'
    )


    @jwt_required()
    def get(self):
        data = Item.parser.parse_args()
        item = self.findItem(data['name'])
        if item:
            return item
        return {'message': 'Item not found!'}, 404
       
        # data = request.get_json()
        # item = next(filter(lambda x: x['name'] == data['name'], items), None)
        # return {'item': item}, 200 if item else 404

    @classmethod
    def findItem(cls, name):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
   
        if row:
            return {'item': {
                'name': row[0],
                'price': row[1]
            }}

    @classmethod
    def insert(cls, item):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
  
        query = "INSERT INTO items VALUES (?, ?)"
        result = cursor.execute(query, (item['name'], item['price']))
        
        connection.commit()
        connection.close()  

    @classmethod
    def update(cls, item):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
  
        query = "UPDATE items SET price=? WHERE name=?"
        result = cursor.execute(query, (item['price'], item['name']))
        
        connection.commit()
        connection.close()


    @jwt_required()
    def post(self):
        data = Item.parser.parse_args()
        if self.findItem(data['name']):
            return {'message' : "An item with name '{}' already exists.".format(data['name'])}, 400
        item = {'name' : data['name'], 'price' : data['price']}
        
        try:
            self.insert(item)
        except:
            return {'message': 'An error occured while insertingn item'}, 500
        return item, 201

        # data = request.get_json()
        # if next(filter(lambda x : x['name'] == data['name'], items), None):
        #     return {'message' : "An item with name '{}' already exists.".format(data['name'])}, 400
        # else:
        #     item = {'name' : data['name'], 'price' : data['price']}
        #     items.append(item)
        #     return items, 201


    
    @jwt_required()
    def delete(self):
        connection, cursor = DatabaseConfig('data').createConnection()  # This is to create connection with database 'data' file and to execute it
        data = Item.parser.parse_args()
        if self.findItem(data['name']):
            query = "DELETE FROM items WHERE name=?"
            result = cursor.execute(query, (data['name'],))
            connection.commit()
            connection.close() 
            return {'message' : 'Item deleted!'}
        return {'message': 'Item does not exists!'}

        # global items
        # data = request.get_json()
        # items = list(filter(lambda x: x['name'] != data['name'], items))
        # return {'message' : 'Item deleted!'}

    @jwt_required()
    def put(self):
        data = Item.parser.parse_args()
        item = self.findItem(data['name'])
        updatedItem = {'name': data['name'], 'price': data['price']}

        if item is None:
            try:
                self.insert(updatedItem)
            except:
                return {"message": "An error occured while inserting item"}, 500
        
        else:
            try:
                self.update(updatedItem)
            except:
                return{"message": "An error occured while inserting item"}, 500
        return updatedItem

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

