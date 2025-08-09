# controllers/admin_forms.py

# external imports
from flask_wtf import FlaskForm
from wtforms import PasswordField, SelectField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Optional

## admin game form

class GameForm(FlaskForm):
  game_name = StringField('Game Name: ', render_kw={'placeholder': 'Game Name'}, validators=[DataRequired()])
  console_id = SelectField('Console', choices=[], default=0)
  submit = SubmitField('Save Game')

## admin console form

class ConsoleForm(FlaskForm):
  console_name = StringField('Console Name: ', render_kw={'placeholder': 'Console Name'}, validators=[DataRequired()])
  submit = SubmitField('Save Console')

## admin subscription form

class SubscriptionForm(FlaskForm):
  subscription_name = StringField('Subscription Name: ', render_kw={'placeholder': 'Subscription Name'}, validators=[DataRequired()])
  rentals_allowed = StringField('Rentals Allowed: ', render_kw={'placeholder': 'Rentals'}, validators=[DataRequired()])
  price = StringField('Price: ', render_kw={'placeholder': 'Price'}, validators=[DataRequired()])
  submit = SubmitField('Save Subscription')
