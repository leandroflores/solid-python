# Open-Closed Principle

## Introduction

In this chapter, we presents a overview and a practice of **Open-Closed Principle**.

## Definition

*"Software entities should be open for extension, but close for modification"*

In a **base class**, as **entity**, we do not modify directly this class (because the risk of dependencies). However, we can extend **new classes** having the **entity** as **superclass**.

## Practical Example

Considering the above example:

```python
import math

class AreaCalculator:

    def area(self, shape: object) -> float:
        if isinstance(shape, Circle):
            return math.pi * shape.radius ** 2
        if isinstance(shape, Rectangle):
            return shape.width * shape.height

class Circle:

    def __init__(self, radius: float):
        self.radius: float = radius

class Rectangle:

    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height

```

In this case, this code calculates the area of different shapes using conditional statements inside the `AreaCalculator` class.

This violates the **Open-Closed Principle**, which states that a class should be **open for extension** but **closed for modification**.

To add more shapes, we would need to **modify** the method `area` in the `AreaCalculator` class by adding more conditional statements.

This approach makes the code **less flexible** and **more prone** to errors.

In this example, we can define an **Abstract Class** named `Shape`, with an **abstract method** named `area`. Therefore, the **classes** that extends the `Shape` class must implements the `area` method.

```python
import math

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        ...

class Circle(Shape):

    def __init__(self, radius: float):
        self.radius: float = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):

    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height

    def area(self) -> float:
        return self.width * self.height

class AreaCalculator:

    def area(self, shape: Shape) -> float:
        return shape.area()

```

The `Shape` **class** defines a contract with the `area` **abstract method**. Both `Circle` and `Rectangle` now inherit from `Shape` and implement their own `area()` methods.

The `AreaCalculator` class calls the `area()` method on the `Shape` object directly, without the need for conditional statements.

This **adheres** to the **Open-Closed Principle** because we can now add more shapes without modifying the `AreaCalculator` class.

The code is **more flexible** and **easier** to **extend** with new feature.
