from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt

class Restaurant(db.Model):
    __tablename__ = "restaurant"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    num_boxes = db.Column(db.Integer) # num boxes currently on restaurant

    def __repr__(self):
        return "<Restaurant '{}'>".format(self.id)