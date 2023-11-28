from sqlalchemy.exc import SQLAlchemyError
from src.repositories.base_repository import BaseRepository
from src.schemas.farm import FarmInDBBase, FarmCreate, FarmUpdate, FarmDelete
from fastapi import APIRouter, HTTPException


class FarmController:
    def __init__(self, farm_repository: BaseRepository):
        self._farm_repository = farm_repository
        self.router = APIRouter(prefix="/farm")
        self.router.add_api_route("/{farm_id}", self.read_farm, methods=["GET"], response_model=FarmInDBBase)
        self.router.add_api_route("/", self.put_farm, methods=["PUT"], response_model=FarmInDBBase)
        self.router.add_api_route("/{farm_id}", self.update_farm, methods=["POST"], response_model=FarmInDBBase)
        self.router.add_api_route("/{farm_id}", self.delete_farm, methods=["DELETE"])

    async def read_farm(self, farm_id: int):
        return self._farm_repository.get_by_id(farm_id)

    async def put_farm(self, farm: FarmCreate):
        return self._farm_repository.create(farm)

    async def update_farm(self, farm: FarmUpdate):
        updated_farm = self._farm_repository.update(farm)
        if updated_farm is None:
            raise HTTPException(status_code=404, detail="Farm not found")
        return updated_farm

    async def delete_farm(self, farm_id: int):
        try:
            delete_farm = self._farm_repository.delete(farm_id)
            if delete_farm is not None:
                raise HTTPException(status_code=404, detail="Farm not found")
        except SQLAlchemyError as error:
            raise HTTPException(status_code=422, detail={"error": str(error)})
