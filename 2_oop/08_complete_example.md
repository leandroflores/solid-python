# Object Oriented Programming

## Complete Example

In this example, we will use the concepts of **interface**, **implementation**, and **instances**.

```python
import math

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

  def __init__(self, color: str, radius: float):
    super().__init__(color)
    self.radius: float = radius

  def area(self) -> float:
    return math.pi * (self.radius ** 2)

  def perimeter(self) -> float:
    return 2 * math.pi * self.radius

def process_shape(obj: Shape):
    print(obj.description())

rectangle: Rectangle = Rectangle("Blue", 1.30, 3.25)
print(rectangle.area())
print(rectangle.perimeter())
print(rectangle.color)

circle: Circle = Circle("Green", 5.18)
print(circle.area())
print(circle.perimeter())
print(circle.color)

process_shape(rectangle)
process_shape(circle)

```
