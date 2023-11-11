from flask import request
from flask_restx import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """

    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        data = request.json
        return Auth.login_user(data)


@api.route('/logout')
class UserLogout(Resource):
    """
        Logout Resource
    """

    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
