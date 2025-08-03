# controllers/admin_catalog.py
  
# internal imports
#from .forms import ConsoleForm, SubscriptionForm, UserForm
from models.models import db, catalog, consoles
# external imports
from flask import render_template
import logging

def index():
  return render_template('admin/admin.html')

def show_catalog():
  return render_template('admin/catalog.html')

def edit_game(game_id):
  pass
