from pydantic import BaseModel


class BaseMessengerModel(BaseModel):
    setting2: str


class BaseSerialConfig(BaseModel):
    port: str
    baudrate: int


class SerialSendConfigV1(BaseSerialConfig):
    offset: int


class SerialConfigModelV1(BaseModel):
    client_count: int
    input_configs: list[BaseSerialConfig]
    output_configs: list[SerialSendConfigV1]
    buffer_size: int = 100
