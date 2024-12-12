# Singleton

## Introduction

**Singleton** is a **creational design pattern** that ensures that a class has only one instance and provides an **easy** global access to that instance.

The pattern does not stipulate what to do with a **Singleton**.

The main tenets of this pattern are?
- **Ensure** that the **class** has only a **single instance**.
- Provide **easy global access** to this **instance**.
- Control how it is **instantiated**.
- Any **critical region** must be entered **serially**.

All clients have **global access** to a **single instance**.

## Implementation

There are a few ways in which we could implement the **Singleton**.

**Python** does **not** really have **constructors** but it does **have** a **creation** and **initialization** routines for classes.

It does not **strictly** have a **static** keyword for variables, but it does support **class-level** variables and methods which for all purposes are **static**.

The **Singleton Pattern** can be implemented in a number of different ways in Python. Some possible methods include:
- **Base Class**
- **Decorator**
- **Metaclass**

From those, the **Metaclass** is **best suited** for this purpose since with it we can manipulate and control the **task of class creation** itself.

## Python Functions

Some of general **Python** function overrides:

- `__new__`: is a **static method** that is responsible for **creating** and **returning** a **new instance** of a **class**. It is the first step in the object **instantiation** process. It is typically overriden when you need to **control** the object **creation process**.
- `__init__`: is an **instance method** that is responsible for **initializing** an object's attributes **after** it has been created by the `__new__`. The `__init__` method **does not return** a value and is **called** automatically **after** the object is created. This method is typically overriden to **define custom** attribute initialization for the class.
- `__call__`: is an **instance method** that allows a class's instance to be **called** as if they were functions.

## Singleton Versions

We will build three different versions of the **Singleton**: 
- **Classic GoF Singleton**
  - This will give us the most **simple** and **generic** version.
  - We will **control constructor access**.
  - Instantiation will be through a **static method**.
- **Simple (Naive) Singleton**
  - No **constructor control**.
  - Instantiation will be through **constructor method**.
  - We will use the `__new__` method override.
- **Metaclass Singleton**
- **Best version** of implementation.
- We will override the `__call__` method.
- We could also use the `__new__` and `__init__` methods.

### Classic GoF Implementation

Here is a classic way that we could implement the **Singleton Pattern** in Python:
- Only one **static attribute** for the unique instance with initial value `None`.
- Only one **private constructor** method.
- An **public static method** to return the **instance**.

We have a **lazy instantiation** because we instantiate the object when it is used.

```python

class ClassicSingleton:
    _instance = None

    def __init__(self):
        raise RuntimeError("Call instance() method.")

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance

s1 = ClassicSingleton.get_instance()
s2 = ClassicSingleton.get_instance()

print(type(s1))
print(s1)
print(id(s1))

print("")

print(type(s2))
print(s2)
print(id(s2))

```

### Simple Python Implementation

A simple way in which we could create a **Singleton** in Python is as follows:
- Only one **static attribute** for the unique instance with initial value `None`.
- Only one **constructor** method that control the **instance**.

We have a **lazy instantiation** because we instantiate the object when it is instantiated.

```python

class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()

print(type(s1))
print(s1)
print(id(s1))

print("")

print(type(s2))
print(s2)
print(id(s2))
```

### Metaclass Python Implementation

Using the **Metaclass** is probably the **best way** to create a **Singleton** in Python.

A **metaclass** in Python is a class that defines the behavior and rules for creating other class. In other words, metaclasses are the "class of classes".

By default, all Python class **implicitly** **inherit** from the **type built-in class**, which is itself a **metaclass**.

**Metaclasses** allow us to **customize** the class **creation process** and modify class attributes, methods, or other properties before the class is actually created.

They provide a way to **apply** certain **behaviors** consistently across **multiple classes**.

We have two versions of **Metaclass Singleton**: **lazy** and **eager** instantiation.

To implement the **metaclass**, we need to have:
- A superclass named **SingletonMeta** with a **dictionary** of **instances** and overrides the `__call__` method to control.
- A subclass **Singleton**.

Here is a version with **lazy instantiation**:

```python

class SingletonMeta(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):

    def some_operation(self) -> None:
        ...

s1 = Singleton()
s2 = Singleton()

print(type(s1))
print(s1)
print(id(s1))

print("")

print(type(s2))
print(s2)
print(id(s2))

```

An **eager instantiation** is good for in the context of a **Singleton**:
- Allows for data **preload** and **caching**.
- Allows for **connectivity** pre-caching.
- Important when **access** is **frequent** and needs to be **fast**.
- We **initialize** and **load** the instance **before** we need it.
- Python **does not** support **eager instantiation** out of the box or in an elegant manner.
- Using **metaclass** we can achieve **eager instantiation** when the **metaclass** is **executed**.

The **sequence** for **eager instantiation** in **Python** is:
  1) Load **metaclass** in memory.
  2) Execute the `__init__` method.
  3) Execute the `__load__` method.

Here is a version with an **eager instantiation**:

```python

class SingletonMeta(type):
    _instances: dict = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instances[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):

    def __init__(self):
        ...

s1 = Singleton()
s2 = Singleton()

print(type(s1))
print(s1)
print(id(s1))

print("")

print(type(s2))
print(s2)
print(id(s2))

```

## Final Remarks

Few things to keep in mind when implementing the **Singleton Pattern** in **Python**:
- Allows for consistency of usage.
- Provides flexibility of easy modification of initialization logic.
- Allows for ease of expanding the setup and initialization code.
- Better flow than a constructor since the name could be uniform across different class names and implementations.
