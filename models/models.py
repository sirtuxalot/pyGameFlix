# models/models.py

# external imports
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

## supporting tables

class consoles(db.Model):
  __tablename__ = 'consoles'
  console_id = db.Column(db.Integer, primary_key=True)
  console_name = db.Column(db.Text, unique=True, nullable=False)

  def __init__(self, console_name):
    self.console_name = console_name

class subscriptions(db.Model):
  __tablename__ = 'subscriptions'
  subscription_id = db.Column(db.Integer, primary_key=True)
  subscription_name = db.Column(db.Text, unique=True, nullable=False)
  rentals_allowed = db.Column(db.Integer)
  price = db.Column(db.Text)

  def __init__(self, subscription_name, rentals_allowed, price):
    self.subscription_name = subscription_name
    self.rentals_allowed = rentals_allowed
    self.price = price

## supported tables

class catalog(db.Model):
  __tablename__ = 'catalog'
  game_id = db.Column(db.Integer, primary_key=True)
  game_name = db.Column(db.Text)
  console_id = db.Column(db.Integer, db.ForeignKey('consoles.console_id'), nullable=False)
  renter_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

  def __init__(self, game_name, console_id, renter_id):
    self.game_name = game_name
    self.console_id = console_id
    self.renter_id = renter_id

class users(db.Model):
  __tablename__ = 'users'
  user_id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.Text)
  last_name = db.Column(db.Text)
  email = db.Column(db.Text, unique=True, nullable=False)
  address = db.Column(db.Text)
  city = db.Column(db.Text)
  state = db.Column(db.Text)
  zip_code = db.Column(db.Integer)
  password = db.Column(db.Text)
  subscription_id = db.Column(db.Integer, db.ForeignKey('subscriptions.subscription_id'), nullable=False)
  access_level = db.Column(db.Integer)
  enabled = db.Column(db.Boolean)

  def __init__(self, first_name, last_name, email, address, city, state, zip_code, password, subscription_id, access_level, enabled):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.address = address
    self.city = city
    self.state = state
    self.zip_code = zip_code
    self.password = password
    self.subscription_id = subscription_id
    self.access_level = access_level
    self.enabled = enabled