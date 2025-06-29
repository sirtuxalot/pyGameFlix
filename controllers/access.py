# controllers/access.py

# internal imports
from models.models import db, users, subscriptions  
# external imports
from flask import redirect, render_template, url_for
from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms import PasswordField, SelectField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
import json
import logging
import requests

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
  form = LoginForm()
  if form.validate_on_submit():
    endpoint = "http://localhost:5001/login"
    credentials = {
      'email': form.email.data,
      'password': generate_password_hash(form.password.data),
    }
    headers = {
      'Content-type': 'application/json',
      'Accept': 'text/plain'
    }
    login_request = requests.post(endpoint, data=json.dumps(credentials), headers=headers)
    logging.debug(login_request)
    return redirect(url_for("index"))
  return render_template('access/login.html', form=form)

def logout():
  session.clear()  # Wipe out user and its token cache from session
  return redirect(url_for("index"))

def register():
  form = RegistrationForm()
  form.subscription.choices = [('0', 'Select Subscription Plan')] + [(subscription.subscription_id, subscription.subscription_name
    ) for subscription in subscriptions.query.order_by(subscriptions.subscription_id
    ).filter(subscriptions.subscription_name.not_like('-- Select Subscription --'))]
  if form.validate_on_submit():
    endpoint = "http://localhost:5001/register"
    newUser = {
      'first_name': form.first_name.data,
      'last_name': form.last_name.data,
      'address': form.address.data,
      'city': form.city.data,
      'state': form.state.data,
      'zip_code': form.zip_code.data,
      'email': form.email.data,
      'password': generate_password_hash(form.password.data),
      'subscription_id': form.subscription.data,
      'access_level': 99
    }
    headers = {
      'Content-type': 'application/json',
      'Accept': 'text/plain'
    }
    new_user_request = requests.post(endpoint, data=json.dumps(newUser), headers=headers)
    logging.debug(new_user_request)
    return redirect(url_for('access.login'))
  return render_template('access/register.html', form=form)