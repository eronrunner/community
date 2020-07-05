from mongoengine import DoesNotExist

from model import User
from object_management import Manager
from mongo_connection import get_collection, client

class UserManager(Manager):
  COLLECTION = "user"

  @staticmethod
  def create(linked_id: str):
    coll = get_collection(UserManager.COLLECTION)
    user =  coll.find_one({"_user_linked_id": linked_id})
    if user:
      raise Exception(f"${linked_id} is exist")
    n_user = User(_user_linked_id=linked_id)
    n_user.save()
    return n_user

  @staticmethod
  def get(_id: str):
    try:
      obj = User.objects.get(_id=_id)
      return obj
    except DoesNotExist as ex:
      print(ex)
      return None

  @staticmethod
  def list(self, page_size, num_page):
    pass

  @staticmethod
  def delete(linked_id: str):
    coll = get_collection(UserManager.COLLECTION)
    return coll.find_one_and_delete({"_user_linked_id": linked_id})
