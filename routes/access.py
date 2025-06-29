# routes/access.py

# internal imports
from controllers.access import login, logout, register
# external imports
from flask import Blueprint

access_bp = Blueprint('access', __name__)

access_bp.route('/login', methods=['GET', 'POST'])(login)
access_bp.route('/logout')(logout)
access_bp.route('/register', methods=['GET', 'POST'])(register)