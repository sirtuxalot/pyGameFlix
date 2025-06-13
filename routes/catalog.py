# routes/catalog.py

# internal imports
from controllers.catalog import index
# external imports
from flask import Blueprint

catalog_bp = Blueprint('catalog', __name__)

catalog_bp.route('/')(index)