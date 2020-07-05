from bson import ObjectId
from mongoengine import DoesNotExist
from pymongo import WriteConcern
from datetime import datetime
from model import Post
from object_management import Manager
from mongo_connection import get_collection, client
from external import externalapi

class PostManager(Manager):

  COLLECTION = "post"
  DRIVE = externalapi.get_drive()

  @staticmethod
  def create(title: str, author_id: str, content: str, content_type: str):
    with client.start_session() as session:
      try:
        with session.start_transaction():
          content_file = PostManager.DRIVE.CreateFile({'title': f"{title}_{datetime.utcnow().timestamp()}.{content_type}"})
          content_file.SetContentString(content)
          content_file.Upload()
          n_post = Post(title=title, author=author_id, file_id=content_file['id'])
          return n_post.save()
      except Exception as ex:
        print(ex)

  @staticmethod
  def get(_id: str):
    try:
      post = Post.objects.get(_id=_id)
      return post
    except DoesNotExist as ex:
      print(ex)
      return None

  @staticmethod
  def list(page_size, page_num):
    coll = get_collection(PostManager.COLLECTION)
    cursor = coll.find().skip(page_size * (page_num - 1)).limit(page_size)
    return list(cursor)

  @staticmethod
  def delete(_id: str):
    coll = get_collection(PostManager.COLLECTION)
    return coll.find_one_and_delete({"_id": _id})
