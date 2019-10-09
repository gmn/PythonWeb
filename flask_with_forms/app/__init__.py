
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

#
# app
#
app = Flask(__name__)
app.config['SECRET_KEY'] = 'really-long-and-ineffable-password'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    os.getcwd(), 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#
# db
#
db = SQLAlchemy(app)

#
# routes, models
#
from app import routes, models
