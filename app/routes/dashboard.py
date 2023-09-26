# Like home.py, this file is a Python Module because it has a .py extension & it belongs to the routes package
# Every variable or function belonging to a Python Module can be imported in other modules or files
# This is different from Node which requires you to export variables or functions from a file before you can import them
from flask import Blueprint, render_template, session
from app.models import Post
from app.db import get_db

from app.utils.auth import login_required

# we're prefixing every route in this blueprint with /dashboard by setting equal to url_prefix
# Routes will then be /dashboard and /dashboard/edit/<id> when they're registered
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
@login_required
def dash():
  db = get_db()
  posts = (
    db.query(Post)
    .filter(Post.user_id == session.get('user_id'))
    .order_by(Post.created_at.desc())
    .all()
  )

  return render_template(
  'dashboard.html',
  posts=posts,
  loggedIn=session.get('loggedIn')
  )  

@bp.route('/edit/<id>')
@login_required
def edit(id):
  # get single post by id
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  # render edit page
  return render_template(
    'edit-post.html',
    post=post,
    loggedIn=session.get('loggedIn')
  )