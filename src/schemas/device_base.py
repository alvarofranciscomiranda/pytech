from datetime import datetime
from pydantic import BaseModel


class DeviceBase(BaseModel):
    name: str


class DeviceCreate(BaseModel):
    name: str
    farm_id: int


class DeviceUpdate(BaseModel):
    name: str
    farm_id: int


# Properties shared by models stored in DB
class DeviceInDBBase(DeviceBase):
    id: int
    created_at: datetime
    farm_id: int

    class Config:
        from_attributes = True
