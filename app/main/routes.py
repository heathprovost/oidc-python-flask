import json
from flask import render_template, redirect, session, url_for
from app.main import bp
from app.extensions import oauth

@bp.route('/', methods=['GET', 'POST'])
def home():
  userinfo = session.get('userinfo')
  id_token = session.get('id_token')
  return render_template('home.html', userinfo=userinfo, id_token=id_token)

@bp.route('/login', methods=['GET', 'POST'])
def login():
  redirect_uri = url_for('main.callback', _external=True)
  return oauth.oidc.authorize_redirect(redirect_uri)

@bp.route('/logout')
def logout():
  session.pop('userinfo', None)
  session.pop('id_token', None)
  return redirect('/')

@bp.route('/callback', methods=['GET', 'POST'])
def callback():
  token = oauth.oidc.authorize_access_token()
  session['id_token'] = json.dumps(token['userinfo'], sort_keys=True, indent=2)
  session['userinfo'] = json.dumps(oauth.oidc.userinfo(token=token), sort_keys=True, indent=2)
  return redirect('/')
