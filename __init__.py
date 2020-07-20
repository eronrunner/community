import os
import sys
import logging.config
import pathlib

APP_SETTINGS = os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig')
DEV_SERVER_NAME = os.environ.get('DEV_SERVER_NAME', 'localhost:5000')
LOGGER = os.environ.get('APP_LOGGER', 'dev')

HOME = str(os.path.abspath(pathlib.Path(__name__).parent))
if HOME not in sys.path:
    sys.path.append(HOME)

# JSON Encoder

# BaseConverter

# logging
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(LOGGER)
