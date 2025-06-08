# models.py

from pyGameFlix import db

## supporting tables

class consoles(db.Model):
  __tablename__ = 'consoles'
  console_id = db.Column(db.Integer, primary_key=True)
  console_name = db.Column(db.Text)

  def __init__(self, console_name):
    self.console_name = console_name

class subscriptions(db.Model):
  __tablename__ = 'subscriptions'
  subscription_id = db.Column(db.Integer, primary_key=True)
  subscription_name = db.Column(db.Text)
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
  console_id = db.Column(db.Integer, db.ForeignKey('consoles.console_id'))
  renter_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

  def __init__(self, game_name, console_id, renter_id):
    self.game_name = game_name
    self.console_id = console_id
    self.renter_id = renter_id

class users(db.Model):
  __tablename__ = 'users'
  user_id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.Text)
  last_name = db.Column(db.Text)
  email = db.Column(db.Text, unique=True)
  address = db.Column(db.Text)
  city = db.Column(db.Text)
  state = db.Column(db.Text)
  zip = db.Column(db.Integer)
  password = db.Column(db.Text)
  subscription_id = db.Column(db.Integer, db.ForeignKey('subscriptions.subscription_id'))
  access_level = db.Column(db.Integer)
  
