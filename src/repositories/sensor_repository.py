from src.models.sensor import Sensor
from src.repositories.base_repository import BaseRepository


class SensorRepository(BaseRepository):
    def __init__(self, session):
        super(SensorRepository, self).__init__(session, Sensor)
