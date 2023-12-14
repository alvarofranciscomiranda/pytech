from sqlalchemy import Column, DateTime, String, Integer, func, Float, ForeignKey
from sqlalchemy.orm import mapped_column
from src.models.base import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    sensor_id = Column(Integer, ForeignKey("sensor.id"), primary_key=True, nullable=False)
    read_at = Column(DateTime, primary_key=True, nullable=False)
    irradiation = Column(Float)
    module_temperature = Column(Float)
    ambient_temperature = Column(Float)
    wind_velocity = Column(Float)
    insolation = Column(Float)
    status = Column(Float)
    etotal_c = Column(Float)

    def __repr__(self):
        return f"sensor: {self.sensor_id}, timestamp: {self.read_at}"
