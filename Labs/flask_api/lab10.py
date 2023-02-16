from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask_restful import Api,Resource
from database import db
from resources import  routes
from database.models import Product 


app = Flask(__name__)
app.secret_key = "Kamran"
app.config['MONGO_URI'] = "mongodb://localhost:27017/Product"
api=Api(app)
db.initialize_db(app)
routes.initialize_routes(api)
mongo = PyMongo(app)

# @app.route('/add', methods=['POST'])
# def add_product():
#     _json = request.json
#     _name = _json['name']
#     _desc = _json['desc']
#     _price = _json['price']

#     if _name and _desc and _price and request.method == 'POST':
        
#         id = mongo.db.product.insert_one({
#             'name' : _name,
#             'desc': _desc,
#             'price': _price
#         })

#         resp = jsonify('Added successfully')

#         resp.status_code = 200

#         return resp
#     else:
#         return not_found()

# @app.errorhandler(404)
# def not_found(error = None):
#     message = {
#         "status code": 404,
#         "message": "Unsuccessful"
#     }

#     resp = jsonify(message)
#     resp.status_code = 404
#     return resp


@app.route('/addProducts')
def add_product():
    return render_template('addProducts.html')

@app.route('/updateProduct')
def show():
    return render_template('update.html')

@app.route('/searchProduct')
def search():
    return render_template('search.html')

@app.route('/deleteProduct')
def delete():
    return render_template('delete.html')

@app.route('/showProducts')
def show_product():
    return render_template('show.html')

@app.route('/products')
def get_products():
    products = mongo.db.product.find()
    resp = dumps(products)
    return resp

@app.route('/products/<id>')
def get_product(id):
    products = mongo.db.product.find_one({'_id':ObjectId(id)})
    resp = dumps(products)
    return resp

@app.route('/products/<id>')
def limit_product(id):
    products = mongo.db.product.find().limit(id)
    resp = dumps(products)
    return resp




# @app.route('/products/<query>')
# def search_product(query):
#     print(query)
#     myquery = { "name": query }
#     products = mongo.db.product.find(myquery)
#     resp = dumps(products)
#     return resp


# @app.route('/delete/<id>', methods=['DELETE'])
# def delete(id):
#     mongo.db.product.delete_one({'_id':ObjectId(id)})
#     resp = jsonify("Deleted Successfully")
#     return resp

# @app.route('/update/<id>', methods=['PUT'])
# def update(id):
#     _id = id
#     _json = request.json
#     _name = _json['name']
#     _desc = _json['desc']
#     _price = _json['price']

#     if _name and _email and _password and _id and request.method == 'PUT':
        

#         mongo.db.product.update_one({'_id':ObjectId(id)  }, {'$set':{'name':_name,'desc':_desc,'price:':_price}})
       
#         resp = jsonify('updated successfully')

#         resp.status_code = 200

#         return resp
#     else:
#         return not_found()

if __name__ == "__main__":
    app.run(debug=True)