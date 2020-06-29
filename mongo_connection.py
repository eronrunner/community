from mongoengine import connect, Document
from pymongo import WriteConcern, ReadPreference, MongoClient
from pymongo.read_concern import ReadConcern

client = connect("post", host="192.168.116.129", port=27017, alias="post_db")
print(client.db_name.command('ping'))

base_metadata = {
  "read_concern": ReadConcern('local'),
  "write_concern": WriteConcern(1, wtimeout=1000),
  "read_preference": ReadPreference.PRIMARY
}

def get_collection(collection: str):
  db = client.get_database("post", **base_metadata)
  coll = db[collection]
  return coll