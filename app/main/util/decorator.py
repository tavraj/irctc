from http import HTTPStatus
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt


def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get('is_administrator', False):
                return fn(*args, **kwargs)
            return dict(
                message="admins only!"
            ), HTTPStatus.UNAUTHORIZED

        return decorator

    return wrapper
