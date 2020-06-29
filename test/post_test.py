import unittest

from model import User, Post
from mongo_connection import get_collection
from object_management.PostManager import PostManager
from utils import gen_uuid

if __name__ == '__main__':
  import mongo_connection
  author = User.objects.get(_user_linked_id="nphatdat@gmail.com")
  print(author)
  manager = PostManager()
  n_post = manager.create(title="TTTTT", author_id=author, content="json content", content_type="json")
  print(n_post.to_json())
  # manager.delete(n_post._id)
  # print(gen_uuid())