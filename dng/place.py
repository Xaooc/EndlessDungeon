from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from dng.database import Base

class Place(Base):
    __tablename__ = "place"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    ivent = Column(String)