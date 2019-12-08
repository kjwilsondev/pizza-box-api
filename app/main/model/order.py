from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt

class Order(db.Model):
    __tablename__ = "order"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    grubhub_user = db.Column(db.Integer, unique=True, nullable=False)
    grubhub_driver = db.Column(db.Integer, unique=True, nullable=False)
    restaurant_id = db.Column(db.Integer)
    boxes_given = db.Column(db.Integer)
    boxes_owed = db.Column(db.Integer)

    def __repr__(self):
        return "<Order '{}'>".format(self.id)