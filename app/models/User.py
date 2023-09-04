# Importing Base from app.db allows the User class to inherit from it
from app.db import Base
# Import Column, Integer, String, and validates from sqlalchemy to help us define our model
from sqlalchemy import Column, Integer, String
# validates is a decorator that allows us to add validation logic to our models
from sqlalchemy.orm import validates
# bcrypt is a password hashing function that allows us to store passwords securely in the database
import bcrypt

# salt is a random sequence added to the password before hashing to make the hash more secure
salt = bcrypt.gensalt()

# Created a User class that inherits from Base
# Base is a SQLAlchemy class created in the schema.sql that helps us map our models to real MySQL tables
# User class, we declare several properties that the parent class (Base) will inherit
# __tablename__ is a special SQLAlchemy variable that tells SQLAlchemy the name of the table we want to map to this class
# id, username, email, and password are all columns in the users table
# nullable=False means that the column cannot be empty
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

# validates is a decorator that allows us to add validation logic to our models
# validates takes 2 arguments: the name of the column we want to validate and the value of the column
# validate_email() uses the assert keyword to make sure that the email address contains the @ character
  @validates('email')
  def validate_email(self, key, email):
    # make sure email address contains @ character
    assert '@' in email

    return email
  
# validate_password() uses the assert keyword to make sure that the password is at least 5 characters long
# bcrypt.hashpw() takes 2 arguments: the password and the salt
# The validate_password() function now returns an encryptedversion of the password
  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4

  # encrypt password, then test by running seeds.py & mysql -u root -p in terminal
  # MySQL shell: USE python_news_db; + SELECT * FROM users;
    return bcrypt.hashpw(password.encode('utf-8'), salt)
  
  # checkpw() method to compare incoming pw (pw parameter) with the hashed pw saved on User object (self.password)
  def verify_password(self, password):
    return bcrypt.checkpw(
      password.encode('utf-8'),
      self.password.encode('utf-8')
    )
