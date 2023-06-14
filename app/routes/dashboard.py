# Like home.py, this file is a Python Module because it has a .py extension & it belongs to the routes package
# Every variable or function belonging to a Python Module can be imported in other modules or files
# This is different from Node which requires you to export variables or functions from a file before you can import them
from flask import Blueprint, render_template

# we're prefixing every route in this blueprint with /dashboard by setting equal to url_prefix
# Routes will then be /dashboard and /dashboard/edit/<id> when they're registered
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
  return render_template('dashboard.html')

@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')