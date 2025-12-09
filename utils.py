import string
from collections.abc import Iterable, Callable


class Item[T]:
    def __init__(self, value: T):
        self._value = value

    def print(self):
        print(self._value)


class Stream[T](Iterable[T]):
    @classmethod
    def digits(cls):
        return Stream(string.digits)

    def __init__(self, iterable: Iterable[T]):
        self._value = tuple(iterable)

    def __iter__(self):
        return iter(self._value)

    def map[R](self, function: Callable[[T], R]):
        return Stream(map(function, self._value))

    def sum(self):
        return Item(sum(self._value))

    def reverse(self):
        stream: Stream[T] = Stream(reversed(self._value))
        return stream

    def collect(self):
        return list(self._value)


def iterate_input_lines():
    with open("input") as f:
        lines = f.readlines()
    return Stream(lines)
