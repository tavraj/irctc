from uuid import uuid4
from http import HTTPStatus
from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data.get('email')).first()
    if user:
        return {
            'status': 'fail',
            'message': 'User already exists. Please Log in.'
        }, HTTPStatus.CONFLICT
    user = User(
        **data,
        public_id=uuid4().__str__()
    )
    save_changes(user)
    return {
        'status': 'success',
        'message': 'Successfully registered.'
    }, HTTPStatus.CREATED


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
