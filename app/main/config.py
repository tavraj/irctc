import os
from datetime import timedelta


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'postgresql://om-divine:password@localhost:5432/netra'
    )
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'om-divine')
    # JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=30)
    PROPAGATE_EXCEPTIONS = True
    DEBUG = True


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    JWT_COOKIE_SECURE = True
    # JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)


class TestingConfig(Config):
    pass


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
