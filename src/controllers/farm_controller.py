from datetime import datetime

from src.repositories.base_repository import BaseRepository
from fastapi import APIRouter
from pydantic import BaseModel


farm_router = APIRouter(prefix="/farm")

class Farm(BaseModel):
    id: int
    name: str
    created_at: datetime

class FarmController:
    def __init__(self, farm_repository: BaseRepository):
        self._farm_repository = farm_repository

    @farm_router.get("/{farm_id}")
    async def read_farm(self, farm_id: int):
        return self._farm_repository.get_by_id(farm_id)

    # @app.put("/farms/{farm_id}")
    # def update_farm(self, farm_id: int, farm: dict):

