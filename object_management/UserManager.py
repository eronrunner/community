from model import User
from object_management import Manager
from mongo_connection import get_collection, client

class UserManager(Manager):
  COLLECTION = "user"

  def create(self, linked_id: str):
    coll = get_collection(self.COLLECTION)
    users = coll.find({})
    print(list(users) if users else users)
    user =  coll.find_one({"_user_linked_id": linked_id})
    if user:
      raise Exception(f"${linked_id} is exist")
    n_user = User(_user_linked_id=linked_id)
    n_user.save()
    return n_user

  def get(self, _id: str):
    pass

  def list(self, page_size, num_page):
    pass

  def delete(self, linked_id: str):
    coll = get_collection(self.COLLECTION)
    return coll.find_one_and_delete({"_user_linked_id": linked_id})
