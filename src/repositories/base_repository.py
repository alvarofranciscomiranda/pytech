from functools import lru_cache

from sqlalchemy.exc import SQLAlchemyError
from src.repositories.abstract_repository import IRepository
from src.models.base import Base
from pydantic import BaseModel as BaseSchema
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class BaseRepository(IRepository):

    def __init__(self, session: Session, cls: Base):
        # initialize database connection
        self._session: Session = session
        self._class: Base = cls

    def get_by_id(self, object_id):
        return self._session.query(self._class).filter(self._class.id == object_id).first()

    @lru_cache
    def get_by_property(self, property, property_value):
        return self._session.query(self._class).filter(self._class.__getattribute__(self._class, property) == property_value).first()

    def get_all(self, offset: int, limit: int):
        query = self._session.query(self._class)

        # Apply offset and limit if provided
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)

        return query.all()

    def create(self, schema: BaseSchema):
        try:
            obj_in_data = jsonable_encoder(schema)
            db_obj = self._class(**obj_in_data)
            self._session.add(db_obj)
            self._session.commit()
            self._session.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as error:
            self._session.rollback()
            raise error

    def update(self, object_id: int, schema: BaseSchema):
        try:
            object_db = self._session.query(self._class).filter(self._class.id == object_id).first()
            if object_db is None:
                return
            object_db = self._update_model_from_schema(schema, object_db)
            self._session.add(object_db)
            self._session.commit()
            self._session.refresh(object_db)
            return object_db
        except SQLAlchemyError as error:
            self._session.rollback()
            raise error

    def delete(self, object_id: int):
        try:
            object_db = self._session.query(self._class).filter(self._class.id == object_id).first()
            if object_db is None:
                return "not found"
            self._session.delete(object_db)
            self._session.commit()
            return
        except SQLAlchemyError as error:
            self._session.rollback()
            raise error

    def _update_model_from_schema(self, schema: BaseSchema, model: Base):
        for k, v in schema.__dict__.items():
            if hasattr(model, k):
                setattr(model, k, v)

        return model
