# Python has its own oackage manager called pip (similar to npm)
# Use (. venv/bin/activate) to activate the virtual environment in MacOS
# Once the virtual environment is activated, run (pip install flask) to install Flask
# The __init__.py file is required to treat the app directory as a package.
# It corresponds to the index.js file in Node.js, or the server.js file in Express
# When Flask runs the "app" package, it looks for the __init__.py file and runs it
# Then tries to call the create_app() function, so must define it
# Importing Flask so we can use the Flask() constructor function, then use def keyword to define the create_app() function
# To start the Flask server, first (export FLASK_APP=app) environment variable,
# Then run run (python3 -m flask run) in the terminal (default port is 5000)
from flask import Flask
# We can import home directly from the routes package because we defined it in the routes __init__.py file
# If we didnt import and rename the home blueprint in the routes __init__.py file, we would have to import it like this:
# from app.routes.home import bp as home
from app.routes import home, dashboard

# Note that a 2x space indentation signifies a code block in Python, not curly braces
# Here we a new app variable and set some initial Flask configuration
def create_app(test_config=None):
  # set up app config
  # __name__ is a special variable in Python that gets the name of the current Python module
  # the app should serve static files from the root directory, not the /static directory
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    # SECRET_KEY is used by Flask and extensions to keep data safe
    SECRET_KEY='super_secret_key'
  )

# Here we register the home blueprint with the app
# Blueprint is just a way to organize related routes together
  @app.route('/hello')
  def hello():
    # Whatever is returned from the function will be rendered in the browser
    return 'hello world'
  
  # register the home blueprint with the app 
  # after registering each blueprint, in the terminal run export FLASK_APP=app then python3 -m flask run
  app.register_blueprint(home)
  app.register_blueprint(dashboard)

  return app

# Access the MySQL shell by running (mysql -u root -p) in the terminal pw sql
# To create a new database, run (CREATE DATABASE python_news_db;) then exit
# We're doing the rest in Python and an ROM called SQLAlchemy which we need to install
# Start virtual server by (. venv/bin/activate) & then Run (pip install sqlalchemy pymysql python-dotenv) to install necessary dependencies
# Next, create a .env file in the root directory and add the following:
# (DB_URL=mysql+pymysql://root:sql@localhost/python_news_db)
