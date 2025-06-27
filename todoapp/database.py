# Create database engine and session for SQLAlchemy
# This file sets up the database connection and session management for the FastAPI application.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:urpasswd@localhost/TodoApplicationDatabase'
#SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:urpasswd@localhost:3306/TodoApplicationDatabase'

#This connect_args is for sqlite only.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})
#engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
