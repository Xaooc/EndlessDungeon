from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from dng.database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)
    active_pers = Column(Integer)
