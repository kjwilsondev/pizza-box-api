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
        # TODO: plaid token
        # TODO: phone numbers for texting updates
    })

class BoxDto:
    api = Namespace('box', description='box operations')
    box = api.model('box', {
        'id': fields.String(required=True, description='box ids'),
        'registered_on': fields.String(required=True, description='registration'),
        'trips': fields.String(required=False, description='trips'),
        'public_id': fields.String(required=True, description='public id')
    })
