from dataclasses import fields

import attr
from xtelligent_serial.data_structs.struct_registry import register_struct_family
from .fixtures import DataClass, AttrsClass, dataclass_descriptor, attrs_descriptor  # pylint: disable=unused-import

# pylint: disable=redefined-outer-name

def test_dataclass_descript(dataclass_descriptor):
    registry = register_struct_family(dataclass_descriptor)
    assert registry.has(DataClass)
    assert not registry.has(AttrsClass)
    assert not registry.has(object)

def test_attrs_descript(attrs_descriptor):
    registry = register_struct_family(attrs_descriptor)
    assert registry.has(AttrsClass)
    assert not registry.has(DataClass)
    assert not registry.has(object)
