from sqlalchemy import Column, Date, Integer, String, Boolean
from sqlalchemy.sql import func

from database import Base

class Game(Base):
    __tablename__ = "games"

    stage_number = Column(Integer, index=True, primary_key=True)
    despcription = Column(String, index=True)
    ending_date = Column(Date, server_default=func.current_date())


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, unique=True, index=True)
    stage_1 = Column(Boolean, index=True, default=False)
    stage_2 = Column(Boolean, index=True, default=False)
