from src.schemas.device_base import DeviceBase, DeviceCreate, DeviceUpdate, DeviceInDBBase


class SensorBase(DeviceBase):
    pass


class SensorCreate(DeviceCreate):
    pass


class SensorUpdate(DeviceUpdate):
    pass


# Properties shared by models stored in DB
class SensorInDBBase(DeviceInDBBase):
    pass
