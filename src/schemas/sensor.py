from datetime import datetime
from pydantic import BaseModel


class SensorBase(BaseModel):
    name: str


class SensorCreate(BaseModel):
    name: str
    farm_id: int


class SensorUpdate(BaseModel):
    id: int
    name: str
    farm_id: int


# Properties shared by models stored in DB
class SensorInDBBase(SensorBase):
    id: int
    created_at: datetime
    farm_id: int

    class Config:
        orm_mode = True
