#DeliverIT2/app/__init__.py
from flask import Flask

#instantiate app object
app = Flask(__name__)

#import parcels.py and users.py from views

from app.api.v2.views import users


