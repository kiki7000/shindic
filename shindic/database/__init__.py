from dotenv import load_dotenv
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

__all__ = ("engine", "db_session", "Base", "get_db")

load_dotenv()

database_password = getenv("DB_PASSWORD")
database_url = f"mysql://root:{database_password}@localhost:3306/shindic"

engine = create_engine(
    database_url
)
db_session = scoped_session(sessionmaker(autoflush=False, autocommit=False, bind=engine))

Base = declarative_base()


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
