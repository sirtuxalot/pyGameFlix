# controllers/admin_consoles.py
  
# internal imports
from .forms import ConsoleForm
from models.models import db, consoles
# external imports
from flask import render_template
import logging

def show_consoles():
  form = ConsoleForm()
  if form.validate_on_submit():
    pass
  consoles_query = db.session.query(consoles.console_id, consoles.console_name
    ).order_by(consoles.console_name
    ).filter(consoles.console_name.not_like('-- Select Console --'))
  for console in consoles_query:
    logging.debug("'%s' '%s'" % (console[0], console[1]))
  return render_template('admin/consoles.html', consoles=consoles_query)

def edit_console(console_id):
  pass
