from flask import render_template, session
from app.main import main
from app.util import is_authenticated

@main.route('/')
def home():
  return render_template('home.html')

@main.route('/profile')
@is_authenticated
def profile():
  return render_template('profile.html')
