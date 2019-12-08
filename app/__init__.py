# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.auth_controller import api as auth_ns

from .main.controller.user_controller import api as user_ns
from .main.controller.driver_controller import api as driver_ns
from .main.controller.order_controller import api as order_ns
from .main.controller.restaurant_controller import api as restaurant_ns
from .main.controller.cleaner_controller import api as cleaner_ns

blueprint = Blueprint('api', __name__)

# TODO: Authorizations
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

api = Api(blueprint,
          title='Pizza Box Backend',
          version='1.0',
          authorizations=authorizations,
          description='the resuable pizza box api'
          )

api.add_namespace(auth_ns)
api.add_namespace(user_ns, path='/user')
api.add_namespace(driver_ns, path='/driver')
api.add_namespace(order_ns, path='/order')
api.add_namespace(restaurant_ns, path='/restaurant')
api.add_namespace(cleaner_ns, path='/cleaner')