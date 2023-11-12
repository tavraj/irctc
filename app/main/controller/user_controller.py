from flask import request
from flask_restx import Resource

from .. import cache
from ..util.dto import UserDto
from ..service.user_service import *
from ..util.decorator import admin_required

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('List of registered users')
    @admin_required()
    @api.marshal_list_with(_user, envelope='data')
    @cache.cached()
    def get(self):
        return get_all_users()

    @api.response(HTTPStatus.CREATED, 'User successfully created')
    @api.doc("create a new user")
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return save_new_user(data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(HTTPStatus.NOT_FOUND, 'User not found')
class User(Resource):
    @api.doc("get a user")
    @api.marshal_with(_user)
    @cache.cached()
    def get(self, public_id):
        user = get_a_user(public_id)
        if user:
            return user
        api.abort(HTTPStatus.NOT_FOUND)
