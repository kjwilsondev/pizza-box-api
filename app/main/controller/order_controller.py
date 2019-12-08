from flask import request
from flask_restplus import Resource

from ..util.dto import OrderDto
from ..util.decorator import token_required, admin_token_required
from ..service.order_service import save_new_order, get_all_orders, get_a_order
from functools import wraps

api = OrderDto.api
_order = OrderDto.order

@api.route('/')
class OrderList(Resource):
    @api.doc('list_of_registered_orders', security='apiKey')
    # TODO: @admin_token_required
    @api.marshal_list_with(_order, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_orders()

    @api.doc('create a new order')
    @api.response(201, 'Order successfully created.')
    @api.expect(_order, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_order(data=data)