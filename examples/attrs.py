'''
Expand the code to view.

Run:
    $ python attrs.py
    Voila! Vector2d(start=Point(x=0.0, y=2.5), end=Point(x=10.0, y=-5.0))
'''

# Use the incredible attrs module that was around before dataclasses.
import attr
import attr.validators as validators

from xtelligent_serial.data_structs import register_struct_family, describe_struct_family
from xtelligent_serial.json import from_json

# The magic steps:
register_struct_family(describe_struct_family('attrs', attr.has, attr.fields))


@attr.s(frozen=True, repr=True, str=True)
class Point:
    x = attr.ib(type=float, validator=validators.instance_of(
        float), converter=float)
    y = attr.ib(type=float, validator=validators.instance_of(
        float), converter=float)


@attr.s(frozen=True, repr=True, str=True)
class Vector2d:
    start = attr.ib(type=Point, validator=validators.instance_of(Point))
    end = attr.ib(type=Point, validator=validators.instance_of(Point))


SOME_JSON = '''
{
    "start": {"x": 0, "y": 2.5},
    "end": {"x": 10, "y": -5}
}
'''
vec = from_json(Vector2d, SOME_JSON)
print('Voila!', vec)
