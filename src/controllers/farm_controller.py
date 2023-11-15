from src.repositories.base_repository import BaseRepository


class FarmController():
    def __int__(self, farm_repository: BaseRepository):
        self._farm_repository = farm_repository
