# Desc: initialize database connection
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
# import g from flask to store db connection in app context.
# g is an object that temporarily provides context to the application during a request globally
from flask import g

# bc we used a .env to fake the env variable, we need to first call load_dotenv() to load the .env file from the python-dotenv module
# In production, DB_URL would be an actual env variable set on the server
load_dotenv()

# connect to database using env variable
# engine variable manages the overall connection to the database
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# session variable generates temporary connections to the database to perform CRUD operations
Session = sessionmaker(bind=engine)
# Base variable helps us map our models to real MySQL tables
Base = declarative_base()

# initialize the database
def init_db(app):
  Base.metadata.create_all(engine)

  app.teardown_appcontext(close_db) # close db connection when app context ends

# get_db() to ensure that each request has access to a valid database conn. object
def get_db():
  # if db key not in g object, create a new db connection object using the Session() class from SQLAl
  if 'db' not in g:
    # store db connection in app context
    g.db = Session()
    # return db conn. so routes & functions can use it. Perform CRUD operations on db conn.
    return g.db

# leveraging the @app context processor to close the conn when the request officially terminates
# Adding a teardown function to close the db connection when the app context ends
def close_db(e=None):
  # pop() method finds & removes db from g object. if db =/= none, then db.close() is ends connection
  db = g.pop('db', None)

  if db is not None:
    db.close()
    # No need for return g.db here bc this is a teardown function, not a route handler