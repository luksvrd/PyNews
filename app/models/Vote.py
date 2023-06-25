from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey

# The Vote model will be used to track which users voted on which posts 
# by creating a many-to-many relationship between the two tables.
class Vote(Base):
  __tablename__ = 'votes'
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  post_id = Column(Integer, ForeignKey('posts.id'))