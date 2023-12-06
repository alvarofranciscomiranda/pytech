import csv
import os
from src.models.farm import Farm
from src.models.inverter import Inverter
from src.models.meter import Meter
from src.models.sensor import Sensor
from src.repositories.abstract_repository import IRepository
from glob import glob


class FarmsDevices:

    def __init__(self, farm_repository: IRepository,
                 sensor_repository: IRepository,
                 inverter_repository: IRepository,
                 meter_repository: IRepository,
                 search_folder: str
                 ):
        self.farm_repository: IRepository = farm_repository
        self.sensor_repository: IRepository = sensor_repository
        self.inverter_repository: IRepository = inverter_repository
        self.meter_repository: IRepository = meter_repository
        self.search_folder: str = search_folder

    def parse_farm_devices(self, farm: Farm, folder):
        for file in os.listdir(folder):
            with open(folder+file,  newline='') as csvfile:
                devices = csvfile.readline()
                devices = devices.split(";")
                for device in devices:
                    if device != '""':
                        self.create_devices_from_file(device, farm)

    def parse_farm_folder(self):
        for folder in glob(self.search_folder, recursive=True):
            farm_name = folder.split(os.sep)[2]
            farm = self.farm_repository.get_by_property("name", farm_name)
            if farm is None:
                farm = Farm(name=farm_name)
                farm = self.farm_repository.create(farm)
            self.parse_farm_devices(farm, folder)

    def create_devices_from_file(self, device, farm: Farm):

        if 'Sensor' in device:
            sensor = self.sensor_repository.get_by_property("name", device)
            if sensor is None:
                farm_id = farm.id
                sensor_name = device.replace('"', '')
                new_sensor = Sensor(name=sensor_name, farm_id=farm_id)
                self.sensor_repository.create(new_sensor)

        if 'Inverter' in device:
            inverter = self.inverter_repository.get_by_property("name", device)
            if inverter is None:
                farm_id = farm.id
                inverter_name = device.replace('"', '')
                new_inverter = Inverter(name=inverter_name, farm_id=farm_id)
                self.inverter_repository.create(new_inverter)

        if 'Meter' in device:
            meter = self.meter_repository.get_by_property("name", device)
            if meter is None:
                farm_id = farm.id
                meter_name = device.replace('"', '')
                new_meter = Meter(name=meter_name, farm_id=farm_id)
                self.meter_repository.create(new_meter)
