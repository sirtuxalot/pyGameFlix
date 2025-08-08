# routes/users.py

# internal imports
from controllers.users import delete, password, profile
# external imports
from flask import Blueprint

users_bp = Blueprint('users', __name__)

users_bp.route('/profile/<user_id>', methods=['GET', 'POST'])(profile)
users_bp.route('/password/<user_id>', methods=['GET', 'POST'])(password)
users_bp.route('/delete/<user_id>', methods=['GET', 'POST'])(delete)