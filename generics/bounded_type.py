from typing import Generic, TypeVar


class Animal:
    def speak(self) -> str:
        return "Some sound"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"


TAnimal = TypeVar('TAnimal', bound=Animal)


class AnimalTrainer(Generic[TAnimal]):
    def __init__(self, animal: TAnimal):
        self._animal = animal

    def train(self) -> str:
        return f"""Training
        {self._animal.__class__.__name__}
        to say {self._animal.speak()}"""

    def get_animal(self) -> TAnimal:
        return self._animal

    def __repr__(self) -> str:
        return f"AnimalTrainer({self._animal!r})"


if __name__ == "__main__":
    dog_trainer = AnimalTrainer[Dog](Dog())
    print(dog_trainer.train())
    print(dog_trainer.get_animal())
    print(dog_trainer)
