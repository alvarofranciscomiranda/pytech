from typing import List, Union
from sqlalchemy.exc import SQLAlchemyError
from src.repositories.base_repository import BaseRepository
from src.schemas.sensor import SensorInDBBase, SensorCreate, SensorUpdate
from fastapi import APIRouter, HTTPException


class SensorController:
    def __init__(self, sensor_repository: BaseRepository):
        self._sensor_repository = sensor_repository
        self.router = APIRouter(prefix="/sensor", tags=["Sensors"])
        self.router.add_api_route("/{sensor_id}", self.read_sensor, methods=["GET"], response_model=SensorInDBBase)
        self.router.add_api_route("/", self.read_sensors, methods=["GET"], response_model=List[SensorInDBBase])
        self.router.add_api_route("/", self.create_sensor, methods=["POST"], response_model=SensorInDBBase)
        self.router.add_api_route("/{sensor_id}", self.update_sensor, methods=["PUT"], response_model=SensorInDBBase)
        self.router.add_api_route("/{sensor_id}", self.delete_sensor, methods=["DELETE"])

    async def read_sensor(self, sensor_id: int):
        read_sensor = self._sensor_repository.get_by_id(sensor_id)
        if read_sensor is None:
            raise HTTPException(status_code=404, detail="Sensor not found")
        return read_sensor

    async def read_sensors(self, offset: int = 0, limit: Union[int, None] = 5):
        try:
            read_sensors = self._sensor_repository.get_all(offset, limit)
            return read_sensors
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})

    async def create_sensor(self, sensor: SensorCreate):
        try:
            created_sensor = self._sensor_repository.create(sensor)
            return created_sensor
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})

    async def update_sensor(self, sensor_id: int, sensor: SensorUpdate):
        try:
            updated_sensor = self._sensor_repository.update(sensor_id, sensor)
            if updated_sensor is None:
                raise HTTPException(status_code=404, detail="Sensor not found")
            return updated_sensor
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})

    async def delete_sensor(self, sensor_id: int):
        try:
            delete_sensor = self._sensor_repository.delete(sensor_id)
            if delete_sensor is not None:
                raise HTTPException(status_code=404, detail="Sensor not found")
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})
