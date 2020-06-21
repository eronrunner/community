from mongoengine import connect, Document
from pymongo import WriteConcern, ReadPreference, MongoClient
from pymongo.read_concern import ReadConcern

client = connect("post", host="192.168.116.129", port=27017, alias="post_db")

base_metadata = {
  "read_concern": ReadConcern('local'),
  "write_concern": WriteConcern("majority", wtimeout=1000),
  "read_preference": ReadPreference.PRIMARY
}

def get_collection(collection: str):
  db = client["post"]
  print(client.db_name.command('ping'))
  coll = db[collection]
  return coll

def get_mapper(cls):
  if issubclass(cls, Document): return cls
  else: raise Exception(f"${cls} is not a Document mapper")