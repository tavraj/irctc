from uuid import uuid4
from http import HTTPStatus
from app.main import db
from app.main.model.train import Train
from app.main.model.booking import Booking

def get_booking_details(booking_id):
    return Booking.query.filter_by(id=booking_id).first()

def book_seat(user_id, train_id):
    train = Train.query.get(train_id)
    if train.max_seats > train.occupied_seats:
        booking = Booking(user_id=user_id, train_id=train_id, booking_status=True)
        db.session.add(booking)
        db.session.commit()
        train.occupied_seats += 1
        db.session.commit()
        return {"message": "Seat booked successfully."}, HTTPStatus.OK
    else:
        return {"message": "No seats available for booking."}, HTTPStatus.BAD_REQUEST