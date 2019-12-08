import uuid
import datetime

from app.main import db
from app.main.model.driver import Driver


def save_new_driver(data):
    driver = Driver.query.filter_by(email=data['email']).first()
    if not driver:
        new_driver = Driver(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_driver)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Driver already exists. Please Log in.',
        }
        return response_object, 409


def get_all_drivers():
    return Driver.query.all()


def get_a_driver(public_id):
    return Driver.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()