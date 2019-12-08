import uuid
import datetime

from app.main import db
from app.main.model.order import Order


def get_all_orders():
    return Order.query.all()