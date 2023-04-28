import json
from flask import redirect, url_for
from flask_login import login_user, login_required, logout_user
from app.auth import auth
from app.auth.user import User
from app.extensions import oauth

@auth.route('/login', methods=['GET', 'POST'])
def login():
  redirect_uri = url_for('auth.callback', _external=True)
  return oauth.oidc.authorize_redirect(redirect_uri)

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.home'))

@auth.route('/callback', methods=['GET', 'POST'])
def callback():
  token = oauth.oidc.authorize_access_token()
  print(json.dumps(token['userinfo'], sort_keys=True, indent=2))
  print(json.dumps(oauth.oidc.userinfo(token=token), sort_keys=True, indent=2))
  login_user(User(json.dumps(token['userinfo'], sort_keys=True, indent=2)))
  return redirect(url_for('main.profile'))
