from src.read_csv import run_function
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from src.repositories.sensor_repository import SensorRepository
from src.models.sensor import Sensor
from src.models.farm import Farm

import os


engine = create_engine(os.getenv("DB_URI"))

def app():
    with engine.connect() as conn:


        sensor_repository  = SensorRepository(conn)
        farm1 = Farm(1, "Farm1")
        sensor1 = Sensor(1, farm1, "Sensor1")
        sensor_repository.create()
        #stmt = text("select * from pg_database")
        #print(conn.execute(stmt).fetchall())


if __name__ == "__main__":

    filename = 'resources/farm_data/farm1/minute_values.csv'
    app()
    #run_function()