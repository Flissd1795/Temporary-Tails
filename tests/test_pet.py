from lib.models import Pet
from lib.models import User
from extensions import db

"""Tests to see whether pet creation works correctly."""
def test_create_pet(app):
    with app.app_context():
        pet = Pet(name='Buddy', breed='Labrador', age=3, size='Large', duration='2 months', image_url='http://example.com/buddy.jpg')
        db.session.add(pet)
        db.session.commit()

        assert pet.id is not None
        assert pet.name == 'Buddy'
        assert pet.breed == 'Labrador'
        assert pet.age == 3
        assert pet.size == 'Large'
        assert pet.duration == '2 months'
        assert pet.image_url == 'http://example.com/buddy.jpg'

"""Tests to see whether pet retrieval works correctly."""
def test_get_pet(app):
    with app.app_context():
        pet = Pet(name='Buddy', breed='Labrador', age=3, size='Large', duration='2 months', image_url='http://example.com/buddy.jpg')
        db.session.add(pet)
        db.session.commit()

        retrieved = Pet.query.filter_by(name='Buddy').first()
        assert retrieved is not None
        assert retrieved.id == pet.id
        assert retrieved.name == 'Buddy'
        assert retrieved.breed == 'Labrador'
        assert retrieved.age == 3
        assert retrieved.size == 'Large'
        assert retrieved.duration == '2 months'
        assert retrieved.image_url == 'http://example.com/buddy.jpg'

"""Tests to see whether pet deletion works correctly."""
def test_delete_pet(app):
    with app.app_context():
        pet = Pet(name='Buddy', breed='Labrador', age=3, size='Large', duration='2 months', image_url='http://example.com/buddy.jpg')
        db.session.add(pet)
        db.session.commit()

        db.session.delete(pet)
        db.session.commit()         

        deleted = Pet.query.filter_by(name='Buddy').first()
        assert deleted is None


"""Tests to see whether pet update works correctly."""
def test_update_pet(app):
    with app.app_context():
        pet = Pet(name='Buddy', breed='Labrador', age=3, size='Large', duration='2 months', image_url='http://example.com/buddy.jpg')
        db.session.add(pet)
        db.session.commit()

        pet.name = 'Max'
        pet.breed = 'Golden Retriever'
        pet.age = 4
        pet.size = 'Medium'
        pet.duration = '1 month'
        pet.image_url = 'http://example.com/max.jpg'
        db.session.commit()

        updated = Pet.query.get(pet.id)
        assert updated.name == 'Max'
        assert updated.breed == 'Golden Retriever'
        assert updated.age == 4
        assert updated.size == 'Medium'
        assert updated.duration == '1 month'
        assert updated.image_url == 'http://example.com/max.jpg'

"""Tests to see whether pet representation works correctly."""
def test_pet_repr(app):
    with app.app_context():
        pet = Pet(name='Buddy', breed='Labrador', age=3, size='Large', duration='2 months', image_url='http://example.com/buddy.jpg')
        db.session.add(pet)
        db.session.commit()

        assert repr(pet) == f"<Pet {pet.id} {pet.name}>"

"""Tests to see whether pet owner relationship works correctly."""
def test_pet_owner_relationship(app):
    with app.app_context():
        # Create a user
        user = User(username='Fliss', email='fliss@fliss.com', password='password')
        db.session.add(user)
        db.session.commit()
        # Create a pet and assign the user as the owner
        pet = Pet(name='Buddy', breed='Labrador', age=3, size='Large', duration='2 months', image_url='http://example.com/buddy.jpg', owner_id=user.id)
        db.session.add(pet)
        db.session.commit() 
        # Check the relationship
        assert pet.owner is not None
        assert pet.owner.id == user.id
        assert pet.owner.username == 'Fliss'    
