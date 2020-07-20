import os
import FlaskApp

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False
    SECRET_KEY = 'secret'
    # To use SQL DB, SQLAlchemy_DATABASE_URI = os.eviron['DATABASE_URI']

class ProductionConfig(Config):
    DEBUG = False

class StageConfig(Config):
    DEBUG = True
    TESTING = True

class DevelopmentConfig(Config):
    DEBUG = True
    SERVER_NAME = FlaskApp.DEV_SERVER_NAME
    # DB_SERVER = '127.0.0.1'

class TestingConfig(Config):
    TESTING = True