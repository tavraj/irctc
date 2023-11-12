import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from prometheus_flask_exporter.multiprocess import PrometheusMetrics, UWsgiPrometheusMetrics
from .config import config_by_name

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

metrics = PrometheusMetrics.for_app_factory()
if os.environ.get('ENV') == 'production':
    metrics = UWsgiPrometheusMetrics.for_app_factory()
metrics.info(name='Pikachu', description='by om divine', version='1.0')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name.get(config_name))
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    metrics.init_app(app)
    metrics.start_http_server(9100)
    return app
