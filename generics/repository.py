from typing import Generic, TypeVar, List

T = TypeVar('T')


class Repository(Generic[T]):
    def __init__(self):
        self._items: List[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def get_all(self) -> List[T]:
        return self._items

    def find(self, predicate) -> List[T]:
        return [item for item in self._items if predicate(item)]

    def __repr__(self) -> str:
        return f"Repository({self._items!r})"


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"User(name={self.name!r}, age={self.age!r})"


if __name__ == "__main__":
    user_repo = Repository[User]()
    user_repo.add(User("Alice", 30))
    user_repo.add(User("Bob", 25))

    for user in user_repo.get_all():
        print(user)
