#app/api/v1/models/users.py

from datetime import datetime

'''
This module contains api data. Here, data structures are used
to store data in memory
'''

class Users:
    '''This class creates a blueprint for the user object'''
    userId = 0
    
    def __init__(self):
        #list of users
        self.users =[]
        
    def add_user(self, username, email):
        #user create account entries
        self.__class__.userId += 1
        self.username = username
        self.email = email
        self.date_created = str(datetime.now())
        
        #check for similar usernames
        for self.user in self.users:
            if(self.username == self.user["username"]):
                return "User with name {} already exists".format(self.username), 400
                
        #user fields
        self.user = {
            "userId": self.__class__.userId,
            "username": self.username,
            "email": self.email,
            "date_created": self.date_created
        }
        
        #add new user to users list
        self.users.append(self.user)
        return self.user
        
    def get_users(self):
        #return a list of all users
        return self.users

    def get_user_by_id(self, id):
        #get a specific user by userId
        user_by_id = [user for user in self.users if user['userId'] == id]
        return user_by_id
        
    def update_user(self, id, newname, newemail):
        #change user details
        user_to_patch = [user for user in self.users if user['userId'] == id]
        user_to_patch[0]['username'] = newname
        user_to_patch[0]['email'] = newemail
        