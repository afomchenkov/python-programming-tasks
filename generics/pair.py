from typing import Generic, TypeVar, Tuple

K = TypeVar('K')
V = TypeVar('V')


class Pair(Generic[K, V]):
    def __init__(self, key: K, value: V):
        self._key = key
        self._value = value

    def get_key(self) -> K:
        return self._key

    def get_value(self) -> V:
        return self._value

    def set_key(self, key: K) -> None:
        self._key = key

    def set_value(self, value: V) -> None:
        self._value = value

    def __repr__(self) -> str:
        return f"Pair({self._key!r}, {self._value!r})"

    def to_tuple(self) -> Tuple[K, V]:
        return (self._key, self._value)


if __name__ == "__main__":
    int_str_pair = Pair[int, str](1, "one")
    print(int_str_pair)

    key = int_str_pair.get_key()
    value = int_str_pair.get_value()
    print(f"Key: {key}, Value: {value}")

    int_str_pair.set_key(2)
    int_str_pair.set_value("two")
    print(int_str_pair)

    pair_tuple = int_str_pair.to_tuple()
    print(f"Tuple representation: {pair_tuple}")
