# controllers/admin_users.py
  
# internal imports
from models.models import db, subscriptions, users
# external imports
from flask import redirect, render_template, session, url_for
import logging
from sqlalchemy import asc

def show_users():
  if "jwt_token" not in session:
    return redirect(url_for("access.login"))
  else:
    users_query = db.session.query(users.user_id, users.first_name, users.last_name, users.email, users.address, users.city, users.state, users.zip_code, users.access_level, subscriptions.subscription_name, users.enabled
      ).join(subscriptions
      ).order_by(users.last_name
      ).order_by(users.first_name
      ).filter(users.email.not_like('test.user@ist412.io'))
    for user in users_query:
      logging.debug("'%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s'" % (user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9], user[10]))
    return render_template('admin/users.html', users=users_query)

def set_permission(user_id):
  if "jwt_token" not in session:
    return redirect(url_for("access.login"))
  else:
    user_permission = users.query.get_or_404(user_id)
    if user_permission.enabled == True:
      user_permission.enabled = False
      db.session.commit()
      logging.info("User ID %s has been disabled" % user_id)
    else:
      user_permission.enabled = True
      db.session.commit()
      logging.info("User ID %s has been enabled" % user_id)
    return redirect(url_for('admin.show_users'))