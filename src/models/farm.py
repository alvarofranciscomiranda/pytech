from sqlalchemy import Column, DateTime, String, Integer, func
from src.models.base import Base
from sqlalchemy.orm import relationship


class Farm(Base):
    __tablename__ = "farm"

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    created_at = Column(DateTime, default=func.now())
    sensors = relationship(
        "Sensor",
        cascade="all,delete-orphan",
        back_populates="owner",
        uselist=True,
    )

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"