import uuid
import datetime

from app.main import db
from app.main.model.restaurant import Restaurant


def get_all_restaurants():
    return Restaurant.query.all()