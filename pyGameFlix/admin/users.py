# admin/users.py

# local imports
import pyGameFlix
from pyGameFlix import db
from pyGameFlix.models import users
# external imports
from flask import Blueprint

users_bp = Blueprint('users', __name__)

@users_bp.route('/')
def index():
  pass
