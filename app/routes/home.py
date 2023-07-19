from flask import Blueprint, render_template
# home.py is a Python Module because it has a .py extension & its belongs to the routes package
from app.models import Post
from app.db import get_db
# Blueprint() lets us consolidate routes into a single file
# This corresponds to using Router() in Express
bp = Blueprint('home', __name__, url_prefix='/')


# @bp is a decorator that tells Flask to associate the / URL path with the index() function
# decorators are used to define routes and bind them to specific functions
@bp.route('/')
# def index() is the function that will be triggered when the URL path / is visited
def index():
  # get all posts
  # calls get_db() function to retrieve a database connection object
  db = get_db()
  # Query to fetch all posts from the db and order them by their created_at attribute in descending order. 
  # The result of the query is assigned to the posts variable.
  posts = db.query(Post).order_by(Post.created_at.desc()).all()
  # The render_template() function is provided by Flask and is used to generate HTML content using Jinja2 templating engine.
  # pass the 'homepage.html' template and the posts variable as template parameters
  return render_template(
    'homepage.html',
    posts=posts
  )

@bp.route('/login')
def login():
  return render_template('login.html')

# <id> is a dynamic parameter that will captured from the URL and passed as an argument to the function
@bp.route('/post/<id>')
# single(id) takes the id parameter, which corresponds to the dynamic part of the URL path
def single(id):
  # query the Post model based on the provided id. 
  # The filter() method filters the posts based on the condition Post.id == id. 
  # The one() method fetches the single post that matches the filter condition.
  # once template is rendered, the context for route terminates & teardown cluses db conn.
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()
  # pass the 'single-post.html' template and the post variable as template parameters
  return render_template(
    'single-post.html',
    post=post
  )

# You can import any variables or functions defined in Python Modules into other modules or files
# We only care about the bp variable thanks to the @bp.route() decorator, so we import it like this:
# from app.routes.home import bp