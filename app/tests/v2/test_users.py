#DeliverIT2/app/tests/v2/test_users.py
"""
Test the v2 users with pytest
"""
import datetime
import json
import unittest

#local imports
from app import app

class UserTestCase(unittest.TestCase):
    """
    This class represents the Users test cases
    """
    def setUp(self):
        self.app = app.test_client()
        #self.client = 

        # create roles
        self.regular_role = {
            "role_name": "regular"
        }

        self.admin_role = {
            "role_name": "admin"
        }

        # create account
        self.admin = {
            "username": "TestAdmin",
            "email": "testadmin@gmail.com",
            "password": "123Admin",
            "confirm-password": "123Admin"
        }

        self.regular = {
            "username": "TestRegular",
            "email": "testregular@gmail.com",
            "password": "123Regular",
            "confirm-password": "123Regular"
        }
    
    #def test_roles():
        