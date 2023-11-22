from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from src.models.base import Base
from sqlalchemy.orm import relationship

class Sensor(Base):
    __tablename__ = "sensor"

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    created_at = Column(DateTime, default=func.now())
    farm_id = Column(String(60), ForeignKey("farm.id"), nullable=True)
    owner = relationship("Farm", back_populates="sensors")

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, from farm: {self.farm_id}"
