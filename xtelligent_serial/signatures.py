from collections.abc import Sequence, Iterable, Mapping
from typing import Union, Callable, Any, Type

JSONSerializable = Union[int, float, bool, str, Sequence, Iterable, Mapping]
Serializer = Callable[[Any], JSONSerializable]
Deserializer = Callable[[JSONSerializable], Any]
