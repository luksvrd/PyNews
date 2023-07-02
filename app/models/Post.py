# Just tech news will have a one to many relationship between users and posts
# One user can have many posts, but each post can only belong to one user
from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy.ext.hybrid import hybrid_property
# select & func is a SQLAlchemy function that will allow us to access the number of votes a post has as a column 
# by selecting the number of records in the votes table where the post_id matches the id of the post we're querying
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
# column_property is a SQLAlchemy function that will allow us to access the number of votes a post has as a column
from sqlalchemy.orm import relationship, column_property

class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  # user_id is defined as a foreign key that references the users table
  user_id = Column(Integer, ForeignKey('users.id'))
  
  # added created_at and updated_at columns that use Pythons built in datetime module to generate timestamps
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
# A hybrid_property is a SQLAlchemy decorator that creates a new property on the Post model that behaves like a column in the database
# It is a property that can function as either an instance method or a class method
# Count can be retrieved both at the class (in a query filter) & at the instance level (as a property of a Post object).
  @hybrid_property
  def vote_count(self):
      return select([func.count(Vote.id)]).where(Vote.post_id == self.id)
  
  # user = relationship() is a SQLAlchemy relationship that connects Post to the User model
  user = relationship('User')
  # the Post model includes a dynamic relationship to the Comment model, meaning that a query for a comment should also include information about the author
  # the cascade='all,delete' argument in the relationship() function means that when a post is deleted, all of its associated comments should be deleted as well
  comments = relationship('Comment', cascade='all,delete')
  

  votes = relationship('Vote', cascade='all,delete')

# The Post model now has two defined relationships: one for users and one for comments. 
# Querying for a post returns both data subsets. 
# Bc the comments model also defines a relationship, querying for a post returns the comment-to-user subset as well.

# The following JSON helps conceptualize this data structure:
# {
#   "id": 1,
#   "title": "How to Learn Python",
#   "user_id": 2,
#   "user": {
#     "id": 2,
#     "username": "lernantino" // post author
#   },
#   "comments": [
#     {
#       "id": 1,
#       "comment_text": "Great article!",
#       "post_id": 1,
#       "user_id": 3,
#       "user": {
#         "id": 3,
#         "username": "someone_else" // comment author
#       }
#     }
#   ]
# }