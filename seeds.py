from app.models import User
# this is where the db variables we created in the db/__init__.py file come into play
# we import the Session and engine variables from the db package so that we can use them to interact with the database
# The code uses the Base class together with the engine variable to do 2 things:
# drops all existing tables, then creates any tables that Base mapped in a class like User
# In the terminal, run python3 seeds.py to drop and rebuild the tables in the database.
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
  User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
  User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
  User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
  User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
  User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])

db.commit()

db.close()