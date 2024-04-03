from datetime import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, Column, JSON

Base = declarative_base()


class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    permissions = Column(JSON)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey("roles.id"))
