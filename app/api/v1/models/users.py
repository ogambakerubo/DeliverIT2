# app/api/v1/models/users.py
from datetime import datetime

'''
This module contains api data. Here, data structures are used
to store data in memory
'''


class Users:
    '''This class creates a blueprint for the user object'''
    # The user ID
    userId = 0

    def __init__(self):
        # list of users
        self.users = []
        # list of unsubscribed users
        self.unsub = []

    def add_user(self, username, email):
        # user create account entries
        self.__class__.userId += 1
        self.username = username
        self.email = email
        self.date_created = str(datetime.now())

        # check for similar usernames
        for user in self.users:
            if(user["username"] == self.username):
                return "User with name {} already exists".format(self.username)

        # user fields
        self.user = {
            "userId": self.__class__.userId,
            "username": self.username,
            "email": self.email,
            "date_created": self.date_created
        }

        # add new user to users list
        self.users.append(self.user)
        return self.user

    def get_users(self):
        # return a list of all users
        return self.users

    def get_user_by_id(self, userId):
        # get a specific user by userId
        user_by_id = [user for user in self.users if user['userId'] == userId]
        return user_by_id

    def update_user(self, userId, newname, newemail):
        # change user details
        user_to_patch = [
            user for user in self.users if user['userId'] == userId]
        user_to_patch[0]['username'] = newname
        user_to_patch[0]['email'] = newemail
        # insert date_modified key
        date_modified = str(datetime.now())
        user_to_patch[0]['date_modified'] = date_modified

        return user_to_patch

    def delete_user(self, userId):
        # delete a specific user by userId
        delete_user = [user for user in self.users if user['userId'] == userId]
        self.unsub.append(delete_user[0])
        self.users.remove(delete_user[0])
        return "User with id {} deleted".format(userId)
