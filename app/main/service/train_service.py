from uuid import uuid4
from http import HTTPStatus
from app.main import db
from app.main.model.train import Train
from app.main.model.booking import Booking



def save_new_train(data):
    train = Train.query.filter_by(name=data.get('name')).first()
    if train:
        return {
            'status': 'fail',
            'message': 'Train already exists. Please Log in.'
        }, HTTPStatus.CONFLICT
    train = Train(
        **data,
    )
    save_changes(train)
    return {
        'status': 'success',
        'message': 'Successfully registered.'
    }, HTTPStatus.CREATED


def get_all_trains():
    return Train.query.all()


def get_a_train(id):
    return Train.query.filter_by(id=id).first()


def get_trains_with_available_seats(source, destination):
    return Train.query.filter(Train.source == source, Train.destination == destination, Train.max_seats > Train.occupied_seats).all()



def save_changes(data):
    db.session.add(data)
    db.session.commit()
