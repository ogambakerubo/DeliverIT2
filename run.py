# DeliverIT2/run.py
import os
from flask import Flask
from app import app

# webserver accessible to computers in the network
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    