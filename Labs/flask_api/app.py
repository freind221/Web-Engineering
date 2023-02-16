from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "Kamran"
app.config['MONGO_URI'] = "mongodb://localhost:27017/Users"

mongo = PyMongo(app)

@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and request.method == 'POST':
        _hashed = generate_password_hash(_password)
        id = mongo.db.Users.insert_one({
            'name' : _name,
            'email': _email,
            'password': _hashed
        })

        resp = jsonify('Added successfully')

        resp.status_code = 200

        return resp
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error = None):
    message = {
        "status code": 404,
        "message": "Unsuccessful"
    }

    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.route('/users')
def get_users():
    users = mongo.db.Users.find()
    resp = dumps(users)
    return resp

@app.route('/users/<id>')
def get_user(id):
    users = mongo.db.Users.find_one({'_id':ObjectId(id)})
    resp = dumps(users)
    return resp


@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    mongo.db.Users.delete_one({'_id':ObjectId(id)})
    resp = jsonify("Deleted Successfully")
    return resp

@app.route('/update/<id>', methods=['PUT'])
def update(id):
    _id = id
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and _id and request.method == 'PUT':
        _hashed = generate_password_hash(_password)

        mongo.db.Users.update_one({'_id':ObjectId(id)  }, {'$set':{'name':_name,'email':_email,'password:':_hashed}})
       
        resp = jsonify('updated successfully')

        resp.status_code = 200

        return resp
    else:
        return not_found()

if __name__ == "__main__":
    app.run(debug=True)