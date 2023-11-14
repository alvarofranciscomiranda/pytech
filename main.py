from src.read_csv import run_function
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

import os


def app():
    engine = create_engine(os.getenv("DB_URI"))

    # Create the tables
    Base.metadata.create_all(engine)

    # Create a session factory
    session = scoped_session(sessionmaker(bind=engine))

    sensor_repository = BaseRepository(session, Sensor)
    farm_repository = FarmRepository(session)
    inverter_repository = BaseRepository(session, Inverter)

    # farms = farm_repository.get_all()
    # for f in farms:
    #     print(f)

    # new_sensor = Sensor(farm_id=1, name="Sensor5")
    # created_sensor = sensor_repository.create(new_sensor)
    # print("Created Sensor:", created_sensor)
    #
    # new_inverter = Inverter(farm_id=1, name="Inverter1")
    # created_inverter = inverter_repository.create(new_inverter)
    # print("Created Inverter:", created_inverter)

    sensor21 = sensor_repository.get_by_id(3)
    # print(sensor21.__class__)
    # print(sensor21)
    sensor21.name = "sensor421"
    sensor_repository.update(sensor21)
    print(sensor21)
    sensor_repository.delete(sensor21)
    print(sensor21)

    #
    # farms = sensor_repository.get_all()
    # for f in farms:
    #     print(f)
    #
    # created_farm = farm_repository.create(name="Farm1")
    #
    # new_sensor = Sensor(farm_id=1, name=""Sensor1")
    # created_sensor = sensor_repository.create(farm_id=1, name="Sensor1")
    # print("Created Sensor:", created_sensor)
    #
    # farm1 = Farm(id=1, name="Farm1")
    # sensor1 = Sensor(id=1, farm_id=farm1.id, name="Sensor1")
    # sensor_repository.create(sensor1)
    # stmt = text("select * from pg_database")
    # print(conn.execute(stmt).fetchall())


if __name__ == "__main__":

    filename = 'resources/farm_data/farm1/minute_values.csv'
    app()
    #run_function()