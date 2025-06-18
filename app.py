from flask import Flask
from extensions import db
from config import Config 
from models import *

# Initialise flask and config
def create_app():
    app = Flask(__name__ )
    app.config.from_object(Config)
    db.init_app(app) # registers the app with SQLAlchemy

# Create all database tables if they don't exist yet 
    with app.app_context():
        db.create_all()
        print("tables created")
    
    return app

app = create_app()

# Example route
@app.route("/")
def home():
    return "App is running"

if __name__ == "__main__":
    app.run(debug=True)