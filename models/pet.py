# from ..app import db
from flask_login import UserMixin
from datetime import datetime
from extensions import db


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    breed = db.Column(db.String(50))
    age = db.Column(db.Integer)
    size = db.Column(db.String(20))
    duration = db.Column(db.String(100))  # How long fostering is needed
    image_url = db.Column(db.String(255))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Pet {self.id} {self.name}"
