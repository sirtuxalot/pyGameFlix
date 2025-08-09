# controllers/admin_subscriptions.py
  
# internal imports
from .admin_forms import SubscriptionForm
from models.models import db, subscriptions
# external imports
from flask import redirect, render_template, request, session, url_for
import logging
from sqlalchemy import asc

def show_subscriptions():
  if "jwt_token" not in session:
    return redirect(url_for("access.login"))
  else:
    form = SubscriptionForm()
    if form.validate_on_submit():
      try:
        new_subscription = subscriptions(
          subscription_name=form.subscription_name.data,
          rentals_allowed=form.rentals_allowed.data,
          price=form.price.data)
        db.session.add(new_subscription)
        db.session.commit()
        logging.info("New subscription level: %s added" % form.subscription_name.data)
      except DataError:
        db.session.rollback()
        return render_template('exceptions.html', exception="Data Error: Divide by Zero, Value out of Range, etc...")
      except IntegrityError:
        db.session.rollback()
        return render_template('exceptions.html', exception="subscription already exists!")
    subscriptions_query = db.session.query(subscriptions.subscription_id, subscriptions.subscription_name, subscriptions.rentals_allowed, subscriptions.price
      ).order_by(asc(subscriptions.rentals_allowed)
      ).filter(subscriptions.subscription_name.not_like('-- Select Subscription --'))
    for subscription in subscriptions_query:
      logging.debug("'%s' '%s' '%s' '%s'" % (subscription[0], subscription[1], subscription[2], subscription[3]))
    return render_template('admin/subscriptions.html', subscriptions=subscriptions_query, form=form)

def edit_subscription(subscription_id):
  if "jwt_token" not in session:
    return redirect(url_for("access.login"))
  else:
    subscription_edit = subscriptions.query.get_or_404(subscription_id)
    form = SubscriptionForm()
    if form.validate_on_submit():
      subscription_edit.subscription_name = form.subscription_name.data
      subscription_edit.rentals_allowed = form.rentals_allowed.data
      subscription_edit.price = form.price.data
      db.session.commit()
      logging.info("Subscription: %s updated!" % form.subscription_name.data)
      return redirect(url_for('admin.show_subscriptions'))
    elif request.method == 'GET':
      form.subscription_name.data = subscription_edit.subscription_name
      form.rentals_allowed.data = subscription_edit.rentals_allowed
      form.price.data = subscription_edit.price
    return render_template('admin/edit_subscription.html', form=form)