from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://u_gymmanager:12345@localhost:5432/gymmanager_db")

class Base(DeclarativeBase):
    pass

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()