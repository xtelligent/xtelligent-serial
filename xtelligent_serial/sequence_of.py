from dataclasses import dataclass
from typing import Type

from .registry import register_deserializer, deserialize

seq_type_cache = {}

@dataclass(frozen=True,eq=True,repr=True)
class SequenceOfType:
    type: Type

    def __getitem__(self, t):
        sot = seq_type_cache.get(t, None)
        if sot:
            return sot
        def initializer(self, **kwargs):
            SequenceOfType.__init__(self, t)
        new_sot = type(f'SequenceOfType[{t}]', (SequenceOfType,), {
            '__init__': initializer
        })
        seq_type_cache[t] = new_sot
        def ds(raw_data: new_sot):
            return [deserialize(item) for item in raw_data]
        register_deserializer(new_sot, ds)
        return new_sot

SequenceOf = SequenceOfType(object)
