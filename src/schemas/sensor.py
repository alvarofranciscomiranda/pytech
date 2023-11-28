from datetime import datetime
from pydantic import BaseModel

from typing import Sequence


class SensorBase(BaseModel):
    id: int
    name: str
    created_at: datetime
    farm_id: int


class SensorCreate(BaseModel):
    name: str
    farm_id: int


class SensorUpdate(BaseModel):
    id: int
    name: str
    farm_id: int


class SensorDelete(BaseModel):
    id: str


# Properties shared by models stored in DB
class SensorInDBBase(SensorBase):
    id: int
    name: str
    created_at: datetime
    farm_id: int

    class Config:
        orm_mode = True
