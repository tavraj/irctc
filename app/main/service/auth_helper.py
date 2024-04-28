import traceback
from http import HTTPStatus
from app.main.model.user import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity

class Auth:

    @staticmethod
    def login_user(data):
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = create_access_token(
                    identity=user.id,
                    additional_claims={"is_administrator": user.admin}
                )
                if auth_token:
                    return {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'access_token': auth_token
                    }, HTTPStatus.OK
                return {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }, HTTPStatus.UNAUTHORIZED
        except Exception:
            traceback.print_exc()
            return {
                'status': 'fail',
                'message': 'Try again'
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    @staticmethod
    def logout_user(data):
        return {
            'status': 'unimplemented',
            'header': data
        }, HTTPStatus.BAD_GATEWAY
    
    def get_current_user_id():
    # Extract user ID from JWT token
        user_id = get_jwt_identity()
        return user_id
