from flask import request
from flask_restplus import Resource

from ..util.dto import DriverDto
from ..util.decorator import token_required, admin_token_required
from ..service.driver_service import save_new_driver, get_all_drivers, get_a_driver
from functools import wraps

api = DriverDto.api
_driver = DriverDto.driver

@api.route('/')
class DriverList(Resource):
    @api.doc('list_of_registered_drivers', security='apiKey')
    # TODO: @admin_token_required
    @api.marshal_list_with(_driver, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_drivers()

    @api.doc('create a new driver')
    @api.response(201, 'Driver successfully created.')
    @api.expect(_driver, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_driver(data=data)