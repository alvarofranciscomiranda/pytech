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

    def get_all(self):
        return self._session.query(self._class).all()

    def get_by_id(self, object_id):
        return self._session.query(self._class).filter(self._class.id == object_id).first()

    def create(self, schema: BaseSchema):
        obj_in_data = jsonable_encoder(schema)
        db_obj = self._class(**obj_in_data)
        self._session.add(db_obj)
        self._session.commit()
        self._session.refresh(db_obj)
        return db_obj

    def update(self, schema: BaseSchema):
        object_db = self._session.query(self._class).filter(self._class.id == schema.id).first()
        if object_db is None:
            return
        object_db = self._update_model_from_schema(schema, object_db)
        self._session.add(object_db)
        self._session.commit()
        self._session.refresh(object_db)
        return object_db

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
