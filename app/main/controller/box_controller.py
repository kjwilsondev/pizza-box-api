# CREATE
# create a box

# READ
# get a box
# get all boxes

# UPDATE
# update box location

# DESTROY
# delete a box

from flask import request
from flask_restplus import Resource

from ..util.dto import BoxDto
from ..util.decorator import token_required, admin_token_required
from ..service.box_service import save_new_box, get_all_boxes, get_a_box
from functools import wraps

api = BoxDto.api
_box = BoxDto.box

@api.route('/')
class BoxList(Resource):
    @api.doc('list_of_registered_boxes', security='apiKey')
    @api.marshal_list_with(_box, envelope='data')
    # get all boxes
    def get(self):
        """List all registered boxes"""
        return get_all_boxes()

    @api.doc('create a new box')
    @api.response(201, 'Box successfully created.')
    @api.expect(_user, validate=True)
    # CREATE
    # create a box
    def post(self):
        """Creates a new Box """
        data = request.json
        return save_new_box(data=data)

@api.route('/<public_id>')
@api.param('public_id', 'The Box identifier')
@api.response(404, 'Box not found.')
class Box(Resource):
    # READ
    # get a box
    @api.doc('get a box', security='apiKey')
    @api.marshal_with(_box)
    def get(self, public_id):
        """get a box given its identifier"""
        box = get_a_box(public_id)
        if not box:
            api.abort(404)
        else:
            return box

    # UPDATE
    # update box location
    @api.doc('delete a box', security='apiKey')
    @api.marshal_with(_box)
    def update(self, public_id):
        """get a box given its identifier"""
        box = get_a_box(public_id)
        if not box:
            api.abort(404)
        else:
            db.session.update(box)
            db.session.commit()
            return redirect("/")

    # DESTROY
    # delete a box
    @api.doc('delete a box', security='apiKey')
    @api.marshal_with(_box)
    def delete(self, public_id):
        """get a box given its identifier"""
        box = get_a_box(public_id)
        if not box:
            api.abort(404)
        else:
            db.session.delete(box)
            db.session.commit()
            return redirect("/")
