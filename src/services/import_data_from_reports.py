import csv
import os
from glob import glob

from src.models.base import Base
from src.models.farm import Farm
from src.repositories.abstract_repository import IRepository
from src.models.sensor_data import SensorData
from src.models.inverter_data import InverterData
from src.models.meter_data import MeterData


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

    def create_devices_data(self, timestamp, row):
        # print(timestamp)

        result = {}

        for k, v in row.items():
            device, measure = k.split('|')
            if device not in result:
                result[device] = {}

            result[device][measure] = v

        for device, measures_data in result.items():
            is_last_device = list(result.keys())[-1]
            if device == is_last_device:
                continue

            if 'Sensor' in device:
                sensor_id = self.sensor_repository.get_by_property("name", device)
                sensor_data = SensorData(sensor_id=sensor_id, read_at=timestamp)
                self.associate_data_sensor(sensor_data, measures_data)
                # print(f"Device: {device}")
            if 'Inverter' in device:
                inverter_id = self.inverter_repository.get_by_property("name", device)
                inverter_data = InverterData(inverter_id=inverter_id, read_at=timestamp)
                self.associate_data_inverter(inverter_data, measures_data)
                # print(f"Device: {device}")
            if 'Meter' in device:
                meter_id = self.meter_repository.get_by_property("name", device)
                meter_data = MeterData(meter_id=meter_id, read_at=timestamp)
                self.associate_data_meter(meter_data, measures_data)
                # print(f"Device: {device}")


        exit()

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

                self.create_devices_data(timestamp, row)

    def get_farms_data(self):
        for folder in glob(self.search_folder, recursive=True):
            farm_name = folder.split(os.sep)[2]
            farm = self.farm_repository.get_by_property("name", farm_name)
            self.get_devices_data(folder)
            break

    def associate_data_sensor(self, sensor_data: SensorData, measures_data):

        sensor_data.irradiation = measures_data.get("Irradiation (W/m2)")
        sensor_data.module_temperature = measures_data.get("Module temperature (°C)")
        sensor_data.ambient_temperature = measures_data.get("Ambient temperature (°C)")
        sensor_data.wind_velocity = measures_data.get("Wind velocity (m/s)")
        sensor_data.insolation = measures_data.get("Insolation (Wh/m2)")
        sensor_data.status = measures_data.get("Status")
        sensor_data.etotal_C = measures_data.get("Etotal_C (WattEver)al")

    def associate_data_inverter(self, inverter_data: InverterData, measures_data):

        inverter_data.pac = measures_data.get("Pac (W)")
        inverter_data.pdc1 = measures_data.get("Pdc1 (W)")
        inverter_data.pdc2 = measures_data.get("Pdc2 (W)")
        inverter_data.pdc3 = measures_data.get("Pdc3 (W)")
        inverter_data.pdc4 = measures_data.get("Pdc4 (W)")
        inverter_data.pdc5 = measures_data.get("Pdc5 (W)")
        inverter_data.pdc6 = measures_data.get("Pdc6 (W)")
        inverter_data.udc1 = measures_data.get("Udc1 (V)")
        inverter_data.udc2 = measures_data.get("Udc2 (V)")
        inverter_data.udc3 = measures_data.get("Udc3 (V)")
        inverter_data.udc4 = measures_data.get("Udc4 (V)")
        inverter_data.udc5 = measures_data.get("Udc5 (V)")
        inverter_data.udc6 = measures_data.get("Udc6 (V)")
        inverter_data.temperature = measures_data.get("Temperature (°C)")
        inverter_data.status = measures_data.get("Status")
        inverter_data.error = measures_data.get("Error")
        inverter_data.uac = measures_data.get("Uac (V)")
        inverter_data.uac1 = measures_data.get("Uac1 (V)")
        inverter_data.uac2 = measures_data.get("Uac2 (V)")
        inverter_data.uac3 = measures_data.get("Uac3 (V)")
        inverter_data.idc1 = measures_data.get("Idc1 (mA)")
        inverter_data.idc2 = measures_data.get("Idc2 (mA)")
        inverter_data.idc3 = measures_data.get("Idc3 (mA)")
        inverter_data.idc4 = measures_data.get("Idc4 (mA)")
        inverter_data.idc5 = measures_data.get("Idc5 (mA)")
        inverter_data.idc6 = measures_data.get("Idc6 (mA)")
        inverter_data.cos = measures_data.get("Cos(Phi)")
        inverter_data.yield_ = measures_data.get("Yield (Wh)")
        inverter_data.iac = measures_data.get("Iac (mA)")
        inverter_data.iac1 = measures_data.get("Iac1 (mA)")
        inverter_data.iac2 = measures_data.get("Iac2 (mA)")
        inverter_data.iac3 = measures_data.get("Iac3 (mA)")


    def associate_data_meter(self, meter_data: MeterData, measures_data):

        meter_data.pac = measures_data.get("Pac (W)")
        meter_data.status = measures_data.get("Status")
        meter_data.error = measures_data.get("Error")
        meter_data.pac1 = measures_data.get("Pac1 (W)")
        meter_data.pac2 = measures_data.get("Pac2 (W)")
        meter_data.pac3 = measures_data.get("Pac3 (W)")
        meter_data.uac1 = measures_data.get("Uac1 (V)")
        meter_data.uac2 = measures_data.get("Uac2 (V)")
        meter_data.uac3 = measures_data.get("Uac3 (V)")
        meter_data.qac1 = measures_data.get("Qac1 (var)")
        meter_data.qac2 = measures_data.get("Qac2 (var)")
        meter_data.qac3 = measures_data.get("Qac3 (var)")
        meter_data.iac1 = measures_data.get("Iac1 (mA)")
        meter_data.iac2 = measures_data.get("Iac2 (mA)")
        meter_data.iac3 = measures_data.get("Iac3 (mA)")
        meter_data.fac = measures_data.get("Fac (Hz)")
        meter_data.cos = measures_data.get("Cos(Phi)")
        meter_data.pac_raw = measures_data.get("Pac raw (W)")
        meter_data.etotal_c = measures_data.get("Etotal_C (WattEver)")
        meter_data.etotal_forward = measures_data.get("Etotal Forward (Wh)")
        meter_data.etotal_reverse = measures_data.get("Etotal Reverse (Wh)")
        meter_data.etotal_raw = measures_data.get("Etotal Raw (Wh)")
        meter_data.yield_ = measures_data.get("Yield (Wh)")



        # model_data_attributes = dir(meter_data)
        # Filter out attributes you don't want to consider
        # valid_model_attributes = \
        #     [attr for attr in model_data_attributes
        #      if not callable(getattr(meter_data, attr))
        #      and not attr.startswith('_')
        #      and attr not in ('registry', 'metadata')]

        # print(valid_model_attributes)
        # for measure, value in measures_data.items():
        #
        #     print(f"  Measure: {measure}, Value: {value}")


