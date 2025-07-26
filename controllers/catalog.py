# controllers/catalog.py

# external imports
from flask import render_template

def index():
  return render_template('catalog/catalog.html')
