# admin/catalog.py

# local imports
import pyGameFlix
from pyGameFlix import db
from pyGameFlix.models import users
# external imports
from flask import Blueprint

catalog_bp = Blueprint('catalog', __name__)

@catalog_bp.route('/')
def index():
  pass
