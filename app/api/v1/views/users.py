#app/api/v1/views/users.py
import models.users
from flask import Flask, jsonify

#instantiate app object
app = Flask(__name__)

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
    return jsonify({'message': 'User successfully created'})

#retrieve all users endpoint
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify({'users': user.get_users()})
    
#retrieve single user endpoint
@app.route('/api/v1/users/<int:id>', methods=['GET'])

