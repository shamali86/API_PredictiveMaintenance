from pydantic import BaseModel

class MachineFailure(BaseModel):
    airtemperature: float
    processtemperature: float
    rotationalspeed: float
    torque: float
    toolwear: float