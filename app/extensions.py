from authlib.integrations.flask_client import OAuth
from authlib.integrations.flask_oauth2 import ResourceProtector
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

require_oauth = ResourceProtector()
oauth = OAuth()
