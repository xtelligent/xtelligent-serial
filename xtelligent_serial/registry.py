from collections.abc import Sequence, Iterable, Mapping
from functools import singledispatch
from inspect import ismethod, isfunction, signature
from typing import Any, Type

from .signatures import JSONSerializable, Serializer, Deserializer

# pylint: disable=redefined-builtin, unused-argument

def iscallable(v):
    return ismethod(v) or isfunction(v)

def props(target):
    return {k: v for k, v in [(k, getattr(target, k)) for k in dir(target) if not k.startswith('_')] if not iscallable(v)}

@singledispatch
def serialize(target) -> JSONSerializable:
    return None if target is None else serialize(props(target))

@serialize.register
def _(target: Mapping) -> JSONSerializable:
    return {k: serialize(v) for k, v in target.items()}

@serialize.register
def _(target: Sequence) -> JSONSerializable:
    return [serialize(item) for item in list(target)]

@serialize.register
def _(target: Iterable) -> JSONSerializable:
    return [serialize(item) for item in target]

@serialize.register
def _(target: int) -> JSONSerializable:
    return target

@serialize.register
def _(target: float) -> JSONSerializable:
    return target

@serialize.register
def _(target: bool) -> JSONSerializable:
    return target

@serialize.register
def _(target: str) -> JSONSerializable:
    return target

TYPEKEY = '?__type__?'

# def fjd_for_dataclass(type, raw_data):
#     type_fields = {f.name:f for f in fields(type)}
#     kwargs = {k: deserialize(type_fields[k].type, v) for k, v in raw_data.items() if k in type_fields}
#     return type(**kwargs)

@singledispatch
def fjd(raw_data: JSONSerializable, **kwargs) -> Any:
    if raw_data is None:
        return None
    # t = raw_data.get(TYPEKEY) or type(object)
    # if is_dataclass(t):
    #     return fjd_for_dataclass(t, raw_data)
    raise ValueError(f'No deserialization method for {raw_data}')



def deserialize(type: Type, raw_data: JSONSerializable) -> Any:
    func = fjd.dispatch(type)
    if not func:
        raise ValueError(f'No deserialization handler for type {type}')
    if isinstance(raw_data, Mapping): # Assume dict:object, never list!
        return func({**raw_data, TYPEKEY: type}, type=type)
    return func(raw_data, type=type)

@fjd.register
def _(i: int, **kwargs):
    return i
@fjd.register
def _(f: float, **kwargs):
    return f
@fjd.register
def _(s: str, **kwargs):
    return s
@fjd.register
def _(b: bool, **kwargs):
    return b


def register_serializer(type: Type, func: Serializer):
    assert isfunction(func)
    @serialize.register
    def _(target: type) -> JSONSerializable:
        return func(target)

def register_deserializer(type: Type, func: Deserializer):
    assert isfunction(func)
    sig = signature(func)
    def f1(raw_data, **kwargs): # pylint: disable=invalid-name
        return func(raw_data)
    f = func if len(sig.parameters) == 2 else f1
    @fjd.register
    def _ds(raw_data, **kwargs) -> type:
        return f(raw_data, **kwargs)
