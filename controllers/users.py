# controllers/users.py

# internal imports
from .forms import ChangePwdForm, ProfileForm
from .access import encrypt_password, load_public_key
from models.models import db, subscriptions, users
# external imports
from flask import redirect, render_template, request, session, url_for
import json
import logging
import requests

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

def password(user_id):
  if "jwt_token" not in session:
    return redirect(url_for("access.login"))
  else:
    user_profile = users.query.get_or_404(user_id)
    form = ChangePwdForm()
    if form.validate_on_submit():
      user_profile.password = encrypt_password(form.password.data, load_public_key())
      # generate variables used with the json request
      endpoint = "http://localhost:5001/password"
      updateUserPW = {
        'user_id': user_id,
        'password': encrypt_password(form.password.data, load_public_key()),
      }
      headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain'
      }
      # construct and send the new user post request
      update_user_request = requests.post(endpoint, data=json.dumps(updateUserPW), headers=headers)
      update_password = update_user_request.json()
      if update_password['message'] == "SUCCESS: Password updated.":
        return render_template('users/change_pw.html', result=update_password['message'], form=form)
    return render_template('users/change_pw.html', result="", form=form)
  return redirect(url_for('index'))

def delete(user_id):
  if "jwt_token" not in session:
    return redirect(url_for("access.login"))
  else:
    user_profile = users.query.get_or_404(user_id)
    # generate variables used with the json request
    endpoint = "http://localhost:5001/delete"
    deleteUser = {
      'user_id': user_id,
    }
    headers = {
      'Content-type': 'application/json',
      'Accept': 'text/plain'
    }
    # construct and send the new user post request
    delete_user_request = requests.post(endpoint, json.dumps(deleteUser), headers=headers)
    delete_account = delete_user_request.json()
    if delete_account['message'] == "SUCCESS: Account deleted!":
      session.clear()
      return redirect(url_for('index'))