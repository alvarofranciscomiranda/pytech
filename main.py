from src.controllers.inverter_controller import InverterController
from src.controllers.meter_controller import MeterController
from src.models.meter import Meter
from sqlalchemy import create_engine

from src.repositories.abstract_repository import IRepository
from src.repositories.base_repository import BaseRepository
from src.models.sensor import Sensor
from src.models.farm import Farm
from src.models.inverter import Inverter
from src.models.base import Base
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from fastapi import FastAPI
from src.controllers.farm_controller import FarmController
from src.controllers.sensor_controller import SensorController
import os

from src.services.create_farm_from_report import FarmsDevices


def session_creator() -> Session:
    engine = create_engine(os.getenv("DB_URI"))

    # Create the tables
    Base.metadata.create_all(engine)

    # Create a session factory
    session = scoped_session(sessionmaker(bind=engine))

    return session


def app():
    app = FastAPI()
    session = session_creator()
    farm_repository: IRepository = BaseRepository(session, Farm)
    sensor_repository: IRepository = BaseRepository(session, Sensor)
    inverter_repository: IRepository = BaseRepository(session, Inverter)
    meter_repository: IRepository = BaseRepository(session, Meter)


    # Create an instance of the FarmRouter class and pass the FastAPI app instance
    farm_controller = FarmController(farm_repository)
    sensor_controller = SensorController(sensor_repository)
    inverter_controller = InverterController(inverter_repository)
    meter_controller = MeterController(meter_repository)

    # Include the router in the main FastAPI app
    app.include_router(farm_controller.router)
    app.include_router(sensor_controller.router)
    app.include_router(inverter_controller.router)
    app.include_router(meter_controller.router)

    return app


def main():
    session = session_creator()
    farm_repository: IRepository = BaseRepository(session, Farm)
    sensor_repository: IRepository = BaseRepository(session, Sensor)
    inverter_repository: IRepository = BaseRepository(session, Inverter)
    meter_repository: IRepository = BaseRepository(session, Meter)
    path = "resources/farm_data/*/"
    service = FarmsDevices(farm_repository, sensor_repository, inverter_repository, meter_repository, path)
    service.main()

if __name__ == "__main__":

    # app()
    main()
