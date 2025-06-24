import pytest
from lib.models import User
from extensions import db

"""Tests to see whether user creation works correctly."""
def test_create_user(app):
    with app.app_context():
        user = User(username='Fliss', email='fliss@fliss.com', password='password', role='rehomer')
        db.session.add(user)
        db.session.commit()

        assert user.id is not None
        assert user.username == 'Fliss'
        assert user.email == 'fliss@fliss.com'
        assert user.role == 'rehomer'

"""Tests to see whether user retrieval works correctly."""
def test_get_user(app):
    with app.app_context():
        user = User(username='Fliss', email='fliss@fliss.com', password='password')
        db.session.add(user)
        db.session.commit()

        retrieved = User.query.filter_by(username='Fliss').first()
        assert retrieved is not None
        assert retrieved.id == user.id
        assert retrieved.username == 'Fliss'
        assert retrieved.email == 'fliss@fliss.com'

"""Tests to see whether user deletion works correctly."""
def test_delete_user(app):
    with app.app_context():
        user = User(username='Fliss', email='fliss@fliss.com', password='password')
        db.session.add(user)
        db.session.commit()

        db.session.delete(user)
        db.session.commit()         

        deleted = User.query.filter_by(username='Fliss').first()
        assert deleted is None

"""Tests to see whether user update works correctly."""
def test_update_user(app):
    with app.app_context():
        user = User(username='Fliss', email='fliss@fliss.com', password='password')
        db.session.add(user)
        db.session.commit()

        user.username = 'Alice'
        user.email = 'alice@alice.com'
        db.session.commit()

        updated = User.query.get(user.id)
        assert updated.username == 'Alice'
        assert updated.email == 'alice@alice.com'


"""Tests to see whether user password hashing works correctly."""
def test_user_password_hashing(app):
    with app.app_context():
        user = User(username='Fliss', email='fliss@fliss.com')
        # Set the hashed password using the method defined in the User model   
        user.set_password('securepassword')
        db.session.add(user)
        db.session.commit()

        assert user.password != 'securepassword'  # Ensure the password is hashed
        # Check password re-hashes 'securepassword', compares the new hash with the stored one, returns True if they match
        assert user.check_password('securepassword')  # Check the password against the hash
        assert not user.check_password('wrongpassword')  # Ensure wrong password fails

"""Tests to see whether user authentication works correctly."""

"""Tests to see whether user authorization works correctly."""

"""Tests to see whether user image upload works correctly."""

"""Tests to see whether user profile retrieval works correctly."""

"""Tests to see whether user profile update works correctly."""