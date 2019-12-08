from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt

class Cleaner(db.Model):
    __tablename__ = "cleaner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    num_boxes = db.Column(db.Integer) # num boxes currently on cleaner

    def __repr__(self):
        return "<Cleaner '{}'>".format(self.id)