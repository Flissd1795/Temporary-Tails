from app import db
from flask_login import UserMixin
from datetime import datetime
from extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20))  # "rehomer" or "fosterer"
    pets = db.relationship('Pet', backref='owner')
    image_url = db.Column(db.String(255))

    def __repr__(self):
        return f"<User {self.id} {self.username}>"
