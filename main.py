from src.read_csv import run_function
from src.repositories_tests import repositories_tests, in_memory_repositories_tests
from sqlalchemy import create_engine
from src.repositories.sensor_repository import SensorRepository
from src.repositories.farm_repository import FarmRepository
from src.repositories.base_repository import BaseRepository
from src.models.sensor import Sensor
from src.models.farm import Farm
from src.models.inverter import Inverter
from src.models.base import Base
from sqlalchemy.orm import scoped_session, sessionmaker
from fastapi import FastAPI
from src.controllers.farm_controller import FarmController
import os


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None
#
#
# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
#
#
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

def session_creator():
    engine = create_engine(os.getenv("DB_URI"))

    # Create the tables
    Base.metadata.create_all(engine)

    # Create a session factory
    session = scoped_session(sessionmaker(bind=engine))

    return session


def create_routers():
    app = FastAPI()
    session = session_creator()
    farm_repository = BaseRepository(session, Farm)

    # Create an instance of the ItemRouter class and pass the FastAPI app instance
    farm_controller = FarmController(farm_repository)

    # Include the router in the main FastAPI app
    app.include_router(farm_controller.router)

    return app


if __name__ == "__main__":

    filename = 'resources/farm_data/farm1/minute_values.csv'
    #session = session_creator()
    #repositories_tests(session)
    # in_memory_repositories_tests()
    #run_function()
    create_routers()
