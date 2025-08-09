# controllers/admin_consoles.py
  
# internal imports
from .admin_forms import ConsoleForm
from models.models import db, catalog, consoles
# external imports
from flask import redirect, render_template, request, session, url_for
import logging
from sqlalchemy import func
from sqlalchemy.exc import DataError, IntegrityError

def show_consoles():
  if "jwt_token" not in session:
    return redirect(url_for("access.login"))
  else:
    form = ConsoleForm()
    if form.validate_on_submit():
      try:
        new_console = consoles(
          console_name=form.console_name.data)
        db.session.add(new_console)
        db.session.commit()
        logging.info("New console: %s added!" % form.console_name.data)
      except DataError:
        db.session.rollback()
        return render_template('exceptions.html', exception="Data Error: Divide by Zero, Value out of Range, etc...")
      except IntegrityError:
        db.session.rollback()
        return render_template('exceptions.html', exception="Console already exists!")
    game_count_query = db.session.query(catalog.console_id, func.count(catalog.console_id
      ).label('game_count')
      ).group_by(catalog.console_id
      ).filter(catalog.console_id != 1)
    game_count_subquery = game_count_query.subquery()
    consoles_query = db.session.query(consoles.console_id, consoles.console_name, game_count_subquery.c.game_count
      ).order_by(consoles.console_name
      ).join(game_count_subquery, consoles.console_id == game_count_subquery.c.console_id, isouter=True
      ).filter(consoles.console_name.not_like('-- Select Console --'))
    for console in consoles_query:
      logging.debug("'%s' '%s' '%s'" % (console[0], console[1], console[2]))
    return render_template('admin/consoles.html', consoles=consoles_query, form=form)

def edit_console(console_id):
  if "jwt_token" not in session:
    return redirect(url_for("access.login"))
  else:
    console_edit = consoles.query.get_or_404(console_id)
    form = ConsoleForm()
    if form.validate_on_submit():
      console_edit.console_name = form.console_name.data
      db.session.commit()
      logging.info("Console: %s updated!" % form.console_name.data)
      return redirect(url_for('admin.show_consoles'))
    elif request.method == 'GET':
      form.console_name.data = console_edit.console_name
    return render_template('admin/edit_console.html', form=form)