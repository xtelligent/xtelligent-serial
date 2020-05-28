from functools import update_wrapper
from typing import Type

from .registry import register_deserializer, register_serializer
from .signatures import Serializer, Deserializer

def serializer(type: Type):
    def wrapper(func: Serializer):
        update_wrapper(wrapper, func)
        register_serializer(type, func)
        return func
    return wrapper

def deserializer(type: Type):
    def wrapper(func: Deserializer):
        update_wrapper(wrapper, func)
        register_deserializer(type, func)
        return func
    return wrapper

def serialization(Cls):
    register_serializer(Cls, lambda raw_data: Cls.__serializer__(Cls, raw_data))
    register_deserializer(Cls, lambda raw_data: Cls.__deserializer__(Cls, raw_data))
    return Cls
