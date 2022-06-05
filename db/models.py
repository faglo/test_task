from enum import unique
from db.engine import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql.array import ARRAY


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True)
    spent_money = Column(Integer)
    gems = Column(ARRAY(String), server_default="{}")
