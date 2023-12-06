from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from src.models.base import Base
from sqlalchemy.orm import mapped_column


class Inverter(Base):
    __tablename__ = "inverter"

    id = Column(Integer, primary_key=True)
    farm_id = Column(Integer, ForeignKey("farm.id"))
    name = Column(String(60))
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"