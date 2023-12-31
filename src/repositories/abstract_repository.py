from abc import ABC, abstractmethod
from src.models.base import Base
from pydantic import BaseModel as BaseSchema


class IRepository(ABC):
    @abstractmethod
    def get_all(self, offset: int, limit: int):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def get_by_property(self, property, property_value):
        raise NotImplementedError

    @abstractmethod
    def create(self, item):
        raise NotImplementedError

    @abstractmethod
    def update(self, id, item):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError

    @abstractmethod
    def _update_model_from_schema(self, schema: BaseSchema, model: Base):
        raise NotImplementedError
