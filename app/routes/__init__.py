# The .home syntax directs the import to the home.py module in the routes package. 
# Its a relative import, meaning that the import is relative to the current file.
# Next, we import the bp object but rename it to home so that we can use it in the routes/__init__.py file.
from .home import bp as home

from .dashboard import bp as dashboard
