# controllers/users.py

# internal imports
from .forms import ProfileForm
from models.models import db, subscriptions, users
# external imports
from flask import redirect, render_template, request, session, url_for
import logging

def profile(user_id):
  if "jwt_token" not in session:
    return redirect(url_for("access.login"))
  else:
    user_profile = users.query.get_or_404(user_id)
    form = ProfileForm()
    form.subscription.choices = [('0', 'Select Subscription Plan')] + [(subscription.subscription_id, subscription.subscription_name
      ) for subscription in subscriptions.query.order_by(subscriptions.subscription_id
      ).filter(subscriptions.subscription_name.not_like('-- Select Subscription --'))]
    if form.validate_on_submit():
      user_profile.first_name = form.first_name.data
      user_profile.last_name = form.last_name.data
      user_profile.address = form.address.data
      user_profile.city = form.city.data
      user_profile.state = form.state.data
      user_profile.zip_code = form.zip_code.data
      user_profile.email = form.email.data
      user_profile.subscription_id = form.subscription.data
      db.session.commit()
      return redirect(url_for('index'))
    elif request.method == 'GET':
      form.first_name.data = user_profile.first_name
      form.last_name.data = user_profile.last_name
      form.address.data = user_profile.address
      form.city.data = user_profile.city
      form.state.data = user_profile.state
      form.zip_code.data = user_profile.zip_code
      form.email.data = user_profile.email
      form.subscription.data = user_profile.subscription_id
  return render_template('users/profile.html', default_subscription=form.subscription.data, form=form)
