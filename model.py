from datetime import datetime
from utils import gen_uuid

from mongoengine import *

class User(Document):
  _id = UUIDField(binary=False,required=True, primary_key=True, default=gen_uuid())
  _user_linked_id = StringField(required=True, index=True, unique=True)

  meta = {'db_alias': "post_db",
          'collection': 'user'}
# class Author(User):
#   pass

# class Viewer(User):
#   viewed_date = DateTimeField(required=True, default=datetime.utcnow())

class Post(Document):
  _id = UUIDField(binary=False, required=True, primary_key=True, default=gen_uuid())
  title = StringField(required=True, index=True)
  author = ReferenceField(User, required=True, index=True, reverse_delete_rule=CASCADE)
  content = StringField(null=True)
  created_date = DateTimeField(required=True, default=datetime.utcnow())
  # TODO - viewers = ListField(ReferenceField(User), default=None)
  # TODO - tags = ListField(null=True)

