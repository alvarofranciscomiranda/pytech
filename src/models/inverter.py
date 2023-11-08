from sqlalchemy import Column, DateTime, String, Integer, func
from src.models.base import Base

class Inverter(Base):
    __tablename__ = "inverter"

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"