import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_caching import Cache
from .config import config_by_name

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()
cache = Cache()

# metrics = PrometheusMetrics.for_app_factory()
# if os.environ.get('ENV') == 'production':
#     metrics = UWsgiPrometheusMetrics.for_app_factory()
# metrics.info(name='Aladdin', description='Aladdin API', version='1.0')


def create_app(config_name):
    app = Flask(__name__)
    app_config = config_by_name.get(config_name)
    app.config.from_object(app_config)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cache.init_app(app, config=app_config.CACHE_CONFIG)
    # metrics.init_app(app)
    # metrics.start_http_server(app_config.METRICS_HOST)
    return app
