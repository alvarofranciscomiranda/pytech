from src.schemas.device_base import DeviceBase, DeviceCreate, DeviceUpdate, DeviceInDBBase


class InverterBase(DeviceBase):
    pass


class InverterCreate(DeviceCreate):
    pass


class InverterUpdate(DeviceUpdate):
    pass


# Properties shared by models stored in DB
class InverterInDBBase(DeviceInDBBase):
    pass
