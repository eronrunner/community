import os
import __init__

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False
    SECRET_KEY = 'secret'
    SERVER_NAME = __init__.SERVER_NAME
    # To use SQL DB, SQLAlchemy_DATABASE_URI = os.eviron['DATABASE_URI']

class ProductionConfig(Config):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'prod'

class StageConfig(Config):
    DEBUG = True
    TESTING = True

class DevelopmentConfig(Config):
    DEBUG = False
    SECRET_KEY = 'dev'
    # DB_SERVER = '127.0.0.1'

class TestingConfig(Config):
    TESTING = True