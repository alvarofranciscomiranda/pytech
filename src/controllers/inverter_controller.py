from typing import List, Union
from sqlalchemy.exc import SQLAlchemyError
from src.repositories.base_repository import BaseRepository
from src.schemas.inverter import InverterInDBBase, InverterCreate, InverterUpdate
from fastapi import APIRouter, HTTPException


class InverterController:
    def __init__(self, inverter_repository: BaseRepository):
        self._inverter_repository = inverter_repository
        self.router = APIRouter(prefix="/inverter", tags=["Inverters"])
        self.router.add_api_route("/{inverter_id}", self.read_inverter, methods=["GET"], response_model=InverterInDBBase)
        self.router.add_api_route("/", self.read_inverters, methods=["GET"], response_model=List[InverterInDBBase])
        self.router.add_api_route("/", self.create_inverter, methods=["POST"], response_model=InverterInDBBase)
        self.router.add_api_route("/{inverter_id}", self.update_inverter, methods=["PUT"], response_model=InverterInDBBase)
        self.router.add_api_route("/{inverter_id}", self.delete_inverter, methods=["DELETE"])

    async def read_inverter(self, inverter_id: int):
        read_inverter = self._inverter_repository.get_by_id(inverter_id)
        if read_inverter is None:
            raise HTTPException(status_code=404, detail="Inverter not found")
        return read_inverter

    async def read_inverters(self, offset: int = 0, limit: Union[int, None] = 5):
        try:
            read_inverters = self._inverter_repository.get_all(offset, limit)
            return read_inverters
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})

    async def create_inverter(self, inverter: InverterCreate):
        try:
            created_inverter = self._inverter_repository.create(inverter)
            return created_inverter
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})

    async def update_inverter(self, inverter_id: int, inverter: InverterUpdate):
        try:
            updated_inverter = self._inverter_repository.update(inverter_id, inverter)
            if updated_inverter is None:
                raise HTTPException(status_code=404, detail="Inverter not found")
            return updated_inverter
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})

    async def delete_inverter(self, inverter_id: int):
        try:
            delete_inverter = self._inverter_repository.delete(inverter_id)
            if delete_inverter is not None:
                raise HTTPException(status_code=404, detail="Inverter not found")
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})
