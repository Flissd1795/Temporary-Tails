import pytest
from lib.app_factory import create_app
from extensions import db
# Reusable pieces of setup to pluf into any test
@pytest.fixture
# Creates app fixture
def app():
    # Creates fresh Flask app instance using create_app() function
    app = create_app()
    app.config.update({
        "TESTING": True, # so Flask knows we're using it for tests
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:", # in-memory DB (don't touch real data)
        "WTF_CSRF_ENABLED": False
    })

    with app.app_context():
        db.create_all() # creates all tables for testing
        yield app # gives tests access to this app - pauses here to run tests with app
        db.session.remove() # cleans up after tests
        db.drop_all() # clean up after tests

@pytest.fixture
# gives a test client 
def client(app):
    return app.test_client()