from src.schemas.device_base import DeviceBase, DeviceCreate, DeviceUpdate, DeviceInDBBase


class MeterBase(DeviceBase):
    pass


class MeterCreate(DeviceCreate):
    pass


class MeterUpdate(DeviceUpdate):
    pass


# Properties shared by models stored in DB
class MeterInDBBase(DeviceInDBBase):
    pass
