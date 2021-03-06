# DeliverIT2/app/api/v2/views/users.py
import os
from flask import jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# local imports
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", '')
from app import app
from app.api.v2.models import users

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
jwt = JWTManager(app)

# instantiate db object
db = users.Users()

# create database schemas
db.create_schemas()

#create roles
db.add_role()

@app.route('/auth/signup', methods=['POST'])
# create new user endpoint
def add_new_user():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    email = request.json.get('email', None)
    confirm_password = request.json.get('confirm-password', None)

    #fill in the fields
    if not username:
        return jsonify({"message": "Fill in username"}), 400
    if not password:
        return jsonify({"message": "Fill in password"}), 400
    if not email:
        return jsonify({"message": "Fill in email"}), 400
    if not confirm_password:
        return jsonify({"message": "Fill in password"}), 400
    if not confirm_password == password:
        return jsonify({"message": "password and confirm-password MUST match"}), 400

    parsejson = request.get_json()
    username = parsejson['username']
    email = parsejson['email']
    password = parsejson['password']
    confirm_password = parsejson['confirm-password']

    if username and email and password and confirm_password:
        return jsonify({'feedback': db.add_user(username, email, password)}), 201


@app.route('/auth/login', methods=['POST'])
# retrieve single user by email
def get_user_by_email():
    password = request.json.get('password', None)
    email = request.json.get('email', None)

    #fill in the fields
    if not password:
        return jsonify({"message": "Fill in password"}), 400
    if not email:
        return jsonify({"message": "Fill in email"}), 400

    parsejson = request.get_json()
    password = parsejson['password']
    email = parsejson['email']

    user_data = db.get_user_by_email(email, password)
    # use tokens to control db access
    try:
        if email == user_data['email']:
            access_token = create_access_token(identity=email)
            return jsonify({'access_token': access_token, 'role_id': user_data['role_id']}), 200
    except TypeError:
        return jsonify({"message": "wrong email or password"})

@app.route('/admin/signup', methods=['POST'])
# create new admin endpoint
def add_new_admin():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    email = request.json.get('email', None)
    confirm_password = request.json.get('confirm-password', None)

    #fill in the fields
    if not username:
        return jsonify({"message": "Fill in username"}), 400
    if not password:
        return jsonify({"message": "Fill in password"}), 400
    if not email:
        return jsonify({"message": "Fill in email"}), 400
    if not confirm_password:
        return jsonify({"message": "Fill in password"}), 400
    if not confirm_password == password:
        return jsonify({"message": "password and confirm-password MUST match"}), 400

    parsejson = request.get_json()
    username = parsejson['username']
    email = parsejson['email']
    password = parsejson['password']
    confirm_password = parsejson['confirm-password']

    if username and email and password and confirm_password:
        return jsonify({'feedback': db.add_admin(username, email, password)}), 201


@app.route('/admin/login', methods=['POST'])
# retrieve single admin by email
def get_admin_by_email():
    password = request.json.get('password', None)
    email = request.json.get('email', None)

    #fill in the fields
    if not password:
        return jsonify({"message": "Fill in password"}), 400
    if not email:
        return jsonify({"message": "Fill in email"}), 400

    parsejson = request.get_json()
    password = parsejson['password']
    email = parsejson['email']

    user_data = db.get_admin_by_email(email, password)
    # use tokens to control db access
    try:
        if email == user_data['email']:
            access_token = create_access_token(identity=email)
            return jsonify({'access_token': access_token, 'role_id': user_data['role_id']}), 200
    except TypeError:
        return jsonify({"message": "wrong email or password"})

@app.route('/auth/account', methods=['PATCH'])
@jwt_required
#update user account
def update_user():
    current_user = get_jwt_identity()
    email = current_user
    regular_data = db.user_access(email)
    #verify and grant access
    if regular_data['role_id'] == 1 or regular_data['role_id'] == 2:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        confirm_password = request.json.get('confirm-password', None)

        #fill in the fields
        if not username:
            return jsonify({"message": "Fill in username"}), 400
        if not password:
            return jsonify({"message": "Fill in password"}), 400
        if not confirm_password:
            return jsonify({"message": "Fill in password"}), 400
        if not confirm_password == password:
            return jsonify({"message": "password and confirm-password MUST match"}), 400

        parsejson = request.get_json()
        username = parsejson['username']
        password = parsejson['password']
        confirm_password = parsejson['confirm-password']

        if username and password and confirm_password:
            return jsonify({'feedback': db.update_user(username, email, password)}), 201

@app.route('/admin/accounts', methods=['GET'])
@jwt_required
# get all users and their details
def get_all_users():
    current_user = get_jwt_identity()
    email = current_user
    admin_user = db.user_access(email)
    #verify and grant access
    if admin_user['role_id'] == 2:
        return jsonify({'users': db.get_all_users()}), 200
    #access denied
    return jsonify({'message': 'Access Denied!'}), 401
