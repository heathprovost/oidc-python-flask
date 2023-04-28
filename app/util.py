from functools import wraps
from flask import redirect, url_for, session

def is_authenticated(f):
  @wraps(f)
  def decorator(*args, **kwargs):
    if session.get('is_authenticated'):
      return f(*args, **kwargs)
    else:
      return redirect(url_for("auth.login"))
  return decorator
