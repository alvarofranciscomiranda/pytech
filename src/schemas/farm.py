from datetime import datetime
from pydantic import BaseModel

from typing import Sequence


class FarmBase(BaseModel):
    id: int
    name: str
    created_at: datetime


class FarmCreate(BaseModel):
    name: str


class FarmUpdate(BaseModel):
    id: int
    name: str


class FarmDelete(BaseModel):
    id: int


# Properties shared by models stored in DB
class FarmInDBBase(FarmBase):
    id: int
    name: str
    created_at: datetime

    class Config:
        orm_mode = True


