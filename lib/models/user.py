from flask_login import UserMixin
from datetime import datetime
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash   


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

    # Hash password - password is raw password typed by user
    def set_password(self, plain_password):
        # Generate_password_hash is a function from werkzeug.security that hashes the password
        # The resulting hash gets stored in password column of database
        self.password = generate_password_hash(plain_password)

    def check_password(self, plain_password):
        # Check_password_hash is a function from werkzeug.security that checks the password
        # The resulting hash gets compared with the password column of database
        return check_password_hash(self.password, plain_password)