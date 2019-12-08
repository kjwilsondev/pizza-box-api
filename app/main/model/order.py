from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt

class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    grubhub_user = db.Column(db.Integer)
    grubhub_driver = db.Column(db.Integer)
    restaurant = db.Column(db.Integer)
    boxes_given = db.Column(db.Integer)
    boxes_owed = db.Column(db.Integer)

    def __repr__(self):
        return "<Order '{}'>".format(self.id)