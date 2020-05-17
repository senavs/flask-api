import os
from abc import ABC

PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(PROJECT_DIR)


class ConfigBase(ABC):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'simplest secrete key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(ConfigBase):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(BASE_DIR, 'dev-db.sqlite'))


class TestingConfig(ConfigBase):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(BASE_DIR, 'test-db.sqlite'))


class ProductionConfig(ConfigBase):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
