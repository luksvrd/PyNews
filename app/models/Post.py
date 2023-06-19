# Just tech news will have a one to many relationship between users and posts
# One user can have many posts, but each post can only belong to one user
from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Post(Base):
  __tablename__ = 'posts'
  # user = relationship() is a SQLAlchemy relationship that connects Post to the User model
  # The relationship() function takes 2 arguments: the model we're relating to and the back_populates argument that references the relationship() function in the User model
  user = relationship('User')
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  # user_id is defined as a foreign key that references the users table
  user_id = Column(Integer, ForeignKey('users.id'))
  # added created_at and updated_at columns that use Pythons built in datetime module to generate timestamps
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)