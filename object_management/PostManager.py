from object_management import Manager
from mongo_connection import get_collection

class PostManager(Manager):

  COLLECTION = "post"

  def create(self, title: str, author_id: str, content: str):
    pass

  def get(self, _id):
    pass

  def list(self, page_size, page_num):
    coll = get_collection(self.COLLECTION)
    cursor = coll.find().skip(page_size * (page_num - 1)).limit(page_size)
    return list(cursor)