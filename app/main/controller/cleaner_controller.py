from flask import request
from flask_restplus import Resource

from ..util.dto import CleanerDto
from ..util.decorator import token_required, admin_token_required
from ..service.cleaner_service import save_new_cleaner, get_all_cleaners, get_a_cleaner
from functools import wraps

api = CleanerDto.api
_cleaner = CleanerDto.cleaner

@api.route('/')
class CleanerList(Resource):
    @api.doc('list_of_registered_cleaners', security='apiKey')
    # TODO: @admin_token_required
    @api.marshal_list_with(_cleaner, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_cleaners()

    @api.doc('create a new cleaner')
    @api.response(201, 'Cleaner successfully created.')
    @api.expect(_cleaner, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_cleaner(data=data)