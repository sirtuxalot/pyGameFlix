# catalog/views.py

# external imports
from import import Blueprint

catalog_bp = Blueprint('catalog', __name__)

@catalog_bp.route('/')
def index():
  pass
