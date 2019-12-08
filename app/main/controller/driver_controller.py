from flask import request
from flask_restplus import Resource

from ..util.dto import DriverDto
from ..util.decorator import token_required, admin_token_required
# from ..service.user_service import save_new_user, get_all_users, get_a_user
from functools import wraps

api = DriverDto.api
_driver = DriverDto.driver