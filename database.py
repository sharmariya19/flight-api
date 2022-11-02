from config import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Generator

SQLALCHEMY_DATABASE_URL = setting.DATABSE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()

# Dependency Injection
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
