# Serialization + JSON

![Lint+Test](https://github.com/xtelligent/xtelligent-serial/workflows/Lint+Test/badge.svg?branch=master)

## Synopsis

This library is intended to serialize objects to and from Python primitives. That is,
objects will be represented as dict, list, int, float, bool, and str. The resulting
primitives may be easily serialized to JSON using `python.json` or this library.

Because the library focuses on primitives, it could be useful for serialization to
other formats.

## Documentation

[API Reference](https://xtelligent.github.io/xtelligent-serial/docs/xtelligent_serial/)

## Example

[Source Code](https://xtelligent.github.io/xtelligent-serial/docs/index.html)

Run it!

```bash
$ python simple.py
<class '__main__.HasADate'>: {"d": "2020-05-28T02:46:05", "i": 2}
<class '__main__.Point'>: {"x": 21, "y": 12}
```

## Roadmap

* Integration with `json.JSONDecoder` and `json.JSONEncoder`. For now, this module is an alternative
to the `json` module.
* Serialization convenience methods on the decorators.
* Support for automatic deserialization. Right now, it is required to pass a parameter indicating
the type to deserialize to.
