from flask import Flask
from extensions import db
from config import Config 
from lib.models import *
from lib.app_factory import create_app

app = create_app()

# Example route
@app.route("/")
def home():
    return "App is running"

if __name__ == "__main__":
    app.run(debug=True)