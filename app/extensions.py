from authlib.integrations.flask_client import OAuth
from authlib.integrations.flask_oauth2 import ResourceProtector

require_oauth = ResourceProtector()
oauth = OAuth()
