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

# subscriptions seed data
def seed_subscriptions(db_server, subscription_db):
  subscription_objects = [
    subscription_db(subscription_name='-- Select Subscription --', rentals_allowed=0, price='0.00'),
    subscription_db(subscription_name='Standard', rentals_allowed=1, price='4.99'),
    subscription_db(subscription_name='Bronze', rentals_allowed=2, price='9.99'),
    subscription_db(subscription_name='Silver', rentals_allowed=3, price='13.99'),
    subscription_db(subscription_name='Gold', rentals_allowed=5, price='16.99'),
    subscription_db(subscription_name='Platinum', rentals_allowed=7, price='18.99'),
  ]
  db_server.session.add_all(subscription_objects)
  db_server.session.commit()

# user seed data
def seed_users(db_server, users_db):
  user_objects = [
    users_db(first_name='App', last_name='Admin', email='app.admin@ist412.io', address='19 Maxwell Road', city='Seffner', state='FL', zip_code=33584, password='$2b$12$H4aKs6GS/a4GOiyQoqNKp.s8yjM.xqLSo2MlyDR0VU8onCGwhlw5G', subscription_id=1, access_level=1),
    users_db(first_name='Test', last_name='User', email='test.user@ist412.io', address='17 Ruby Ridge Way', city='Delton', state='MI', zip_code=49046, password='$2b$12$9jjTG4shlDhDQKpCwnzn5ezjOvfS/pb8CbZBt1YMDZGIWd143wyne', subscription_id=4, access_level=99),
  ]
  db_server.session.add_all(user_objects)
  db_server.session.commit()