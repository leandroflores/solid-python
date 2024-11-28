# Object Oriented Programming

## Practical Example

In this example, we will use the concepts of **interface**, **implements**, and **methods** (**concretes** and **abstracts**).

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self) -> str:
        ...

    def description(self) -> str:
        return f"{self.__class__.__name__} says: {self.sound()}"

class Dog(Animal):

    def sound(self) -> str:
        return "Woof!"

class Cat(Animal):

    def sound(self) -> str:
        return "Meow!"

dog: Dog = Dog()
print(dog.description())

cat: Cat = Cat()
print(cat.description())

```

In this example, the `description` method is used in **subclasses** of `Animal` class. And `sound` method is customized for different kind of `Animal`.
