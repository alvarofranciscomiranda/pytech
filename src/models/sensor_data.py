from sqlalchemy import Column, DateTime, String, Integer, func, Float, ForeignKey
from sqlalchemy.orm import mapped_column
from src.models.base import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    sensor_id = mapped_column(ForeignKey("sensor.id"), primary_key=True)
    read_at = Column(DateTime, primary_key=True)
    irradiation = Column(Integer)
    module_temperature = Column(Integer)
    ambient_temperature = Column(Integer)
    wind_velocity = Column(Float)
    insolation = Column(Integer)
    status = Column(Integer)
    etotal_C = Column(Integer)