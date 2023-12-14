from abc import ABC, abstractmethod
from src.models.base import Base
from pydantic import BaseModel as BaseSchema


class IDataRepository(ABC):

    @abstractmethod
    def bulk_insert_data(self, data_list):
        raise NotImplementedError

    def my_bulk_update(self, cls: Base, data: list, keys):
        pass