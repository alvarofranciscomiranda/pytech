from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from src.models.base import Base
from sqlalchemy.orm import mapped_column


class Sensor(Base):
    __tablename__ = "sensor"

    id = Column(Integer, primary_key=True)
    farm_id = mapped_column(ForeignKey("farm.id"))
    name = Column(String(60))
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, from farm: {self.farm_id}"
