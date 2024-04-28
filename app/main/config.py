import os
from datetime import timedelta


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'postgresql://ash:pokemon@localhost:5432/aladdin'
    )
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'ash')
    # JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=300)
    PROPAGATE_EXCEPTIONS = True
    METRICS_HOST = 9100
    CACHE_CONFIG = {
        'CACHE_DEFAULT_TIMEOUT': 300,
        'CACHE_TYPE': 'SimpleCache',
        'DEBUG': True
    }


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    JWT_COOKIE_SECURE = True
    # JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)


class TestingConfig(Config):
    TESTING = True


config_by_name = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
    testing=TestingConfig,
)
