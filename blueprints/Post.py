from flask import request, make_response, jsonify, Blueprint
import __init__

templates = '/'.join([__init__.HOME, 'templates'])
POST = Blueprint(__file__, __name__,
                    template_folder=templates,
                    static_folder='static',
                    url_prefix='/api/post')


@POST.route('/', methods=['POST'])
def create():
    data = request.get_json()
    return make_response(jsonify({"content": "create_post"}), 200)

@POST.route('/', methods=['DELETE'])
def remove():
    data = request.get_json()
    return make_response(jsonify({"content": "remove_post"}), 200)

@POST.route('/<string:_id>', methods=['GET'])
def get(_id):
    data = request.get_json()
    return make_response(jsonify(content="get_post"), 200)

