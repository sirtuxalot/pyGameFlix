# controllers/admin_subscriptions.py
  
# internal imports
from .forms import SubscriptionForm
from models.models import db, subscriptions
# external imports
from flask import render_template
import logging
from sqlalchemy import asc

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