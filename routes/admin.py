# routes/admin.py

# internal imports
from controllers.admin import index
# external imports
from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

admin_bp.route('/')(index)