from flask_restplus import Namespace, fields

class AuthDto:
    api = Namespace('auth', description='authentication operations')
    user_auth = api.model('auth', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
    
class UserDto:
    api = Namespace('user', description='user operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

class DriverDto:
    api = Namespace('driver', description='driver operations')
    driver = api.model('driver', {
        'email': fields.String(required=True, description='driver email address'),
        'username': fields.String(required=True, description='driver username'),
        'password': fields.String(required=True, description='driver password'),
        'public_id': fields.String(description='driver Identifier'),
        'destination': fields.String(description='driver destination'),
        'num_boxes': fields.Integer(description='driver num of boxes')
    })
