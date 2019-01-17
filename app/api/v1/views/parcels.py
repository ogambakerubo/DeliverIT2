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
