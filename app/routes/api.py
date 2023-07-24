# This file is where we define all API enpoints

# We need blueprint to organize related routes together
# request to get the data from the request body (this corresponds to req.body in Express)
# jsonify to send JSON responses back to the client
from flask import Blueprint, request, jsonify
# Importing the User model
from app.models import User
# Importing the get_db function from app.db to get the database connection
from app.db import get_db
# Importing sys module to print error messages to the terminal
import sys

# define the blueprint to be used in the app
bp = Blueprint('api', __name__, url_prefix='/api')

# add signup route to resolve /api/users as a POST to receive data using flask's request object
@bp.route('/users', methods=['POST'])
def signup():
  # data is a python dictionary, which means we have to use bracket notation to access its values
  # data isn't a JSON object yet, so we need to call request.get_json() to convert it
  data = request.get_json()
  # call get_db() function to get a database connection
  db = get_db()

# Wrapping creation logic in a try/except block, similar to a try/catch in JavaScript
# If the try block fails, the except block will run sending a JSON error message to the front end
  try:
    # attempt creating a new user
    newUser = User(
      # data['username'] is the username value from the data object
      username = data['username'],
      email = data['email'],
      password = data['password']
    )

    # Use db.add() method to prep the INSET stmt, then db.commit() to officially update the db
    db.add(newUser)
    # commit() method saves all changes to the database
    db.commit()
  except:
    print(sys.exc_info()[0])

    # insert failed, so rollback and send error to front end 
    # rollback() method used to prevent app from crashing if the db.add() or db.commit() methods fail
    db.rollback()
    return jsonify(message = 'Signup failed'), 500
  # An AssertionError thrown when custom validation fails
  # An IntegrityError is thrown when a UNIQUE constraint is violated

  # Using Flask func jsonify() to send back JSON notation that includes the ID of a new user
  return jsonify(id = newUser.id)