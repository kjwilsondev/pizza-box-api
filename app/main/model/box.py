from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt

# Box class inherits from db.Model class which declares the class as a model for sqlalchemy
class Box(db.Model):
    """ Box Model for storing box related details """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    trips = db.Column(db.Integer) # number of trips box has made
    # TODO: Chain Restaurant = String
    # TODO: Number of Trips = Integer
    # TODO: Recent Users = array(queue) of last 5 users
    # TODO: Material (assuming there are many types of boxes): String
    public_id = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return "<Box '{}'>".format(self.id)
