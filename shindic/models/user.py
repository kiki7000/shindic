from shindic.database import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import validates

from re import match, compile


class Users(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, unique=True)
    username = Column(String, unique=True)

    @validates("email")
    def validate_email(self, _, email):
        email_regex = compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if match(email_regex, email) is None and len(email) <= 200:
            return True

        raise ValueError("Invalid email address  [INVALID_EMAIL]")
