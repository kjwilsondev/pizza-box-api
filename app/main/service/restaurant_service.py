import uuid
import datetime

from app.main import db
from app.main.model.restaurant import Restaurant

def save_new_restaurant(restaurant):
    restaurant = Restaurant.query.filter_by(name=data['name']).first()
    if not restaurant:
        new_restaurant = Restaurant(
            public_id=str(uuid.uuid4()),
            name=data['name'],
            num_boxes=data['num_boxes'],
            restaurant_id=data['restaurant_id']
        )

        save_changes(new_restaurant)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered restaurant.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Restaurant already exists.',
        }
        return response_object, 409

def get_a_restaurant(name):
    return Restaurant.query.filter_by(name=name).first()

def get_all_restaurants():
    return Restaurant.query.all()

def save_changes(data):
    # commits the changes to database
    db.session.add(data)
    db.session.commit()