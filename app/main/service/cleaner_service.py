import uuid
import datetime

from app.main import db
from app.main.model.cleaner import Cleaner

def get_all_cleaners():
    return Cleaner.query.all()

def save_changes(data):
    # commits the changes to database
    db.session.add(data)
    db.session.commit()