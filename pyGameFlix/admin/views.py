# admin/views.py

# external imports
from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

from .catalog import catalog_bp
from .users import users_bp

@admin_bp.route('/')
def index():
  pass
