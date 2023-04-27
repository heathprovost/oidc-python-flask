from flask import Flask
from config import Config
from app.extensions import oauth

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  oauth.init_app(app)
  oauth.register('oidc')

  from app.main import bp as main_bp
  app.register_blueprint(main_bp)

  return app
