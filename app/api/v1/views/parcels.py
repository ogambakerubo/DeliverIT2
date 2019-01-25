# DeliverIT2/app/api/v1/views/parcels.py
from flask import jsonify, request
from app import app

# import parcels.py from models
from ..models import parcels


# instantiate parcel object
parcel = parcels.Parcels()


@app.route('/api/v1/parcels', methods=['POST'])
def add_new_parcel():
    # create new parcel endpoint
    parsejson = request.get_json()
    parcel_name = parsejson['parcel_name']
    quantity = parsejson['quantity']
    pickup_location = parsejson['pickup_location']
    drop_location = parsejson['drop_location']
    userId = parsejson['userId']

    return jsonify({'feedback': parcel.add_parcel(parcel_name, int(quantity), pickup_location, drop_location, int(userId))}), 201


@app.route('/api/v1/users/<int:userId>/parcels', methods=['GET'])
def user_parcels(userId):
    # retrieve specific user parcels endpoint
    return jsonify({'user parcels': parcel.user_parcels(userId)}), 200


@app.route('/api/v1/parcels', methods=['GET'])
def get_parcels():
    # retrieve all parcels endpoint
    return jsonify({'parcels': parcel.get_parcels()}), 200


@app.route('/api/v1/parcels/<int:parcelId>', methods=['GET'])
def get_parcel_by_id(parcelId):
    # retrieve single parcel endpoint
    return jsonify({'parcel': parcel.get_parcel_by_id(parcelId)}), 200


@app.route('/api/v1/parcels/<int:parcelId>', methods=['PATCH'])
def update_parcel(parcelId):
    # change parcel details endpoint
    parsejson = request.get_json()
    parcel_name = parsejson['parcel_name']
    quantity = parsejson['quantity']
    pickup_location = parsejson['pickup_location']
    drop_location = parsejson['drop_location']

    return jsonify({'Updated parcel': parcel.update_parcel(parcelId, parcel_name, int(quantity), pickup_location, drop_location)}), 201


@app.route('/api/v1/parcels/<int:parcelId>/status-update', methods=['PATCH'])
def change_status(parcelId):
    # change parcel delivery status endpoint
    return jsonify({'Status updated': parcel.change_status(parcelId)}), 201


@app.route('/api/v1/cancelled-parcels', methods=['GET'])
def cancelled():
    # retrieve all cancelled updates
    return jsonify({'Cancelled parcels': parcel.cancelled()}), 200


@app.route('/api/v1/parcels/<int:parcelId>/cancel', methods=['PUT'])
def cancel_parcel(parcelId):
    # cancel parcel order endpoint
    return jsonify({'message': parcel.delete_parcel(parcelId)}), 200

