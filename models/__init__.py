from flask import Flask
from extensions import db
from flask_sqlalchemy import SQLAlchemy #SQLalchemy used as ORM (Object Relational Mapper) to talk to PostgreSQL
from flask_login import LoginManager #library to handle user login/logout and session managemenent

# Instances of SQLAlchemy and LoginManager
# Created outside app function so they can be reused anywhere (models, routes etc.)
db = SQLAlchemy()
login_manager = LoginManager()

# Importing all the models
from .user import User
from .pet import Pet
from .request import Request
from .notification import Notification

# Defining function that returns new Flask app
def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialises SQLAlchemy with Flask app so it knows how to connect to db
    db.init_app(app)
    # Tells Flask-Login to work with this app
    login_manager.init_app(app)

    # Imports routes.py where I'll define web routes
    # Registers it as a blueprint - Flask way of organising routes so codebase is cleaned
    from . import routes
    app.register_blueprint(routes.bp)

    # Returns fully configured Flask app object, ready to run and test
    return app 