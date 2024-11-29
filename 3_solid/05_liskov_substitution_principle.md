# Liskov Substitution Principle

## Introduction

In this chapter, we presents a overview and a practice of **L**iskov **S**ubstitution **P**rinciple (**LSP**).

## Definition

*"Functions that use pointes, or references to base classes, must be able to use objects of derived classes without knowing it.*

If `ClassB` is a **subclass** of `ClassA`, then we should be able to replace `ClassA` with `ClassB` without interrupting the behavior of the program.

## Practical Example

Considering the above example:

```python

class Bird:

    def fly(self) -> None:
        print("I can fly!")

class Penguin(Bird):

    def fly(self) -> None:
        print("I can not fly!")

```

In this case, the initial code has a `Penguin` **class** that **inherits** from the `Bird` **class** and **overrides** the `fly()` method.

This violates the **L**iskov **S**ubstitution **P**rinciple (**LSP**), which states that **objects** of a **superclass** should be able to be replaced with objects of a **subclass** without affecting the correctness of the program.

If we were to use the `Penguin` class in a context where a `Bird` is expected, we might get unexpected behavior due to the **overriden** `fly()` method.

This can lead to errors and inconsistencies in the code.

In this example, we can define a new level of hierarchy, considering a class named `FlyingBird`  and `NonFlyingBird`, declaring the `fly()` method in `Bird` as **abstract method**. Therefore, the `Penguin` class can extends `NonFlyingBird` class with the implementation of the `fly()` method on `NonFlyingBird` class.

```python
from abc import ABC, abstractmethod

class Bird(ABC):

    @abstractmethod
    def fly(self) -> None:
        ...

class FlyingBird(Bird):

    def fly(self) -> None:
        print("I can fly!")

class NonFlyingBird(Bird):

    def fly(self) -> None:
        print("I can not fly!")

class Penguin(NoFlyingBird):
    ...

```

In the refactored solution, we introduced two new classes: `FlyingBird` and `NonFlyingBird`, both inheriting from the `Bird` **abstract class**.

The `FlyingBird` class implements the `fly()` method, while the `NonFlyingBird` class **provides** an alternative implementation for the `fly()` method.

The `Penguin` class now inherits from `NonFlyingBird`.

This **adheres** to the **Liskov Substitution Principle** because any subclasses of `Bird` can now be substituted without altering the correctness of the program.

The code is **more robust** and **less prone** to errors.
