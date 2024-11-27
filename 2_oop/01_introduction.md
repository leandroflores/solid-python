# Object Oriented Programming

## Introduction

In this chapter, we make a refresher of the **Python** language with reference to **Object Oriented Programming** (**OOP**). We will discuss the following main concepts:
- Classes and Objects
- Encapsulation
- Inheritance:
  - Interface Contracts
  - Abstract Classes
- UML Diagrams for OOP

## Class and Objects

**Classes** are simple (or more complex) **recipes** that are used to create two main things:
- Provide a **data container**:
  - **Variables**
  - **Constants**
- Provide **operations** on **data**:
  - **Functions** or **methods**
  
We can use the **Classes** to create **instances** of **objects** which hold the specific data what we can operate on.

With Python, an example:

```python
class Greeting:

    def __init__(self, name: str):
        self.name: str = name

    def say_hello(self) -> None:
        print(f"Hello, {self.name}!")

greeting = Greeting("Paul")
greeting.say_hello()
```

Class Diagram can be defined with one single attribute: `name`, and a method `say_hello` with no parameters and with `void` return.

## Encapsulation

In general, a well designed **class** already achieves **encapsulation** in the sense that it **gathers** all the relevant **data** and **funcionality**. It helps us with controlling complexity as well.

Do have these points in mind:
- Create **classes** for **all** the **objects** you need in your code.
- Create **collections** of **related objects** so that can be treated as **units**.

```python

class Author:

    def __init__(self, name: str, birth_year: str):
        self.name: str = name
        self.birth_year: str = birth_year

    def details(self) -> str:
        return f"{self.name} (born {self.birth_year})"


class Book:

    def __init__(self, title: str, year: str, author: Author):
        self.title: str = title
        self.year: str = year
        self.author: Author = author

    def details(self) -> str:
        return f"'{self.title}' by {self.author.details()}, published in {self.year}."

author: Author = Author("George Orwell", "1903")
book: Book = Book("1984", "1949", author)
print(book.details())

```

Therefore, we have a **Book** which agreggates a single **Author**. An **Author** is smaller encapsulation of the **Book**.

## Inheritance

**Inheritance** allows us to **generalize**. We can think of it as a tree which grows more complex as we keep on extending its branches.

We start with some **property** or **behaviour** that is **present** in different **instances** or **types** of **entities**.

We then create new and more **specialized** versions of the **parent** by **inheriting** either **data** and/or **behaviour** in the **children**.

In above example, we have a **superclass** named `Animal`, and two **subclasses**: `Dog` and `Cat`.


```python

class Animal:

  def __init__(self, name: str):
    self.name: str = name


  def speak(self) -> None:
    return f"{self.name} speaks ..."

class Dog(Animal):

  def speak(self) -> None:
    return f"{self.name} barks ..."

class Cat(Animal):

  def speak(self) -> None:
    return f"{self.name} meows ..."


dog: Dog = Dog("Bob")
cat: Cat = Cat("Whiskers")

dog.speak()
cat.speak()
```

Every **animal** can speak. But every animal speaks in a own way.

### Inheritance - Interfaces

**Interfaces** is about **contracts**. 

A **contract** is like a **promise** that you will provide some specific behaviour. In classes this means that you **promise** to provide some funcionality.

One way to **create** a **contract** is through a concept of **Interface**. In Python, we do not have a strict interface. We use an **abstract class** with no implementation.

```python
from abc import ABC, abstractmethod

class MyInterface(ABC):

  @abstractmethod
  def my_method(self) -> None:
    ...

class MyClass(MyInterface):

  def my_method(self) -> None:
    return "my_method in MyClass"

class AnotherClass(MyInterface):

  def my_method(self) -> None:
    return "my_method in Another class"


object_1: MyClass = MyClass()
object_1.my_method()

object_2: AnotherClass = AnotherClass()
object_2.my_method()

```

**Classes** can **implement** many **interfaces**. In the example, `MyClass` and `AnotherClass` **implements** the `MyInterface` interface (as **abstract class**).

Em Python, to enforce contracts, we can use **type hinting**.

### Inheritance - Abstract Classes

**Abstract Classes** is about partially implemented **contracts** which is about **reuse**.

In many cases you have actual funcionality not just a signature but actual funcionality behind the signature that you would like to have all child classes inherit.

This is where you would use an **Abstract Class**:
  - You can **add** specific **implemented** methods.
  - Specific **constants** or **variabels**.

```python

from abc import ABC, abstractmethod

class Shape(ABC):

  def __init__(self, color: str):
    self.color: str = color

  @absctractmethod
  def area(self) -> float:
    ...

  @abstractmethod
  def perimeter(self) -> float:
    ...

  def description(self) -> str:
    return f"{self.__class__.__name__} has the color: {self.color}"

class Rectangle(Shape):

  def __init__(self, color: str, width: float, height: float):
    super().__init__(color)
    self.width: float = width
    self.height: float = height

  def area(self) -> float:
    return self.width * self.height

  def perimeter(self) -> float:
    return 2 * (self.width + self.height)


class Circle(Shape):

  def __init__(self, color: str, radio: float):
    super().__init__(color)
    self.radio: float = radio

  def area(self) -> float:
    return 3.14 * (self.radio ** 2)

  def perimeter(self) -> float:
    return 2 * 3.14 * self.radio

r1: Rectangle = Rectangle("Blue", 1.30, 3.25)
print(r1.area())
print(r1.perimeter())
print(r1.description())

r2: Rectangle = Rectangle("Red", 15.00, 7.50)
print(r2.area())
print(r2.perimeter())
print(r2.description())

c1: Circle = Circle("Green", 5.18)
print(c1.area())
print(c1.perimeter())
print(c1.description())

```