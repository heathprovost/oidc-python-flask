from flask import render_template
from flask_login import login_required, current_user
from app.main import main

@main.route('/')
def home():
  return render_template('home.html', current_user=current_user)

@main.route('/profile')
@login_required
def profile():
  return render_template('profile.html', user_name=current_user.name, userinfo_json=current_user.id)
