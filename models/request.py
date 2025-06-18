# from ..app import db
# from flask_login import UserMixin
from datetime import datetime
from extensions import db


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requester_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    requester = db.relationship('User', backref='requests')
    pet = db.relationship('Pet', backref='requests')
