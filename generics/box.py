from typing import Generic, TypeVar

T = TypeVar('T')


class Box(Generic[T]):
    def __init__(self, value: T):
        self._value = value

    def get(self) -> T:
        return self._value

    def set(self, value: T) -> None:
        self._value = value

    def __repr__(self) -> str:
        return f"Box({self._value!r})"


if __name__ == "__main__":
    int_box = Box
    str_box = Box[str]("hello")

    # print(int_box.get())
    print(str_box.get())

    int_box_instance = int_box(42)
    print(int_box_instance)

    str_box_instance = str_box
    print(str_box_instance)

    str_box_instance.set("world")
    print(str_box_instance.get())
    print(str_box_instance)
