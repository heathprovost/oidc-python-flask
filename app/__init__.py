from flask import Flask
from config import Config
from app.auth.user import User
from app.extensions import oauth, login_manager

# we are not using a database or model so we are storing our entire
# userinfo object serialized into the id property of our User object.
# flask_login expects to be working with a database and model so it
# wants to "load" the User from the database by id. Instead we just
# pass the user_id (which is the userinfo object in json format) and
# our User class de-serializes it for us. If anything goes wrong we
# just return None and flask_login will ensure that the user is not
# authenticated

def register_user_loader(login_manager):
  @login_manager.user_loader
  def load_user(user_id):
    try:
      return User(user_id)
    except:
      return None

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  oauth.init_app(app)
  oauth.register('oidc')
  login_manager.init_app(app)
  register_user_loader(login_manager)

  # blueprint for auth routes in our app
  from app.auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  # blueprint for non-auth parts of app
  from app.main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app
