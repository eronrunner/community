from flask import Flask, render_template, url_for
from werkzeug.utils import redirect

import __init__
from blueprints.Post import POST

APP = Flask("COMMUNITY",
            instance_relative_config=True,
            template_folder=__init__.TEMPLATES_FOLDER,
            static_folder=__init__.STATIC_FOlDER,)

APP.config.from_object(__init__.APP_SETTINGS)
APP.url_map.converters['regex'] = __init__.RegexConverter

APP.register_blueprint(POST, url_prefix='/api/post')

@APP.route('/', methods=['GET'])
def index():
    return render_template('build/index.html')

@APP.route('/<regex(".*"):uid>', methods=['GET'])
def re(uid):
    return redirect(url_for('index'))

if __name__ == '__main__':
    if __init__.APP_SETTINGS == 'config.DevelopmentConfig':
        APP.run()
    elif __init__.APP_SETTINGS == 'config.ProductionConfig':
        from waitress import serve
        serve(APP, host=__init__.SERVER_RUN_HOST, port=__init__.SERVER_RUN_PORT)