from bson import ObjectId
from pymongo import WriteConcern
from datetime import datetime
from model import Post
from object_management import Manager
from mongo_connection import get_collection, client
from external import externalapi

class PostManager(Manager):

  COLLECTION = "post"
  DRIVE = externalapi.get_drive()

  def create(self, title: str, author_id: str, content: str, content_type: str):
    with client.start_session() as session:
      try:
        with session.start_transaction():
          content_file = self.DRIVE.CreateFile({'title': f"{title}_{datetime.utcnow().timestamp()}.{content_type}"})
          content_file.SetContentString(content)
          content_file.Upload()
          n_post = Post(title=title, author=author_id, file_id=content_file['id'])
          return n_post.save()
      except Exception as ex:
        print(ex)


  def get(self, _id):
    pass

  def list(self, page_size, page_num):
    coll = get_collection(self.COLLECTION)
    cursor = coll.find().skip(page_size * (page_num - 1)).limit(page_size)
    return list(cursor)

  def delete(self, _id: str):
    coll = get_collection(self.COLLECTION)
    coll.delete_one({"_id": _id})