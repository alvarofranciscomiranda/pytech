from typing import List, Union
from sqlalchemy.exc import SQLAlchemyError
from src.repositories.base_repository import BaseRepository
from src.schemas.meter import MeterInDBBase, MeterCreate, MeterUpdate
from fastapi import APIRouter, HTTPException


class MeterController:
    def __init__(self, meter_repository: BaseRepository):
        self._meter_repository = meter_repository
        self.router = APIRouter(prefix="/meter", tags=["Meters"])
        self.router.add_api_route("/{meter_id}", self.read_meter, methods=["GET"], response_model=MeterInDBBase)
        self.router.add_api_route("/", self.read_meters, methods=["GET"], response_model=List[MeterInDBBase])
        self.router.add_api_route("/", self.create_meter, methods=["POST"], response_model=MeterInDBBase)
        self.router.add_api_route("/{meter_id}", self.update_meter, methods=["PUT"], response_model=MeterInDBBase)
        self.router.add_api_route("/{meter_id}", self.delete_meter, methods=["DELETE"])

    async def read_meter(self, meter_id: int):
        read_meter = self._meter_repository.get_by_id(meter_id)
        if read_meter is None:
            raise HTTPException(status_code=404, detail="Meter not found")
        return read_meter

    async def read_meters(self, offset: int = 0, limit: Union[int, None] = 5):
        try:
            read_meters = self._meter_repository.get_all(offset, limit)
            return read_meters
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})

    async def create_meter(self, meter: MeterCreate):
        try:
            created_meter = self._meter_repository.create(meter)
            return created_meter
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})

    async def update_meter(self, meter_id: int, meter: MeterUpdate):
        try:
            updated_meter = self._meter_repository.update(meter_id, meter)
            if updated_meter is None:
                raise HTTPException(status_code=404, detail="Meter not found")
            return updated_meter
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})

    async def delete_meter(self, meter_id: int):
        try:
            delete_meter = self._meter_repository.delete(meter_id)
            if delete_meter is not None:
                raise HTTPException(status_code=404, detail="Meter not found")
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})
