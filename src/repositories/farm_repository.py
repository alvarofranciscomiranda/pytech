from src.models.farm import Farm
from src.repositories.base_repository import BaseRepository


class FarmRepository(BaseRepository):
    def __init__(self, session):
        super(FarmRepository, self).__init__(session, Farm)
