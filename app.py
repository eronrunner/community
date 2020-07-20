from flask import Flask

import FlaskApp

APP = Flask("FlaskApp", instance_relative_config=True)

APP.config.from_object(FlaskApp.APP_SETTINGS)

if __name__ == '__main__':
    APP.run()