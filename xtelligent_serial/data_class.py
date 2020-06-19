from abc import ABC
from dataclasses import is_dataclass, fields
from typing import Type

from .registry import register_deserializer, deserialize

dispatcher = {}

def ds_dataclass(type, raw_data):
    type_fields = {f.name:f for f in fields(type)}
    kwargs = {k: deserialize(type_fields[k].type, v) for k, v in raw_data.items() if k in type_fields}
    return type(**kwargs)

def register_specific_type(type: Type):
    f = dispatcher.get(type)
    if f:
        return f
    def ds(raw_data):
        return ds_dataclass(type, raw_data)
    dispatcher[type] = ds
    return ds

class DataClassProxy(ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        if is_dataclass(subclass):
            register_specific_type(subclass)
            return True
        return False

def ds_hook(raw_data, **kwargs): # check kwargs for type and dispatch accordingly.
    type = kwargs.get('type')
    if not type:
        raise ValueError('No type argument supplied')
    f = dispatcher.get(type)
    if not f:
        raise NotImplementedError(f'No serializer for type {type}')
    return f(raw_data)


register_deserializer(DataClassProxy, ds_hook)
