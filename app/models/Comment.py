from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Comment(Base):
  __tablename__ = 'comments'
  id = Column(Integer, primary_key=True)
  comment_text = Column(String(255), nullable=False)
  # user_id and post_id are defined as foreign keys that reference the users and posts tables
  user_id = Column(Integer, ForeignKey('users.id'))
  post_id = Column(Integer, ForeignKey('posts.id'))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

  # Including a dynamic property here for user, meaning that a query for a comment should also include information about the author
  user = relationship('User')