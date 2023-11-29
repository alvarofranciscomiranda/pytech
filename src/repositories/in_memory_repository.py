from src.repositories.abstract_repository import IRepository
from src.models.base import Base


class InMemoryRepository(IRepository):

    def __init__(self):
        self._data_source = []

    def get_all(self):
        if hasattr(self, '_data_source'):
            return self._data_source

    def get_by_id(self, object_id):
        if hasattr(self, '_data_source'):
            return next((obj for obj in self._data_source if obj.id == object_id), None)

    def create(self, obj: Base):
        if hasattr(self, '_data_source'):
            obj.id = len(self._data_source) + 1
            self._data_source.append(obj)
            return obj

    def update(self, obj_id: int, obj: Base):
        if hasattr(self, '_data_source'):
            existing_obj = next((o for o in self._data_source if o.id == obj.id), None)
            if existing_obj:
                for key, value in obj.__dict__.items():
                    setattr(existing_obj, key, value)
                return existing_obj
            else:
                return None

    def delete(self, obj: Base):
        if hasattr(self, '_data_source'):
            existing_obj = next((o for o in self._data_source if o.id == obj.id), None)
            if existing_obj:
                self._data_source.remove(existing_obj)
                return True
            else:
                return False
