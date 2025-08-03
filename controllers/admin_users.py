# controllers/admin_users.py
  
# internal imports
from .forms import UserForm
from models.models import db, subscriptions, users
# external imports
from flask import render_template
import logging
from sqlalchemy import asc

def show_users():
  form = UserForm()
  if form.validate_on_submit():
    pass
  users_query = db.session.query(users.user_id, users.first_name, users.last_name, users.email, users.address, users.city, users.state, users.zip_code, users.access_level, subscriptions.subscription_name
    ).join(subscriptions
    ).order_by(users.last_name
    ).order_by(users.first_name
    ).filter(users.email.not_like('test.user@ist412.io'))
  for user in users_query:
    logging.debug("'%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s'" % (user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9]))
  return render_template('admin/users.html', users=users_query)

def edit_user(user_id):
  pass
