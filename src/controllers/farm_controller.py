from src.repositories.base_repository import BaseRepository
from src.schemas.farm import FarmInDBBase, FarmCreate
from fastapi import APIRouter


class FarmController:
    def __init__(self, farm_repository: BaseRepository):
        self._farm_repository = farm_repository
        self.router = APIRouter(prefix="/farm")
        self.router.add_api_route("/{farm_id}", self.read_farm, methods=["GET"], response_model=FarmInDBBase)
        self.router.add_api_route("/", self.put_farm, methods=["PUT"], response_model=FarmInDBBase)

    async def read_farm(self, farm_id: int):
        return self._farm_repository.get_by_id(farm_id)

    async def put_farm(self, farm: FarmCreate):
        return self._farm_repository.create(farm)



# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}