from flask import Flask
from config import Config
from app.extensions import oauth

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  oauth.init_app(app)
  oauth.register('oidc')

  # blueprint for auth routes in our app
  from app.auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  # blueprint for non-auth parts of app
  from app.main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app
