import os

class Config:
    # Used to sign session cookies and protect form submissions
    SECRET_KEY = os.environ.get("SECRET_KEY", "devkey")
    # This tells SQLAlchemy to create file 'temporary_tails.db' in project root
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///temporary_tails.db"
    )
    # Disables feature we don't need - avoids unnecessary memory usage
    SQLALCHEMY_TRACK_MODIFICATIONS = False
