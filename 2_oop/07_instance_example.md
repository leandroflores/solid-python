# Object Oriented Programming

## Instance Example

In this example, we will use the concepts of **interface**, **abstract methods**, and **override** for these **methods**.

```python
from abc import ABC, abstractmethod

class MyInterface(ABC):

    @abstractmethod
    def my_method(self) -> None:
        ...

class MyClass(MyInterface):

    def my_method(self) -> None:
        print("my_method in MyClass")

class AnotherClass(MyInterface):

    def my_method(self) -> None:
        print("my_method in Another")

class NewClass:

    def some_method(self) -> None:
        print("I am not implementing MyInterface")

def process_my_interface(obj: MyInterface):
    obj.my_method()
    print("The object has implemented MyInterface")

object_1: MyClass = MyClass()
process_my_interface(object_1)

object_2: AnotherClass = AnotherClass()
process_my_interface(object_2)

object_3: NewClass = NewClass()
process_my_interface(object_3)

```

In this example, type hints on `process_my_interface` only accepts an `MyInterface` instance (typing hint). The `object_3` is not from `MyInterface` type.


However, in Python, this will not raise a runtime error, but static type checkers will complain (warning). This last sentence will raise an attribute error, because the instance of `NewClass` do not have the `my_method` implemented.
