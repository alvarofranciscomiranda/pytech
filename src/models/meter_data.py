from sqlalchemy import Column, DateTime, String, Integer, func, Float, ForeignKey
from sqlalchemy.orm import mapped_column
from src.models.base import Base

class MeterData(Base):
    __tablename__ = "meter_data"

    meter_id = mapped_column(ForeignKey("meter.id"), primary_key=True)
    read_at = Column(DateTime, primary_key=True)
    pac = Column(Integer)
    yiel = Column(Integer)
    status = Column(Integer)
    error = Column(Integer)
    etotal_c = Column(Integer)
    pac1 = Column(Integer)
    pac2 = Column(Integer)
    pac3 = Column(Integer)
    uac1 = Column(Integer)
    uac2 = Column(Integer)
    uac3 = Column(Integer)
    qac1 = Column(Integer)
    qac2 = Column(Integer)
    qac3 = Column(Integer)
    iac1 = Column(Integer)
    iac2 = Column(Integer)
    iac3 = Column(Integer)
    fac = Column(Integer)
    cos = Column(Integer)
    pac_raw = Column(Integer)
    etotal_forward = Column(Integer)
    etotal_reverse = Column(Integer)
    etotal_raw = Column(Integer)