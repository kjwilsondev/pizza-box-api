import uuid
import datetime

from app.main import db
from app.main.model.box import Box

def save_new_box(data):
    box = Box.query.filter_by(email=data['email']).first()
    if not box:
        new_box = Box(
            id=str(uuid.uuid4()),
            public_id=str(uuid.uuid4()),
            trips=data['trips'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_box)
        return generate_token(new_box)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Box already exists. Please Log in.',
        }
        return response_object, 409

def generate_token(box):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(box.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

def get_all_boxes():
    return Box.query.all()

def get_a_box(public_id):
    return Box.query.filter_by(public_id=public_id).first()

def save_changes(data):
    # commits the changes to database
    db.session.add(data)
    db.session.commit()
