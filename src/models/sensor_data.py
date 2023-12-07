from sqlalchemy import Column, DateTime, String, Integer, func, Float, ForeignKey
from sqlalchemy.orm import mapped_column
from src.models.base import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    sensor_id = Column(Integer, ForeignKey("sensor.id"), nullable=False)
    read_at = Column(DateTime, primary_key=True, nullable=False)
    irradiation = Column(Integer)
    module_temperature = Column(Integer)
    ambient_temperature = Column(Integer)
    wind_velocity = Column(Float)
    insolation = Column(Integer)
    status = Column(Integer)
    etotal_C = Column(Integer)

    def __repr__(self):
        return f"sensor: {self.sensor_id}, timestamp: {self.read_at}"
