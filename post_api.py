from flask import request
from flask.blueprints import Blueprint

from object_management.PostManager import PostManager

POST_API = Blueprint(name='POST_API', template_folder='template')

@POST_API.route('/posts/<string:id>', methods=['GET'])
def get_post(_id):
  data = request.get_json()
  post = PostManager.get(_id)
  return post