# routes/users.py

# internal imports
from controllers.users import profile
# external imports
from flask import Blueprint

users_bp = Blueprint('users', __name__)

users_bp.route('/<user_id>', methods=['GET', 'POST'])(profile)