from flask import request
from flask_restx import Resource

from .. import cache
from ..util.dto import TrainDto
from ..service.train_service import *
from ..util.decorator import admin_required


api = TrainDto.api
_train = TrainDto.train


@api.route('/')
class TrainList(Resource):
    @api.doc('List of registered trains')
    @api.marshal_list_with(_train, envelope='data')
    @cache.cached()
    def get(self):
        return get_all_trains()

    @api.response(HTTPStatus.CREATED, 'train successfully created')
    @api.doc("create a new user")
    @admin_required()
    @api.expect(_train, validate=True)
    def post(self):
        data = request.json
        return save_new_train(data)


@api.route('/<id>')
@api.param('id', 'The User identifier')
@api.response(HTTPStatus.NOT_FOUND, 'User not found')
class User(Resource):
    @api.doc("get a user")
    @api.marshal_with(_train)
    @cache.cached()
    def get(self, id):
        train = get_a_train(id)
        if train:
            return train
        api.abort(HTTPStatus.NOT_FOUND)


@api.route('/availability')
@api.doc(params={'source': 'Source station', 'destination': 'Destination station'})
class TrainAvailability(Resource):
    @api.doc('Get available trains between source and destination')
    def get(self):
        source = api.payload['source']
        destination = api.payload['destination']
        trains = get_trains_with_available_seats(source, destination)
        return trains
    

