from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'DMart',
        'items': [
            {
                'name': 'Tooth Brush',
                'price': 25
            },

            {
                'name': 'Shampoo',
                'price': 350

            },

            {
                'name': 'Biscuits',
                'price': 90
            }
        ]

    },

    {
        'name': 'Bigbazaar',
        'items': [
            {
                'name': 'Tea Powder',
                'price': 25

            },

            {
                'name': 'Milk',
                'price': 30

            },

            {
                'name': 'Rice',
                'price': 260
            }
        ]
    },

    {
        'name': 'Apna Bazaar',
        'items': [
            {
                
            }
        ]
    }


]



# Get /stores gives details of all stores
@app.route('/stores')
def getStores():
    return jsonify({'stores': stores})


# Get /store gives details of single store
@app.route('/store/<string:name>')   #http://127.0.0.1:5000/store/dmart
def getStore(name):
    print("Requested name of store:", name)
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found'})



# Post /store data: {name}
@app.route('/store', methods =['POST'])   #http://127.0.0.1:5000/store
def createStore():
    requestData = request.get_json()
    print("This is the incoming request:", requestData)
    newStore = {
        'name': requestData['name'],
        'item':[]

    }
    stores.append(newStore)
    return jsonify({'stores': stores}, {'Count': len(stores)})

# Post /store/<string:name>item{name: , price:}
@app.route('/store/<string:name>/item', methods =['POST'])
def createStoreItem(name):
    requestData = request.get_json()
    for store in stores:
        if store ['name'] == name:
            newItem = {
                'name': requestData['name'],
                'price': requestData['price']
            }
            store['items'].append(newItem)
            return jsonify(newItem)
    return jsonify({'message': 'Store not found'})


# Get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def getItemStore(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store not found'})




#@app.route('/')  #http://127.0.0.1:5000/
#def home():
#    return "This is the first Flask API"

app.run(port=5000)