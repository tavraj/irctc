from flask_restx import Resource
from ..util.dto import BookingDto
from ..service.booking_service import *
from ..service.auth_helper import get_current_user_id 

api = BookingDto.api

@api.route('/booking/<int:booking_id>')
class BookingDetail(Resource):
    @api.doc('Get specific booking details')
    def get(self, booking_id):
        booking = get_booking_details(booking_id)
        return booking
    
@api.route('/book/<int:train_id>')
class BookSeat(Resource):
    @api.doc('Book a seat on a particular train')
    def post(self, train_id):
        user_id = get_current_user_id()  
        return book_seat(user_id, train_id)