import os

from src.models.farm import Farm
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

    def main(self):
        for folder in glob(self.search_folder, recursive=True):
            farm_name = folder.split(os.sep)[2]
            farm = Farm(name=farm_name)
            self.farm_repository.create(farm)

            print(farm_name)
