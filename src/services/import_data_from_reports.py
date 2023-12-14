import csv
import os
from glob import glob
from src.repositories.abstract_data_repository import IDataRepository
from src.repositories.abstract_repository import IRepository
from src.models.sensor_data import SensorData
from src.models.inverter_data import InverterData
from src.models.meter_data import MeterData


class DevicesData:

    def __init__(self, farm_repository: IRepository,
                 sensor_repository: IRepository,
                 inverter_repository: IRepository,
                 meter_repository: IRepository,
                 device_data_repository: IDataRepository,
                 search_folder: str
                 ):
        self.farm_repository: IRepository = farm_repository
        self.sensor_repository: IRepository = sensor_repository
        self.inverter_repository: IRepository = inverter_repository
        self.meter_repository: IRepository = meter_repository
        self.device_data_repository: IDataRepository = device_data_repository
        self.search_folder: str = search_folder

    def create_devices_data(self, timestamp, row):

        separated_dicts = {}
        for key, value in row.items():

            if key == '\n|\n':
                continue

            # Extract the left part of the key before '|'
            device = key.split('|')[0].strip()

            # Check if the left part is already a key in the separated_dicts
            if device not in separated_dicts:
                separated_dicts[device] = {}

            # Add the key-value pair to the corresponding separated dictionary
            separated_dicts[device][key] = value

        # remove device name from measures names
        for device, device_data in separated_dicts.items():
            updated_device_data = {}

            for key, value in device_data.items():
                measure = key.split('|')[-1].strip()
                # Update the key based on your mapping
                if measure in self.tag_to_column_mapping:
                    updated_key = self.tag_to_column_mapping[measure]
                else:
                    updated_key = key

                # Update the dictionary with the new key-value pair
                updated_device_data[updated_key] = value

            updated_device_data['read_at'] = timestamp

            # Update the original dictionary with the modified device_data
            separated_dicts[device] = updated_device_data

            if 'Sensor' in device:
                sensor = self.sensor_repository.get_by_property("name", device)
                sensor_data = SensorData(sensor_id=sensor.id, **updated_device_data)
                # print(f"Device: {sensor}")
                yield sensor_data
            if 'Inverter' in device:
                inverter = self.inverter_repository.get_by_property("name", device)
                inverter_data = InverterData(inverter_id=inverter.id, **updated_device_data)
                # print(f"Device: {inverter}")
                yield inverter_data
            if 'Meter' in device:
                meter = self.meter_repository.get_by_property("name", device)
                meter_data = MeterData(meter_id=meter.id, **updated_device_data)
                # print(f"Device: {meter_data}")
                yield meter_data

    def get_devices_data(self, folder):

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
                    if device == "":
                        continue

                    headers.append(device + '|' + head)

                reader = csv.DictReader(csvfile, dialect=dialect, fieldnames=headers)
                sensor_data = []
                inverter_data = []
                meter_data = []
                for row in reader:

                    if row.get("Timestamp") is None or row.get("Timestamp") == "":
                        continue
                    timestamp = row.pop("Timestamp")

                    for k, v in row.items():

                        # catch irrelevant rows
                        if v == "":
                            continue
                        try:
                            float(v)
                        except ValueError or TypeError as e:
                            print(k, v, e)
                            exit()

                    for device_data in self.create_devices_data(timestamp, row):
                        if isinstance(device_data, SensorData):
                            sensor_data.append(device_data.__dict__)
                        if isinstance(device_data, InverterData):
                            inverter_data.append(device_data.__dict__)
                        if isinstance(device_data, MeterData):
                            meter_data.append(device_data.__dict__)

                # self.device_data_repository.bulk_insert_data(devices_data)
                self.device_data_repository.my_bulk_update(MeterData, meter_data)

    def get_farms_data(self):
        for folder in glob(self.search_folder, recursive=True):
            self.get_devices_data(folder)
            break

    # Create a tag-to-column mapping
    tag_to_column_mapping = {
            'Irradiation (W/m2)': 'irradiation',
            'Module temperature (°C)': 'module_temperature',
            'Ambient temperature (°C)': 'ambient_temperature',
            'Wind velocity (m/s) ': 'wind_velocity',
            'Insolation (Wh/m2)': 'insolation',
            'Status': 'status',
            'Etotal_C (WattEver)': 'etotal_c',
            'pac': 'Pac (W)',
            'Pdc1 (W)': 'pdc1',
            'Pdc2 (W)': 'pdc2',
            'Pdc3 (W)': 'pdc3',
            'Pdc4 (W)': 'pdc4',
            'Pdc5 (W)': 'pdc5',
            'Pdc6 (W)': 'pdc6',
            'Udc1 (V)': 'udc1',
            'Udc2 (V)': 'udc2',
            'Udc3 (V)': 'udc3',
            'Udc4 (V)': 'udc4',
            'Udc5 (V)': 'udc5',
            'Udc6 (V)': 'udc6',
            'Temperature (°C)': 'temperature',
            'Error': 'error',
            'Uac (V)': 'uac',
            'Uac1 (V)': 'uac1',
            'Uac2 (V)': 'uac2',
            'Uac3 (V)': 'uac3',
            'Idc1 (mA)': 'idc1',
            'Idc2 (mA)': 'idc2',
            'Idc3 (mA)': 'idc3',
            'Idc4 (mA)': 'idc4',
            'Idc5 (mA)': 'idc5',
            'Idc6 (mA)': 'idc6',
            'Cos(Phi)': 'cos',
            'Yield (Wh)': 'yield_',
            'Iac (mA)': 'iac',
            'Iac1 (mA)': 'iac1',
            'Iac2 (mA)': 'iac2',
            'Iac3 (mA)': 'iac3',
            'Pac (W)': 'pac',
            'Pac1 (W)': 'pac1',
            'Pac2 (W)': 'pac2',
            'Pac3 (W)': 'pac3',
            'Qac1 (var)': 'qac1',
            'Qac2 (var)': 'qac2',
            'Qac3 (var)': 'qac3',
            'Fac (Hz)': 'fac',
            'Pac raw (W)': 'pac_raw',
            'Etotal Forward (Wh)': 'etotal_forward',
            'Etotal Reverse (Wh)': 'etotal_reverse',
            'Etotal Raw (Wh)': 'etotal_raw',
            'Timestamp': 'read_at'
        }
