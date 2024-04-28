from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.train_controller import api as train_ns
from .main.controller.booking_controller import api as booking_ns


blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    blueprint,
    title="Aladdin Server",
    version='1.0',
    description='flask api',
    doc='/doc'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(train_ns,path='/train')
api.add_namespace(train_ns,path='/booking')
