from src.repositories.base_repository import BaseRepository
from src.repositories.farm_repository import FarmRepository
from src.repositories.in_memory_repository import InMemoryRepository
from src.models.sensor import Sensor
from src.models.farm import Farm
from src.models.inverter import Inverter
from src.models.base import Base
from sqlalchemy.orm import scoped_session


def repositories_tests(session: scoped_session):



    sensor_repository = BaseRepository(session, Sensor)
    farm_repository = BaseRepository(session, Farm)
    inverter_repository = BaseRepository(session, Inverter)

    farm21 = farm_repository.get_by_id(3)
    farm_repository.delete(farm21)
    farm22 = farm_repository.get_by_id(4)
    farm_repository.delete(farm22)
    # print(sensor21)

    # farms = farm_repository.get_all()
    # for f in farms:
    #     print(f)
    #
    # sensors = sensor_repository.get_all()
    # for f in sensors:
    #     print(f)
    #
    # new_sensor = Sensor(farm_id=1, name="Sensor5")
    # created_sensor = sensor_repository.create(new_sensor)
    # print("Created Sensor:", created_sensor)
    #
    # new_inverter = Inverter(farm_id=1, name="Inverter1")
    # created_inverter = inverter_repository.create(new_inverter)
    # print("Created Inverter:", created_inverter)
    #
    # sensor21 = sensor_repository.get_by_id(13)
    # print(sensor21.__class__)
    # print(sensor21)
    # sensor21.name = "313"
    # sensor_repository.update(sensor21)
    # print(sensor21)
    # sensor_repository.delete(sensor21)
    # print(sensor21)

    # new_sensor2 = Sensor(farm_id=1, name="Sensor1")
    # created_sensor2 = sensor_repository.create(new_sensor2)
    # print("Created Sensor:", created_sensor2)
    #
    # farm1 = Farm(id=1, name="Farm1")
    # sensor1 = Sensor(farm_id=farm1.id, name="Sensor1")
    # created_sensor3 = sensor_repository.create(sensor1)
    # print("Created Sensor:", created_sensor3)


def in_memory_repositories_tests():
    sensor_repository = InMemoryRepository()
    farm_repository = InMemoryRepository()
    inverter_repository = InMemoryRepository()

    new_farm = Farm(name="Farm55")
    farm_repository.create(new_farm)

    new_sensor = Sensor(farm_id=1, name="Sensor1")
    new_sensor2 = Sensor(farm_id=1, name="Sensor2")

    new_inverter = Inverter(farm_id=1, name="Inverter1")
    new_inverter2 = Inverter(farm_id=1, name="Inverter2")

    sensor_repository.create(new_sensor)
    sensor_repository.create(new_sensor2)

    inverter_repository.create(new_inverter)
    inverter_repository.create(new_inverter2)

    sensors = sensor_repository.get_all()
    for f in sensors:
        print(f)

    sensor11 = sensor_repository.get_by_id(2)
    sensor11.name = "novo_nome"

    sensors = sensor_repository.get_all()
    for f in sensors:
        print(f)

    sensor_repository.delete(sensor11)

    sensors = sensor_repository.get_all()
    for f in sensors:
        print(f)





