from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from Database import Base, engine

class User(Base):
    __tablename__ = "users"  # Lowercase and plural to follow SQL naming conventions
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    admin = Column(Boolean, default=False)
    
    # Relationship to stories
    stories = relationship("Story", back_populates="author", cascade="all, delete, delete-orphan")

class Story(Base):
    __tablename__ = "stories"  # Lowercase and plural
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    text = Column(String)
    date = Column(DateTime, default=datetime.utcfromtimestamp)  # Fixed to use datetime.utcnow()
    
    # Foreign key pointing to the User table
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="stories")  # Corrected to match the `User.stories`

# At the end of your script, add the following to create tables
Base.metadata.create_all(engine)
