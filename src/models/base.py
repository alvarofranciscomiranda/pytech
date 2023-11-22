from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel


class Base(DeclarativeBase):
    pass


# class ControllerBase(Base, BaseModel):
#     pass