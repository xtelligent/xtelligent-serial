from dataclasses import dataclass
from xtelligent_serial.data_class import DataClassProxy

@dataclass
class DC:
    x: int

def test_is_instance():
    assert isinstance(DC(1), DataClassProxy)
    assert issubclass(DC, DataClassProxy)
