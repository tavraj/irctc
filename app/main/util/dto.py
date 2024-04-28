from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The user email address'),
        'password': fields.String(required=True, description='The user password')
    })

class TrainDto:
    api = Namespace('train', description='authentication related operations')
    train = api.model('train', {
        'name': fields.String(required=True, description='user email address'),
        'source': fields.String(required=True, description='user username'),
        'destination': fields.String(required=True, description='user password'),
    })

class BookingDto:
    api = Namespace('booking', description='Booking related operations')
    
    booking = api.model('booking', {
        'id': fields.Integer(required=True, description='Booking ID'),
        'user_id': fields.Integer(required=True, description='User ID'),
        'train_id': fields.Integer(required=True, description='Train ID'),
        'booking_status': fields.Boolean(required=True, description='Booking Status'),
    })