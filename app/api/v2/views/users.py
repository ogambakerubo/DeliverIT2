#DeliverIT2/app/api/v2/views/users.py
from flask import jsonify, request
from flask_jwt_extended import JWTManager,jwt_required, create_access_token, get_jwt_identity

#local imports
from app import app
from app.api.v2.models import users

#Setup the Flask-JWT-Extended extension


#instantiate db object
db = users.Users()

#create database schemas
db.create_schemas()

@app.route('/auth/signup', methods=['POST'])
#create new user endpoint
def add_new_user():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    email = request.json.get('email', None)

    if not username:
        return jsonify({"message": "Fill in username"}), 400
    if not password:
        return jsonify({"message": "Fill in password"}), 400
    if not email:
        return jsonify({"message": "Fill in email"}), 400

    parsejson = request.get_json()
    username = parsejson['username']
    email = parsejson['email']
    password = parsejson['password']
    #create roles
    role_name = "reguser"
    db.add_role(role_name)

    if username and email and password:
        return jsonify({'feedback': db.add_user(username, email, password)}), 201
