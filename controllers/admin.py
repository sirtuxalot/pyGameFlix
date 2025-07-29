# controllers/admin.py
  
# internal imports
from .forms import ConsoleForm, SubscriptionForm, UserForm
from models.models import db, catalog, consoles, subscriptions, users
# external imports
from flask import render_template
import logging
from sqlalchemy import asc

def index():
  return render_template('admin/admin.html')

## catalog / games 

def show_catalog():
  return render_template('admin/catalog.html')

def edit_game(game_id):
  pass

## consoles

def show_consoles():
  form = ConsoleForm()
  if form.validate_on_submit():
    pass
  consoles_query = db.session.query(consoles.console_id, consoles.console_name
    ).order_by(consoles.console_name
    ).filter(consoles.console_name.not_like('-- Select Console --'))
  for console in consoles_query:
    logging.debug("'%s' '%s'" % (console[0], console[1]))
  return render_template('admin/consoles.html', consoles=consoles_query)

def edit_console(console_id):
  pass

## subscriptions

def show_subscriptions():
  form = SubscriptionForm()
  if form.validate_on_submit():
    pass
  subscriptions_query = db.session.query(subscriptions.subscription_id, subscriptions.subscription_name, subscriptions.rentals_allowed, subscriptions.price
    ).order_by(asc(subscriptions.rentals_allowed)
    ).filter(subscriptions.subscription_name.not_like('-- Select Subscription --'))
  for subscription in subscriptions_query:
    logging.debug("'%s' '%s' '%s' '%s'" % (subscription[0], subscription[1], subscription[2], subscription[3]))
  return render_template('admin/subscriptions.html', subscriptions=subscriptions_query)

def edit_subscription(subscription_id):
  pass

## users

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
