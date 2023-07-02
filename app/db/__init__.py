# Desc: initialize database connection
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

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