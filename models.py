from sqlalchemy import Column, Integer, String
from database import Base

class Dato(Base):
    __tablename__ = "datos"
    id = Column(Integer, primary_key=True, index=True)
    mensaje = Column(String, index=True)
