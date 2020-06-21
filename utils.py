import uuid
from uuid import SafeUUID

def gen_uuid():
  return uuid.UUID(uuid.uuid4().hex, is_safe=SafeUUID.safe).hex