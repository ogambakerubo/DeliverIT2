# app/api/v1/models/parcels.py

from datetime import datetime

'''
This module contains api data. Here, data structures are used
to store data in memory
'''


class Parcels:
    '''This class creates a blueprint for the parcel object'''
    # The parcel ID
    parcelId = 0

    def __init__(self):
        # list of parcels
        self.parcels = []
        self.deleted_parcels = []
        self.parcel_status = "pending"

    def add_parcel(self, parcel_name, quantity, pickup_location, drop_location, userId):
        # create parcel entries
        self.__class__.parcelId += 1
        self.parcel_name = parcel_name
        self.quantity = quantity
        self.pickup_location = pickup_location
        self.drop_location = drop_location
        self.userId = userId
        self.date_created = str(datetime.now())

        # parcel fields
        self.parcel = {
            "parcelId": self.__class__.parcelId,
            "parcel_name": self.parcel_name,
            "quantity": self.quantity,
            "pickup_location": self.pickup_location,
            "drop_location": self.drop_location,
            "parcel_status": self.parcel_status,
            "userId": self.userId,
            "date_created": self.date_created
        }

        # add new parcel to parcels list
        self.parcels.append(self.parcel)
        return self.parcel

    def user_parcels(self, userId):
        # return a list of parcels of specific user
        parcels_by_userId = [
            parcel for parcel in self.parcels if parcel['userId'] == userId]
        return parcels_by_userId

    def get_parcels(self):
        # return a list of all parcels
        return self.parcels

    def get_parcel_by_id(self, parcelId):
        # get a specific parcel by parcelId
        parcel_by_id = [
            parcel for parcel in self.parcels if parcel['parcelId'] == parcelId]
        return parcel_by_id

    def update_parcel(self, parcelId, parcel_name, quantity, pickup_location, drop_location):

        # check if parcel status is delivered
        for parcel in self.parcels:
            if(parcel.get("parcel_status") == "delivered"):
                return "Parcel with ID number {} has already been delivered".format(parcelId)

        # change parcel details
        parcel_to_patch = [
            parcel for parcel in self.parcels if parcel['parcelId'] == parcelId]
        parcel_to_patch[0]['parcel_name'] = parcel_name
        parcel_to_patch[0]['quantity'] = quantity
        parcel_to_patch[0]['pickup_location'] = pickup_location
        parcel_to_patch[0]['drop_location'] = drop_location

        date_modified = str(datetime.now())
        parcel_to_patch[0]['date_modified'] = date_modified

        return parcel_to_patch

    def change_status(self, parcelId):
        # change parcel delivery status
        parcel_status_update = [
            parcel for parcel in self.parcels if parcel['parcelId'] == parcelId]
        parcel_status_update[0]['parcel_status'] = "delivered"

        date_delivered = str(datetime.now())
        parcel_status_update[0]['date_delivered'] = date_delivered

        return parcel_status_update

    def cancelled(self):
        # return a list of cancelled orders
        return self.deleted_parcels

    def delete_parcel(self, parcelId):
        # delete a specific parcel by parcelId
        delete_parcel = [
            parcel for parcel in self.parcels if parcel['parcelId'] == parcelId]
        self.deleted_parcels.append(delete_parcel[0])
        self.parcels.remove(delete_parcel[0])
        return "User with id {} deleted".format(parcelId)

