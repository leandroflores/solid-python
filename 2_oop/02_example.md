# Object Oriented Programming

## Practical Example

In this example, we will use the concepts of **inheritance**, **superclass**, **subclass**, and **method override**.

```python

class Greeting:

    def __init__(self, name: str):
        self.name: str = name

    def say_hello(self) -> None:
        print(f"Hello, {self.name}!")

class BetterGreeting(Greeting):

    def say_hello(self) -> None:
        super().say_hello()
        print(f"Hello, Better {self.name}!")

greeting_1: Greeting = Greeting("John")
greeting_2: BetterGreeting = BetterGreeting("John")

greeting_1.say_hello()
greeting_2.say_hello()

```
