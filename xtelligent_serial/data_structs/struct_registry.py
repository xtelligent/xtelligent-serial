from abc import ABC
# from dataclasses import is_dataclass, fields
from typing import Type

from ..registry import register_deserializer, deserialize
from .struct_descriptor import DescriptorInterface

dispatcher = {}

class FamilyRegistry(ABC):
    @classmethod
    def has(cls, t: Type) -> bool:
        '''Returns True if the type is serialized by the registry.'''
        raise NotImplementedError


def register_struct_family(descriptor: DescriptorInterface) -> FamilyRegistry:

    def ds_struct(t, raw_data):
        type_fields = {f.name:f for f in descriptor.get_fields(t)}
        kwargs = {k: deserialize(type_fields[k].type, v) for k, v in raw_data.items() if k in type_fields}
        return t(**kwargs)

    def register_specific_type(t: Type):
        f = dispatcher.get(t)
        if f:
            return f
        def ds(raw_data): # pylint: disable=invalid-name
            return ds_struct(t, raw_data)
        dispatcher[t] = ds
        return ds

    class StructProxy(ABC):
        @classmethod
        def __subclasshook__(cls, subclass):
            if descriptor.is_instance(subclass):
                register_specific_type(subclass)
                return True
            return False

    def ds_hook(raw_data, **kwargs): # check kwargs for type and dispatch accordingly.
        t = kwargs.get('type')
        if not t:
            raise ValueError('No type argument supplied')
        f = dispatcher.get(t)
        if not f:
            raise NotImplementedError(f'No serializer for type {t}')
        return f(raw_data)

    register_deserializer(StructProxy, ds_hook)
    class Registry:
        @classmethod
        def has(cls, t: Type) -> bool:
            return issubclass(t, StructProxy) and t in dispatcher
    return Registry
