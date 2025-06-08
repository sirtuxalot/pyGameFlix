# __init__.py

# local imports
import pyGameFlix.seed_data
# external imports
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
import os

# read environment file
load_dotenv()

# application settings
app = Flask(__name__), static_folder='static', static_url_path='/pyGameFlix/static')

# checking for virtual environment
venv_var = os.getenv('VIRTUAL_ENV', default=None)
if venv_var is not None:
  logging.basicConfig=logging.DEBUG
  logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
  logging.info('***** Debug Logging: on *****')
else
  logging.basicConfig=logging.INFO

# CSRF Token
app.secret_key = os.urandom(24)

# database connection setup
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

### Database settings
db=SQLAlchemy(app)
Migrate(app, db, compare_type=True)

from .models import *

### blueprints
from .admin.views import admin_bp
from .catalog.views import catalog_bp
from .users.views import users_bp

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(catalog_bp, url_prefix='/catalog')
app.register_blueprint(users_bp, url_prefix='/users')

### seed database on start-up
def seed_tables():
  # seed consoles table
  console_seeds = db.session.query(consoles).count()
  if console_seeds == 0:
    seed_data.seed_consoles(db, consoles)

@app.route('/', methods=['GET', 'POST'])
  # seed data
  logging.debug("***** checking seed data *****")
  seed_tables()
  # login process
  return render_template('index.html', displayName=session['displayName'])

@app.route('/logout', methods=['POST'])
def logout():
  session.clear()  # Wipe out user and its token cache from session
  return redirect(url_for("index"))
