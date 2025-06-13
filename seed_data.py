# console seed data
def seed_consoles(db_server, consoles_db):
  console_objects = [
    consoles_db(console_name='Nintendo Switch'),
    consoles_db(console_name='Nintendo Switch 2'),
    consoles_db(console_name='Nintendo Wii'),
    consoles_db(console_name='Playstation'),
    consoles_db(console_name='Playstation 2'),
    consoles_db(console_name='Playstation 3'),
    consoles_db(console_name='Playstation 4'),
    consoles_db(console_name='Playstation 5'),
    consoles_db(console_name='Playstation (PSP)'),
    consoles_db(console_name='Playstation (PS Vita)'),
    consoles_db(console_name='XBox'),
    consoles_db(console_name='XBox 360'),
    consoles_db(console_name='XBox One'),
    consoles_db(console_name='XBox Series S'),
    consoles_db(console_name='XBox Series X'),
  ]
  db_server.session.add_all(console_objects)
  db_server.session.commit()
