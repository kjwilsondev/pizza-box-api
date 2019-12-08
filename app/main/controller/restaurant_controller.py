from flask import request
from flask_restplus import Resource

from ..util.dto import RestaurantDto
from ..util.decorator import token_required, admin_token_required
from ..service.restaurant_service import save_new_restaurant, get_all_restaurants, get_a_restaurant
from functools import wraps

api = RestaurantDto.api
_restaurant = RestaurantDto.restaurant

@api.route('/')
class RestaurantList(Resource):
    @api.doc('list_of_registered_restaurants', security='apiKey')
    # TODO: @admin_token_required
    @api.marshal_list_with(_restaurant, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_restaurants()

    @api.doc('create a new restaurant')
    @api.response(201, 'Restaurant successfully created.')
    @api.expect(_restaurant, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_restaurant(data=data)