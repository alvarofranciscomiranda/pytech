from sqlalchemy import Column, DateTime, String, Integer, func, Float, ForeignKey
from sqlalchemy.orm import mapped_column
from src.models.base import Base

class InverterData(Base):
    __tablename__ = "inverter_data"

    inverter_id = Column(Integer, ForeignKey("inverter.id"), primary_key=True, nullable=False)
    read_at = Column(DateTime, primary_key=True, nullable=False)
    pac = Column(Float)
    pdc1 = Column(Float)
    pdc2 = Column(Float)
    pdc3 = Column(Float)
    pdc4 = Column(Float)
    pdc5 = Column(Float)
    pdc6 = Column(Float)
    yield_ = Column("yield", Float)
    udc1 = Column(Float)
    udc2 = Column(Float)
    udc3 = Column(Float)
    udc4 = Column(Float)
    udc5 = Column(Float)
    udc6 = Column(Float)
    temperature = Column(Float)
    uac = Column(Float)
    uac1 = Column(Float)
    uac2 = Column(Float)
    uac3 = Column(Float)
    status = Column(Float)
    error = Column(Float)
    iac = Column(Float)
    idc1 = Column(Float)
    idc2 = Column(Float)
    idc3 = Column(Float)
    idc4 = Column(Float)
    idc5 = Column(Float)
    idc6 = Column(Float)
    cos = Column(Float)
    iac1 = Column(Float)
    iac2 = Column(Float)
    iac3 = Column(Float)

    def __repr__(self):
        return f"inverter: {self.inverter_id}, timestamp: {self.read_at}"
