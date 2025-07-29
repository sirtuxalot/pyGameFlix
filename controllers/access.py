# controllers/access.py

# internal imports
from .forms import LoginForm, RegistrationForm
from models.models import db, subscriptions, users
# external imports
import base64
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from flask import redirect, render_template, session, url_for
from pathlib import Path
import json
import jwt
import logging
import requests

# support functions

def validate_jwt(token):
  unverified_headers = jwt.get_unverified_header(token)
  x509_certificate = load_pem_x509_certificate(
    Path("keys/public_crt.pem").read_text().encode()
  ).public_key()
  return jwt.decode(
    token,
    key=x509_certificate,
    algorithms=unverified_headers["alg"],
  )

def load_public_key():
  with open('keys/public_key.pem', 'rb') as pem_file:
    public_key = serialization.load_pem_public_key(pem_file.read())
  return public_key

def encrypt_password(message, public_key):
  encrypted = public_key.encrypt(message.encode('utf-8'), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
  return base64.b64encode(encrypted).decode('utf-8')

# access functions

def login():
  # initialize the form variable
  form = LoginForm()
  if form.validate_on_submit():
    # generate variables used with the json request
    endpoint = "http://localhost:5001/login"
    credentials = {
      'email': form.email.data,
      'password': encrypt_password(form.password.data, load_public_key())
    }
    headers = {
      'Content-type': 'application/json',
      'Accept': 'text/plain'
    }
    # construct and send the user login post request
    login_request = requests.post(endpoint, data=json.dumps(credentials), headers=headers)
    userProfile = login_request.json()
    #logging.debug(userProfile)
    if userProfile['message'] == "SUCCESS: User credentials authenticated!":
      logging.debug(validate_jwt(userProfile['jwt_token']))
      session["access_level"] = userProfile['access_level']
      session["address"] = userProfile['address']
      session["city"] = userProfile['city']
      session["email"] = userProfile['email']
      session["first_name"] = userProfile['first_name']
      session["jwt_token"] = userProfile['jwt_token']
      session["last_name"] = userProfile['last_name']
      session["message"] = userProfile['message']
      session["state"] = userProfile['state']
      session["subscription_id"] = userProfile['subscription_id']
      session["user_id"] = userProfile['user_id']
      session["zip_code"] = userProfile['zip_code']
    else:
      return render_template('access/login.html', denied=userProfile['message'], message="Please login to GameFlix", form=form)
    



    #logging.debug(session)
    # redirect user to index afer successful login
    return redirect(url_for("index"))
  # open the loginform to be filled out by the user
  return render_template('access/login.html', denied="", message="Please login to GameFlix", form=form,)

def logout():
  session.clear()  # Wipe out user and its token cache from session
  return redirect(url_for("index"))

def register():
  # initialize form variable
  form = RegistrationForm()
  # generate subscription choices from suscriptions table
  form.subscription.choices = [('0', 'Select Subscription Plan')] + [(subscription.subscription_id, subscription.subscription_name
    ) for subscription in subscriptions.query.order_by(subscriptions.subscription_id
    ).filter(subscriptions.subscription_name.not_like('-- Select Subscription --'))]
  if form.validate_on_submit():
    # generate variables used with the json request
    endpoint = "http://localhost:5001/register"
    newUser = {
      'first_name': form.first_name.data,
      'last_name': form.last_name.data,
      'address': form.address.data,
      'city': form.city.data,
      'state': form.state.data,
      'zip_code': form.zip_code.data,
      'email': form.email.data,
      'password': bcrypt.generate_password_hash(form.password.data).decode('utf-8'),
      'subscription_id': form.subscription.data,
      'access_level': 99
    }
    headers = {
      'Content-type': 'application/json',
      'Accept': 'text/plain'
    }
    # construct and send the new user post request
    new_user_request = requests.post(endpoint, data=json.dumps(newUser), headers=headers)
    userProfile = new_user_request.json
    #logging.debug(userProfile)
    # redirect user to login form after successful registration
    return redirect(url_for('access.login'))
  # open the register form to be filled out by the user
  return render_template('access/register.html', message="Complete form to join GameFlix", form=form)