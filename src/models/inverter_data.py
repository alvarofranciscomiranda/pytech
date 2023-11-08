from sqlalchemy import Column, DateTime, String, Integer, func, Float, ForeignKey
from sqlalchemy.orm import mapped_column
from src.models.base import Base

class InverterData(Base):
    __tablename__ = "inverter_data"

    inverter_id = mapped_column(ForeignKey("inverter.id"), primary_key=True)
    read_at = Column(DateTime, primary_key=True)
    pac = Column(Integer)
    pdc1 = Column(Integer)
    pdc2 = Column(Integer)
    pdc3 = Column(Integer)
    pdc4 = Column(Integer)
    yld = Column(Integer)
    udc1 = Column(Integer)
    udc2 = Column(Integer)
    udc3 = Column(Integer)
    udc4 = Column(Integer)
    temperature = Column(Integer)
    uac = Column(Integer)
    status = Column(Integer)
    error = Column(Integer)
    iac = Column(Integer)
    idc1 = Column(Integer)
    idc2 = Column(Integer)
    idc3 = Column(Integer)
    idc4 = Column(Integer)