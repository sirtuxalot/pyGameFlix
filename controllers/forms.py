# controllers/forms.py

# external imports
from flask_wtf import FlaskForm
from wtforms import PasswordField, SelectField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Optional

## access forms

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

## profile form

class ProfileForm(FlaskForm):
  first_name = StringField('First Name: ', validators=[DataRequired()])
  last_name = StringField('Last Name: ', validators=[DataRequired()])
  address = StringField('Street Address: ', validators=[DataRequired()])
  city = StringField('City: ', validators=[DataRequired()])
  state = StringField('State: ', validators=[DataRequired()])
  zip_code = StringField('Zip Code: ', validators=[DataRequired()])
  email = StringField('E-mail: ', validators=[DataRequired(), Email()])
  subscription = SelectField('Subscription', choices=[])
  submit = SubmitField('Update User')

## admin game form

class GameForm(FlaskForm):
  pass

## admin console form

class ConsoleForm(FlaskForm):
  pass

## admin subscription form

class SubscriptionForm(FlaskForm):
  pass

## admin user form

class UserForm(FlaskForm):
  pass