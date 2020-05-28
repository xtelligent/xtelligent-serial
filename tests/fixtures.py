from dataclasses import dataclass
from xtelligent_serial import (deserializer, serializer, serialization,
    to_serializable, from_serializable)

import pytest

@serialization
class Boo:
    def __init__(self, x):
        self.root = x

    @property
    def y(self):
        return self.root * 2

    def __serializer__(cls, instance):
        return {'x': instance.root, 'y': instance.y}
    
    def __deserializer__(cls, raw_data):
        return cls(raw_data['x'])

class Yah:
    def __init__(self, x):
        self.root = x

    @property
    def y(self):
        return self.root * 2

@serializer(Yah)
def serialize_yah(yah: Yah):
    return {'x': yah.root, 'y': yah.y}

@deserializer(Yah)
def deserialize_yah(raw_data) -> Yah:
    return Yah(raw_data['x'])

@dataclass
class NoneAble:
    x: object
