# DeliverIT2/app/api/v1/views/users.py
from flask import jsonify, request
from app import app

# import users.py from models
from ..models import users


# instantiate user object
user = users.Users()

# create new user endpoint


@app.route('/api/v1/users', methods=['POST'])
def add_new_user():
    parsejson = request.get_json()
    username = parsejson['username']
    email = parsejson['email']
    return jsonify({'feedback': user.add_user(username, email)}), 201

# retrieve all users endpoint


@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify({'users': user.get_users()}), 200

# retrieve single user endpoint


@app.route('/api/v1/users/<int:userId>', methods=['GET'])
def get_user_by_id(userId):
    return jsonify({'user': user.get_user_by_id(userId)}), 200

# change user details endpoint


@app.route('/api/v1/users/<int:userId>', methods=['PATCH'])
def update_user(userId):
    parsejson = request.get_json()
    username = parsejson['username']
    email = parsejson['email']
    return jsonify({'Updated user': user.update_user(userId, username, email)}), 201

# delete user account endpoint


@app.route('/api/v1/users/<int:userId>', methods=['DELETE'])
def delete_user(userId):
    user.delete_user(userId)
    return jsonify({'message': 'Account successfully deleted'}), 204
