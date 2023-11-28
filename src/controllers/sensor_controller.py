from src.repositories.base_repository import BaseRepository
from src.schemas.sensor import SensorInDBBase, SensorCreate, SensorUpdate, SensorDelete
from fastapi import APIRouter, HTTPException


class SensorController:
    def __init__(self, sensor_repository: BaseRepository):
        self._sensor_repository = sensor_repository
        self.router = APIRouter(prefix="/sensor")
        self.router.add_api_route("/{sensor_id}", self.read_sensor, methods=["GET"], response_model=SensorInDBBase)
        self.router.add_api_route("/", self.put_sensor, methods=["PUT"], response_model=SensorInDBBase)
        self.router.add_api_route("/{sensor_id}", self.update_sensor, methods=["POST"], response_model=SensorInDBBase)
        self.router.add_api_route("/{sensor_id}", self.delete_sensor, methods=["DELETE"])

    async def read_sensor(self, sensor_id: int):
        return self._sensor_repository.get_by_id(sensor_id)

    async def put_sensor(self, sensor: SensorCreate):
        return self._sensor_repository.create(sensor)

    async def update_sensor(self, sensor: SensorUpdate):
        updated_sensor = self._sensor_repository.update(sensor)
        if updated_sensor is None:
            raise HTTPException(status_code=404, detail="Sensor not found")
        return updated_sensor

    async def delete_sensor(self, sensor: SensorDelete):
        delete_sensor = self._sensor_repository.delete(sensor)
        if delete_sensor is not None:
            raise HTTPException(status_code=404, detail="Sensor not found")
