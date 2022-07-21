from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Dmart',
        'items': [
            {
                'name': 'Tooth Brush',
                'price': 25
            },
            {
                'name': "Shampoo",
                'price': 350
            },
            {
                'name': "Biscuits",
                'price': 90
            }
        ]
    },
    {
        'name': "Bigbazaar",
        'items': [
            {
                'name': "Tea Powder",
                'price': 250
            },
            {
                'name': "Milk",
                'price': 25
            },
            {
                'name': "Oil",
                'price': 300
            }
        ]
    },
    {
        'name': "Apna Bazaar",
        'items': []
    }
]


# GET /stores  gives details of all stores
@app.route('/stores')
def getStores():
    return jsonify({'stores': stores})


# GET /store/<string:name>   gives details of single store
@app.route('/store/<string:name>')  # http://127.0.0.1:500/store/dmart
def getStore(name):
    print("Requested name of store: ", name)
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found'})


# POST /store data: {name:}
@app.route('/store', methods=['POST'])  # http://127.0.0.1:5000/store
def createStore():
    requestData = request.get_json()
    print("This is the incoming request: ", requestData)
    newStore = {
        'name': requestData['name'],
        'item': []
    }
    stores.append(newStore)
    return jsonify({'stores': stores}, {'Count': len(stores)})


# POST /store/<string:name>/item {name: , price: }
@app.route('/store/<string:name>/item', methods=['POST'])
def createStoreItem(name):
    requestData = request.get_json()
    print("This is the incoming request: ", name)
    for store in stores:
        if store['name'] == name:
            newItem = {
                'name': requestData['name'],
                'price': requestData['price']
            }
            store['items'].append(newItem)
            return jsonify(newItem)
    return jsonify({'message': 'Store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def getItemInStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store not found'})


# @app.route('/')  # http://127.0.0.1:5000/
# def home():
#     return "This is the first Flask API"


app.run(port=5000)
