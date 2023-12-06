from sqlalchemy import Column, DateTime, String, Integer, func, Float, ForeignKey
from sqlalchemy.orm import mapped_column
from src.models.base import Base

class InverterData(Base):
    __tablename__ = "inverter_data"

    inverter_id = Column(Integer, ForeignKey("inverter.id"), nullable=False)
    read_at = Column(DateTime, primary_key=True, nullable=False)
    pac = Column(Integer)
    pdc1 = Column(Integer)
    pdc2 = Column(Integer)
    pdc3 = Column(Integer)
    pdc4 = Column(Integer)
    pdc5 = Column(Integer)
    pdc6 = Column(Integer)
    yield_ = Column("yield", Integer)
    udc1 = Column(Integer)
    udc2 = Column(Integer)
    udc3 = Column(Integer)
    udc4 = Column(Integer)
    udc5 = Column(Integer)
    udc6 = Column(Integer)
    temperature = Column(Integer)
    uac = Column(Integer)
    uac1 = Column(Integer)
    uac2 = Column(Integer)
    uac3 = Column(Integer)
    status = Column(Integer)
    error = Column(Integer)
    iac = Column(Integer)
    idc1 = Column(Integer)
    idc2 = Column(Integer)
    idc3 = Column(Integer)
    idc4 = Column(Integer)
    idc5 = Column(Integer)
    idc6 = Column(Integer)
    cos = Column(Integer)
