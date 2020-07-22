import os
import sys
import logging.config
import pathlib

from werkzeug.routing import BaseConverter

APP_SETTINGS = os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig')
SERVER_RUN_PORT = int(os.environ.get('SERVER_RUN_PORT', '5000'))
SERVER_RUN_HOST = os.environ.get('SERVER_RUN_HOST', 'localhost')
PROTOCOL = 'http'
SERVER_NAME = f'{SERVER_RUN_HOST}:{SERVER_RUN_PORT}'
LOGGER = os.environ.get('APP_LOGGER', 'dev')

HOME = str(os.path.abspath(pathlib.Path(__file__).parent))
if HOME not in sys.path:
    sys.path.append(HOME)

TEMPLATES_FOLDER = 'templates'
STATIC_FOlDER = 'templates/build/static'

# JSON Encoder

# URL CONVERTER
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


# logging
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(LOGGER)
