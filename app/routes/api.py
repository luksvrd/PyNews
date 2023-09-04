# This file is where we define all API enpoints

# We need blueprint to organize related routes together
# request to get the data from the request body (this corresponds to req.body in Express)
# jsonify to send JSON responses back to the client
# session to keep track of user's logged in state (this corresponds to req.session in Express)
from flask import Blueprint, request, jsonify, session
# Importing the User model
from app.models import User
# get_db function to get database connection
from app.db import get_db
# Importing sys module to print error messages to the terminal
import sys

# define the blueprint to be used in the app
bp = Blueprint('api', __name__, url_prefix='/api')

# add signup route to resolve /api/users as a POST to receive data using flask's request object
@bp.route('/users', methods=['POST'])
def signup():
  # data isn't a JSON object yet, so we need to call request.get_json() to convert it
  data = request.get_json()
  # call get_db() to get database connection
  db = get_db()

# Wrapping creation logic in a try/except block, similar to a try/catch in JavaScript
# If try block fails, except block will run sending a JSON error message to the front end
  try:
    # attempt creating a new user
    newUser = User(
      # data is a python dictionary, which means we have to use bracket notation to access its values
      username = data['username'],
      email = data['email'],
      password = data['password']
    )

    # Use db.add() method to prep the INSERT stmt, then db.commit() to officially update db
    db.add(newUser)
    # commit() method saves all changes to database
    db.commit()
  except:
    print(sys.exc_info()[0])

    # insert failed, so rollback and send error to front end 
    # rollback() method used to prevent app from crashing if db.add() or db.commit() methods fail
    db.rollback()
    return jsonify(message = 'Signup failed'), 500

  # clear any existing session data and then set the user_id and loggedIn properties
  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True
  # Using jsonify() (Flask func) to send back JSON notation that includes ID of a new user
  return jsonify(id = newUser.id)

# Add logout POST route to clear session data & return 204 status code (no content) 
@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204

# 
@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()

  try:
    user = db.query(User).filter(User.email == data['email']).one()
  except:
    print(sys.exc_info()[0])
    
    # if user is found, check password and start session
  if user.verify_password(data['password']) == False:
    session.clear()
    session['user_id'] = user.id
    session['loggedIn'] = True
    return jsonify(id = user.id)
  
  return jsonify(message = 'Incorrect credentials'), 400
  