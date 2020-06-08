# Serialization + JSON

![Lint+Test](https://github.com/xtelligent/xtelligent-serial/workflows/Lint+Test/badge.svg?branch=master)

## Synopsis

This library is intended to serialize objects to and from Python primitives. That is,
objects will be represented as dict, list, int, float, bool, str, and None. The resulting
primitives may be easily serialized to JSON using `python.json` or this library.

Because the library focuses on representation with native primitives, it could be useful
for serialization to other formats.

## Usage

The library uses `decorators` to mark methods in charge of serialization. There's a
`serializer` decorator that associates a function with serializing a specific type, and
there's a corresponding `deserializer`:

```python
@serializer(datetime)
def dthandler(dt: datetime):
    return dt.isoformat()


@deserializer(datetime)
def str2dt(datestr: str):
    return datetime.fromisoformat(datestr)
```

Finally, the library implements a `serialization` decorator to make a class in charge of
serializing itself. Please see the
[example](https://xtelligent.github.io/xtelligent-serial/docs/examples/simple.html) to illustrate.

The `xtelligent_serial.json` namespace includes two convenience methods for reading and writing to
and from JSON. The `from_json` and `to_json` functions are documented
[here](https://xtelligent.github.io/xtelligent-serial/docs/xtelligent_serial/json/index.html). The
functions serialize types that your code supports with the serialization decorators.

## Automatic `dataclass` support

Python's `dataclass` with the `frozen` option creates the rough equivalent of a `NamedTuple`, but you
may still add methods and properties. Immutability is a great practice for creating testable,
readable code. A frozen `dataclass` does not acquire the "infinite state machine" behaviors common
to object-oriented class design. It is beyond the scope of this document to create full justification
of immutability, and there is an abundance of material on this subject. It is obvious that a frozen
`dataclass` maps very well to JSON documents. The consistent structure of `dataclass` types make it
straightforward for this library to support these classes automatically, without decorators. The only
caveat is that all member attribute types must be supported by decorators, or they must also be
primitive or `dataclass` types. Again, please see the
[example](https://xtelligent.github.io/xtelligent-serial/docs/examples/simple.html) to illustrate.

## Documentation

[API Reference](https://xtelligent.github.io/xtelligent-serial/docs/xtelligent_serial/)

## Example

[Source Code](https://xtelligent.github.io/xtelligent-serial/docs/examples/simple.html)

## Roadmap

* Integration with `json.JSONDecoder` and `json.JSONEncoder`. For now, this module is an alternative
to the `json` module.
* Serialization convenience methods on the decorators.
* Support for automatic deserialization. Right now, it is required to pass a parameter indicating
the type to deserialize to.
* Research automatic support for NamedTuple.
