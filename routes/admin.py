# routes/admin.py

# internal imports
from controllers.admin_catalog import index, show_catalog, edit_game
from controllers.admin_consoles import show_consoles, edit_console
from controllers.admin_subscriptions import show_subscriptions, edit_subscription
from controllers.admin_users import show_users, edit_user
# external imports
from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

admin_bp.route('/')(index)

# show
admin_bp.route('/catalog', methods=['GET', 'POST'])(show_catalog)
admin_bp.route('/consoles', methods=['GET', 'POST'])(show_consoles)
admin_bp.route('/subscriptions', methods=['GET', 'POST'])(show_subscriptions)
admin_bp.route('/users', methods=['GET', 'POST'])(show_users)

# edit
admin_bp.route('/game/<int:game_id>', methods=['GET', 'POST'])(edit_game)
admin_bp.route('/console/<int:console_id>', methods=['GET', 'POST'])(edit_console)
admin_bp.route('/subscription/<int:subscription_id>', methods=['GET', 'POST'])(edit_subscription)
admin_bp.route('/users/<int:user_id>', methods=['GET', 'POST'])(edit_user)