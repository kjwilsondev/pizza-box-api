import uuid
import datetime

from app.main import db
from app.main.model.box import Box

def save_new_box(data):
    box = Box.query.filter_by(public_id=data['public_id']).first()
    if not box:
        new_box = Box(
            id=str(uuid.uuid4()),
            public_id=str(uuid.uuid4()),
            trips=data['trips'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_box)
        return new_box
    else:
        response_object = {
            'status': 'fail',
            'message': 'An error occurred',
        }
        return response_object, 409

def get_all_boxes():
    return Box.query.all()

def get_a_box(public_id):
    return Box.query.filter_by(public_id=public_id).first()

def get_box_driver(public_id):
    box_driver = Box.query.filter_by(public_id=public_id).first()
    return box_driver.driver

def save_changes(data):
    # commits the changes to database
    db.session.add(data)
    db.session.commit()
