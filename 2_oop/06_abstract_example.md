# Object Oriented Programming

## Interface Example

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

interface_1: MyInterface = MyInterface()

object_1: MyClass = MyClass()
object_1.my_method()

object_2: AnotherClass = AnotherClass()
object_2.my_method()

```

In this example, we can not instantiate an object of `MyInterface` class, because this class have an **abstract method**.

**Abstract Class** can have **concrete** and **abstract** **methods**.

In Python, we do not have the concept of **Interface**. Then, we can create an **Abstract Class** with no **concrete methods**. It is a way to define an **Interface** in Python.

**Classes** can implement many **interfaces**.
