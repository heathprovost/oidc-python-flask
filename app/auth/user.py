import json
from types import SimpleNamespace as Namespace
from flask_login import UserMixin

class User(UserMixin):
  def __init__(self, userinfo_json):
     # we just de-serialize the entire userinfo object and map it to our class properties
     userinfo = json.loads(userinfo_json, object_hook=lambda d: Namespace(**d))
     # we store the serialized data as the id to make flask_login happy
     self.id = userinfo_json
     # the well known fields of the id_token are mapped to properties of the user
     self.sub = userinfo.sub
     self.email = userinfo.email
     self.email_verified = userinfo.email_verified
     self.name = userinfo.name
     self.given_name = userinfo.given_name
     self.family_name = userinfo.family_name
