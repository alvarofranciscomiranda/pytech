import csv
import os
from glob import glob

from src.models.farm import Farm
from src.repositories.abstract_repository import IRepository


class DevicesData:

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

    def get_devices_data(self, farm: Farm, folder):
        for file in os.listdir(folder):

            with open(folder+file,  newline='') as csvfile:
                devices = csvfile.readline()
                dialect = csv.Sniffer().sniff(devices)

                devices = devices.split(";")
                measures = csvfile.readline().split(";")
                headers = ['Timestamp']

                for x in range(1, len(measures)):
                    device = devices[x] if devices[x] != '""' else device
                    device = device.replace('"', '')

                    head = measures[x]
                    head = head.replace('"', '')

                    headers.append(device + ';' + head)

                reader = csv.DictReader(csvfile, dialect=dialect, fieldnames=headers)

                for row in reader:
                    n = 0
                    for k, v in row.items():
                        if v is None:
                            continue
                        print(k, v)
                    if n == 1:
                        exit()
                    n += 1

    def get_farms_data(self):
        for folder in glob(self.search_folder, recursive=True):
            farm_name = folder.split(os.sep)[2]
            farm = self.farm_repository.get_by_property("name", farm_name)
            self.get_devices_data(farm, folder)
            break




