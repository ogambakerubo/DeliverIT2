# DeliverIT2/app/api/v1/views/parcels.py
from flask import jsonify, request
from app import app

# import parcels.py from models
from ..models import parcels


# instantiate parcel object
parcel = parcels.Parcels()

# create new parcel endpoint


@app.route('/api/v1/parcels', methods=['POST'])
def add_new_parcel():
    parsejson = request.get_json()
    parcel_name = parsejson['parcel_name']
    quantity = parsejson['quantity']
    pickup_location = parsejson['pickup_location']
    drop_location = parsejson['drop_location']
    userId = parsejson['userId']
    return jsonify({'feedback': parcel.add_parcel(parcel_name, int(quantity), pickup_location, drop_location, int(userId))}), 201

# retrieve specific user parcels endpoint


@app.route('/api/v1/users/<int:userId>/parcels', methods=['GET'])
def user_parcels(userId):
    return jsonify({'user parcels': parcel.user_parcels(userId)}), 200

# retrieve all parcels endpoint


@app.route('/api/v1/parcels', methods=['GET'])
def get_parcels():
    return jsonify({'parcels': parcel.get_parcels()}), 200

# retrieve single parcel endpoint


@app.route('/api/v1/parcels/<int:parcelId>', methods=['GET'])
def get_parcel_by_id(parcelId):
    return jsonify({'parcel': parcel.get_parcel_by_id(parcelId)}), 200

