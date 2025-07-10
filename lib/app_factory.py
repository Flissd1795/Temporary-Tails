# lib/app_factory.py
from flask import Flask
from extensions import db, login_manager
from config import Config
from lib.models import *  # just to register all models
# from lib.routes import bp  # your blueprint(s)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app
