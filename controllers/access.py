# controllers/access.py

# internal imports
from models.models import db, users, subscriptions  
# external imports
from flask import redirect, render_template, url_for
from flask_wtf import FlaskForm
from flask_bcrypt import Bcrypt
from wtforms import PasswordField, SelectField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
import json
import logging
import requests

## settings
bcrypt = Bcrypt()

## forms
class LoginForm(FlaskForm):
  email = StringField('E-mail:', validators=[DataRequired(), Email()])
  password = PasswordField('Password: ', validators=[DataRequired()])
  submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
  first_name = StringField('First Name: ', validators=[DataRequired()])
  last_name = StringField('Last Name: ', validators=[DataRequired()])
  address = StringField('Street Address: ', validators=[DataRequired()])
  city = StringField('City: ', validators=[DataRequired()])
  state = StringField('State: ', validators=[DataRequired()])
  zip_code = StringField('Zip Code: ', validators=[DataRequired()])
  email = StringField('E-mail: ', validators=[DataRequired(), Email()])
  password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('confirm_password', message='Passwords must match!')])
  confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired()])
  subscription = SelectField('Subscription', choices=[], default=0)
  submit = SubmitField('Create User')

  def check_email(self, field):
    if users.query.filter_by(email=field.data).first():
      raise ValidationError('Your e-mail has already been registered.')

## functions
def login():
  # initialize the form variable
  form = LoginForm()
  if form.validate_on_submit():
    # generate variables used with the json request
    endpoint = "http://localhost:5001/login"
    credentials = {
      'email': form.email.data,
      'password': bcrypt.generate_password_hash(form.password.data).decode('utf-8'),
    }
    headers = {
      'Content-type': 'application/json',
      'Accept': 'text/plain'
    }
    # construct and send the user login post request
    login_request = requests.post(endpoint, data=json.dumps(credentials), headers=headers)
    # redirect user to index afer successful login
    return redirect(url_for("index"))
  # open the loginform to be filled out by the user
  return render_template('access/login.html', form=form)

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
    # redirect user to login form after successful registration
    return redirect(url_for('access.login'))
  # open the register form to be filled out by the user
  return render_template('access/register.html', form=form)