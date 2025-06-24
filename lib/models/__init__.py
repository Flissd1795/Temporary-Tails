from extensions import db
from flask_sqlalchemy import SQLAlchemy #SQLalchemy used as ORM (Object Relational Mapper) to talk to PostgreSQL

# Importing all the models
from .user import User
from .pet import Pet
from .request import Request
from .notification import Notification
