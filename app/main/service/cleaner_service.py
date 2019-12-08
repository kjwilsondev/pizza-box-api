import uuid
import datetime

from app.main import db
from app.main.model.cleaner import Cleaner


def get_all_orders():
    return Cleaner.query.all()