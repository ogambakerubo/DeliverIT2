#DeliverIT2/app/__init__.py
from flask import Flask

#instantiate app object
app = Flask(__name__)

#import parcels.py from views
from app.api.v1.views import parcels

