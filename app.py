from flask import Flask

import __init__
from blueprints.Post import POST

APP = Flask("COMMUNITY", instance_relative_config=True)

APP.config.from_object(__init__.APP_SETTINGS)

APP.register_blueprint(POST)

if __name__ == '__main__':
        APP.run()
        # from waitress import serve
        # serve(APP, host='0.0.0.0', port=5000)