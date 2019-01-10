#app/api/v1/views/users.py
from flask import Flask, jsonify
from datetime import datetime

#instantiate app object
app = Flask(__name__)

#instantiate user object
user = users.Users()

#create new user endpoint
@app.route('/api/v1/users', methods=['POST'])
def add_new_user():
    parsejson = request.get_json()
    userId = parsejson['userId']
    username = parsejson['username']
    email = parsejson['email']
    date_created = parsejson['date_created']
    user.add_user(int(userId), username, email, date_created)
    return jsonify({'message': 'User successfully created'}), 201

#retrieve all users endpoint
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify({'users': user.get_users()}), 200
    
#retrieve single user endpoint
@app.route('/api/v1/users/<int:userId>', methods=['GET'])
def get_user_by_id(userId):
    return jsonify({'user': user.get_user_by_id()}), 200

#change user details endpoint
@app.route('/api/v1/users/<int:userId>', methods=['PATCH'])
def update_user(userId):
    parsejson = request.get_json()
    username = parsejson['username']
    email = parsejson['email']
    return jsonify({'user': user.update_user(userId, username, email)}), 201
    
#delete user account endpoint
@app.route('/api/v1/users/<int:userId>', methods=['DELETE'])
def delete_user(userId):
    user.delete_user(userId)
    return jsonify({'message': 'Account successfully deleted'}), 204
    