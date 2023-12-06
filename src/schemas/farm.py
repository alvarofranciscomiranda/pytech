from datetime import datetime
from pydantic import BaseModel


class FarmBase(BaseModel):
    name: str


class FarmCreate(BaseModel):
    name: str


class FarmUpdate(BaseModel):
    name: str


# Properties shared by models stored in DB
class FarmInDBBase(FarmBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


