from src.repositories.abstract_repository import IRepository
from src.models.base import Base
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


class BaseRepository(IRepository):

    def __init__(self, session, cls: Base):
        # initialize database connection
        self._session = session
        self._class: Base = cls

    def get_all(self):
        return self._session.query(self._class).all()

    def get_by_id(self, object_id):
        return self._session.query(self._class).filter(self._class.id == object_id).first()

    def create(self, obj: BaseModel):
        obj_in_data = jsonable_encoder(obj)
        db_obj = self._class(**obj_in_data)
        self._session.add(db_obj)
        self._session.commit()
        self._session.refresh(obj)
        return obj

    def update(self, obj: Base):
        new_object = self._session.query(obj.__class__).filter(self._class.id == obj.id).first()
        self._session.add(new_object)
        self._session.commit()
        self._session.refresh(obj)
        return obj

    def delete(self, obj: Base):
        delete_object = self._session.query(obj.__class__).filter(self._class.id == obj.id).first()
        self._session.delete(delete_object)
        self._session.commit()
