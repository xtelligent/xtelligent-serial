# Serialization - JSON

## Synopsis

This library is intended to serialize objects to and from Python primitives. That is,
objects will be represented as dict, list, int, float, bool, and str. The resulting
primitives may be easily serialized to JSON using `python.json` or this library.

Because the library focuses on primitives, it could be useful for serialization to
other formats.

## Example

```python
from dataclasses import dataclass
from datetime import datetime

from xtelligent_serial import deserializer, serializer, serialization
from xtelligent_serial.json import to_json, from_json

@serializer(datetime)
def dthandler(dt: datetime):
    return dt.isoformat()

@deserializer(datetime)
def str2dt(datestr: str):
    return datetime.fromisoformat(datestr)

@dataclass
class HasADate:
    d: datetime
    i: int

def try_serialization(first_instance):
    json = to_json(first_instance)
    cls = first_instance.__class__
    print(f'{cls}:', json)
    second_instance = from_json(cls, json)
    return first_instance, second_instance

first_instance, second_instance = try_serialization(HasADate(datetime.utcfromtimestamp(1590633965), 2))
assert first_instance.d == second_instance.d
assert first_instance.i == second_instance.i

@serialization
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __serializer__(cls, instance):
        return {'x': instance.x, 'y': instance.y}
    
    def __deserializer__(cls, raw_data):
        return cls(raw_data['x'], raw_data['y'])

first_instance, second_instance = try_serialization(Point(21, 12))
assert first_instance.x == second_instance.x
assert first_instance.y == second_instance.y
```

## Roadmap

#. API reference.
#. Integration with `json.JSONDecoder` and `json.JSONEncoder`. For now, this module is an alternative
to the `json` module.
#. Serialization convenience methods on the decorators.
#. Support for automatic deserialization. Right now, it is required to pass a parameter indicating
the type to deserialize to.
