from flask import redirect, url_for, session
from app.auth import auth
from app.extensions import oauth
from app.util import is_authenticated

@auth.route('/login')
def login():
  redirect_uri = url_for('auth.callback', _external=True)
  return oauth.oidc.authorize_redirect(redirect_uri)


@auth.route('/logout')
@is_authenticated
def logout():
  session.pop('user')
  session['is_authenticated'] = False
  return redirect(url_for('main.home'))


@auth.route('/callback')
def callback():
  token = oauth.oidc.authorize_access_token()
  session['is_authenticated'] = True
  session['user'] = token['userinfo']
  return redirect(url_for('main.profile'))
