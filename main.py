# main.py

# local imports
import seed_data
from models.models import db, consoles, subscriptions, users
from routes.access import access_bp
from routes.admin import admin_bp
from routes.catalog import catalog_bp
from routes.users import users_bp
# external imports
from dotenv import load_dotenv
from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
import os

# read environment file
load_dotenv()

# application settings
app = Flask(__name__, static_folder='static', static_url_path='/static')

# checking for virtual environment
venv_var = os.getenv('VIRTUAL_ENV', default=None)
if venv_var is not None:
  logging.basicConfig(level=logging.DEBUG)
  logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
  logging.info('***** Debug Logging: on *****')
else:
  logging.basicConfig=logging.INFO

# CSRF Token
app.secret_key = os.urandom(24)

# database connection setup
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

### Database settings
db.init_app(app)
Migrate(app, db, compare_type=True)

### blueprints
app.register_blueprint(access_bp, url_prefix='/access')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(catalog_bp, url_prefix='/catalog')
app.register_blueprint(users_bp, url_prefix='/users')

### seed database on start-up
def seed_tables():
  # seed consoles table
  console_seeds = db.session.query(consoles).count()
  if console_seeds == 0:
    seed_data.seed_consoles(db, consoles)
  # seed subscriptions table
  subscription_seeds = db.session.query(subscriptions).count()
  if subscription_seeds == 0:
    seed_data.seed_subscriptions(db, subscriptions)
  # seed users table
  user_seeds = db.session.query(users).count()
  if user_seeds == 0:
    seed_data.seed_users(db, users)

# root level routes
@app.route('/')
def index():
  # seed data
  logging.debug("***** checking seed data *****")
  seed_tables()
  # login process
  return render_template('index.html')

if __name__ == '__main__':
  if venv_var is not None:
    app.run(debug=True, ssl_context='adhoc', port=5000) 
  else:
    app.run(port=5000)
