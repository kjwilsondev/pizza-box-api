import uuid
import datetime

from app.main import db
from app.main.model.order import Order

def save_new_order(order):
    order = Order.query.filter_by(id=data['grubhub_user']).first()
    if not order:
        new_order = Order(
            public_id=str(uuid.uuid4()),
            grubhub_user=data['grubhub_user'],
            grubhub_driver=data['grubhub_driver'],
            restaurant_id=data['restaurant_id'],
            boxes_given=data['boxes_given'],
            boxes_owed=data['boxes_owed'],
            registered_on=datetime.datetime.utcnow()
        )

        save_changes(new_order)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Order already exists.',
        }
        return response_object, 409

def get_all_orders():
    return Order.query.all()

def get_an_order(public_id):
    return Order.query.filter_by(public_id=public_id).first()