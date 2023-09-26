from flask import session, redirect
# functools is a Python module that contains several helper funcitons we can use to change other functions.
# wraps() is a decorator that will preserve the function name and docstring of the function passed in
from functools import wraps

# Define a login_required() function that expects to receive another function as an argument (which it captures as the func parameter)
# goal of this Python decorator we're building is to redirect a user who isn't logged in (a user for whom no session exists) or to run the original route function for a user who is logged in.
def login_required(func):
  @wraps(func)
  def wrapped_function(*args, **kwargs):
    # if logged in, call original function with original arguments
    if session.get('loggedIn') == True:
      return func(*args, **kwargs)

    return redirect('/login')
  
  return wrapped_function


