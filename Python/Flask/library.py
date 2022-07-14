from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

books = []

class Book(Resource):
    def get(self):
        data = request.get_json()
        book = next(filter(lambda x: x['name'] == data['name'], books), None)
        return {'book': book}, 200 if book else 404

    def post(self):
        data = request.get_json()
        if next(filter(lambda x: x['name'] == data['name'], books), None):
            return {'message': "A book with name {} already exists.".format(data['name'])}, 400
        else:
            book = {'name': data ['name'], 'author': data['author'], 'pages': data['pages'],'price': data['price'], 'discount': data['discount'] }
            books.append(book)
            return books, 201

    def delete(self):
        global books
        data = request.get_json()
        books = list(filter(lambda x: x['name'] != data['name'], books))
        return {'message': 'Book deleted'}

    def put(self):
        data = request.get_json()
        book = next(filter(lambda x: x['name'] == data['name'], books))
        if book is None:
            book = {'name': data['name'], 'author': data['author'], 'pages': data['pages'],'price': data['price'], 'discount': data['discount']}
            books.append(book)
        else:
            book.update(data)
        return book


class BookList(Resource):
    def get(self):
        return {'books': books}

api.add_resource(Book, '/book')    
api.add_resource(BookList, '/books')

app.run(port=5000, debug = True)
