from datetime import datetime
from pydantic import BaseModel

from typing import Sequence


class FarmBase(BaseModel):
    id: int
    name: str
    created_at: datetime


class FarmCreate(FarmBase):
    name: str


class FarmUpdate(FarmBase):
    name: str


# Properties shared by models stored in DB
class FarmInDBBase(FarmBase):
    id: int
    name: str
    created_at: datetime

    class Config:
        orm_mode = True


