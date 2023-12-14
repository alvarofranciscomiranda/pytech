from sqlalchemy import inspect
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import Session
from src.models.base import Base
from src.models.inverter_data import InverterData
from src.models.meter_data import MeterData
from src.models.sensor_data import SensorData
from src.repositories.abstract_data_repository import IDataRepository


class DeviceDataRepository(IDataRepository):
    def __init__(self, session: Session):
        self._session: Session = session

    def my_bulk_update(self, cls: Base, data: list):
        table = cls.__table__
        stmt = insert(table)
        primary_keys = [key.name for key in inspect(table).primary_key]
        update_dict = {c.name: c for c in stmt.excluded if not c.primary_key}

        stmt = stmt.on_conflict_do_update(index_elements=primary_keys, set_=update_dict)
        self._session.execute(stmt, data)
        self._session.commit()

    def bulk_insert_data(self, data_list):
        try:
            for device_data in data_list:
                existing_data = self.check_existing_data(device_data)
                if existing_data is None:
                    self._session.add(device_data)
                    self._session.commit()
        except IntegrityError as error:
            # Handle any integrity errors (e.g., unique constraint violations)
            self._session.rollback()
            raise error

    # def bulk_insert_data(self, data_list):
        #     self._session.bulk_save_objects(data_list)
        #     self._session.commit()
        # except SQLAlchemyError as error:
        #     self._session.rollback()
        #     raise error

    def check_existing_data(self, data):
        # Determine the ID column and value based on the type of data
        if isinstance(data, MeterData):
            id_value = data.meter_id
            existing_data = (
                self._session.query(type(data))
                .filter(type(data).meter_id == id_value, type(data).read_at == data.read_at)
                .first()
            )
        elif isinstance(data, InverterData):
            id_value = data.inverter_id
            existing_data = (
                self._session.query(type(data))
                .filter(type(data).inverter_id == id_value, type(data).read_at == data.read_at)
                .first()
            )
        elif isinstance(data, SensorData):
            id_value = data.sensor_id
            existing_data = (
                self._session.query(type(data))
                .filter(type(data).sensor_id == id_value, type(data).read_at == data.read_at)
                .first()
            )
        else:
            # Handle unknown data type
            raise ValueError("Unknown data type")

        return existing_data
