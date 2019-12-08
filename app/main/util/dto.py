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
        'num_boxes': fields.Integer(description='driver num of boxes')
    })

class RestaurantDto:
    api = Namespace('restaurant', description='restaurant operations')
    restaurant = api.model('restaurant', {
        'name': fields.String(required=True, description='restaurant name'),
        'num_boxes': fields.Integer(description='restaurant num of boxes')
    })

class CleanerDto:
    api = Namespace('cleaner', description='cleaner operations')
    cleaner = api.model('cleaner', {
        'name': fields.String(required=True, description='cleaner name'),
        'num_boxes': fields.Integer(description='cleaner num of boxes')
    })

class OrderDto:
    api = Namespace('order', description='order operations')
    order = api.model('order', {
        'grubhub_user': fields.Integer(required=True, description='grubhub user id'),
        'grubhub_driver': fields.Integer(required=True, description='grubhub driver id'),
        'restaurant': fields.Integer(required=True, description='restaurant id'),
        'boxes_given': fields.Integer(description='number of boxes being given'),
        'boxes_owed': fields.Integer(description='number of boxes user owes')
    })
