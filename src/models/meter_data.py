from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from src.models.base import Base


class MeterData(Base):
    __tablename__ = "meter_data"

    meter_id = Column(Integer, ForeignKey("meter.id"), primary_key=True, nullable=False)
    read_at = Column(DateTime, primary_key=True, nullable=False)
    pac = Column(Float)
    yield_ = Column("yield", Float)
    status = Column(Float)
    error = Column(Float)
    etotal_c = Column(Float)
    pac1 = Column(Float)
    pac2 = Column(Float)
    pac3 = Column(Float)
    uac1 = Column(Float)
    uac2 = Column(Float)
    uac3 = Column(Float)
    qac1 = Column(Float)
    qac2 = Column(Float)
    qac3 = Column(Float)
    iac1 = Column(Float)
    iac2 = Column(Float)
    iac3 = Column(Float)
    fac = Column(Float)
    cos = Column(Float)
    pac_raw = Column(Float)
    etotal_forward = Column(Float)
    etotal_reverse = Column(Float)
    etotal_raw = Column(Float)

    def __repr__(self):
        return f"meter: {self.meter_id}, read_at: {self.read_at}, yield: {self.yield_}, status: {self.status}, error: {self.error}, etotal_c: {self.etotal_c}, pac1: {self.pac1}"
