from src.read_csv import run_function
from src.repositories_tests import repositories_tests
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from src.repositories.sensor_repository import SensorRepository
from src.repositories.farm_repository import FarmRepository
from src.repositories.base_repository import BaseRepository
from src.models.sensor import Sensor
from src.models.farm import Farm
from src.models.inverter import Inverter
from src.models.base import Base
from sqlalchemy.orm import scoped_session, sessionmaker
from typing import Union
from fastapi import FastAPI
import os

app = FastAPI()
def application():
    engine = create_engine(os.getenv("DB_URI"))

    # Create the tables
    Base.metadata.create_all(engine)

    # Create a session factory
    session = scoped_session(sessionmaker(bind=engine))

    #stmt = text("select * from pg_database")
    #print(conn.execute(stmt).fetchall())

    return session


if __name__ == "__main__":

    filename = 'resources/farm_data/farm1/minute_values.csv'
    session = application()
    repositories_tests(session)
    #run_function()